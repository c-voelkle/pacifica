"""Apply CR-045, CR-046 and CR-047 to the financial workbook.

    python3 finance/build/cr045_047_omsk_kars.py IN.xlsx OUT.xlsx

IN is the CR-043 workbook (cr043_legion_pay.py). The script never recalculates;
run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

What the three CRs move, at the model's scale:
- CR-046 P7 settles what London collects in 1927 (planning-note B8): nothing. The Baku
  review is withdrawn, Pacifica stays operator and the Royal Navy takes a fixed allowance
  at Batum at market price. The Crown share (lever oil_baku) is unchanged; its comment
  and the Baku Events row note now say so.
- CR-047 D2-D3: the Kars plebiscite of 1921, held under Pacifican commissioners with the
  Office of Public Measures keeping the registers, is a small Treasury programme (one new
  lever and one Events row), MODEL.
- CR-045 (Mikhailov, Kashevarov, Maria) and the rest of CR-046 (the Petrograd account,
  Copenhagen, Stalin) carry no Pacifican Treasury money: the Copenhagen gold is British,
  and the Reserve Bank's and the Office's secret payments are below the model's resolution.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl
from openpyxl.comments import Comment

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "CR-045-047, 31 Oct 2026"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-047: the three districts (31 Oct 2026) —",
    ("kars_vote", "Kars plebiscite, 1921: Pacifican commissioners and the Office's registers", 0.4, 0.6, "$m",
     "Model estimate",
     "CR-047 D2-D3: a vote by district on the Russian rolls of 1914 in the Kars province (290,654 people in 1897; "
     "about 360,000 by 1916). Commissioners, a supervising detachment drawn from the Black Sea squadron's marines, "
     "Office clerks for the registers and the return of voters expelled in 1918: on the scale of the 1920-21 "
     "Schleswig and Upper Silesia commissions, about $1 a resident in 1921 dollars. Stress: more returning voters "
     "to carry and feed."),
]

EVENTS = [
    [1921, 1921, "Kars plebiscite: Pacifican commissioners and the Office's registers", "Programme", None,
     "Armenia", "=kars_vote", None, "No", "Approved", "§32 (CR-047 D2-D3)",
     "The vote the National Pact accepted, by district on the 1914 rolls; Treaty of Kars, 13 October 1921. Amount MODEL"],
]

BAKU_LEVER_NOTE = (
    "CR-041 N14: joint Anglo-Pacifican concession with Azerbaijan, Pacifica operating, Britain the strategic say. "
    "About 4 Mt a year to the Pacifican side. CR-046 P7 (31 Oct 2026) settles what London collects in 1927 (B8): "
    "the seventh-year review is withdrawn, Pacifica stays operator and the Royal Navy takes a fixed allowance at "
    "Batum at market price, so the Crown share is unchanged after 1927. Amount MODEL.")
BAKU_ROW_NOTE = ("Joint with Britain; the 1927 review is withdrawn (CR-046 P7) and the navy's Batum allowance is "
                 "sold at market price, so the Crown share is unchanged")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)

    # 1. Baku: lever comment and Events note (no amount changes)
    ref = wb.defined_names["oil_baku"].attr_text
    row = int(ref.split("$")[-1])
    L = wb["Levers"]
    assert L.cell(row, 3).value == 3 and L.cell(row, 4).value == 1.5, "unexpected oil_baku values"
    L.cell(row, 3).comment = Comment(BAKU_LEVER_NOTE, AUTHOR)
    E = wb["Events"]
    baku = [r for r in range(6, base.EVENTS_LAST + 1)
            if E.cell(r, 4).value == "Baku joint concession: Pacifica's operating share, Crown share"]
    assert len(baku) == 1, baku
    E.cell(baku[0], 13).value = BAKU_ROW_NOTE

    # 2. Kars plebiscite
    base.add_levers(wb, LEVERS)
    for v in EVENTS:
        base.add_event(wb, v)

    # 3. Changes
    C = wb["Changes"]
    n = C.max_row + 1
    C.cell(n, 1).value = "31 Oct: CR-045-047"
    C.cell(n, 2).value = "Baku 1927; Kars vote"
    C.cell(n, 3).value = ("CR-046 P7: the 1927 Baku review is withdrawn, so the Crown share (oil_baku) is unchanged after "
                          "1927 (comment and note only). CR-047: the Kars plebiscite of 1921, a Programme row from lever "
                          "kars_vote. CR-045 and the rest of CR-046 move no Treasury money.")
    for c in range(1, 4):
        C.cell(n, c)._style = copy.copy(C.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
