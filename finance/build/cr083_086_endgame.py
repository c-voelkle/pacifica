"""CR-083 to CR-086: the endgame of 1931-32 in the workbook (24 November 2026).

    python3 finance/build/cr083_086_endgame.py IN.xlsx OUT.xlsx [--off]

IN is the workbook after cr081_082_provisioning.py (the last step of cr057_rebuild_pair.py). The
script never recalculates; run LibreOffice afterwards. With --off the master lever eg_on is saved
at 0 in both cases, which must reproduce IN's values exactly.

Authorization: the author, 23 November 2026, 23:52 ("Please run the third review and then proceed
to rebuild the models"), and 24 November 2026, 14:56 ("Please proceed to rebuild the workbooks"),
after the four CRs were approved (13:08) and merged to main (pull request 88). Every amount is
MODEL, and the sizes marked "drafter's proposal" are proposals for bands the CRs leave OPEN.

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

AUTHOR = "the author, 23 November 2026, 23:52, and 24 November 2026, 14:56 (CR-083 to CR-086, approved 24 November 2026)"
base.AUTHOR = AUTHOR

LEVERS = [
    "— CR-083 to CR-086: the endgame of 1931-32 (approved 24 Nov 2026) —",
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
    ("eg_stab", "Private stabilization credits to Britain and Germany, 1932 ($m)", 300, 400, "$m",
     "CR-086 B1 (MODEL, no source)", "Private San Francisco syndicates; the Bank discounts, the Treasury does not borrow. France sits on gold and asks for no credit (CR-086 B3). Memo: if it is entered as Private lending the gold and money tests must be read again."),
    ("eg_gulf_floor", "The oil trust's undertaking to the Gulf, 1932-37: floor as a share of its 1929-31 liftings", 0.75, 0.75, "share",
     "Author, 24 Nov 2026, 15:56 (\"I approve three-quarters.\")", "CR-084 B3.4. Checked on the Endgame sheet against the energy workbook's Gulf crude."),
    ("eg_gbr_scale", "Great Bear: output against the central profile (295 t U to 1932)", 1, 0.68, "multiple",
     "Author, 24 Nov 2026, 16:26; CR-086 A (band 200-350 t)", "Central profile 5, 10, 15 and 25 t U a year from 1913, 1917, 1922 and 1927: summer barges. Stress is the band's low end."),
    ("eg_gbr_cost", "Uranium cost, Great Bear (1913 $/kg U)", 8.5, 11.0, "$/kg",
     "Author, 24 Nov 2026, 16:26 (MODEL, by analogy)", "Rich vein ore with silver, four legs of river and portage freight: between Fergana (8) and Joachimsthal (9)."),
    ("eg_sweep_cost", "Uranium cost, Urgeirica's dumps and Radium Hill, 1926-27 (1913 $/kg U)", 10.0, 12.0, "$/kg",
     "Story assumption (MODEL, no source)", "About 25 t U bought as dumps, ore and stock (CR-086 A)."),
    ("eg_be_rate", "Belgium's royalty at Shinkolobwe from 1929 (1913 $/kg U; floor $0.6m a year)", 5.0, 6.0, "$/kg",
     "Author, 24 Nov 2026, 16:26 (MODEL)", "CR-086 A: the revision of 1928-29. The flat $0.6m had fallen from $4.00 to $2.40 a kg when output rose in 1927."),
    ("eg_be_radium", "Belgium's larger free allowance of radium salt, 1929-32 (1913 $m a year)", 0.10, 0.15, "$m",
     "Author, 24 Nov 2026, 16:26 (MODEL)", "Taken off the Atomic sheet's radium and source trade."),
    ("eg_indies", "Indies treasury bond, autumn 1932: the tranche placed in San Francisco ($m)", 20, 30, "$m",
     "Author, 24 Nov 2026, 16:26 (MODEL, by analogy)", "CR-084 C1. Private placement, no guarantee by the Realm or the Concord. Sized against the Indies' dollar issues in New York in 1922: $40m in January, $40m in March and $20m in April, at 6%."),
    ("eg_guaymas", "Guaymas port bonds placed in San Francisco, 1932 ($m)", 5, 8, "$m",
     "Author, 24 Nov 2026, 16:26 (MODEL, by analogy)", "CR-086 E2. A third of the Huludao Harbour Trust (CR-042): wharves and dredging in a sheltered bay with a railway."),
    ("eg_cn_res", "China's reserve compact of 1932: the balance that moves under it ($m)", 25, 40, "$m",
     "Author, 24 Nov 2026, 16:26 (MODEL, by analogy)", "CR-086 B6. Not a new balance: the Money sheet already counts $100m in 1932 for Korea, the Gulf and China's reserve banks, and this is the part that moves under China's own compact. China's interior stays on silver."),
    ("eg_sg_capital", "Singapore: naval works not built after the halt (GBP m; Britain's money)", 5.0, 5.0, "GBP m",
     "Author, 24 Nov 2026, 16:26; Hansard (MODEL)", "The scheme in the Navy Estimates is GBP 7.75m (Hansard, 23 Nov 1927 and 15 Mar 1932), taken without the floating dock (GBP 0.97m); about GBP 2.8m is spent by the spring of 1932 (GBP 3.44m by February 1933, less most of the 1932 vote of GBP 0.69m)."),
    ("eg_sg_inhand", "Singapore: of which the work in hand under the decision of 1930 (GBP m)", 2.3, 2.3, "GBP m",
     "Hansard, 9 and 15 March 1932 (MODEL)", "Estimate for the contract and contingent services GBP 5.145m, less about GBP 2.8m spent. The rest of the GBP 5.0m was already deferred to a review in 1935."),
    ("eg_sg_other", "Singapore: Army and Air works in the scheme of 1929 (GBP m)", 2.6, 2.6, "GBP m",
     "Hansard, 17 December 1929", "GBP 2.0m on Army funds and GBP 0.6m on Air funds, beside GBP 9.0m on Navy Votes, in the whole scheme of GBP 11.6m; how much of it the halt saves is not sized."),
    ("eg_sg_upkeep", "Singapore: yearly upkeep of a capital-ship dockyard avoided (GBP m a year)", 0.4, 0.5, "GBP m",
     "Author, 24 Nov 2026, 16:26 (MODEL, no source)", "No hull is paid off: the ships go elsewhere."),
    ("eg_fx", "Sterling in 1932 ($ a pound)", 3.5, 3.5, "$",
     "Quotations of 1932; Bank of England", "3.50 in mid-January, 3.82 at the end of March, 3.61 at the start of July, 3.30 in late October, a low of 3.145 on 29 November. The year's average, about 3.51, is recalled; the table was not reached. Par before September 1931 was 4.8665."),
    ("eg_nz_paid", "New Zealand's Singapore instalments paid to March 1932, credited by London (GBP m)", 0.60, 0.60, "GBP m",
     "Author, 24 Nov 2026, 16:26; Papers Past and Hansard", "GBP 125,000 a year from 1927-28, cut to GBP 100,000 in 1931: four at 125,000 and one at 100,000."),
    ("eg_seria", "Seria: the oil trust's offtake from Shell in 1932 (m bbl)", 0.5, 0.3, "m bbl",
     "Author, 24 Nov 2026, 16:26 (MODEL)", "Output began in the first quarter of 1932; exports were 371,591 t in 1934. Sold in Asia in place of Gulf crude; East Borneo's new blocks give nothing before 1935."),
    ("eg_yen", "Yen reset against the gold dollar", 0.2, 0.25, "share",
     "CR-085 A7 (MODEL)", "Inside the band of 20-25%."),
]

ROWS = [
    (1871, 1871, "British Columbia: loan to the colony with the Puget Sound rail link (CR-083)", "Loan", "Continental", "British Columbia",
     "=eg_on*eg_bc_loan", "No", "Approved", "§15 (CR-083 A2)", "The colony stays outside Confederation"),
    (1928, 1931, "Tokyo station: Tokyo Dento's civil works and turbines, against the cost on Atomic (CR-085)", "Receipt", None, "Japan",
     "=eg_on*eg_tk_cost*eg_tk_share/4", "No", "Approved", "§32 (CR-085 C1)", "Closes the Atomic sheet's 'financing OPEN, entered as Pacifica's'"),
    (1932, 1932, "Fanning and Washington: plantation buyout into the Ka Lokahi trust (CR-084)", "Purchase", None, "Britain",
     "=eg_on*eg_fanning", "No", "Approved", "§37 (CR-084 B4)", "Fanning Island Limited, at published valuation"),
    (1932, 1932, "Prairie wheat contract, first harvest: the Patrimony board's purchase (CR-083; memo, no Treasury cash)", "Commitment",
     None, "Canada", "=eg_on*eg_wheat_t*eg_wheat_usd/1000000", "No", "Approved", "§34 (CR-083 A11)", "Ten harvests, 1932-41; resold in Asia"),
    (1932, 1932, "Caledonia: the dominion's gold-dollar bonds refunded by private syndicates (CR-083; memo)", "Commitment",
     None, "Caledonia", "=eg_on*eg_bc_debt", "No", "Approved", "§37 (CR-083 A10)", "Bonds San Francisco already holds; no Treasury share, no Development Fund lending abroad"),
    (1932, 1932, "Private stabilization credits under the monetary settlement (CR-086; memo)", "Commitment",
     None, "Britain & Germany", "=eg_on*eg_stab", "No", "Approved", "§37 (CR-086 B1)", "Private syndicates; not the Treasury's"),
    (1932, 1932, "Indies treasury bond, the San Francisco tranche (CR-084; memo, private placement)", "Commitment",
     None, "Netherlands Indies", "=eg_on*eg_indies", "No", "Approved", "§37 (CR-084 C1)", "After the States General approve the Batavia Compact; no guarantee"),
    (1932, 1932, "Guaymas port bonds placed in San Francisco (CR-086; memo, private)", "Commitment",
     None, "Mexico", "=eg_on*eg_guaymas", "No", "Approved", "§37 (CR-086 E2)", "Secured on port dues under Mexico's charter; a third of Huludao (CR-042)"),
]

# Yearly series on the Endgame sheet, rows aligned with the Atomic sheet (row 6 = 1846, row 92 = 1932).
def _gbr(y: int) -> float:
    return 25 if y >= 1927 else 15 if y >= 1922 else 10 if y >= 1917 else 5 if y >= 1913 else 0


SWEEP = {1926: 15, 1927: 10}


def gulf_crude() -> dict:
    """Gulf crude that can come home, 1929-32, from the energy workbook's cached values (Fuels, column F)."""
    p = Path(__file__).resolve().parents[2] / "energy" / "Pacifica_energy_model_1846-1932.xlsx"
    S = openpyxl.load_workbook(p, data_only=True)["Fuels"]
    if S["F5"].value != "Gulf crude that can come home (m bbl)":
        raise SystemExit(f"energy workbook: Fuels!F5 is not the Gulf crude column: {S['F5'].value!r}")
    out = {}
    for r in range(6, S.max_row + 1):
        y = S.cell(r, 1).value
        if y in (1929, 1930, 1931, 1932):
            v = S.cell(r, 6).value
            if not isinstance(v, (int, float)):
                raise SystemExit("energy workbook has no cached values; recalculate it first")
            out[y] = round(float(v), 1)
    return out


