"""CR-083 to CR-086: the endgame of 1931-32 in the workbook (24 November 2026).

    python3 finance/build/cr083_086_endgame.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after cr081_082_provisioning.py (the last step of cr057_rebuild_pair.py). The
script never recalculates; run LibreOffice afterwards. With --off the master lever eg_on is saved
at 0 in both cases, which must reproduce IN's values exactly.

Authorization: the author, 23 November 2026, 23:52 ("Please run the third review and then proceed
to rebuild the models"). The four CRs are DRAFTS on branch drafts/cr083-086-endgame and are not
canon; this step lives on that branch with them. Every amount is MODEL, and the sizes marked
"drafter's proposal" are proposals for bands the drafts leave OPEN.

What this adds:
- Loans, Europe group, 1932: Britain's cancelled annuities written off (CR-084 B1, T-A2). The
  workbook holds the Treasury's European claims as one balance repaid at a flat rate, so Britain's
  part is a lever (eg_uk_share) and the 62-year schedule of 1923 is worked on the new Endgame sheet:
  53 annuities left after the moratorium year; Caledonia's two and the signature's four from the
  near end and the retrenchment's eleven from the end of the schedule (author, 24 November 2026,
  00:12); the suspended annuity written off on 1 August.
- Events rows: the loan of 1871 to British Columbia (CR-083 A2); Tokyo Dento's share of the Tokyo
  station, as a receipt against a cost the Atomic sheet enters as Pacifica's (CR-085 C1); the
  Fanning and Washington plantation buyout (CR-084 B4); and three memos that move no Treasury cash:
  the Patrimony board's prairie wheat contract (CR-083 A11), the private refunding of the dominion's
  gold-dollar bonds (CR-083 A10) and the private stabilization credits (CR-086 B1).
- An Endgame sheet (memo): the annuity arithmetic, Britain's yearly payment before and after, and
  the yen reset's effect on Japan's quota in yen (CR-085 A7).

What is not added, and why:
- the Singapore saving and New Zealand's rebate: Britain's money;
- the Mariveles dock: the Philippine crown's budget; the Indies bond and the Guaymas port bonds:
  private placements, no Treasury cash;
- Great Bear's ore, the Portuguese and South Australian purchases and the monazite stock (CR-086
  Part A): they belong on the Atomic sheet, whose sources are fixed in cr049/cr050; shown as a memo
  on the Endgame sheet until those scripts are reopened;
- the Kansai station: no ground broken before May 1933, after the book's last year;
- Belgium's higher royalty from 1929: inside the Atomic sheet's contracts line (no separate size);
- Japan's rice and Hokkaido (CR-085 D1): the population model, not this workbook;
- the Gulf's lifting-share undertaking, Seria's offtake and Bintan's bauxite: the energy workbook
  (not rebuilt in this step; the tonnages are OPEN in CR-084).
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "the author, 23 November 2026, 23:52 (CR-083 to CR-086, drafts)"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-083 to CR-086: the endgame of 1931-32 (drafts; 24 Nov 2026) —",
    ("eg_on", "Endgame: 1 = on; 0 = the input workbook exactly", 1, 1, "switch",
     "Author, 23 Nov 2026, 23:52", "0 reproduces the input workbook exactly."),
    ("eg_uk_share", "Britain's part of the Treasury's European claims", 0.6, 0.6, "share",
     "Story assumption (MODEL, no source)", "The workbook holds Britain's, France's and the others' debts as one balance."),
    ("eg_rate", "Britain's funding of 1923: interest", 0.033, 0.033, "rate",
     "Paths, coupon on European loans", "Canon: 'at reduced interest'."),
    ("eg_left", "Annuities left after the moratorium year (1933-1985)", 53, 53, "annuities",
     "CR-084 B1", "Sixty-two from 1923; 1923-1930 paid, 1931-32 suspended."),
    ("eg_n1", "Tranche 1, Caledonia: annuities cancelled, from the near end (1932-33 onward)", 2, 2, "annuities",
     "Author, 24 Nov 2026, 00:12 (MODEL)", "CR-083 A7. Earned by the Severance Act, late June 1932."),
    ("eg_n2", "Tranche 2, the retrenchment: annuities cancelled, from the end of the schedule", 11, 13, "annuities",
     "Author, 24 Nov 2026, 00:12 (MODEL); Stress is the top of the band of 20", "CR-084 B1. Trigger: Westminster ratifies the retrenchment treaty, autumn 1932."),
    ("eg_n3", "Tranche 3, the signature: annuities cancelled, from the near end, after Caledonia's", 4, 5, "annuities",
     "Author, 24 Nov 2026, 00:12 (MODEL); T-A2 Case B", "CR-084 B5. Trigger: Westminster ratifies the Final Act, autumn 1932."),
    ("eg_bc_loan", "Loan of 1871 to the colony of British Columbia ($m)", 2, 3, "$m",
     "CR-083 A2 (MODEL)", "With the Puget Sound rail link and free entry for coal, timber and fish."),
    ("eg_bc_debt", "The dominion's gold-dollar bonds refunded by private syndicates, 1932 ($m)", 90, 120, "$m",
     "CR-083 A3, A10 (MODEL, recalled)", "Mountain section, the Pacific Great Eastern and war borrowing. Our timeline's province owed well over $100m by 1932 (to verify). A refunding of bonds San Francisco already holds: memo, no new outflow."),
    ("eg_wheat_t", "Prairie wheat contract: tonnes a harvest", 1000000, 1200000, "tonnes",
     "Author, 24 Nov 2026, 00:12 (MODEL)", "CR-083 A11. Canada sold 5.6 million tonnes abroad in 1931-32 (population/data/provisioning.toml)."),
    ("eg_wheat_usd", "Prairie wheat contract: price ($ a tonne)", 18, 18, "$ a tonne",
     "As pv_gran_usd (MODEL)", "The slump's price."),
    ("eg_fanning", "Fanning and Washington: plantation buyout ($m)", 0.4, 0.6, "$m",
     "CR-084 B4 (MODEL, no source)", "At published valuation, from Fanning Island Limited."),
    ("eg_tk_cost", "Tokyo station: cost as entered on Atomic, current $m", 22.4, 22.4, "$m",
     "Atomic sheet, 1928-1931", "8, 10, 10 and 4 in 1913 $m at the Paths price level."),
    ("eg_tk_share", "Tokyo station: Tokyo Dento's share (site, containment, turbines, grid)", 0.55, 0.45, "share",
     "CR-085 C1 (MODEL)", "The Works supplies the nuclear island and core on a 20-year lease."),
    ("eg_stab", "Private stabilization credits to Britain, Germany and France, 1932 ($m)", 300, 400, "$m",
     "CR-086 B1 (MODEL, no source)", "Private San Francisco syndicates; the Bank discounts, the Treasury does not borrow. Memo: if it is entered as Private lending the gold and money tests must be read again."),
    ("eg_yen", "Yen reset against the gold dollar", 0.2, 0.25, "share",
     "CR-085 A7 (MODEL)", "Inside the band of 20-25%."),
]

ROWS = [
    (1871, 1871, "British Columbia: loan to the colony with the Puget Sound rail link (CR-083)", "Loan", "Continental", "British Columbia",
     "=eg_on*eg_bc_loan", "No", "Draft", "§15 (CR-083 A2)", "The colony stays outside Confederation"),
    (1928, 1931, "Tokyo station: Tokyo Dento's civil works and turbines, against the cost on Atomic (CR-085)", "Receipt", None, "Japan",
     "=eg_on*eg_tk_cost*eg_tk_share/4", "No", "Draft", "§32 (CR-085 C1)", "Closes the Atomic sheet's 'financing OPEN, entered as Pacifica's'"),
    (1932, 1932, "Fanning and Washington: plantation buyout into the Ka Lokahi trust (CR-084)", "Purchase", None, "Britain",
     "=eg_on*eg_fanning", "No", "Draft", "§37 (CR-084 B4)", "Fanning Island Limited, at published valuation"),
    (1932, 1932, "Prairie wheat contract, first harvest: the Patrimony board's purchase (CR-083; memo, no Treasury cash)", "Commitment",
     None, "Canada", "=eg_on*eg_wheat_t*eg_wheat_usd/1000000", "No", "Draft", "§34 (CR-083 A11)", "Ten harvests, 1932-41; resold in Asia"),
    (1932, 1932, "Caledonia: the dominion's gold-dollar bonds refunded by private syndicates (CR-083; memo)", "Commitment",
     None, "Caledonia", "=eg_on*eg_bc_debt", "No", "Draft", "§37 (CR-083 A10)", "Bonds San Francisco already holds; no Treasury share, no Development Fund lending abroad"),
    (1932, 1932, "Private stabilization credits under the monetary settlement (CR-086; memo)", "Commitment",
     None, "Britain, Germany & France", "=eg_on*eg_stab", "No", "Draft", "§37 (CR-086 B1)", "Private syndicates; not the Treasury's"),
]


def add_rows(wb) -> list[str]:
    ids = []
    for a, b, label, cat, grp, party, h, gold, status, sec, basis in ROWS:
        r = base.add_event(wb, [a, b, label, cat, grp, party, h, None, gold, status, sec, basis])
        if r > 400:
            raise SystemExit("Events table full")
        ids.append(wb["Events"].cell(r, 1).value)
    return ids


def build_sheet(wb) -> None:
    S = wb.create_sheet("Endgame")
    S["A1"] = "The endgame of 1931-32 (CR-083 to CR-086; drafts, MODEL)"
    S["A2"] = ("Britain's 62-year funding of 1923 as level annuities at eg_rate. The Loans sheet takes the write-off of 1932 from "
               "cell B14. Everything here is a memo except B14.")
    rows = [
        ("Britain's part of the Treasury's European claims, end of 1931 ($m)", "=eg_uk_share*Loans!O91"),          # 4
        ("Value of one annuity for $1 a year over the annuities left", "=(1-(1+eg_rate)^-eg_left)/eg_rate"),          # 5
        ("Britain's annuity ($m a year)", "=B4/B5"),                                                                    # 6
        ("Tranche 1, Caledonia (near end): principal cancelled, share of the book", "=(1-(1+eg_rate)^-eg_n1)/eg_rate/B5"),  # 7
        ("Tranche 2, the retrenchment (far end): share of the book",
         "=(1+eg_rate)^-(eg_left-eg_n2)*(1-(1+eg_rate)^-eg_n2)/eg_rate/B5"),                                     # 8
        ("Tranche 3, the signature (near end, after Caledonia's): share of the book",
         "=(1+eg_rate)^-eg_n1*(1-(1+eg_rate)^-eg_n3)/eg_rate/B5"),             # 9
        ("All three tranches: share of the book cancelled", "=B7+B8+B9"),                                              # 10
        ("Annuities cancelled, by count", "=eg_n1+eg_n2+eg_n3"),                                                       # 11
        ("By count, share of the annuities left", "=B11/eg_left"),                                                     # 12
        ("The suspended annuity of 1931-32: principal part written off ($m)", "=B4*Paths!AA90"),                        # 13
        ("Written off in 1932 ($m) [read by Loans]", "=eg_on*(B4*B10+B13)"),                                           # 14
        ("Britain pays nothing in the annuity years", '="1932-33 to "&(1931+eg_n1+eg_n3)&"-"&(eg_n1+eg_n3+32)'),                                             # 15
        ("Britain's last annuity year ends in", "=1985-eg_n2"),                                                      # 16
        ("If all three tranches came from the end (item 84-8 as first approved): share of the book",
         "=(1+eg_rate)^-(eg_left-B11)*(1-(1+eg_rate)^-B11)/eg_rate/B5"),                                               # 17
        ("Tranche 1 ($m)", "=B4*B7"), ("Tranche 2 ($m)", "=B4*B8"), ("Tranche 3 ($m)", "=B4*B9"),                      # 18-20
        (None, None),
        ("Yen reset: Japan's gold-dollar quota costs this much more in yen", "=1/(1-eg_yen)-1"),                       # 22
        ("Japan's quota of the common budget ($m a year; Events E85 gives Pacifica's)", "=10*(1-pac_quota)"),          # 23
        (None, None),
        ("Memo, not in the Atomic sheet (CR-086 Part A): Great Bear ore to 1932, t U", "200 to 350"),
        ("Memo: Urgeirica dumps and Radium Hill purchase, t U", "small; OPEN"),
        ("Memo: prairie wheat contract over ten harvests ($m)", "=eg_wheat_t*eg_wheat_usd*10/1000000"),
    ]
    for i, (lab, f) in enumerate(rows, start=4):
        if lab is None:
            continue
        S.cell(i, 1).value = lab
        S.cell(i, 2).value = f
    S.column_dimensions["A"].width = 86
    S.column_dimensions["B"].width = 18
    for r in (7, 8, 9, 10, 12, 17, 22):
        S.cell(r, 2).number_format = "0.0%"
    for r in (4, 6, 13, 14, 18, 19, 20, 23):
        S.cell(r, 2).number_format = "0.0"


def write_off(wb) -> None:
    L = wb["Loans"]
    f = L["N92"].value
    if not (isinstance(f, str) and f.startswith("=IF($A92=1918")):
        raise SystemExit(f"Loans!N92 is not the expected write-off formula: {f!r}")
    L["N92"].value = f + "+Endgame!$B$14"


def log(wb, ids: list[str], off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "24 Nov: CR-083 to CR-086 (drafts)"
    Ch.cell(n, 2).value = "The endgame of 1931-32"
    Ch.cell(n, 3).value = (f"Master lever eg_on (at 0 the input workbook exactly). Loans: Britain's cancelled annuities written off in "
                           f"1932 (new Endgame sheet). Events {ids[0]}-{ids[-1]}: the loan of 1871 to British Columbia; Tokyo Dento's "
                           "share of the Tokyo station; the Fanning buyout; memos for the prairie wheat contract, the private refunding "
                           "of the dominion's bonds and the private stabilization credits. Drafts, not canon. MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["eg_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    if "pv_on" not in wb.defined_names:
        raise SystemExit("needs the workbook after cr081_082_provisioning.py")
    if "eg_on" in wb.defined_names:
        raise SystemExit("CR-083 to CR-086 already added")
    base.add_levers(wb, LEVERS)
    ids = add_rows(wb)
    build_sheet(wb)
    write_off(wb)
    log(wb, ids, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, Events {ids[0]}-{ids[-1]}, sheet Endgame")


if __name__ == "__main__":
    main()
