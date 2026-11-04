"""Apply CR-052 (and CR-053 to CR-055 through it) to the financial workbook: the energy link.

    python3 finance/build/cr052_energy_link.py IN.xlsx ENERGY_OUTPUTS.csv OUT.xlsx

IN is the CR-050 workbook (cr050_atomic_retiming.py). ENERGY_OUTPUTS.csv is written by
energy/build/export_energy.py from the energy workbook. The script never recalculates; run
LibreOffice (xlsx skill scripts/recalc.py) afterwards.

The author asked on 4 November 2026 to "rebuild the financial workbook first and assess what
this merge would change" before merging the energy workbook (PR #61). Nothing is linked live
between the two workbooks: the energy results are written here as blue inputs with the
energy workbook's SHA-256, exactly as the energy workbook holds the finance results.

What changes (Story case; Stress keeps the financial workbook's own paths):
- home oil: the CR-052 field model with early water flooding (CT3 C and M8, approved)
  replaces Resources!I, the output before any compact;
- motor vehicles built: the CT5 path (approved: California the most motorized place on
  earth) replaces Champions!U;
- CR-053: the oil trust's minority stakes (Tropical Oil, Lago Petroleum, the Peruvian
  company, Holmes's options, the Mesopotamian share) as an outlay inside the ordinary
  private investment abroad, held at book among the champions' assets abroad, with a
  dividend on the entitlement crude;
- a new sheet, Energy link, carrying the energy workbook's power investment, Development
  Fund credit, utility receipts, royalties and fuel imports as memos (no GDP effect: the
  utilities are already inside non-mining output), and the investment and consumption
  account of finance/investment-share-note.md v2 (item 1): gross domestic investment on the
  inv_share test path, government consumption, net exports, household consumption per
  person, and the industrial index the energy workbook can read (item 2, proportional).
Not done here (OPEN in the note): sector prices (item 3), asia_home after 1915, the
industrial-output derivation beyond the proportional index, and CR-051's costs.
All amounts are MODEL.
"""
from __future__ import annotations

import argparse
import copy
import csv
import sys
from pathlib import Path

import openpyxl
from openpyxl.utils import get_column_letter as col

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "CR-052, 4 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST = 1846, 1932
ROW0 = 6


def row(y: int) -> int:
    return ROW0 + y - FIRST


def interp(points: dict[int, float]) -> dict[int, float]:
    ks = sorted(points)
    out = {}
    for y in range(FIRST, LAST + 1):
        if y <= ks[0]:
            out[y] = points[ks[0]]
        elif y >= ks[-1]:
            out[y] = points[ks[-1]]
        else:
            lo = max(k for k in ks if k <= y)
            hi = min(k for k in ks if k >= y)
            out[y] = points[lo] if lo == hi else points[lo] + (points[hi] - points[lo]) * (y - lo) / (hi - lo)
    return out


LEVERS = [
    "— CR-052: the energy workbook's link (4 Nov 2026) —",
    ("en_paths", "Energy workbook's home oil and vehicle paths (1 = yes; 0 = the paths before CR-052)", 1, 0, "switch",
     "Approved (CR-052 CT3 C, M8, CT5)",
     "Author, 3-4 Nov 2026: the Los Angeles basin giants found 'with the greatest believable haste' (CT3 C), water "
     "flooding fifteen years early (M8), and California the most motorized place on earth (CT5). The paths come from "
     "the energy workbook (Energy link B and D, with its SHA-256). Stress keeps the financial workbook's own paths, "
     "which is how the energy workbook's Stress case reads them."),
    ("conc_div", "CR-053: the oil trust's return on its entitlement crude ($ a barrel)", 0.30, 0.20, "$/bbl",
     "Model estimate",
     "CR-053: crude at cost against equity; the trust's gain is the discount to the market and the minority "
     "dividend, about 30 cents a barrel against a 1929 price of about $1.20. Held at book in the champions' assets "
     "abroad (Energy link W)."),
    ("inv_gap", "Investment share below the Story path (share of GDP)", 0.0, 0.05, "share", "Proposed (CR-052 M2)",
     "finance/investment-share-note.md v2: the Stress case five points lower than Story's test path."),
]