GULF = gulf_crude()


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
    S["A1"] = "The endgame of 1931-32 (CR-083 to CR-086; approved 24 November 2026, MODEL)"
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
        ("Great Bear, Urgeirica and Radium Hill are on the Atomic sheet since 24 November 2026: rows 57 to 61 below", None),
        ("(row kept so that the cells below do not move)", None),
        ("Memo: prairie wheat contract over ten harvests ($m)", "=eg_wheat_t*eg_wheat_usd*10/1000000"),
        ("Memo: uranium mined to 1932 without Great Bear, Urgeirica and Radium Hill, t U (canon before CR-086: about 5,800)", "=SUM(Atomic!B6:F92)"),
        ("Memo: with them, t U (CR-086 A's band was 6,000 to 6,200)", "=Atomic!G94"),
        (None, None),
        ("Japan's rescue of 1927: the Treasury's participation ($m; sheet Japan rescue)", "='Japan rescue'!D11"),
        ("One of five instalments, 1929 to 1933 ($m a year)", "=B31/5"),
        ("Instalments still due after the reset (1932 and 1933): extra cost to Japan in yen, as $m at the old parity", "=2*B32*B22"),
        ("Memo: the Bank of Japan's ceiling and the banks' own repayments are Japan's books, not this workbook's", None),
        (None, None),
        ("Gulf crude the trust brings home, 1929 (m bbl; energy workbook, Fuels, Story case, read at build)", GULF[1929]),   # 36
        ("... 1930", GULF[1930]), ("... 1931", GULF[1931]), ("... 1932", GULF[1932]),                                          # 37-39
        ("1932 as a share of the average of 1929-31", "=B39/AVERAGE(B36:B38)"),                                              # 40
        ("The undertaking's floor (eg_gulf_floor)", "=eg_gulf_floor"),                                                       # 41
        ("Does the floor hold in 1932? (memo; not counted in Problems)", '=IF(B40>=B41,"OK","Check")'),                      # 42
        ("Room above the floor in 1932 (m bbl)", "=B39-B41*AVERAGE(B36:B38)"),                                               # 43
        ("Seria: the trust's offtake in 1932, sold in Asia in place of Gulf crude (m bbl)", "=eg_on*eg_seria"),              # 44
        ("Room above the floor after Seria (m bbl); East Borneo's new blocks give nothing in 1932", "=B43-B44"),             # 45
        (None, None),
        ("Singapore, Britain's money: naval works not built after the halt (GBP m)", "=eg_sg_capital"),                      # 47
        ("... in $m at the pound of 1932", "=B47*eg_fx"),                                                                    # 48
        ("... yearly upkeep of a capital-ship dockyard avoided (GBP m a year); no hull paid off", "=eg_sg_upkeep"),          # 49
        ("New Zealand: instalments paid to March 1932, credited by London (GBP m)", "=eg_nz_paid"),                          # 50
        ("New Zealand: the rest of its GBP 1.0m pledge, not called (GBP m)", "=1-eg_nz_paid"),                               # 51
        (None, None),
        ("China's reserve compact of 1932: the balance in San Francisco that moves under it ($m)", "=eg_on*eg_cn_res"),      # 53
        ("... is part of the balances Money already counts for Korea, the Gulf and China's reserve banks ($m, 1932)", "=Money!G92"),  # 54
        ("... so the compact asks no new gold; the half cover already held against its part ($m)", "=B53/2"),               # 55
        (None, None),
        ("Great Bear ore to 1932 (t U; columns D to I, entered on Atomic)", "=eg_on*SUM(E6:E92)"),                           # 57
        ("Urgeirica's dumps and Radium Hill, 1926-27 (t U)", "=eg_on*SUM(F6:F92)"),                                          # 58
        ("Uranium mined to 1932, all sources (t U; Atomic)", "=Atomic!G94"),                                                 # 59
        ("Belgium's higher royalty, 1929-32 (1913 $m, total)", "=eg_on*SUM(H6:H92)"),                                        # 60
        ("Great Bear: mining, freight and Canada's royalty, 1913-32 (1913 $m, total)",
         "=eg_on*(SUM(E6:E92)*eg_gbr_cost/1000+SUM(G6:G92))"),                                                               # 61
        (None, None),
        ("Singapore: of the works not built, the work in hand under the decision of 1930 (GBP m)", "=eg_sg_inhand"),        # 63
        ("Singapore: the part already deferred to the review of 1935 (GBP m)", "=B47-B63"),                                  # 64
        ("Singapore: Army and Air works in the scheme of 1929, not sized as a saving (GBP m)", "=eg_sg_other"),              # 65
    ]
    for i, (lab, f) in enumerate(rows, start=4):
        if lab is None:
            continue
        S.cell(i, 1).value = lab
        S.cell(i, 2).value = f
    # yearly series, rows as on Atomic
    for c_, h in zip("DEFGHI", ("Year", "Great Bear, t U", "Urgeirica and Radium Hill, t U", "Great Bear: Canada's royalty (1913 $m)",
                                "Belgium: royalty above the flat $0.6m (1913 $m)", "Belgium: free radium salt (1913 $m)")):
        S[f"{c_}5"] = h
    for r in range(6, 93):
        y = 1840 + r
        S[f"D{r}"] = y
        S[f"E{r}"] = f"={_gbr(y)}*eg_gbr_scale" if _gbr(y) else 0
        S[f"F{r}"] = SWEEP.get(y, 0)
        S[f"G{r}"] = 0.10 if y >= 1927 else 0.05 if y >= 1913 else 0
        S[f"H{r}"] = f"=MAX(0,Atomic!E{r}*eg_be_rate/1000-0.6)" if y >= 1929 else 0
        S[f"I{r}"] = "=eg_be_radium" if y >= 1929 else 0
    for c_ in "DEFGHI":
        S.column_dimensions[c_].width = 16
    S.column_dimensions["A"].width = 86
    S.column_dimensions["B"].width = 18
    for r in (7, 8, 9, 10, 12, 17, 22, 40, 41):
        S.cell(r, 2).number_format = "0.0%"
    for r in (4, 6, 13, 14, 18, 19, 20, 23, 28, 29, 31, 32, 33, 36, 37, 38, 39, 43, 44, 45, 47, 48, 49, 50, 51, 53, 54, 55, 57, 58, 59, 60, 61, 63, 64, 65):
        S.cell(r, 2).number_format = "0.0"


