"""Recalculate a financial workbook in the Story and the Stress case and read its checks.

    python3 evaluate.py WORKBOOK.xlsx OUTDIR [--tag NAME]

For each case: copy the workbook, set Levers!E4 (1 = Story, 2 = Stress), recalculate in
LibreOffice (xlsx skill scripts/recalc.py), then read Checks (every year, every column that
reads "Check"), the problem count (Start!C5) and the series the plan's baseline names:
cash, Reserve Fund, public debt, monetary gold, residents (1846-1932). Writes
OUTDIR/<tag>_<case>.json and prints a summary.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

import openpyxl

RECALC = "/mnt/skills/public/xlsx/scripts/recalc.py"
SERIES = {  # sheet, column, label
    "cash": ("Debt & cash", "M"), "cash_target": ("Debt & cash", "E"), "reserve_fund": ("Debt & cash", "S"),
    "public_debt": ("Debt & cash", "R"), "gold": ("Gold & money", "F"), "residents": ("People", "L"),
    "receipts": ("Budget", "M"), "spending": ("Budget", "Y"), "gdp": ("Economy", "O"),
}


def recalc(src: Path, case: int, dst: Path) -> dict:
    wb = openpyxl.load_workbook(src)
    wb["Levers"]["E4"].value = case
    wb.save(dst)
    out = subprocess.run([sys.executable, RECALC, str(dst), "600"], capture_output=True, text=True)
    txt = out.stdout
    res = json.loads(txt[txt.index("{"):])
    return res


def read(path: Path) -> dict:
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    ck = wb["Checks"]
    rows = list(ck.iter_rows(min_row=5, max_row=92, values_only=True))
    head = rows[0]
    fails = {}
    problems = {}
    for r in rows[1:]:
        if not isinstance(r[0], (int, float)):
            continue
        y = int(r[0])
        problems[y] = r[18] or 0
        bad = [str(head[i]) if i < len(head) and head[i] else f"col{i + 1}" for i, v in enumerate(r) if v == "Check"]
        if bad or (r[18] or 0):
            fails[y] = bad
    series = {}
    for k, (sh, col) in SERIES.items():
        ws = wb[sh]
        ci = openpyxl.utils.column_index_from_string(col) - 1
        s = {}
        for r in ws.iter_rows(min_row=6, max_row=92, values_only=True):
            if r and isinstance(r[0], (int, float)):
                s[int(r[0])] = r[ci]
        series[k] = s
    start = wb["Start"]
    return {"problems_total": start["C5"].value, "problems_by_year": problems, "failing": fails, "series": series}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("workbook")
    ap.add_argument("outdir")
    ap.add_argument("--tag", default="run")
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    for case, name in ((1, "story"), (2, "stress")):
        dst = out / f"{a.tag}_{name}.xlsx"
        rc = recalc(Path(a.workbook), case, dst)
        d = read(dst)
        d["recalc"] = {"total_formulas": rc.get("total_formulas"), "total_errors": rc.get("total_errors")}
        (out / f"{a.tag}_{name}.json").write_text(json.dumps(d, indent=1, default=str))
        print(f"{a.tag} {name}: problems {d['problems_total']}, formula errors {rc.get('total_errors')}")
        for y, cols in sorted(d["failing"].items()):
            print(f"   {y}: {d['problems_by_year'][y]}  {'; '.join(cols)}")


if __name__ == "__main__":
    main()