# CR-053 stake outlays, $m current (MODEL, PROPOSED in CR-053)
STAKES = {1920: 6, 1921: 6, 1923: 10, 1924: 22, 1925: 12, 1926: 1, 1928: 8}
STAKE_NOTE = ("CR-053 (MODEL, PROPOSED amounts): Tropical Oil minority 1920-21 ($12m), Lago Petroleum about a fifth "
              "1923-24 ($20m), the Peruvian company 1924-25 ($30m less the Union's reciprocal fifth, $24m), Holmes's "
              "Bahrain and Kuwait options 1926 ($1m), the Mesopotamian share beside the Union's group 1928 ($8m).")

# investment share of GDP, Story test path (finance/investment-share-note.md v2)
INV_SHARE = interp({1846: 0.12, 1850: 0.15, 1860: 0.18, 1870: 0.20, 1880: 0.20, 1887: 0.22, 1895: 0.24,
                    1900: 0.25, 1907: 0.26, 1913: 0.26, 1914: 0.23, 1916: 0.22, 1918: 0.22, 1919: 0.24,
                    1920: 0.27, 1922: 0.28, 1927: 0.29, 1929: 0.28, 1930: 0.26, 1932: 0.24})

# US personal consumption expenditure per person, $ current (BEA NIPA 1.1.5 / population; to verify)
US_PCE = {1929: 77.4e9 / 121.77e6, 1930: 70.1e9 / 123.08e6, 1931: 60.7e9 / 124.04e6, 1932: 48.7e9 / 124.84e6}

# (letter, group, header, note)
HEAD = [
    ("B", "Paths from the energy workbook", "Home oil, energy workbook Story (m bbl)",
     "CR-052 C with M8 (approved): the field model's output, Fuels 'Home oilfields' of the energy workbook, before any compact."),
    ("C", None, "Home oil, the financial workbook's path before CR-052 (m bbl)", "Resources!I as built to CR-050; the Stress case keeps it."),
    ("D", None, "Motor vehicles built, energy workbook Story (thousand)", "CR-052 CT5 (approved): Uses 'Vehicles the finance workbook must build'."),
    ("E", None, "Motor vehicles built, the financial workbook's path before CR-052 (thousand)", "Champions!U as built to CR-050; the Stress case keeps it."),
    ("F", "Power (memo, energy workbook)", "Power investment, Story ($m)", "en_power_capex."),
    ("G", None, "Power investment, Stress ($m)", "en_power_capex, Stress case."),
    ("H", None, "Power investment ($m)", "Counted once, inside gross domestic investment (column AA); no GDP effect."),
    ("I", None, "Development Fund's power credit, Story ($m)", "en_dev_power_credit: capped at the Fund's capacity in the energy workbook."),
    ("J", None, "Development Fund's power credit, Stress ($m)", ""),
    ("K", None, "Development Fund's power credit ($m)", "Financing of part of the power investment, not additional investment."),
    ("L", None, "Utility receipts, Story ($m)", "en_elec_revenue_utility."),
    ("M", None, "Utility receipts, Stress ($m)", ""),
    ("N", None, "Utility receipts ($m)", "Sales of the utilities; already inside non-mining output."),
    ("O", None, "Royalties to the compact peoples, Story ($m)", "en_royalties (CR-051 S8, CR-055)."),
    ("P", None, "Royalties to the compact peoples, Stress ($m)", ""),
    ("Q", None, "Royalties to the compact peoples ($m)", "Utilities to the peoples of the dams' reaches."),
    ("R", None, "Oil imported, value, Story ($m)", "en_oil_import_value: the trust's purchases of Gulf crude and the entitlements."),
    ("S", None, "Oil imported, value, Stress ($m)", ""),
    ("T", None, "Oil imported, value ($m)", "Memo; the trust's Gulf trade stays as Champions builds it."),
    ("U", "CR-053: the oil trust's stakes", "Entitlement crude (m bbl)", "Energy workbook, Fuels conc_*: Maracaibo, De Mares, Peru, Bahrain."),
    ("V", None, "Stakes bought ($m)", STAKE_NOTE),
    ("W", None, "Stakes at book ($m)", "In the champions' assets abroad (Champions!AY); the outlay comes out of the ordinary private investment abroad (Abroad!C)."),
    ("X", None, "Return on the entitlement crude ($m)", "Entitlement crude × conc_div; in the champions' earnings abroad (Champions!AZ) and the chartered industries' profits."),
    ("Y", "Investment and consumption (investment-share note v2)", "Investment share of GDP, Story test path",
     "finance/investment-share-note.md v2: about 15% at settlement, 18-20% in the 1860s-70s, 22-25% under the regency, 25-27% in 1900-13, "
     "22-24% in 1914-19, 27-29% in the 1920s (27% in 1920, 28-29% from 1922), 24-26% in 1930-32. PROPOSED, MODEL."),
    ("Z", None, "Investment share of GDP", "Story path less inv_gap (Stress five points lower)."),
    ("AA", None, "Gross domestic investment ($m)", "Investment share × core GDP. Includes the power investment (H) and the Development Fund's investment."),
    ("AB", None, "Power investment / gross domestic investment", "US electric utilities were about a sixteenth of private investment in the late 1920s (to verify)."),
    ("AC", None, "Industrial index (1913 = 1)", "Investment share over its 1913 value: the proportional baseline of the note (Sol: about 1.08 by 1929). "
     "The energy workbook reads it as ind_idx when its lever ind_src = 2 (off until the author adopts the path)."),
    ("AD", None, "Fund's power credit / the Fund's investment from surpluses", "Development Fund credit to the utilities over 'Debt & cash'!I (the Fund's investment from budget surpluses, "
     "the base of the energy workbook's cap); against the Fund's investment from all sources ('Debt & cash'!N) the share is lower."),
    ("AE", None, "Government consumption ($m)", "Treasury spending on the army, navy, war and operations, civil services, technical programmes and settlement. "
     "Excluded as investment: public works, the Development Fund's 'Investment' events and the atomic power stations (Atomic P); the separation halls and weapons count, "
     "like other military spending, as government consumption. Debt interest and transfers are excluded. County and state spending is inside civil services' share."),
    ("AF", None, "Net exports ($m)", "Net foreign investment less net income from abroad. Net foreign investment: ordinary private investment abroad less "
     "repatriations (Abroad C, F), the Entente share (Abroad D), net public lending abroad ('Debt & cash' B), and the champions' cash investment abroad "
     "less what foreigners finance and plus what is redeemed (Champion funding D, K, Q, R). Net income: income from abroad and interest on public loans abroad "
     "(Abroad M, Budget H) less remittances and payments to foreign holders (Abroad O, V)."),
    ("AG", None, "Household consumption ($m)", "Core GDP less investment, government consumption, net exports and new gold kept as money (Resources R)."),
    ("AH", None, "Household consumption / GDP", ""),
    ("AI", None, "Household consumption per person present ($)", "The author's trade-off view (investment-share note v2): read this, not GDP per person, "
     "for whether Pacificans live visibly better than the Union's citizens."),
    ("AJ", None, "US consumption per person, historical ($)", "BEA personal consumption expenditure over population, 1929-1932 (to verify)."),
    ("AK", None, "Pacifica / US, consumption per person", ""),
]


