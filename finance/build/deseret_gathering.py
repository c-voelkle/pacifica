"""Deseret: the gathering and the Saints' birth rate (16 November 2026).

    python3 finance/build/deseret_gathering.py IN.xlsx OUT.xlsx [--off]

IN is the CR-057 growth workbook built on the Civil War CRs (cr057_growth_engine.py inside
cr057_rebuild_pair.py). The script never recalculates; run LibreOffice afterwards. With --off the
master lever dg_on is saved at 0 in both cases, which must reproduce IN's values exactly.

Authorization: the author, 16 November 2026, 07:02 ("Yes go ahead and add it"), on the proposal of
06:57. In this timeline no Edmunds-Tucker Act dissolves the Perpetual Emigrating Fund (1887) and
confederal law imposes no single marriage system (CR-060), so the gathering of converts to Deseret
goes on after 1887. Story assumption; amounts MODEL.

What the sheet adds, on top of the generic Pacifican rates that Deseret's residents already
follow from their join in 1867 (population/data/joins_cr059_068.toml):
- the gathering: convert arrivals from 1888 (input schedule, mostly from Britain, Scandinavia,
  Germany, the Netherlands and Switzerland), into People E with a small return share;
- the Saints' higher birth rate: a premium on natural increase applied to the Saints' memo stock
  (the 1867 Saints plus the gathering, with descendants), into People D.
Plural marriage itself adds no births: wives in plural unions had slightly fewer children each
(Smith and Kunz 1976; Moorad et al. 2011), so the premium is the Saints' fertility, not polygyny.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402
import cr051_054_055_champions as c51  # noqa: E402

AUTHOR = "the author, 16 November 2026, 07:02"
base.AUTHOR = AUTHOR
row = c51.row
YEARS = c51.YEARS

DESERET_1867 = 68932  # joins_cr059_068.toml: Utah, 1860 and 1870 censuses log-linear to 1867


def schedule(y: int) -> float:
    """Convert arrivals a year in the gathering after 1887 (story assumption).

    Before 1888 the historical gathering is inside the generic streams. The Perpetual Emigrating
    Fund aided about 100,000 emigrants over 1849-1887 (about 2,600 a year); here it continues,
    rises with the missions in northern Europe, falls in the war and ends by 1929, when the
    Church's counsel turns, as it did historically somewhat earlier, to building Zion at home.
    """
    if 1888 <= y <= 1899:
        return 2500
    if 1900 <= y <= 1914:
        return 3500
    if 1915 <= y <= 1918:
        return 1000
    if 1919 <= y <= 1925:
        return 3000
    return {1926: 2000, 1927: 1500, 1928: 1000}.get(y, 0)


LEVERS = [
    "— Deseret: the gathering and the Saints' birth rate (16 Nov 2026) —",
    ("dg_on", "Deseret: 1 = the gathering and the Saints' birth premium on; 0 = the input workbook exactly", 1, 1, "switch",
     "Author, 16 Nov 2026, 07:02",
     "0 reproduces the input workbook exactly. 1 adds the Deseret sheet's convert arrivals to People E and its extra births to People D."),
    ("dg_scale", "Deseret: gathering arrivals × the sheet's schedule", 1.0, 0.5, "multiple",
     "Story assumption (MODEL)",
     "The schedule (Deseret B) continues the Perpetual Emigrating Fund's historical rate (about 100,000 aided in 1849-1887) "
     "after 1887. Stress halves it."),
    ("dg_prem", "Deseret: the Saints' natural increase above Pacifica's (per year)", 0.006, 0.003, "rate",
     "Story assumption (MODEL)",
     "Utah's birth rate stayed well above the US average into the 20th century; the premium is over Pacifica's own rate "
     "(Paths C), which is already above the US's. Plural marriage adds no births by itself (Smith and Kunz 1976)."),
    ("dg_share", "Deseret: Saints' share of Deseret's residents at the join of 1867", 0.95, 0.95, "share",
     "Story assumption (MODEL)", "Utah in 1867 was overwhelmingly Latter-day Saint."),
    ("dg_ret", "Deseret: share of gathered converts who leave again", 0.05, 0.10, "share",
     "Story assumption (MODEL)", "Converts came to stay; the general Americas and Europe return rate (Paths I) does not apply."),
]


def build(wb) -> c51.Sheet:
    S = c51.Sheet(wb, "Deseret", after="Members' land",
                  title="Deseret: the gathering and the Saints' birth rate",
                  purpose=("The gathering of converts to Deseret continues after 1887 (no Edmunds-Tucker Act), and the Saints' "
                           "natural increase runs above Pacifica's. Adds to People D and E; amounts MODEL."))
    S.ws["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. "
                        "Built by finance/build/deseret_gathering.py; all amounts MODEL.")
    S.add("sched", "Convert arrivals in the gathering (schedule)", lambda y, r: schedule(y), is_input=True,
          group="The gathering", note="Story assumption; see the build script's docstring.", fmt="#,##0")
    S.add("arr", "Convert arrivals", lambda y, r: f"={S.cols['sched']}{r}*dg_scale*dg_on", fmt="#,##0")
    S.add("join", "Saints joining with Deseret", lambda y, r: f"=IF($A{r}=1867,{DESERET_1867}*dg_share,0)", fmt="#,##0",
          group="The Saints in Pacifica")
    def stock(y, r):
        prev = f"{S.cols['stock']}{r - 1}" if y > 1846 else "0"
        return (f"={prev}*(1+Paths!C{r}+dg_prem*dg_on)+{S.cols['join']}{r}"
                f"+{S.cols['arr']}{r}*(1-dg_ret)")
    S.cols["stock"] = c51.col(S.n + 1)
    S.add("stock", "Saints in Pacifica (memo)", stock, fmt="#,##0",
          note="Last year's stock × (1 + Pacifica's natural increase + the premium), plus the join of 1867 and the gathering net of returns.")
    S.add("births", "Extra births from the Saints' premium",
          lambda y, r: f"={S.cols['stock']}{r - 1}*dg_prem*dg_on" if y > 1846 else "=0", fmt="#,##0",
          note="Added to People D.")
    S.add("share", "Saints' share of Pacifica's residents",
          lambda y, r: f"=IF(People!L{r}>0,{S.cols['stock']}{r}/People!L{r},0)", fmt="0.0%")
    return S


def link(wb, S: c51.Sheet) -> None:
    P = wb["People"]
    for y in YEARS:
        r = row(y)
        d, e, i = P.cell(r, 4), P.cell(r, 5), P.cell(r, 9)
        for c_ in (d, e, i):
            assert isinstance(c_.value, str) and c_.value.startswith("="), (y, c_.coordinate, c_.value)
        if "Deseret!" in d.value:
            raise SystemExit("People already linked to the Deseret sheet")
        d.value = f"{d.value}+Deseret!{S.cols['births']}{r}"
        e.value = f"={e.value[1:]}+Deseret!{S.cols['arr']}{r}"
        expected = f"=E{r}*Paths!I{r}+(F{r}+G{r}+H{r})*dep_asia"
        if i.value != expected:
            raise SystemExit(f"People I{r} is not the expected formula: {i.value}")
        i.value = (f"=(E{r}-Deseret!{S.cols['arr']}{r})*Paths!I{r}+Deseret!{S.cols['arr']}{r}*dg_ret"
                   f"+(F{r}+G{r}+H{r})*dep_asia")


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "16 Nov: Deseret"
    Ch.cell(n, 2).value = "The gathering and the Saints' birth rate"
    Ch.cell(n, 3).value = ("Master lever dg_on (at 0 the input workbook exactly). Deseret sheet: convert arrivals after 1887 into People E "
                           "(returns at dg_ret, not Paths I), and the Saints' natural-increase premium on their memo stock into People D. "
                           "Story assumption, MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    St = wb["Start"]
    r0 = St.max_row + 1
    St.cell(r0, 1).value = "Deseret"
    St.cell(r0, 2).value = "The gathering of converts after 1887 and the Saints' birth rate (16 November 2026)."
    for c_ in (1, 2):
        St.cell(r0, c_)._style = copy.copy(St.cell(r0 - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["dg_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true", help="save dg_on = 0 in both cases (identity build)")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    for s in ("Growth", "Members' land"):
        if s not in wb.sheetnames:
            raise SystemExit(f"needs the CR-057 growth workbook built on the Civil War CRs (no {s} sheet)")
    if "Deseret" in wb.sheetnames:
        raise SystemExit("Deseret sheet already exists")
    base.add_levers(wb, LEVERS)
    S = build(wb)
    link(wb, S)
    log(wb, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: Deseret sheet, {len(LEVERS) - 1} levers, People D, E and I linked")


if __name__ == "__main__":
    main()
