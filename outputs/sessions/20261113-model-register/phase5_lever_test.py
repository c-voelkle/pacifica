"""Phase 5: check that every cw_* lever moves the model when its cell changes.

    python3 phase5_lever_test.py WORKBOOK.xlsx OUTDIR

Each test sets the lever's Story and Stress cells (Levers C and D) to a test value, recalculates the
Story case in LibreOffice and compares a set of results, summed over 1859-1885, with the run it is
tested against (the workbook as built, or a base with another lever set first). Writes
OUTDIR/lever_test.json and prints one line per lever.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import openpyxl

RECALC = "/mnt/skills/public/xlsx/scripts/recalc.py"
Y0, Y1 = 1859, 1885
METRICS = {  # label: sheet, column, first data row, year of first row
    "receipts": ("Budget", "M", 6, 1846), "spending": ("Budget", "Y", 6, 1846),
    "public_debt": ("Debt & cash", "R", 6, 1846), "reserve_fund": ("Debt & cash", "S", 6, 1846),
    "net_lending": ("Debt & cash", "B", 6, 1846), "gold_paid_out": ("Gold & money", "E", 6, 1846),
    "gold": ("Gold & money", "F", 6, 1846), "residents": ("People", "L", 6, 1846),
    "navy": ("Navy", "V", 6, 1846), "continental_out": ("Loans", "E", 6, 1846),
    "dev_investment": ("Debt & cash", "N", 6, 1846), "private_uses": ("Sources & uses", "K", 135, 1846),
    "idle_gold_source": ("Sources & uses", "R", 135, 1846), "new_gold_kept": ("Resources", "R", 6, 1846),
}
# lever: (test overrides, base overrides)
TESTS = {
    "cw_ny_share": ({"cw_ny_share": 0.5}, {}),
    "cw_ny_home": ({"cw_ny_home": 1.0}, {}),
    "cw_idle_ratio": ({"cw_idle_ratio": 0.12}, {}),
    "cw_rich_early": ({"cw_rich_early": 1.0}, {}),
    "cw_rich_late": ({"cw_rich_late": 2.0}, {}),
    "cw_mission": ({"cw_mission": 0.5}, {}),
    "cw_war61": ({"cw_war61": 8}, {}),
    "cw_occ6264": ({"cw_occ6264": 6}, {}),
    "cw_occ6567": ({"cw_occ6567": 2}, {}),
    "cw_hon_batt": ({"cw_hon_batt": 0.3}, {}),
    "cw_hon_frig": ({"cw_hon_frig": 2}, {}),
    "cw_hon_turret": ({"cw_hon_turret": 0.2}, {}),
    "cw_sitka_gar": ({"cw_sitka_gar": 0.3}, {}),
    "cw_sitka_mail": ({"cw_sitka_mail": 0.1}, {}),
    "cw_inst_opt": ({"cw_inst_opt": 3}, {}),
    "cw_scrip_face": ({"cw_scrip_face": 3}, {}),
    "cw_scrip_price": ({"cw_scrip_face": 3, "cw_scrip_price": 0.9}, {"cw_scrip_face": 3}),
    "cw_setoff_nc": ({"cw_setoff_nc": 1}, {}),
    "cw_nb_credit": ({"cw_ann_nw": 0.1, "cw_nb_credit": 0}, {"cw_ann_nw": 0.1}),
    "cw_union_prop": ({"cw_union_prop": 0.5}, {}),
    "cw_keep64": ({"cw_keep64": 0.2}, {}),
    "cw_keep67": ({"cw_keep67": 0.2}, {}),
    "cw_ann_nw": ({"cw_ann_nw": 0.2}, {}),
    "cw_ann_gb": ({"cw_ann_gb": 0.2}, {}),
    "cw_ann_sw": ({"cw_ann_sw": 0.2}, {}),
    "cw_rc_or": ({"cw_rc_or": 0.5}, {}),
    "cw_washoe": ({"cw_washoe": 0.5}, {}),
    "cw_rc_sw": ({"cw_rc_sw": 0.3}, {}),
    "cw_rc_gb": ({"cw_rc_gb": 0.1}, {}),
    "cw_juarez": ({"cw_juarez": 1}, {}),
    "cw_or_works": ({"cw_or_works": 1}, {}),
    "cw_refugees": ({"cw_refugees": 20000}, {}),
    "cw_priv1867": ({"cw_priv1867": 5}, {}),
    "cw_legion_on": ({"cw_legion_on": 1}, {}),
    "cw_legion_pay": ({"cw_legion_on": 1, "cw_legion_pay": 0.3}, {"cw_legion_on": 1}),
}


def lever_rows(wb) -> dict[str, int]:
    out = {}
    for n, d in wb.defined_names.items():
        if n.startswith("cw_") and d.attr_text.startswith("Levers!$E$"):
            out[n] = int(d.attr_text.split("$")[-1])
    return out


def run(src: Path, overrides: dict, dst: Path) -> dict:
    wb = openpyxl.load_workbook(src)
    rows = lever_rows(wb)
    wb["Levers"]["E4"].value = 1
    for k, v in overrides.items():
        wb["Levers"].cell(rows[k], 3).value = v
        wb["Levers"].cell(rows[k], 4).value = v
    wb.save(dst)
    out = subprocess.run([sys.executable, RECALC, str(dst), "600"], capture_output=True, text=True)
    rc = json.loads(out.stdout[out.stdout.index("{"):])
    wb = openpyxl.load_workbook(dst, data_only=True, read_only=True)
    res = {"errors": rc.get("total_errors"), "problems": wb["Start"]["C5"].value}
    for k, (sh, col, r0, y0) in METRICS.items():
        ws = wb[sh]
        res[k] = sum(float(ws[f"{col}{r0 + y - y0}"].value or 0) for y in range(Y0, Y1 + 1))
    return res


def main() -> None:
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    tmp = out / "tmp.xlsx"
    bases: dict[str, dict] = {}
    results = {}
    for lever, (test, base) in TESTS.items():
        key = json.dumps(base, sort_keys=True)
        if key not in bases:
            bases[key] = run(src, base, tmp)
        b = bases[key]
        t = run(src, test, tmp)
        moved = {k: round(t[k] - b[k], 4) for k in METRICS if abs(t[k] - b[k]) > 1e-6}
        results[lever] = {"test": test, "base": base, "errors": t["errors"], "problems": t["problems"], "moved": moved}
        print(f"{lever:15s} {'MOVES' if moved else 'NO CHANGE'}  errors {t['errors']}  "
              + ", ".join(f"{k} {v:+.2f}" for k, v in list(moved.items())[:5]), flush=True)
    (out / "lever_test.json").write_text(json.dumps({"bases": bases, "results": results}, indent=1))
    tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
