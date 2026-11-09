"""Test that the CR-056 workbook at dyn_mode 0 reproduces the CR-051/054/055 workbook exactly.

    python3 finance/build/cr056_identity.py OLD.xlsx NEW.xlsx

OLD is the CR-051/054/055 workbook (cba70b31...), NEW the CR-056 workbook recalculated in LibreOffice
at dyn_mode 0, both in the same case (Story or Stress). Every cell of every sheet OLD has is compared by value (exact, no tolerance); the
formulas may differ only in Economy C, D, J, Labour B and Champions Z, AF (the hooks) and in Levers, Changes and
Start (new rows). Exit status 1 on any difference.
"""
from __future__ import annotations

import sys

import openpyxl

HOOKS = {("Economy", "C"), ("Economy", "D"), ("Economy", "J"), ("Labour", "B"), ("Champions", "Z"), ("Champions", "AF")}
APPEND_ONLY = {"Levers", "Changes", "Start"}


def main() -> int:
    old_p, new_p = sys.argv[1], sys.argv[2]
    ov, nv = openpyxl.load_workbook(old_p, data_only=True), openpyxl.load_workbook(new_p, data_only=True)
    of, nf = openpyxl.load_workbook(old_p), openpyxl.load_workbook(new_p)
    if nv["Levers"]["E4"].value != ov["Levers"]["E4"].value:
        print("OLD and NEW must be in the same case (Levers E4)"); return 1
    bad_v, bad_f, n = [], [], 0
    for ws in ov.worksheets:
        w2, f1, f2 = nv[ws.title], of[ws.title], nf[ws.title]
        for rw in ws.iter_rows():
            for c in rw:
                n += 1
                a, b = c.value, w2[c.coordinate].value
                if a != b and not (isinstance(a, float) and isinstance(b, float) and a == b):
                    bad_v.append((ws.title, c.coordinate, a, b))
                fa, fb = f1[c.coordinate].value, f2[c.coordinate].value
                if fa != fb and (ws.title, c.column_letter) not in HOOKS and not (ws.title in APPEND_ONLY and fa is None):
                    if not (isinstance(fa, str) and isinstance(fb, str) and ws.title in APPEND_ONLY):
                        bad_f.append((ws.title, c.coordinate, fa, fb))
    print(f"{n} cells compared; {len(bad_v)} value differences; {len(bad_f)} unexpected formula changes")
    for x in (bad_v + bad_f)[:30]:
        print("  ", x)
    return 1 if bad_v or bad_f else 0


if __name__ == "__main__":
    sys.exit(main())
