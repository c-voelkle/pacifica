"""CR-074: the Pacific Companies in the workbook (18 November 2026).

    python3 finance/build/cr074_companies.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after cr071_settlement.py (the last step of cr057_rebuild_pair.py). The script
never recalculates; run LibreOffice afterwards. With --off the master lever cp_on is saved at 0 in
both cases, which must reproduce IN's values exactly (every row's amount is multiplied by cp_on).

Authorization: the author, 18 November 2026, 12:02 ("You can proceed with the integration and then
add the model rows"). Amounts MODEL; the scale comes from CR-074 F ("about 2,000-3,000 men abroad at
any time between 1888 and 1914, about 25,000 served by 1914, about 9,000 warrants redeemed by 1914")
and E (half a farm for five years, a whole farm for ten).

What this adds, as Events rows (Events is read by the Budget, Debt & cash and Saving):
- Ward's bequest of ten thousand taels' worth in gold to the Republic's Treasury, paid out of what the
  consul recovers from the disputed debts (Receipt, 1868);
- the companies' school at Sacramento and the Companies Office (Programme, 1888-1932);
- the Land Fund receipts forgone on the warrants: land given for service instead of sold (a negative
  Receipt, 1893-1932: the first warrants fall due five years after the Act);
- the home half: interest paid on the deposits net of what the Land Fund earns on them (Programme,
  1888-1932).

What is not added, and why:
- the hosts' pay and the prize money of 1878 and 1914 are private income, not Treasury cash;
- the Philippine companies' warrants are the dependency's land, outside the Realm's budget;
- the men abroad are too few to move the population model (2,000-3,000 against about 37 million).
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "the author, 18 November 2026, 12:02"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-074: the Pacific Companies (18 Nov 2026) —",
    ("cp_on", "Pacific Companies: 1 = on; 0 = the input workbook exactly", 1, 1, "switch",
     "Author, 18 Nov 2026, 12:02", "0 reproduces the input workbook exactly. 1 adds the Events rows of CR-074."),
    ("cp_ward_taels", "Pacific Companies: Ward's bequest to the Treasury (taels)", 10000, 10000, "taels",
     "CR-074 L2.7 (APPROVED)", "Ten thousand taels' worth in gold, paid out of what the consul recovers (value, not weight)."),
    ("cp_tael_usd", "Pacific Companies: dollars per Shanghai tael, 1860s", 1.39, 1.39, "$ a tael",
     "Story assumption (MODEL)", "About $1.39 to the Shanghai tael in the 1860s (the Haikwan tael was worth more)."),
    ("cp_cadets", "Pacific Companies: cadets through the Sacramento school a year", 500, 500, "persons",
     "Story assumption (MODEL)", "About 2,500 men abroad on five-year engagements."),
    ("cp_cadet_cost", "Pacific Companies: cost per cadet-year, school and Office ($)", 360, 480, "$",
     "Story assumption (MODEL)", "Keep, instructors, horses, arms and the Office's clerks. Stress: a third more."),
    ("cp_warrants", "Pacific Companies: warrants redeemed a year from 1893", 410, 410, "warrants",
     "CR-074 F (MODEL)", "About 9,000 by 1914 (22 years). The first warrants fall due in 1893, five years into the Act."),
    ("cp_warrant_acres", "Pacific Companies: average acres per warrant", 55, 55, "acres",
     "CR-074 E (MODEL)", "Half farms (40 irrigated or 80 dry) and whole farms (80 or 160), mostly irrigated half farms."),
    ("cp_warrant_price", "Pacific Companies: the Land Fund's price for the same acres ($ an acre)", 3.5, 5.0, "$ an acre",
     "Land Fund, 1888-1914 (MODEL)", "Between L15's prices of 1890 and 1910. Stress: the higher prices of the 1900s."),
    ("cp_abroad", "Pacific Companies: men abroad at any time", 2500, 2500, "persons",
     "CR-074 F (MODEL)", "2,000-3,000 between 1888 and 1914."),
    ("cp_pay", "Pacific Companies: a company man's yearly pay from the host ($)", 360, 360, "$",
     "Story assumption (MODEL)", "At least the Realm's benchmark (CR-038)."),
    ("cp_spread", "Pacific Companies: interest on the home half net of the Land Fund's earnings", 0.01, 0.02, "share",
     "Story assumption (MODEL)", "Half the pay held for an average of 2.5 years."),
]

ROWS = [
    # (id, start, end, label, category, formula for H, section)
    ("E247", 1868, 1868, "Ward's bequest in gold to the Republic's Treasury, out of the debts recovered (CR-074)", "Receipt",
     "=cp_on*cp_ward_taels*cp_tael_usd/1000000", "§19"),
    ("E248", 1888, 1932, "The companies' school at Sacramento and the Companies Office (CR-074)", "Programme",
     "=cp_on*cp_cadets*cp_cadet_cost/1000000", "§25"),
    ("E249", 1893, 1932, "Land Fund receipts forgone on the companies' warrants (CR-074)", "Receipt",
     "=-cp_on*cp_warrants*cp_warrant_acres*cp_warrant_price/1000000", "§25"),
    ("E250", 1888, 1932, "The home half: interest net of the Land Fund's earnings (CR-074)", "Programme",
     "=cp_on*cp_abroad*cp_pay*0.5*2.5*cp_spread/1000000", "§25"),
]


def add_rows(wb) -> None:
    E = wb["Events"]
    used = [r for r in range(6, 401) if E.cell(r, 1).value or E.cell(r, 2).value]
    r = max(used) + 1
    ids = {E.cell(x, 1).value for x in used}
    for rid, a, b, label, cat, h, sec in ROWS:
        if rid in ids:
            raise SystemExit(f"Events already has {rid}")
        for c in range(1, 13):
            E.cell(r, c)._style = copy.copy(E.cell(r - 1, c)._style)
        E.cell(r, 1).value = rid
        E.cell(r, 2).value = a
        E.cell(r, 3).value = b
        E.cell(r, 4).value = label
        E.cell(r, 5).value = cat
        E.cell(r, 8).value = h
        E.cell(r, 9).value = f'=IF(H{r}="","",H{r}*(C{r}-B{r}+1))'
        E.cell(r, 10).value = "Yes" if rid == "E247" else "No"
        E.cell(r, 11).value = "Approved"
        E.cell(r, 12).value = sec
        r += 1
        if r > 400:
            raise SystemExit("Events table full")


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "18 Nov: CR-074"
    Ch.cell(n, 2).value = "The Pacific Companies"
    Ch.cell(n, 3).value = ("Master lever cp_on (at 0 the input workbook exactly). Events E247-E250: Ward's bequest in gold (1868); "
                           "the school at Sacramento and the Companies Office; the Land Fund receipts forgone on the warrants; "
                           "the home half's net interest. The hosts' pay and the prize money are private income, not added. MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["cp_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "sp_on" not in wb.defined_names:
        raise SystemExit("needs the workbook after cr071_settlement.py")
    if "cp_on" in wb.defined_names:
        raise SystemExit("the Pacific Companies already added")
    base.add_levers(wb, LEVERS)
    add_rows(wb)
    log(wb, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, Events E247-E250")


if __name__ == "__main__":
    main()
