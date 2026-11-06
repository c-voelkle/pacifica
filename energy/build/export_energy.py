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
# (key, sheet, header text in row 5 or None for a named range, named range or Paths key)
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
    # CR-051, CR-054 and CR-055 for the financial workbook (finance/build/cr051_054_055_champions.py)
    ("cap_works", "Hydro", "The Works' dams, Pit and upper Feather (MW)", None),
    ("cap_rock", "Hydro", "Rock Island (MW)", None),
    ("cap_bonn", "Hydro", "Bonneville (MW)", None),
    ("cap_rreach", "Hydro", "Rocky Reach (MW)", None),
    ("cap_wells", "Hydro", "Wells (MW)", None),
    ("cap_mcnary", "Hydro", "McNary (MW)", None),
    ("cap_cjoe", "Hydro", "Chief Joseph, laddered (MW)", None),
    ("cap_col2", "Hydro", "Columbia second units (MW)", None),
    ("halls_mw", "Strategic loads", "Halls' draw (MW)", None),
    ("halls_ded", "Strategic loads", "Halls met from dedicated power (MW avg)", None),
    ("works_avg", "Strategic loads", "Works' dams, average output (MW)", None),
    ("feed_mt", "Strategic loads", "Feed plant oil (Mt)", None),
    ("station_mw", "Strategic loads", "Columbia station's draw (MW)", None),
    ("diff_mw", "Strategic loads", "Gaseous-diffusion plant's draw (MW)", None),
    ("wen_mw", "Strategic loads", "Wenatchee smelter (MW avg)", None),
    ("rock_spare", "Strategic loads", "Rock Island left for orchards and pumps (MW avg)", None),
    ("hyd_mf", "Fuels", "Motor fuel gained by hydrogenation (m bbl, memo)", None),
    ("alu_grid", "Uses", "Aluminium for the grid's conductor (kt, memo)", None),
    ("alu_air", "Uses", "… the Concord fleet's aircraft", None),
    ("alu_pool", "Uses", "… the Concord pool, to Japan", None),
    ("alu_civil", "Uses", "… civil uses at home", None),
    ("alu_export", "Uses", "… exported beyond the Concord", None),
] + [(k, "Paths", None, k) for k in ("alu_kt", "alu_hilo", "eln_kt", "haber_kt", "esteel", "zinc_kt", "mg_kt",
                                      "phos_kt", "cu_kt", "hyd_bbl", "rubber_kt", "pig_kt", "tie_mw")] + [
    # The financial workbook's dynamic layer (finance/build/cr056_dynamics.py)
    ("fact_elec", "Uses", "Factory horsepower electric", None),
    ("homes_wired", "Uses", "Homes with electricity (thousand)", None),
    ("homes", "People & output", "Homes (thousand)", None),
    ("fact_gwh", "Uses", "Industry, motors (and process heat if heat_el = 1)", None),
    ("veh_pp", "Uses", "Vehicles per person", None),
    ("us_kwh_pp", "Electricity", "US electricity per person, all producers (kWh)", None),
] + [(k, "Paths", None, k) for k in ("pump_acres", "el_price", "kwh_home")]


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(path: Path) -> dict[str, list[float]]:
    wb = openpyxl.load_workbook(path, data_only=True)
    out = {}
    for key, sheet, header, name in SERIES:
        if sheet == "Paths":  # a Paths row, years across (row key in column A, 1846 in column D)
            ws = wb["Paths"]
            pr = next((r for r in range(6, ws.max_row + 1) if ws.cell(r, 1).value == name), None)
            if pr is None:
                raise SystemExit(f"Paths: no row keyed {name!r}")
            out[key] = [float(v) if isinstance(v, (int, float)) else 0.0
                        for v in (ws.cell(pr, 4 + i).value for i in range(LAST - FIRST + 1))]
            continue
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
