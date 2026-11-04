"""Export the energy workbook's results for the financial workbook (CR-052 W1).

    python3 energy/build/export_energy.py ENERGY.xlsx OUT.csv --recalc PATH_TO_recalc.py

The counterpart of extract_finance.py. The financial workbook does not link to the energy
workbook; its build script (finance/build/cr052_energy_link.py) reads this CSV. The Story
case is read from the saved values of ENERGY.xlsx (Levers!E4 must be 1); the Stress case
is obtained by copying the workbook, setting Levers!E4 = 2 and recalculating it in
LibreOffice. The first line records the energy workbook's SHA-256.
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

FIRST, LAST = 6, 92  # 1846..1932
# (key, sheet, header text in row 5 or None for a named range, named range)
SERIES = [
    ("home_oil", "Fuels", "Home oilfields (m bbl)", None),
    ("conc_oil", "Fuels", "CR-053 concessions: entitlement crude (m bbl)", None),
    ("veh_build", "Uses", "Vehicles the finance workbook must build (thousand)", None),
    ("power_capex", None, None, "en_power_capex"),
    ("power_capex_private", None, None, "en_power_capex_private"),
    ("dev_power_credit", None, None, "en_dev_power_credit"),
    ("elec_revenue", None, None, "en_elec_revenue"),
    ("elec_revenue_utility", None, None, "en_elec_revenue_utility"),
    ("elec_revenue_selfgen", None, None, "en_elec_revenue_selfgen"),
    ("royalties", None, None, "en_royalties"),
    ("oil_import_value", None, None, "en_oil_import_value"),
    ("coal_import_value", None, None, "en_coal_import_value"),
    ("fuel_trade_net", None, None, "en_fuel_trade_net"),
    ("kwh_pp", "Electricity", "Electricity per person (kWh)", None),
    ("mult_gen", "Electricity", "Multiplier: electricity per person vs US", None),
]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(path: Path) -> dict[str, list[float]]:
    wb = openpyxl.load_workbook(path, data_only=True)
    out = {}
    for key, sheet, header, name in SERIES:
        if name:
            dest = list(wb.defined_names[name].destinations)[0]
            ws = wb[dest[0]]
            col = "".join(ch for ch in dest[1].split(":")[0] if ch.isalpha())
        else:
            ws = wb[sheet]
            col = None
            for c in range(1, ws.max_column + 1):
                if ws.cell(5, c).value == header:
                    col = openpyxl.utils.get_column_letter(c)
                    break
            if col is None:
                raise SystemExit(f"{sheet}: no column headed {header!r}")
        vals = []
        for r in range(FIRST, LAST + 1):
            v = ws[f"{col}{r}"].value
            vals.append(float(v) if isinstance(v, (int, float)) else 0.0)
        out[key] = vals
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("energy", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--recalc", type=Path, required=True)
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.energy, data_only=True)
    if wb["Levers"]["E4"].value != 1:
        sys.exit("ENERGY must be saved in the Story case (Levers!E4 = 1)")
    story = read(a.energy)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "stress.xlsx"
        shutil.copy(a.energy, tmp)
        w = openpyxl.load_workbook(tmp)
        w["Levers"]["E4"] = 2
        w.save(tmp)
        subprocess.run([sys.executable, str(a.recalc), str(tmp), "300"], check=True, capture_output=True)
        stress = read(tmp)
    with a.out.open("w", newline="") as f:
        f.write(f"# energy workbook SHA-256 {sha256(a.energy)}\n")
        w = csv.writer(f)
        w.writerow(["year"] + [f"{k}__story" for k, *_ in SERIES] + [f"{k}__stress" for k, *_ in SERIES])
        for i, y in enumerate(range(1846, 1933)):
            w.writerow([y] + [round(story[k][i], 6) for k, *_ in SERIES] + [round(stress[k][i], 6) for k, *_ in SERIES])
    print(f"wrote {a.out}: {len(SERIES)} series x 2 cases")


if __name__ == "__main__":
    main()
