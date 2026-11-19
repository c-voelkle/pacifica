"""CR-076: drink, the duty schedule and coffee in the workbook (19 November 2026).

    python3 finance/build/cr076_drink_coffee.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after cr074_companies.py. The script never recalculates; run LibreOffice afterwards.
Adds a memo sheet "Drink & coffee" that reads People, Prices, Budget and Economy and feeds nothing,
so every value outside Levers, Changes and the new sheet is unchanged (option 1, approved by the
author 19 November 2026, 20:34: "Option 1 mortality lever off is approved"). With --off the master
lever dc_on is saved at 0 and the sheet's amounts are zero.

What the sheet shows, year by year 1846-1932 (all MODEL):
- pure alcohol drunk per resident by period and its split between spirits, wine and beer;
- the duty per gallon of pure alcohol on spirits by period (CR-076 R1-1: about $1.875 in 1852-66,
  $3.50 in 1867-87, $6.375 from 1888, reset every five years with Pacifica's price level), beer and
  wine at their band ratios, the share actually collected (evasion by period);
- the duty, the Spirit Stores' surplus (county option before 1888), the homelands' stores' share;
- the duty as a share of domestic taxes, checked against a ceiling of 35%;
- coffee: pounds per resident, the Realm's consumption, the crops of Kona and the Philippines that
  reach the Realm, the share grown under the Pacific crowns and the import bill.

Not modelled (author's decision): the mortality lever (off); the county earmark is shown as a memo,
since county money is not Treasury money; domestic taxes stay the existing share of non-mining GDP
(the duty is a part of them, not an addition).
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "the author, 19 November 2026, 20:34"
base.AUTHOR = AUTHOR
S = "CR-076 (MODEL)"

LEVERS = [
    "— CR-076: drink, the duty schedule and coffee (19 Nov 2026) —",
    ("dc_on", "Drink & coffee: 1 = on; 0 = amounts zero (the sheet feeds nothing either way)", 1, 1, "switch",
     "Author, 19 Nov 2026, 20:34", "A memo sheet: no other sheet reads it."),
    ("dc_pa_1", "Drink: pure alcohol per resident, 1846-66 (US gallons)", 2.2, 2.6, "gal", S, "Gold-rush drinking."),
    ("dc_pa_2", "Drink: pure alcohol per resident, 1867-87", 1.4, 1.6, "gal", S, "After the members' acts."),
    ("dc_pa_3", "Drink: pure alcohol per resident, 1888-1914", 0.9, 1.1, "gal", S, "The Spirit Stores and the halls."),
    ("dc_pa_4", "Drink: pure alcohol per resident, 1915-32", 0.75, 0.9, "gal", S, "Below the Union's level."),
    ("dc_sp_1", "Drink: spirits' share of pure alcohol, 1846-66", 0.70, 0.70, "share", S, "Whiskey and brandy country."),
    ("dc_sp_2", "Drink: spirits' share, 1867-87", 0.50, 0.55, "share", S, "The ladder moves drinkers to beer and wine."),
    ("dc_sp_3", "Drink: spirits' share, 1888-1914", 0.35, 0.40, "share", S, ""),
    ("dc_sp_4", "Drink: spirits' share, 1915-32", 0.30, 0.35, "share", S, ""),
    ("dc_wi_1", "Drink: wine's share of pure alcohol, 1846-66", 0.10, 0.10, "share", S, "Beer is the remainder."),
    ("dc_wi_2", "Drink: wine's share, 1867-87", 0.15, 0.15, "share", S, ""),
    ("dc_wi_3", "Drink: wine's share, 1888-1914", 0.20, 0.20, "share", S, ""),
    ("dc_wi_4", "Drink: wine's share, 1915-32", 0.25, 0.25, "share", S, ""),
    ("dc_duty_1", "Drink: spirits duty per gallon of pure alcohol, 1852-66 ($)", 1.875, 1.875, "$", "CR-076 R1-1 (APPROVED; MODEL)",
     "About 75 cents on a gallon of 40% whiskey: about half the retail price, at the peak for weak enforcement."),
    ("dc_duty_2", "Drink: spirits duty per gallon of pure alcohol, 1867-87 ($)", 3.50, 3.50, "$", "CR-076 R1-1 (APPROVED; MODEL)",
     "About $1.40 on a gallon of 40% whiskey: about seven-tenths of the retail price."),
    ("dc_duty_3", "Drink: spirits duty per gallon of pure alcohol from 1888, in 1888 prices ($)", 6.375, 6.375, "$",
     "CR-076 R1-1 (APPROVED; MODEL)", "About $2.55 on a gallon of 40% whiskey: 85% of the Stores' price; reset every five years with the price level."),
    ("dc_beer_rel", "Drink: beer's duty per unit of alcohol against spirits'", 0.13, 0.13, "ratio", "CR-076 R1-1 bands (MODEL)",
     "Beer at 5%: about 4 cents a gallon in 1888."),
    ("dc_wine_rel", "Drink: wine's duty per unit of alcohol against spirits'", 0.26, 0.26, "ratio", "CR-076 R1-1 bands (MODEL)",
     "Table wine at 12%: about 20 cents a gallon in 1888; fortified wine folded in."),
    ("dc_coll_1", "Drink: share of the duty collected, 1852-66", 0.60, 0.50, "share", S, "Porous diggings and smuggling."),
    ("dc_coll_2", "Drink: share collected, 1867-87", 0.80, 0.70, "share", S, "Sealed stills, rotated gaugers."),
    ("dc_coll_3", "Drink: share collected from 1888", 0.95, 0.90, "share", S, "No untaxed retail left."),
    ("dc_margin", "Drink: Spirit Stores' surplus per gallon of pure alcohol, 1888 prices ($)", 0.625, 0.50, "$", S,
     "About 25 cents on a gallon of whiskey after salaries and the fixed return."),
    ("dc_county", "Drink: share of spirits sold through county stores, 1867-87", 0.30, 0.20, "share", S, "The county option."),
    ("dc_home", "Drink: share of the duty kept by the nations' own stores", 0.015, 0.015, "share", S, "Kept by the nations (F3)."),
    ("dc_cap", "Drink: ceiling for the duty as a share of domestic taxes (check)", 0.35, 0.35, "share", S,
     "Britain and the Union drew about a third of revenue from drink in the period."),
    ("dc_lb_1", "Coffee: pounds per resident before 1888", 8, 7, "lb", S, ""),
    ("dc_lb_2", "Coffee: pounds per resident, 1888-1914", 12, 11, "lb", S, ""),
    ("dc_lb_3", "Coffee: pounds per resident in 1915", 14, 13, "lb", S, "Rising to 15-18 lb by the late 1920s (CR-076 L4)."),
    ("dc_lb_step", "Coffee: yearly rise in pounds per resident from 1915", 0.2, 0.15, "lb", S, ""),
    ("dc_haw_base", "Coffee: Hawaii's crop reaching the Realm, 1856-89 (t)", 300, 300, "t", S, ""),
    ("dc_haw_step", "Coffee: yearly growth of Hawaii's crop from 1890 (t)", 550, 300, "t", S, "30,000-40,000 acres by 1930 (L4)."),
    ("dc_ph_pre", "Coffee: Philippine crop reaching the Realm, 1876-88 (t)", 8000, 6000, "t", S, "Before the rust of 1889."),
    ("dc_ph_low", "Coffee: Philippine crop reaching the Realm, 1889-97 (t)", 3000, 2000, "t", S, "The rust; Batangas's old trees lost."),
    ("dc_ph_step", "Coffee: yearly growth of the Philippine crop to the Realm from 1898 (t)", 1300, 900, "t", S, ""),
    ("dc_ph_cap", "Coffee: cap on the Philippine crop to the Realm (t)", 36000, 24000, "t", S, "Of a crop of 30,000-60,000 t (L4)."),
    ("dc_cof_price", "Coffee: world price ($ a lb, green)", 0.15, 0.17, "$", S, "Halved in 1931-32 (Brazil's surplus)."),
]

HEAD = ["Year", "Residents (end of year)", "Price level (1913 = 1)", "Pure alcohol per resident (gal)",
        "Spirits' share", "Wine's share", "Beer's share", "Spirits duty per gal of pure alcohol ($)",
        "Share collected", "Drink duty ($m)", "Spirit Stores' surplus ($m)", "Of which kept by the nations' stores ($m)",
        "Duty + surplus ($m)", "Domestic taxes ($m, Budget)", "Duty / domestic taxes", "Check: under the ceiling",
        "Coffee per resident (lb)", "Coffee drunk in the Realm (t)", "Hawaii's crop to the Realm (t)",
        "Philippine crop to the Realm (t)", "Grown under the Pacific crowns / drunk", "Coffee import bill ($m)",
        "Import bill / GDP"]


def era(y_ref: str, a: str, b: str, c: str, d: str) -> str:
    return f"IF({y_ref}<1867,{a},IF({y_ref}<1888,{b},IF({y_ref}<1915,{c},{d})))"


def build_sheet(wb) -> None:
    if "Drink & coffee" in wb.sheetnames:
        raise SystemExit("Drink & coffee already exists")
    ws = wb.create_sheet("Drink & coffee")
    ws["A1"] = "Drink & coffee"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = ("CR-076: the drink duty, the Spirit Stores and coffee, $m. A memo sheet: it reads People, Prices, Budget and "
                "Economy and feeds nothing. The duty is part of domestic taxes, not an addition. All amounts MODEL.")
    ws["A3"] = "Rows run 1846-1932. Levers dc_* on the Levers sheet. Checks in Y5:Z12."
    for c, h in enumerate(HEAD, start=1):
        cell = ws.cell(5, c, h)
        cell.font = Font(bold=True)
    for r in range(6, 93):
        y = f"A{r}"
        ws[f"A{r}"] = 1840 + r
        ws[f"B{r}"] = f"=People!L{r}"
        ws[f"C{r}"] = f"=Prices!C{r}"
        ws[f"D{r}"] = "=" + era(y, "dc_pa_1", "dc_pa_2", "dc_pa_3", "dc_pa_4")
        ws[f"E{r}"] = "=" + era(y, "dc_sp_1", "dc_sp_2", "dc_sp_3", "dc_sp_4")
        ws[f"F{r}"] = "=" + era(y, "dc_wi_1", "dc_wi_2", "dc_wi_3", "dc_wi_4")
        ws[f"G{r}"] = f"=1-E{r}-F{r}"
        # spirits duty per gal PA: none before 1852; 1852-66; 1867-87; from 1888 reset every five years
        reset = f"INDEX(Prices!$C$6:$C$92,1888+5*INT(({y}-1888)/5)-1845)/INDEX(Prices!$C$6:$C$92,1888-1845)"
        ws[f"H{r}"] = (f"=IF({y}<1852,0,IF({y}<1867,dc_duty_1,IF({y}<1888,dc_duty_2,dc_duty_3*{reset})))")
        ws[f"I{r}"] = "=" + f"IF({y}<1867,dc_coll_1,IF({y}<1888,dc_coll_2,dc_coll_3))"
        ws[f"J{r}"] = (f"=dc_on*B{r}*D{r}*H{r}*I{r}*(E{r}+F{r}*dc_wine_rel+G{r}*dc_beer_rel)/1000000")
        ws[f"K{r}"] = (f"=dc_on*B{r}*D{r}*E{r}*IF({y}<1867,0,IF({y}<1888,dc_county,1))*dc_margin"
                       f"*INDEX(Prices!$C$6:$C$92,MAX({y},1888)-1845)/INDEX(Prices!$C$6:$C$92,1888-1845)/1000000")
        ws[f"L{r}"] = f"=J{r}*dc_home"
        ws[f"M{r}"] = f"=J{r}+K{r}"
        ws[f"N{r}"] = f"=Budget!C{r}"
        ws[f"O{r}"] = f'=IF(N{r}>0,J{r}/N{r},"")'
        ws[f"P{r}"] = f'=IF(O{r}="","",IF(O{r}<=dc_cap,"ok","FAIL"))'
        ws[f"Q{r}"] = f"=IF({y}<1888,dc_lb_1,IF({y}<1915,dc_lb_2,dc_lb_3+({y}-1915)*dc_lb_step))"
        ws[f"R{r}"] = f"=dc_on*B{r}*Q{r}*0.45359237/1000"
        ws[f"S{r}"] = f"=dc_on*IF({y}<1856,0,IF({y}<1890,dc_haw_base,dc_haw_base+({y}-1889)*dc_haw_step))"
        ws[f"T{r}"] = (f"=dc_on*IF({y}<1876,0,IF({y}<1889,dc_ph_pre,IF({y}<1898,dc_ph_low,"
                       f"MIN(dc_ph_cap,dc_ph_low+({y}-1897)*dc_ph_step))))")
        ws[f"U{r}"] = f'=IF(R{r}>0,MIN(1,(S{r}+T{r})/R{r}),"")'
        ws[f"V{r}"] = (f"=MAX(0,R{r}-S{r}-T{r})*2204.62*dc_cof_price*IF({y}>=1931,0.5,1)/1000000")
        ws[f"W{r}"] = f'=IF(Economy!O{r}>0,V{r}/Economy!O{r},"")'
        for c in (4, 5, 6, 7, 9, 15, 21):
            ws.cell(r, c).number_format = "0.00"
        for c in (8, 10, 11, 12, 13, 14, 22):
            ws.cell(r, c).number_format = "#,##0.0"
        for c in (2, 18, 19, 20):
            ws.cell(r, c).number_format = "#,##0"
        ws.cell(r, 23).number_format = "0.000%"
    checks = [
        ("Largest duty / domestic taxes, 1852-1932", "=MAX(O12:O92)"),
        ("Years over the ceiling", '=COUNTIF(P12:P92,"FAIL")'),
        ("Duty / domestic taxes, 1888", "=O48"),
        ("Duty / domestic taxes, 1929", "=O89"),
        ("Coffee per resident, 1929 (lb; CR-076: 15-18)", "=Q89"),
        ("Grown under the crowns / drunk, 1929 (CR-076: about a fifth; 15-30%)", "=U89"),
        ("Check: coffee 1929 inside CR-076's ranges", '=IF(AND(Q89>=15,Q89<=18,U89>=0.15,U89<=0.30),"ok","FAIL")'),
    ]
    ws["Y5"] = "Checks"
    ws["Y5"].font = Font(bold=True)
    for i, (lab, f) in enumerate(checks, start=6):
        ws[f"Y{i}"] = lab
        ws[f"Z{i}"] = f
        ws[f"Z{i}"].number_format = "0.0%" if "/" in lab and "lb" not in lab else "0.00"
    ws.column_dimensions["A"].width = 7
    for col in "BCDEFGHIJKLMNOPQRSTUVW":
        ws.column_dimensions[col].width = 14
    ws.column_dimensions["Y"].width = 60
    ws.freeze_panes = "B6"


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "19 Nov: CR-076"
    Ch.cell(n, 2).value = "Drink, the duty schedule and coffee"
    Ch.cell(n, 3).value = ("Memo sheet 'Drink & coffee' (feeds nothing; option 1, author 20:34) and levers dc_*: pure alcohol per "
                           "resident and its split, the duty schedule of R1-1 with the five-yearly reset, collection, the Spirit "
                           "Stores' surplus, the nations' share, the duty against domestic taxes (ceiling 35%), coffee consumption, "
                           "the crowns' crops and the import bill. Mortality lever not built (off). MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["dc_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "cp_on" not in wb.defined_names:
        raise SystemExit("needs the workbook after cr074_companies.py")
    if "dc_on" in wb.defined_names:
        raise SystemExit("CR-076 already added")
    base.add_levers(wb, LEVERS)
    build_sheet(wb)
    log(wb, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, sheet 'Drink & coffee'")


if __name__ == "__main__":
    main()
