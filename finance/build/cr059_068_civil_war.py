"""Phase 4 of the CR-059-068 model plan: the Civil War CRs' fixed items in the financial workbook.

    python3 finance/build/cr059_068_civil_war.py IN.xlsx OUT.xlsx \
        [--joins population/data/joins_cr059_068.toml] [--rates finance/build/paths_c_rates_cr059_068_final.csv]

IN is the current workbook (CR-051/054/055, SHA-256 cba70b31...). The script never
recalculates; run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

Only what the register calls fixed is applied (outputs/sessions/20261113-model-register:
register.csv, the author's decisions of 13 November 2026). Levers stay where the workbook has
them (E07-E09, E14) or at zero where they are new (Sitka); phase 5 adds them.

  1859   London repaid in full, London first (CR-068 CT26). The workbook's single debt pool
         already reaches $3.40m at the end of 1858 and $1.59m at the end of 1859 with the
         Reserve Fund at $3.29m, so no formula changes: E01 records the order.
  1862-  Paths D: every acceding territory joins at the exchange of 1867 (Q1-Q3, Q12;
         population phase 3, C1). Paths C: the population model's implied rate after C1 (D3).
  1866   E10 (peonage and captive compensation, treaties) re-dated from 1865 (CR-061 A2).
  1867-  E11: the $40m vendor credit over 1867-72 in equal sixths, the placeholder for
         lever L05 (CR-062 M2). E13 (Baja) switched off and kept for a separate test (Q12).
         E14 relabelled: the Senate declines the Treasury loan and the money is lent privately
         (CR-062 M3); its amount is lever L13 and is not changed here.
  new    E194 the Hudson's Bay and Puget Sound Agricultural companies' rights, 1861-62, at
         the historical award of $650,000 (Q6). E195-E196 the Sitka garrison and squadron and
         the northern mail from 1867, at zero (lever L04).
  kept   E19 ($25m, 1871-72) and E41 ($6m, 1888-89) already match CR-068 CT28. E20 (Pacifica
         replaces Richmond's surrendered toll revenue) is canon (§13, CR-039) and stays.
"""
from __future__ import annotations

import argparse
import copy
import csv
import tomllib
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment

ROOT = Path(__file__).resolve().parents[2]
AUTH = "CR-059-068 phase 4, 13 Nov 2026"
FIRST = 1846


def row_of(ws, year: int) -> int:
    return year - FIRST + 6


def event_row(ws, eid: str) -> int:
    for r in range(6, 401):
        if ws.cell(r, 1).value == eid:
            return r
    raise KeyError(eid)


