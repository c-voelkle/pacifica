"""Phase 5: headroom 1859-1872 in the Story and Stress cases, with the binding check per year.

    python3 phase5_headroom.py STORY.xlsx STRESS.xlsx OUT.csv

Reads two recalculated workbooks (evaluate.py's <tag>_story.xlsx and <tag>_stress.xlsx). Before 1887
the checks that can fail are: Cash at target, Reserve Fund not negative, Bond markets can absorb them
(Checks L) and Private saving capacity (Checks AD). Cash is always brought to target by drawing the
Reserve Fund first and then borrowing, so the first two cannot fail; the room for one more $1m of
spending in a year is what is left of the Reserve Fund that year plus the smaller of the two margins:

  bond-market margin  = mkt_capacity x GDP + foreign_capacity + idle-gold source (L17) - bonds placed x issue price
  private-saving margin = Sources & uses L (private sources less private uses)

A $1m of extra spending raised by bonds cuts both margins by about $1m, so the smaller one binds. The
room is a one-year figure: spending in one year also raises later interest and repayment a little.
"""
from __future__ import annotations

import csv
import sys

import openpyxl

Y0, Y1, FIRST = 1859, 1872, 1846


def read(path: str) -> list[dict]:
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    lv, d, g, su, b, ec, ck = (wb[s] for s in ("Levers", "Debt & cash", "Gold & money", "Sources & uses",
                                               "Budget", "Economy", "Checks"))
    mkt, foreign, price = lv["E38"].value, lv["E39"].value, lv["E35"].value
    rows = []
    for y in range(Y0, Y1 + 1):
        r, s = y - FIRST + 6, y - FIRST + 135
        gdp = ec[f"O{r}"].value
        bonds = d[f"Y{r}"].value or 0
        idle = su[f"R{s}"].value or 0
        bond_m = mkt * gdp + foreign + idle - bonds * price
        priv_m = su[f"L{s}"].value
        rf_left = d[f"S{r - 1}"].value - d[f"F{r}"].value
        bind = "Bond markets can absorb them" if bond_m < priv_m else "Private saving capacity"
        rows.append({
            "year": y, "gdp": gdp, "receipts": b[f"M{r}"].value, "spending": b[f"Y{r}"].value,
            "balance": b[f"Z{r}"].value, "cash_gap": d[f"M{r}"].value - d[f"E{r}"].value,
            "rf_drawn": d[f"F{r}"].value, "borrowed": d[f"G{r}"].value, "bonds_placed": bonds,
            "reserve_fund": d[f"S{r}"].value, "public_debt": d[f"R{r}"].value, "gold": g[f"F{r}"].value,
            "gold_paid_out": g[f"E{r}"].value, "gold_above_cover": g[f"K{r}"].value, "idle_gold_source": idle,
            "bond_margin": bond_m, "private_margin": priv_m, "rf_left": rf_left,
            "room": rf_left + min(bond_m, priv_m), "binding": bind,
            "checks_failing": [ck.cell(4, c).value for c in range(2, 32) if ck.cell(r, c).value == "Check"],
        })
    return rows


def main() -> None:
    story, stress, out = sys.argv[1:4]
    allrows = []
    for case, path in (("Story", story), ("Stress", stress)):
        for row in read(path):
            allrows.append({"case": case, **row})
    keys = list(allrows[0].keys())
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in allrows:
            w.writerow({k: (round(v, 2) if isinstance(v, float) else v) for k, v in row.items()})
    for case in ("Story", "Stress"):
        print(f"\n{case}: year | spending | borrowed | RF end | debt | gold paid out | bond margin | private margin | room | binding")
        for row in (x for x in allrows if x["case"] == case):
            print(f"{row['year']} | {row['spending']:.1f} | {row['borrowed']:.1f} | {row['reserve_fund']:.1f} | "
                  f"{row['public_debt']:.1f} | {row['gold_paid_out']:.1f} | {row['bond_margin']:.1f} | "
                  f"{row['private_margin']:.1f} | {row['room']:.1f} | {row['binding']}"
                  + (f" | FAILING {row['checks_failing']}" if row["checks_failing"] else ""))


if __name__ == "__main__":
    main()
