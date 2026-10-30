"""Apply CR-042 (Huludao) to the financial workbook.

    python3 finance/build/cr042_huludao.py IN.xlsx OUT.xlsx

IN is the CR-041 workbook (cr041_russian_war.py). The script never recalculates;
run LibreOffice (xlsx skill scripts/recalc.py) afterwards.

Two Treasury loans to China in the Asia group, both MODEL amounts:
- the junior Pacifican share of the Mukden-Jinzhou-Huludao railway loan, 1908-1910,
  led by the British and Chinese Corporation with Britain the senior partner (H6);
- the Treasury's share of the Huludao Harbour Trust bonds, 1910-1914, secured on the
  harbour dues (H3).
The rest of each loan is held by San Francisco savers or British lenders and is not
Treasury cash.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

base.AUTHOR = "CR-042, 30 Oct 2026"

LEVERS = [
    "— CR-042: Huludao (30 Oct 2026) —",
    ("hul_rail", "Mukden-Jinzhou-Huludao railway loan, total", 12, 15, "$m", "Model estimate",
     "CR-042 H6: built 1908-1910 by a British and Pacifican syndicate, Britain the senior partner, led by the British "
     "and Chinese Corporation. About 290 km of new and rebuilt line at about $40,000 a km."),
    ("hul_rail_pac", "Pacifican (junior) share of the railway loan", 0.35, 0.35, "share", "Approved",
     "CR-042 H6: Britain senior, San Francisco junior. The share is MODEL; Britain's seniority is approved."),
    ("hul_rail_pub", "Treasury's part of the Pacifican share", 0.5, 0.5, "share", "Model estimate",
     "The rest placed with San Francisco savers."),
    ("hul_bonds", "Huludao Harbour Trust bonds, total", 15, 20, "$m", "Model estimate",
     "CR-042 H3: the trust's works 1910-1914, bonds placed in San Francisco, secured on the harbour dues."),
    ("hul_pub", "Treasury's share of the trust's bonds", 0.33, 0.4, "share", "Model estimate",
     "The rest placed with San Francisco savers."),
]

EVENTS = [
    [1908, 1910, "Mukden-Jinzhou-Huludao railway: Treasury part of the junior Pacifican share", "Loan", "Asia", "China",
     "=hul_rail*hul_rail_pac*hul_rail_pub/3", None, "No", "Approved", "§27 (CR-042 H6)",
     "British and Pacifican syndicate, Britain senior; secured on the line's receipts"],
    [1910, 1914, "Huludao Harbour Trust bonds: Treasury share", "Loan", "Asia", "China", "=hul_bonds*hul_pub/5", None,
     "No", "Proposed", "§27 (CR-042 H3)", "Keelung pattern; secured on the harbour dues until the bonds are paid"],
]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    base.add_levers(wb, LEVERS)
    for v in EVENTS:
        base.add_event(wb, v)
    C = wb["Changes"]
    n = C.max_row + 1
    C.cell(n, 1).value = "30 Oct: CR-042"
    C.cell(n, 2).value = "Huludao"
    C.cell(n, 3).value = ("CR-042: Treasury loans to China for the Mukden-Jinzhou-Huludao railway (junior share of a British-led "
                          "syndicate, 1908-10) and the Huludao Harbour Trust (1910-14), Asia group.")
    for c in range(1, 4):
        C.cell(n, c)._style = copy.copy(C.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
