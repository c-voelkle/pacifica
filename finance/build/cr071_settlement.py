"""CR-071 Part C, C5: the interior settlement programme of 1867-1887 (17 November 2026).

    python3 finance/build/cr071_settlement.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after deseret_gathering.py (the last step of cr057_rebuild_pair.py). The script
never recalculates; run LibreOffice afterwards. With --off the master lever sp_on is saved at 0 in
both cases, which must reproduce IN's values exactly (every row's amount is multiplied by sp_on).

Authorization: the author, 17 November 2026, 09:14 ("2, 3, 4, 5, 6, and 7 are approved as
proposed"; item 7: build the programme's figures into the workbook). Amounts MODEL; their derivation
is population/settlement_1887.py (population/outputs/settlement_1887.md).

What is already in the workbook and is not added again:
- the people: the population model's 1887 total is fixed; the programme decides where they settle;
- assisted passage: People T (assisted arrivals, about 1.07 million in 1867-87) x assist_cost, in
  Budget T (Settlement & immigration), already costs more than the programme's own passage line, and
  the recruiting offices are inside that cost per assisted arrival;
- the members' land: the Members' land sheet (L15) sells our timeline's census farm acreage from 1867.

What this adds, as Events rows (Events is read by the Budget, Debt & cash and Saving):
- the irrigation districts' dams and canals, lent on Development Fund credit 1872-1887 (Investment),
  and the districts' repayments from water rates 1877-1906 (Receipt), the loss share never repaid;
- the land sold early: the programme sells about 16.9m acres of the interior in 1867-87 at about $1.35,
  ahead of L15's path, on five-year instalments (Receipt, 1870-1891); those acres are then missing
  from L15's later sales at L15's later price (a negative Receipt, 1892-1911). The net is the cost
  of selling the interior cheap to fill it.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "the author, 17 November 2026, 09:14"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-071 C5: the interior settlement programme, 1867-87 (17 Nov 2026) —",
    ("sp_on", "Settlement programme: 1 = on; 0 = the input workbook exactly", 1, 1, "switch",
     "Author, 17 Nov 2026, 09:14", "0 reproduces the input workbook exactly. 1 adds the Events rows of CR-071 C5."),
    ("sp_irr_cap", "Settlement programme: irrigation districts' capital lent, 1872-87 ($m)", 11.2, 11.2, "$m",
     "Story assumption (MODEL)", "About 0.94m acres at $12 (population/settlement_1887.py)."),
    ("sp_irr_loss", "Settlement programme: share of the districts' loans never repaid", 0.25, 0.40, "share",
     "Story assumption (MODEL)", "Defaults and the interest forgone. Stress: 40%."),
    ("sp_acres", "Settlement programme: interior acres sold early, 1867-87 (m)", 16.9, 16.9, "m acres",
     "Story assumption (MODEL)", "About 105,000 farms of 160 acres for the 1.17m extra people of 1887."),
    ("sp_price", "Settlement programme: average price of the early sales ($ an acre)", 1.35, 1.25, "$ an acre",
     "Story assumption (MODEL)", "The Land Fund's floor binds to about 1880 (CR-033); Stress: the floor throughout."),
    ("sp_later_price", "Settlement programme: L15's price for the same acres later ($ an acre)", 2.46, 2.46, "$ an acre",
     "Members' land M, 1900", "What the same acres would have fetched on L15's path, about 1900."),
]

ROWS = [
    # (id, start, end, label, category, formula for H)
    ("E243", 1872, 1887, "Irrigation districts' dams and canals, lent on Development Fund credit (CR-071 C5)", "Investment",
     "=sp_on*sp_irr_cap/16"),
    ("E244", 1877, 1906, "Irrigation districts' repayments from water rates (CR-071 C5)", "Receipt",
     "=sp_on*sp_irr_cap*(1-sp_irr_loss)/30"),
    ("E245", 1870, 1891, "Interior farms sold early under the settlement programme, instalments (CR-071 C5)", "Receipt",
     "=sp_on*sp_acres*sp_price*0.9/22"),
    ("E246", 1892, 1911, "The same acres missing from the members' land sales later (CR-071 C5)", "Receipt",
     "=-sp_on*sp_acres*sp_later_price*0.9/20"),
]


def add_rows(wb) -> None:
    E = wb["Events"]
    used = [r for r in range(6, 401) if E.cell(r, 1).value or E.cell(r, 2).value]
    r = max(used) + 1
    ids = {E.cell(x, 1).value for x in used}
    for rid, a, b, label, cat, h in ROWS:
        if rid in ids:
            raise SystemExit(f"Events already has {rid}")
        for c in range(1, 12):
            E.cell(r, c)._style = copy.copy(E.cell(r - 1, c)._style)
        E.cell(r, 1).value = rid
        E.cell(r, 2).value = a
        E.cell(r, 3).value = b
        E.cell(r, 4).value = label
        E.cell(r, 5).value = cat
        E.cell(r, 8).value = h
        E.cell(r, 9).value = f'=IF(H{r}="","",H{r}*(C{r}-B{r}+1))'
        E.cell(r, 10).value = "No"
        E.cell(r, 11).value = "Proposed"
        r += 1
        if r > 400:
            raise SystemExit("Events table full")


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "17 Nov: CR-071 C5"
    Ch.cell(n, 2).value = "The interior settlement programme, 1867-87"
    Ch.cell(n, 3).value = ("Master lever sp_on (at 0 the input workbook exactly). Events E243-E246: irrigation districts lent on "
                           "Development Fund credit and repaid; the interior's farms sold early and missing from L15's later sales. "
                           "Assisted passage is already in Budget T. MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["sp_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "Deseret" not in wb.sheetnames:
        raise SystemExit("needs the workbook after deseret_gathering.py")
    if "sp_on" in wb.defined_names:
        raise SystemExit("settlement programme already added")
    base.add_levers(wb, LEVERS)
    add_rows(wb)
    log(wb, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, Events E243-E246")


if __name__ == "__main__":
    main()