def build_sheet(wb, data: dict, sha: str, old_oil: dict, old_cars: dict) -> None:
    B = wb["Budget"]
    P = wb["Paths"]
    E = wb.create_sheet("Energy link", index=wb.sheetnames.index("Atomic") + 1)
    E["A1"].value = "Energy link: what the energy workbook gives the financial workbook (CR-052)"
    E["A2"].value = (f"From the energy workbook with SHA-256 {sha} (energy/build/energy_outputs.csv). Home oil and vehicles "
                     "replace the financial workbook's paths in the Story case (lever en_paths); power, the CR-053 stakes and the "
                     "investment and consumption account are memos or new accounts. All amounts MODEL.")
    E["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. Re-run "
                     "finance/build/cr052_energy_link.py when the energy workbook changes.")
    for c, src in (("A1", B["A1"]), ("A2", B["A2"]), ("A3", B["A3"])):
        E[c]._style = copy.copy(src._style)
    grp_style, head_style = B["B4"]._style, B["B5"]._style
    year_style, f_style, in_style = B["A6"]._style, B["B6"]._style, P["B6"]._style
    E.cell(5, 1).value = "Year"
    E.cell(5, 1)._style = copy.copy(B["A5"]._style)
    for L_, grp, head, text in HEAD:
        c = openpyxl.utils.column_index_from_string(L_)
        if grp:
            E.cell(4, c).value = grp
        E.cell(4, c)._style = copy.copy(grp_style)
        E.cell(5, c).value = head
        E.cell(5, c)._style = copy.copy(head_style)
        if text:
            base.note(E.cell(5, c), text, 120)
        E.column_dimensions[L_].width = 13
    E.column_dimensions["A"].width = 8
    E.freeze_panes = "B6"
    r13 = row(1913)
    for y in range(FIRST, LAST + 1):
        r = row(y)
        i = y - FIRST
        E.cell(r, 1).value = y
        E.cell(r, 1)._style = copy.copy(year_style)

        def put(L_: str, value, is_input: bool, fmt: str | None = None) -> None:
            cell = E[f"{L_}{r}"]
            cell.value = value
            cell._style = copy.copy(in_style if is_input else f_style)
            if fmt:
                cell.number_format = fmt

        put("B", round(data["home_oil__story"][i], 4), True)
        put("C", old_oil[y], True)
        put("D", round(data["veh_build__story"][i], 3), True)
        put("E", old_cars[y], True)
        for (s, st, act), key in ((("F", "G", "H"), "power_capex"), (("I", "J", "K"), "dev_power_credit"),
                                  (("L", "M", "N"), "elec_revenue_utility"), (("O", "P", "Q"), "royalties"),
                                  (("R", "S", "T"), "oil_import_value")):
            put(s, round(data[f"{key}__story"][i], 4), True)
            put(st, round(data[f"{key}__stress"][i], 4), True)
            put(act, f"=IF(case_sel=1,{s}{r},{st}{r})", False)
        put("U", round(data["conc_oil__story"][i], 4), True)
        put("V", STAKES.get(y, 0), True)
        put("W", f"=V{r}" if y == FIRST else f"=W{r - 1}+V{r}", False)
        put("X", f"=U{r}*conc_div", False)  # the entitlement is the same in both energy cases
        put("Y", round(INV_SHARE[y], 4), True, "0.0%")
        put("Z", f"=MAX(0,Y{r}-inv_gap)", False, "0.0%")
        put("AA", f"=Z{r}*Economy!O{r}", False)
        put("AB", f"=IF(AA{r}>0,H{r}/AA{r},0)", False, "0.0%")
        put("AC", f"=IF($Z${r13}>0,Z{r}/$Z${r13},1)", False, "0.000")
        put("AD", f"=IF('Debt & cash'!I{r}>0,K{r}/'Debt & cash'!I{r},0)", False, "0%")
        inv_ev = (f"SUMPRODUCT((Events!$B$6:$B$400<=$A{r})*(Events!$C$6:$C$400>=$A{r})"
                  f"*(Events!$E$6:$E$400=\"Investment\")*Events!$H$6:$H$400)")
        put("AE", f"=Budget!N{r}+Budget!O{r}+Budget!P{r}+Budget!Q{r}+Budget!S{r}-{inv_ev}-Atomic!P{r}*atom_scale*Atomic!R{r}+Budget!T{r}", False)
        put("AF", f"=Abroad!C{r}+Abroad!D{r}-Abroad!F{r}+'Debt & cash'!B{r}+'Champion funding'!D{r}-'Champion funding'!K{r}"
                  f"+'Champion funding'!Q{r}+'Champion funding'!R{r}-(Abroad!M{r}+Budget!H{r}-Abroad!O{r}-Abroad!V{r})", False)
        put("AG", f"=Economy!O{r}-AA{r}-AE{r}-AF{r}-Resources!R{r}", False)
        put("AH", f"=IF(Economy!O{r}>0,AG{r}/Economy!O{r},0)", False, "0.0%")
        put("AI", f"=AG{r}*1000000/(Economy!B{r}+People!V{r}+Labour!L{r})", False, "#,##0")
        put("AJ", round(US_PCE[y], 1) if y in US_PCE else None, True, "#,##0")
        put("AK", f'=IF(ISNUMBER(AJ{r}),AI{r}/AJ{r},"")', False, "0.00")