def write_off(wb) -> None:
    L = wb["Loans"]
    f = L["N92"].value
    if not (isinstance(f, str) and f.startswith("=IF($A92=1918")):
        raise SystemExit(f"Loans!N92 is not the expected write-off formula: {f!r}")
    L["N92"].value = f + "+Endgame!$B$14"


def atomic(wb) -> None:
    """Great Bear, the sweep of 1926-27 and Belgium's revision, entered on the Atomic sheet through eg_on."""
    A = wb["Atomic"]
    if A["G5"].value != "Total mined" or A["M5"].value != "Contracts, concessions, shares" or A["T5"].value != "Radium and source trade":
        raise SystemExit("Atomic sheet: columns G, M, T are not where this step expects them")
    for r in range(73, 93):  # 1913-1932
        g, l_, m_, t = (A[f"{c_}{r}"].value for c_ in "GLMT")
        if g != f"=SUM(B{r}:F{r})" or not str(l_).startswith("=(B") or not isinstance(m_, (int, float)) or not isinstance(t, (int, float)):
            raise SystemExit(f"Atomic row {r} is not as expected")
        A[f"G{r}"].value = f"{g}+eg_on*(Endgame!E{r}+Endgame!F{r})"
        A[f"L{r}"].value = f"{l_}+eg_on*(Endgame!E{r}*eg_gbr_cost+Endgame!F{r}*eg_sweep_cost)/1000"
        A[f"M{r}"].value = f"={m_}+eg_on*(Endgame!G{r}+Endgame!H{r})"
        A[f"T{r}"].value = f"={t}-eg_on*Endgame!I{r}"