def note(cell, text: str) -> None:
    cell.comment = Comment(text, AUTH)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--joins", default=str(ROOT / "population" / "data" / "joins_cr059_068.toml"))
    ap.add_argument("--rates", default=str(ROOT / "finance" / "build" / "paths_c_rates_cr059_068_final.csv"))
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    P, E, C = wb["Paths"], wb["Events"], wb["Changes"]

    # --- Paths D: territory joins (population phase 3, C1 and C2)
    j = tomllib.loads(Path(a.joins).read_text(encoding="utf-8"))
    by: dict[int, float] = {1856: float(j["hawaii_1856"])}
    for x in j["join"]:
        by[x["year"]] = by.get(x["year"], 0.0) + x["residents"]
    old = {y: P.cell(row_of(P, y), 4).value for y in range(1856, 1868)}
    assert old[1862] == 177000 and old[1867] == 50000, f"unexpected Paths D: {old}"
    for y in range(1846, 1933):
        c = P.cell(row_of(P, y), 4)
        if isinstance(c.value, (int, float)) or c.value is None:
            c.value = by.get(y, 0)
    note(P["D5"], "Residents who join Pacifica with territory: 1856 Hawaii (Confederation); 1867 the exchange: "
         "Oregon, Washington Territory, Idaho, Washoe, Deseret with southwest Wyoming, western Montana, New Mexico "
         "with Arizona and the San Luis Valley, South Park and the upper Arkansas, Alaska (350,036). Held territories "
         "are not counted before they accede (author, 13 Nov 2026). Sizes: population/data/joins_cr059_068.toml. "
         "Baja is out (E13 switched off). MODEL.")

    # --- Paths C: the population model's implied natural-increase rate after the change (D3)
    rates = {int(r["year"]): float(r["rate"]) for r in csv.DictReader(open(a.rates))}
    for y, v in rates.items():
        c = P.cell(row_of(P, y), 3)
        assert isinstance(c.value, (int, float)), (y, c.value)
        c.value = v

    # --- Events
    r = event_row(E, "E01")
    note(E.cell(r, 4), "CR-068 CT26 (author, 11 Nov 2026): the London bonds are repaid in full in the course of 1859, "
         "London first, with the Reserve Fund untouched before the war. The workbook's single debt pool gives $3.40m "
         "at the end of 1858 and $1.59m at the end of 1859 (Reserve Fund $3.29m): what remains is the Treasury's own "
         "bonds of 1846-52. No formula change.")
    r = event_row(E, "E10")
    assert E.cell(r, 2).value in (1865, "1865")
    E.cell(r, 2).value = 1866
    E.cell(r, 3).value = 1866
    note(E.cell(r, 2), "CR-061 A2: peon creditors paid a quarter of the registered face (cap $100 a peon), $50 a "
         "released captive, from the Confederal Treasury after the abolition ordinance of December 1865: paid in 1866.")
    r = event_row(E, "E11")
    E.cell(r, 2).value = 1867
    E.cell(r, 8).value = "=union_vendor/6"
    E.cell(r, 13).value = "$40m gold, 1867-72, first instalment at the exchange (CR-062 T4, M1)"
    note(E.cell(r, 8), "Equal sixths: the placeholder for lever L05, the split among CR-062 M2's options "
         "(a) $8m + 5 x $6.4m, (b) six of $6.67m, (c) $10m + 5 x $6m. Was 1866-72 in sevenths.")
    r = event_row(E, "E13")
    note(E.cell(r, 8), "Switched off (author, 13 Nov 2026, Q12): Baja is tested as a separate case. The case "
         "is $1m a year in 1867-71; restore 1 to test it.")
    E.cell(r, 8).value = 0
    r = event_row(E, "E14")
    E.cell(r, 4).value = "Private lending to the Union's bankers and the transit companies (the Treasury loan declined)"
    E.cell(r, 7).value = "Union (private)"
    note(E.cell(r, 4), "CR-062 M3 (author, 13 Nov 2026): the Senate declines the Treasury loan in April 1867 and "
         "the money is lent privately to New York and Philadelphia houses and the transit companies. The amount is "
         "lever L13 (phase 5); the old model's $10m stands until then.")
    for eid, amount in (("E19", 12.5), ("E41", 3)):
        assert float(E.cell(event_row(E, eid), 8).value) == amount, eid

    last = max(rr for rr in range(6, 401) if E.cell(rr, 1).value)
    assert E.cell(last, 1).value == "E193"
    new = [
        ("E194", 1861, 1862, "Hudson's Bay and Puget Sound Agricultural companies' rights south of the 49th",
         "Purchase", None, "Britain", 0.325, "Yes", "Proposed", "§10 (CR-059 P10)",
         "Bought openly by the Confederal Treasury after the occupation; the 1869 award as the price, $650,000 "
         "($450,000 and $200,000; to verify). Author, 13 Nov 2026 (Q6)."),
        ("E195", 1867, 1900, "Sitka garrison and squadron", "War & operations", None, None, 0, "No", "Proposed",
         "§14 (CR-062)", "Lever L04, at zero until phase 5."),
        ("E196", 1867, 1900, "Northern mail line to Sitka", "Subsidy & guarantee", None, None, 0, "No", "Proposed",
         "§14 (CR-062)", "Lever L04, at zero until phase 5."),
    ]
    for k, row in enumerate(new, start=1):
        rr = last + k
        for c in range(1, 14):
            E.cell(rr, c)._style = copy.copy(E.cell(last, c)._style)
        vals = list(row)
        for c, v in zip((1, 2, 3, 4, 5, 6, 7, 8), vals[:8]):
            E.cell(rr, c).value = v
        E.cell(rr, 9).value = f'=IF(H{rr}="","",H{rr}*(C{rr}-B{rr}+1))'
        E.cell(rr, 10).value, E.cell(rr, 11).value, E.cell(rr, 12).value, E.cell(rr, 13).value = vals[8:]

    # --- Changes log
    n = C.max_row + 1
    C.cell(n, 1).value = "13 Nov: CR-059-068"
    C.cell(n, 2).value = "Civil War CRs, fixed items"
    C.cell(n, 3).value = ("Model plan phase 4 (build/cr059_068_civil_war.py): Paths D, territories join at the 1867 "
                          "exchange (350,036; none in 1862-66); Paths C after it; E10 to 1866; E11 $40m in 1867-72 "
                          "(sixths, placeholder); E13 Baja off; E14 relabelled (private lending); E194 Hudson's Bay "
                          "rights 1861-62; E195-E196 Sitka at zero. London's 1859 repayment needs no change.")
    for c in range(1, 4):
        C.cell(n, c)._style = copy.copy(C.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
