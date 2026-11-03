"""Apply CR-049 (the atomic programme) to the financial workbook.

    python3 finance/build/cr049_atomic_programme.py IN.xlsx OUT.xlsx

IN is the CR-045-047 workbook (cr045_047_omsk_kars.py). The script never recalculates;
run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

The author asked on 2 November 2026 for the estimate in CR-049-atomic-estimate.md to
enter the workbook "as a new atomic program". This script adds:
- an Atomic sheet, one row a year 1846-1932: uranium mined by source, its use for
  research, weapons and energy, the reserve, the programme's costs and its direct
  returns, in 1913 dollars and in current dollars through the Paths price level;
- levers for the unit costs, vanadium, power and a cost multiplier (Story 1, Stress 1.5);
- Budget links: the programme's cost is added to Technical programmes and its direct
  returns (radium, vanadium, electricity) to State enterprises; the navy's saving after
  1927 is a memo column only and changes nothing in the Navy sheet;
- a Checks column (the reserve is never negative), counted in Problems this year.

All quantities are the central case of the estimate (cr049_atomic_estimate.py) and are
MODEL. Reconstruction credit to Belgium and Bohemia and the Bosnian compensation loan
carry no stated amounts and are not entered (the loan is lent by Pacifican banks, not the
Treasury). Weapons quantities stay a coarse resource bucket, never per device.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl
from openpyxl.utils import get_column_letter as col

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402
import cr049_atomic_estimate as est  # noqa: E402

AUTHOR = "CR-049, 2 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST = 1846, 1932
ROW0 = 6  # 1846


def row(y: int) -> int:
    return ROW0 + y - FIRST


LEVERS = [
    "— CR-049: the atomic programme (2 Nov 2026) —",
    ("atom_cost_rad", "Uranium cost, radium-era by-product (1913 $/kg U)", 6.0, 7.0, "$/kg", "Model estimate",
     "CR-049: uranium recovered from Joachimsthal residues and early Western Slope ore while the source trade pays "
     "for the mines, 1864-1908. Mining, milling and refining."),
    ("atom_cost_wsl", "Uranium cost, Western Slope (1913 $/kg U)", 7.0, 9.0, "$/kg", "Model estimate",
     "CR-049: Roc Creek and Paradox Valley carnotite on the Ute lease, mined for uranium from 1909; low-grade ore, "
     "vanadium recovered alongside."),
    ("atom_cost_joa", "Uranium cost, Joachimsthal (1913 $/kg U)", 9.0, 11.0, "$/kg", "Model estimate",
     "CR-049: the 1909 contract and the 1919 concession; deep vein mining, residues already partly worked."),
    ("atom_cost_shk", "Uranium cost, Shinkolobwe (1913 $/kg U)", 2.5, 3.5, "$/kg", "Model estimate",
     "CR-049: very rich pitchblende; wages paid to free workers (CR-031-R1); freight from Katanga included."),
    ("atom_cost_fer", "Uranium cost, Fergana (1913 $/kg U)", 8.0, 10.0, "$/kg", "Model estimate",
     "CR-049: Tyuya-Muyun, a small concession beside Emba from 1921."),
    ("atom_v_per_u", "Vanadium per tonne of Western Slope uranium", 3.0, 2.0, "t/t", "Model estimate",
     "Carnotite ore carries several times as much vanadium as uranium."),
    ("atom_v_price", "Vanadium, net of recovery (1913 $/kg)", 7.0, 5.0, "$/kg", "Model estimate",
     "Armour, tool and motor steel."),
    ("atom_cf", "Atomic stations: capacity factor", 0.7, 0.6, "share", "Model estimate",
     "Tokyo station from 1928, Pacifican stations 1929-1931."),
    ("atom_power_price", "Atomic stations: wholesale power price (1913 $/kWh)", 0.015, 0.012, "$/kWh",
     "Model estimate", "Wholesale, not retail."),
    ("atom_scale", "Atomic programme: multiplier on non-mining costs", 1.0, 1.5, "x", "Model estimate",
     "Story 1.0 is the central estimate; Stress 1.5 is the estimate's high case (slower separation, dearer halls)."),
]

SOURCES = list(est.SUPPLY.keys())  # radium era, Western Slope, Joachimsthal, Shinkolobwe, Fergana
COST_LEVER = ["atom_cost_rad", "atom_cost_wsl", "atom_cost_joa", "atom_cost_shk", "atom_cost_fer"]

HEAD = [
    # (group, header, note)
    ("Uranium mined, t U", "Radium-era by-product", "Joachimsthal residues and early Western Slope ore, 1864-1908 (input)."),
    (None, "Western Slope", "Roc Creek and Paradox Valley on the Ute lease; mined for uranium from 1909 (input)."),
    (None, "Joachimsthal", "Contract of 1909 (rider to the Bosnian loan), concession of 1919; 1919 includes the wartime stock (input)."),
    (None, "Shinkolobwe", "Option 1915-16; the company three-quarters owned by the Works from 1919 (input)."),
    (None, "Fergana", "Tyuya-Muyun concession beside Emba, from 1921 (input)."),
    (None, "Total mined", "Sum of the sources."),
    ("Uses, t U", "Research installations", "1913, 1916, 1921 (input)."),
    (None, "Weapons (separation feed)", "A coarse resource bucket, never per device: 1911-1927 for the 1920 test and the "
     "three devices of 1927, then a small arsenal whose count is OPEN (input)."),
    (None, "Energy", "Tokyo station first load 1926-27 and refuelling; Pacifican stations 1929-1932 (input)."),
    (None, "Reserve at year end", "Cumulative: mined less used. Seven tenths of everything mined is still held in 1932."),
    ("Costs, 1913 $m", "Mining, milling, refining", "Tonnes by source times the unit-cost levers."),
    (None, "Contracts, concessions, shares", "Joachimsthal premium and royalties, the Shinkolobwe option and "
     "Tanganyika Concessions shares, Ute lease and Fergana fees (input)."),
    (None, "Laboratories and installations", "The Works' atomic laboratories and the research installations (input)."),
    (None, "Separation halls, weapons, tests", "Halls built 1912-1919 and enlarged 1928-1930, their operation and "
     "power, weapon engineering and security, the desert test (1920) and the sea demonstration (1927) (input)."),
    (None, "Power stations", "Tokyo (80 MWe, 1925-1927; financing OPEN, entered as Pacifica's) and four Pacifican "
     "stations of 40 MWe, 1928-1931 (input)."),
    (None, "Total cost (1913 $m)", "Mining plus the other costs times atom_scale."),
    (None, "Price level (1913 = 1)", "Paths."),
    (None, "Total cost ($m)", "Current dollars. Added to Budget: Technical programmes."),
    ("Returns, 1913 $m", "Radium and source trade", "Net margin of the source trade and medical radium (input)."),
    (None, "Vanadium", "Western Slope uranium times atom_v_per_u times atom_v_price."),
    (None, "Atomic stations in service (MWe)", "Input: 80 MWe from 1928, 240 MWe by 1931."),
    (None, "Electricity", "MWe x 8,760 h x atom_cf x atom_power_price."),
    (None, "Direct returns (1913 $m)", "Radium, vanadium and electricity."),
    (None, "Direct returns ($m)", "Current dollars. Added to Budget: State enterprises."),
    ("Result", "Net cost to the Treasury ($m)", "Total cost less direct returns, current dollars."),
    (None, "Navy's saving, memo (1913 $m)", "Capital ships not laid down after 1927: an option, not entered in the "
     "Budget or the Navy sheet."),
    (None, "Cost / real GDP", "Total cost (1913 $m) over Economy real GDP (1913 $m)."),
    (None, "Reserve not negative", "OK or Check; counted on Checks."),
]


def inputs_for(y: int) -> dict[str, float]:
    sup = [est.SUPPLY[s].get(y, 0.0) for s in SOURCES]
    uses = {"research": 0.0, "weapons": 0.0, "energy": 0.0}
    for name, d in est.USES.items():
        key = name.split(":")[0].split(" ")[0].lower()
        uses[key] += d.get(y, 0.0)
    costs = {"acquisition": 0.0, "research": 0.0, "weapons": 0.0, "energy": 0.0}
    for (cat, _), d in est.COSTS.items():
        costs[cat] += d.get(y, 0.0)
    return {
        "sup": sup, **{f"use_{k}": v for k, v in uses.items()}, **{f"cost_{k}": v for k, v in costs.items()},
        "radium": est.RADIUM_MARGIN.get(y, 0.0), "mwe": est.STATION_MWE.get(y, 0.0),
        "navy": est.NAVY_SAVING.get(y, 0.0),
    }


def build_sheet(wb) -> None:
    B = wb["Budget"]
    P = wb["Paths"]
    A = wb.create_sheet("Atomic", index=wb.sheetnames.index("Champions") + 1)
    title, sub, hint = B["A1"], B["A2"], B["A3"]
    A["A1"].value = "Atomic: the Light and Matter Works' programme, 1864-1932"
    A["A2"].value = ("CR-049 (MODEL): uranium mined by source and its use for research, weapons and energy, the reserve, "
                     "the programme's cost and its direct returns. Central case of finance/CR-049-atomic-estimate.md. "
                     "Pacifica means to take as much uranium as it can get; how it gets more is the next CR, and these "
                     "quantities will rise with it.")
    A["A3"].value = ("Years run down the page. Blue = input you can change · black = formula · levers are on Levers "
                     "(CR-049). Hover a column heading for its definition.")
    for c, src in (("A1", title), ("A2", sub), ("A3", hint)):
        A[c]._style = copy.copy(src._style)
    grp_style, head_style = B["B4"]._style, B["B5"]._style
    year_style, f_style = B["A6"]._style, B["B6"]._style
    in_style = P["B6"]._style
    A.cell(5, 1).value = "Year"
    A.cell(5, 1)._style = copy.copy(B["A5"]._style)
    for i, (grp, head, text) in enumerate(HEAD, start=2):
        if grp:
            A.cell(4, i).value = grp
        A.cell(4, i)._style = copy.copy(grp_style)
        A.cell(5, i).value = head
        A.cell(5, i)._style = copy.copy(head_style)
        base.note(A.cell(5, i), text, 110)
    A.column_dimensions["A"].width = 8
    for i in range(2, len(HEAD) + 2):
        A.column_dimensions[col(i)].width = 14
    A.freeze_panes = "B6"

    for y in range(FIRST, LAST + 1):
        r = row(y)
        v = inputs_for(y) if y >= 1864 else None
        A.cell(r, 1).value = y
        A.cell(r, 1)._style = copy.copy(year_style)

        def put(c: int, value, is_input: bool) -> None:
            cell = A.cell(r, c)
            cell.value = value
            cell._style = copy.copy(in_style if is_input else f_style)

        for k in range(5):  # B-F supply
            put(2 + k, round(v["sup"][k], 4) if v else 0, True)
        put(7, f"=SUM(B{r}:F{r})", False)
        put(8, round(v["use_research"], 4) if v else 0, True)
        put(9, round(v["use_weapons"], 4) if v else 0, True)
        put(10, round(v["use_energy"], 4) if v else 0, True)
        prev = f"K{r - 1}+" if y > FIRST else ""
        put(11, f"={prev}G{r}-H{r}-I{r}-J{r}", False)
        put(12, "=(" + "+".join(f"{col(2 + k)}{r}*{COST_LEVER[k]}" for k in range(5)) + ")/1000", False)
        put(13, round(v["cost_acquisition"], 4) if v else 0, True)
        put(14, round(v["cost_research"], 4) if v else 0, True)
        put(15, round(v["cost_weapons"], 4) if v else 0, True)
        put(16, round(v["cost_energy"], 4) if v else 0, True)
        put(17, f"=L{r}+(M{r}+N{r}+O{r}+P{r})*atom_scale", False)
        put(18, f"=Paths!B{r}", False)
        put(19, f"=Q{r}*R{r}", False)
        put(20, round(v["radium"], 4) if v else 0, True)
        put(21, f"=C{r}*atom_v_per_u*atom_v_price/1000", False)
        put(22, v["mwe"] if v else 0, True)
        put(23, f"=V{r}*8760*atom_cf*atom_power_price/1000", False)
        put(24, f"=T{r}+U{r}+W{r}", False)
        put(25, f"=X{r}*R{r}", False)
        put(26, f"=S{r}-Y{r}", False)
        put(27, v["navy"] if v else 0, True)
        put(28, f"=Q{r}/Economy!S{r}", False)
        put(29, f'=IF(K{r}>=-0.001,"OK","Check")', False)
        for c in (28,):
            A.cell(r, c).number_format = "0.00%"

    t = row(LAST) + 2
    A.cell(t, 1).value = "1846-1932"
    A.cell(t, 1)._style = copy.copy(B["A5"]._style)
    for c in list(range(2, 11)) + list(range(12, 18)) + [19, 20, 21, 23, 24, 25, 26, 27]:
        L_ = col(c)
        A.cell(t, c).value = f"=SUM({L_}{row(FIRST)}:{L_}{row(LAST)})"
        A.cell(t, c)._style = copy.copy(head_style)
    A.cell(t, 11).value = f"=K{row(LAST)}"
    A.cell(t, 11)._style = copy.copy(head_style)


def link_budget(wb) -> None:
    B = wb["Budget"]
    assert B["S5"].value == "Technical programmes" and B["F5"].value == "State enterprises"
    for y in range(FIRST, LAST + 1):
        r = row(y)
        for c, src in (("S", "S"), ("F", "Y")):
            f = B[f"{c}{r}"].value
            assert isinstance(f, str) and f.startswith("=") and "Atomic!" not in f
            B[f"{c}{r}"].value = f"{f}+Atomic!{src}{r}"
    base.note(B["S5"], (B["S5"].comment.text + "\n\n" if B["S5"].comment else "")
              + "CR-049: includes the atomic programme's cost (Atomic, current $).", 160)
    base.note(B["F5"], (B["F5"].comment.text + "\n\n" if B["F5"].comment else "")
              + "CR-049: includes the atomic programme's direct returns: radium, vanadium, electricity (Atomic).", 160)


def add_check(wb) -> None:
    C = wb["Checks"]
    c = C.max_column + 1
    assert C.cell(5, c - 1).value == "1861 residents near DEM-01"
    C.cell(5, c).value = "Uranium reserve not negative (CR-049)"
    for rr in (4, 5):
        C.cell(rr, c)._style = copy.copy(C.cell(rr, c - 1)._style)
    base.note(C.cell(5, c), "Atomic: the reserve of uranium mined less used is never negative.", 80)
    for y in range(FIRST, LAST + 1):
        r = row(y)
        C.cell(r, c).value = f"=Atomic!AC{r}"
        C.cell(r, c)._style = copy.copy(C.cell(r, c - 1)._style)
        s = C[f"S{r}"].value
        assert s.endswith('+COUNTIF(AJ%d:AK%d,"Check")' % (r, r)), s
        C[f"S{r}"].value = s + f'+COUNTIF({col(c)}{r},"Check")'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "Atomic" in wb.sheetnames:
        raise SystemExit("Atomic sheet already exists")
    base.add_levers(wb, LEVERS)
    build_sheet(wb)
    link_budget(wb)
    add_check(wb)
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "2 Nov: CR-049"
    Ch.cell(n, 2).value = "Atomic programme"
    Ch.cell(n, 3).value = ("CR-049: new Atomic sheet (uranium by source 1864-1932, uses, reserve, costs and direct "
                           "returns; central case of CR-049-atomic-estimate.md, MODEL). Cost added to Budget Technical "
                           "programmes, returns to State enterprises; navy saving memo only; Checks column for the "
                           "reserve. Levers atom_* (Story 1.0, Stress 1.5 on non-mining costs).")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