def link(wb) -> None:
    R, C, A, K = wb["Resources"], wb["Champions"], wb["Abroad"], wb["Capital accounts"]
    assert R["I5"].value.startswith("Oil output before any compact"), R["I5"].value
    assert C["U5"].value == "Motor vehicles built (thousands)", C["U5"].value
    assert A["C5"].value == "Ordinary investment abroad ($m)", A["C5"].value
    f_style = R["K6"]._style
    for y in range(FIRST, LAST + 1):
        r = row(y)
        R[f"I{r}"].value = f"=IF(en_paths=1,'Energy link'!B{r},'Energy link'!C{r})"
        R[f"I{r}"]._style = copy.copy(f_style)
        C[f"U{r}"].value = f"=IF(en_paths=1,'Energy link'!D{r},'Energy link'!E{r})"
        C[f"U{r}"]._style = copy.copy(C[f"W{r}"]._style)
        a = A[f"C{r}"].value
        assert a == f"=Economy!O{r}*B{r}", a
        A[f"C{r}"].value = f"=Economy!O{r}*B{r}-'Energy link'!V{r}"
        k = K[f"C{r}"].value
        assert k == f"=Champions!AY{r}-Champions!Q{r}", k
        K[f"C{r}"].value = f"=Champions!AY{r}-Champions!Q{r}-'Energy link'!W{r}"
        for L_, add in (("AY", "W"), ("AZ", "X"), ("BB", "X")):
            f = C[f"{L_}{r}"].value
            assert isinstance(f, str) and f.startswith("=") and "Energy link" not in f, (L_, r, f)
            C[f"{L_}{r}"].value = f"{f}+'Energy link'!{add}{r}"
    base.note(R["I5"], (R["I5"].comment.text + "\n\n" if R["I5"].comment else "")
              + "CR-052: the energy workbook's field model (CT3 C with M8) in the Story case (en_paths); Energy link B and C.", 140)
    base.note(C["U5"], (C["U5"].comment.text + "\n\n" if C["U5"].comment else "")
              + "CR-052 CT5: the energy workbook's build path in the Story case (en_paths); Energy link D and E.", 140)
    base.note(A["C5"], (A["C5"].comment.text + "\n\n" if A["C5"].comment else "")
              + "CR-053: less the oil trust's stake purchases, which move into the champions' assets abroad (Energy link V, W).", 140)
    base.note(K["C5"], (K["C5"].comment.text + "\n\n" if K["C5"].comment else "")
              + "CR-052: less the CR-053 oil stakes (Energy link W), which are oil assets financed out of ordinary investment abroad, so that they are not financed twice.", 140)
    for L_, txt in (("AY", "CR-053: plus the oil trust's stakes at book (Energy link W)."),
                    ("AZ", "CR-053: plus the return on the entitlement crude (Energy link X)."),
                    ("BB", "CR-053: plus the return on the entitlement crude (Energy link X).")):
        base.note(C[f"{L_}5"], (C[f"{L_}5"].comment.text + "\n\n" if C[f"{L_}5"].comment else "") + txt, 140)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("energy_csv")
    ap.add_argument("dst")
    a = ap.parse_args()
    lines = Path(a.energy_csv).read_text().splitlines()
    sha = lines[0].split()[-1]
    rdr = list(csv.reader(lines[1:]))
    hdr = rdr[0]
    data = {k: [float(r[j]) for r in rdr[1:]] for j, k in enumerate(hdr) if k != "year"}
    assert [int(r[0]) for r in rdr[1:]] == list(range(FIRST, LAST + 1))

    wb = openpyxl.load_workbook(a.src)
    if "Energy link" in wb.sheetnames:
        raise SystemExit("Energy link sheet already exists: build from the CR-050 workbook")
    R, C = wb["Resources"], wb["Champions"]
    old_oil = {y: R[f"I{row(y)}"].value for y in range(FIRST, LAST + 1)}
    old_cars = {y: C[f"U{row(y)}"].value for y in range(FIRST, LAST + 1)}
    for d in (old_oil, old_cars):
        assert all(isinstance(v, (int, float)) for v in d.values()), "expected input values"
    base.add_levers(wb, LEVERS)
    build_sheet(wb, data, sha, old_oil, old_cars)
    link(wb)
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "4 Nov: CR-052"
    Ch.cell(n, 2).value = "The energy link"
    Ch.cell(n, 3).value = (
        "CR-052 (with CR-053 to CR-055): new Energy link sheet from the energy workbook (SHA-256 " + sha[:16] + "…). "
        "Story case (lever en_paths): home oil from the field model with early water flooding (CT3 C, M8) replaces "
        "Resources!I; vehicles built from the CT5 path replace Champions!U; Stress keeps the earlier paths. CR-053: the "
        "oil trust's stakes ($65m, 1920-28) out of ordinary investment abroad into the champions' assets abroad, with a "
        "return on the entitlement crude (conc_div). Memos: power investment, the Fund's power credit, utility receipts, "
        "royalties, oil imports. The investment and consumption account (inv_share test path, inv_gap) and the "
        "proportional industrial index for the energy workbook (Energy link AC). MODEL.")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    wb.save(a.dst)
    print(f"saved {a.dst}")


if __name__ == "__main__":
    main()