def log(wb, ids: list[str], off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "24 Nov: CR-083 to CR-086"
    Ch.cell(n, 2).value = "The endgame of 1931-32"
    Ch.cell(n, 3).value = (f"Master lever eg_on (at 0 the input workbook exactly). Loans: Britain's cancelled annuities written off in "
                           f"1932 (new Endgame sheet). Events {ids[0]}-{ids[-1]}: the loan of 1871 to British Columbia; Tokyo Dento's "
                           "share of the Tokyo station; the Fanning buyout; memos for the prairie wheat contract, the private refunding "
                           "of the dominion's bonds and the private stabilization credits (Britain and Germany). Approved 24 November 2026; "
                           "rebuilt on main the same day with Japan's rescue instalments and the mined total as memos, and the Gulf "
                           "undertaking's floor of three-quarters (author, 15:56) checked against the energy workbook. Author, 16:26: "
                           "Great Bear (295 t U), Urgeirica and Radium Hill (25 t U) and Belgium's revision of 1929 entered on the "
                           "Atomic sheet; memo rows for the Indies bond and the Guaymas port bonds; memos for Singapore, New "
                           "Zealand, China's reserve compact and Seria's offtake. MODEL.")
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
    atomic(wb)
    log(wb, ids, a.off)
    wb.save(a.dst)
    print(f"wrote {a.dst}: {len(LEVERS) - 1} levers, Events {ids[0]}-{ids[-1]}, sheet Endgame")


if __name__ == "__main__":
    main()
