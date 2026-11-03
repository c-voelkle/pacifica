"""Read the financial workbook's Story and Stress results into finance_inputs.csv.

    python3 energy/build/extract_finance.py FINANCE.xlsx OUT.csv [--recalc PATH_TO_recalc.py]

The energy workbook does not keep its own population, output or oil figures: it takes
them from the financial workbook (handoff section 4, "link, don't copy"). The Story case
is read from the saved values of FINANCE.xlsx (its Levers!E4 must be 1). The Stress case
is obtained by copying the workbook, setting Levers!E4 = 2 and recalculating it in
LibreOffice. Paths C is not re-iterated, as in the finance build notes.

The CSV records the SHA-256 of FINANCE.xlsx in its first line, and the energy build
prints it on the energy workbook's Start sheet, so a stale import is visible.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import openpyxl

# (key, sheet, column, label, unit)
FIELDS = [
    ("pop_res", "People", "L", "Residents at end of year (core Pacifica)", "persons"),
    ("pop_all", "People", "X", "Everyone present, incl. guest workers and the Gulf once a member", "persons"),
    ("pop_gulf", "People", "V", "Gulf Republic residents (once a member)", "persons"),
    ("pop_phil", "People", "U", "Philippine crown residents (separate, not modelled)", "persons"),
    ("guest", "Labour", "L", "Guest workers present", "persons"),
    ("labour", "Labour", "B", "Labour force", "persons"),
    ("gdp", "Economy", "O", "Core GDP", "$m current"),
    ("gdp_real", "Economy", "S", "Real GDP", "1913 $m"),
    ("price", "Economy", "H", "Price level", "1913 = 1"),
    ("gdp_pc", "Economy", "P", "GDP per person present", "$"),
    ("us_gdp_pc", "Economy", "Q", "US GDP per person, historical", "$"),
    ("oil_out", "Resources", "K", "Oil output, home fields", "m bbl"),
    ("oil_price", "Resources", "L", "Oil price", "$/bbl"),
    ("metals", "Resources", "F", "Copper and other metals", "$m"),
    ("gold_ca", "Resources", "B", "California gold", "$m"),
    ("gold_int", "Resources", "C", "Interior gold and silver", "$m"),
    ("steel", "Champions", "R", "Steel output", "m tonnes"),
    ("cars", "Champions", "U", "Motor vehicles built", "thousands"),
    ("chem", "Champions", "Z", "Chemicals and drugs, value added", "$m"),
    ("elec_eq", "Champions", "AF", "Electrical equipment, value added", "$m"),
    ("alum_air", "Champions", "AO", "Aluminium and aircraft", "$m"),
    ("gulf_crude", "Champions", "L", "Gulf crude output", "m bbl"),
    ("gulf_share", "Champions", "M", "Share of Gulf crude refined and sold by Pacifican firms", "share"),
    ("asia_oil", "Champions", "N", "Lamp oil, fuel and bunkers sold in Asia", "m bbl"),
    ("navy_oil", "Navy", "Z", "Navy oil burned", "m bbl"),
    ("navy_ships", "Navy", "K", "Ships in service", "ships"),
    ("atom_mwe", "Atomic", "V", "Atomic stations in service", "MWe"),
    ("dev_inv", "Debt & cash", "I", "Invested by the Development Fund", "$m"),
    ("public_works", "Budget", "R", "Public works", "$m"),
]
FIRST_ROW, LAST_ROW = 6, 92  # 1846..1932


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(path: Path) -> dict[str, list[float]]:
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    out = {}
    for key, sheet, col, *_ in FIELDS:
        ws = wb[sheet]
        vals = []
        for r in range(FIRST_ROW, LAST_ROW + 1):
            v = ws[f"{col}{r}"].value
            vals.append(float(v) if isinstance(v, (int, float)) else 0.0)
        out[key] = vals
    years = [wb["People"][f"A{r}"].value for r in range(FIRST_ROW, LAST_ROW + 1)]
    assert years[0] == 1846 and years[-1] == 1932, years[:2]
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("finance", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--recalc", type=Path, required=True, help="the xlsx skill's scripts/recalc.py")
    a = ap.parse_args()

    chk = openpyxl.load_workbook(a.finance, data_only=True, read_only=True)
    if chk["Levers"]["E4"].value != 1:
        sys.exit("finance workbook must be saved in the Story case (Levers!E4 = 1)")
    story = read(a.finance)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "stress.xlsx"
        shutil.copy(a.finance, tmp)
        wb = openpyxl.load_workbook(tmp)
        wb["Levers"]["E4"] = 2
        wb.save(tmp)
        res = subprocess.run([sys.executable, str(a.recalc), str(tmp), "300"], capture_output=True, text=True)
        if '"success"' not in res.stdout:
            sys.exit("Stress recalculation failed:\n" + res.stdout + res.stderr)
        stress = read(tmp)

    with a.out.open("w", newline="") as f:
        f.write(f"# finance workbook SHA-256 {sha256(a.finance)}\n")
        w = csv.writer(f)
        w.writerow(["key", "case", "label", "unit"] + list(range(1846, 1933)))
        for key, sheet, col, label, unit in FIELDS:
            for case, data in (("story", story), ("stress", stress)):
                w.writerow([key, case, f"{label} ({sheet}!{col})", unit] + [round(v, 4) for v in data[key]])
    print(f"wrote {a.out}: {len(FIELDS)} series x 2 cases")


if __name__ == "__main__":
    main()
