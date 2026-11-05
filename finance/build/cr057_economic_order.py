"""CR-057 in the financial workbook: the money block, the Patrimony, the Crown share, the income tax and the saving account.

    python3 finance/build/cr057_economic_order.py IN.xlsx OUT.xlsx [--off]

IN is the CR-051/054/055 workbook (cr051_054_055_champions.py on the CR-052 link). The script never
recalculates; run LibreOffice (xlsx skill scripts/recalc.py) afterwards. With --off the master lever
c57_on is saved at 0 in both cases: that build must reproduce IN's values exactly (the identity check).

Authorization: the author, 5 November 2026: "Can you update the energy and financial models
accordingly and report back before integrating?" (CR-057 H1-H3, H6, H7; CT13 adapt, CT14 and CT15
amend). Nothing in the storyline or the register changes. All amounts are MODEL.

One master lever, c57_on (Story 1, Stress 1). Everything below is gated by it; at 0 every formula
reduces to the one it replaces (x - 0, x * (1 - 0), IF(c57_on=1, new, old)).

H1, the money block (new sheet Money; Gold & money, Economy, Budget X):
- partner official dollar balances held in San Francisco (Japan, the Philippine peso reserve, the
  others from 1900), covered half in gold; earmarked partner gold is a memo, not Pacifica's;
- from price_from (1914) the money stock M(y) = (gold at end of y-1 - 0.5 x partner balances(y-1)) /
  the working cover (c_work, reached from the cover held at the end of 1913 by c_glide a year; c_ster
  in 1927-28, the sterilization of MR-02), cut back by the automatic
  tightening (guard 3) if the 40% floor on all liabilities would fail; the price level
  P(y) = M(y) / (money_ratio x k_slump(1930-32) x estimated real GDP), estimated from last year's real
  GDP, this year's residents, real growth per resident and output gap: no circular reference;
- Economy!H takes the derived level (the slump_price mechanism goes with it); Economy!S deflates the
  domestic part by it and the world-priced part (mining, the champions, the Gulf) by Paths!B; notes and bank
  reserves = M + the Japan-rescue item; the power estate's bonds go to savers (rb_est 0, CT15) and the
  Reserve Bank buys no Treasury bonds (cb_buy 0, MR-06);
- the new-issue coupon is a real rate plus the trailing five-year price change, floored at 2%; the
  coupon on the stock blends it in as bonds are issued and repaid (Budget X reads last year's);
- domestic costs priced in 1913 dollars in the atomic programme (Atomic R, the Works' deflators) follow
  the derived level; Siberia and the Russian-war events cannot (they feed Gold & money E, which the
  money rule reads) and stay on Paths!B, as do world-priced goods;
- the migration pull (Labour T) and the partners' pull (Partners B) read Pacifica's lead at US prices,
  so a lower Pacifican price level does not read as a poorer Pacifica.
H3, the Patrimony (new sheet Patrimony; Budget, Debt & cash, Economy D):
- royalties, the canal, the state's estates (the Works' own returns of 1917-27 stay with the Works
  for the halls), half the guest-worker levy from 1890 and leased-land rents from 1900 leave the Budget;
- a real 4.5% plus the trailing price change (floor 2%); abroad from 1919 (10% rising to 50% in 1929);
  a 1931-32 loss on the abroad share; nothing spent before 1910, then 3% of last year's value paid
  into the Budget and spent on earmarked works (budget-neutral), building an infrastructure stock;
- the old Development Fund's financing (dev_share, the reserve above the buffer, dev_bonds) off;
- a lagged tax-cut rule on domestic taxes toward a small target surplus (no tax rise in 1930-32);
  a share of each cut saved and invested privately at the ordinary return;
- Economy!D = MIN(dev_cap, (dev_return x (the state's development investment + the Patrimony's
  works) + priv_ret x the private investment from tax cuts) / last year's GDP): the existing flow
  convention of the column (the stocks are memos, as the old Development stock was).
H6, the Crown share: no stake in competitive industries; the chartered stake only on the trunk rights
of way (a fraction lever, crown_row: the workbook has no railway line to isolate them); royalty
floors of one eighth on auctioned leases (oil; minerals as a variant).
H7, the income tax (CT13 adapt): Budget L relabelled; a memo on the War Revenue Act of 1915; no numbers.
H2, the saving account (new sheet Saving): reporting only; investment does not depend on saving yet.
A new check: gold covers 40% of notes and reserves and 50% of the partner balances.
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl
from openpyxl.utils import get_column_letter as col

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cr041_russian_war as base  # noqa: E402

AUTHOR = "CR-057, 5 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST = 1846, 1932
ROW0 = 6
YEARS = range(FIRST, LAST + 1)


def row(y: int) -> int:
    return ROW0 + y - FIRST


def interp(points: dict[int, float], before: float = 0.0) -> dict[int, float]:
    ks = sorted(points)
    out = {}
    for y in YEARS:
        if y < ks[0]:
            out[y] = before
        elif y >= ks[-1]:
            out[y] = points[ks[-1]]
        else:
            lo = max(k for k in ks if k <= y)
            hi = min(k for k in ks if k > y)
            out[y] = points[lo] + (points[hi] - points[lo]) * (y - lo) / (hi - lo)
    return out


# ------------------------------------------------------------------ levers
LEVERS = [
    "— CR-057: the economic order tightened (5 Nov 2026) —",
    ("c57_on", "CR-057 master switch (1 = the money block, the Patrimony, the Crown share and the tax rule on; 0 = the CR-051/054/055 workbook)",
     1, 1, "switch", "PROPOSED (CR-057; author, 5 Nov 2026: update the models and report back)",
     "At 0 every CR-057 formula reduces to the one it replaced: the workbook reproduces cba70b31 exactly in both cases (identity check, "
     "finance/CR-057-workbook.md)."),
    ("price_from", "First year of the derived price level (money block)", 1914, 1914, "year", "PROPOSED (CR-057 H1)",
     "Before it the price level stays Paths!B, so 1913 = 1.00 and real GDP keeps its 1913-dollar base."),
    ("c_work", "Reserve Bank's working gold cover on notes and bank reserves, net of the gold behind partner balances", 0.5, 0.5, "share",
     "PROPOSED (CR-057 B, H1), MODEL",
     "Above the 40% floor (gold_cover). M(y) = (gold at end of y-1 - p_cover x partner balances(y-1)) / c_work. The Bank watches its cover "
     "and its own notes and deposits, never an index of prices (G1)."),
    ("c_glide", "Working cover glide from the 1913 cover (share a year)", 0.025, 0.025, "share a year", "Model estimate (CR-057 H1, interpretation)",
     "The working cover starts at the cover the Bank actually holds at the end of 1913 (net of the partners' 50%) and falls by this much a year until it reaches c_work, "
     "so that the switch to the money rule in 1914 does not print a third more money in one year. 0 = c_work from 1914."),
    ("c_ster", "Working cover in the sterilization years (MR-02)", 0.55, 0.55, "share", "PROPOSED (CR-057 MR-02), MODEL",
     "1927-28: the Bank holds back its own notes and deposits as the gold arrives (G6)."),
    ("ster_from", "Sterilization: first year", 1927, 1927, "year", "PROPOSED (CR-057 MR-02)", ""),
    ("ster_to", "Sterilization: last year", 1928, 1928, "year", "PROPOSED (CR-057 MR-02)", ""),
    ("k_slump", "Money demand in 1930-32 (× money_ratio)", 1.0, 1.10, "×", "Model estimate (CR-057 H1)",
     "Money demand may rise in the slump; 1.05-1.10 tested as a sensitivity (finance/CR-057-workbook.md). Stress takes 1.10 (deeper deflation)."),
    ("p_cover", "Gold cover on partners' official dollar balances", 0.5, 0.5, "share", "APPROVED ratio (CR-057 B, 16:21)",
     "Foreign official money is what runs (Britain, September 1931); the rest in prime commercial bills under 90 days."),
    ("pb_scale", "Partner balances (× the paths on Money)", 1.0, 1.25, "×", "Model estimate (CR-057 H1)", "Stress: larger balances, so less room."),
    ("pb_run", "Run on the partner balances in 1931: share withdrawn in gold", 0.0, 0.3, "share", "Model estimate (CR-057 H1: a Stress run in September 1931)",
     "Withdrawn balances leave in gold (Gold & money E) and the balances fall. Story 0."),
    ("r_real", "Real rate savers lend for on new Treasury bonds", 0.03, 0.035, "share", "Model estimate (CR-057 MR-01)",
     "New-issue coupon after price_from = MAX(cpn_floor, r_real + the trailing five-year price change): low, variable rates set by what savers lend for."),
    ("cpn_floor", "Floor on the new-issue coupon", 0.02, 0.02, "share", "Model estimate (CR-057 MR-01)", ""),
    ("pat_start", "The Patrimony's charter (first year it takes rents)", 1880, 1880, "year", "APPROVED (CR-057 A2: Elias writes it in 1880)", ""),
    ("pat_canal", "The canal's income to the Patrimony from", 1900, 1900, "year", "PROPOSED (CR-057 C)", "The canal opens in 1900."),
    ("levy_from", "Half the guest-worker levy to the Patrimony from", 1890, 1890, "year", "PROPOSED (CR-057 C, author's default)", ""),
    ("levy_pat", "Share of the guest-worker levy to the Patrimony", 0.5, 0.5, "share", "PROPOSED (CR-057 C, author's default)",
     "The rent of the quota. Variant 0.75 (rent-base widening)."),
    ("land_from", "Public domain leased, not sold, from", 1900, 1900, "year", "PROPOSED (CR-057 C)", ""),
    ("land_rent", "Leased public land: rents / core GDP", 0.005, 0.004, "share", "PROPOSED placeholder (CR-057 C), MODEL",
     "Town lots, industrial sites, forests, grazing, water-power sites and the land beside new works. A cautious placeholder; not yet derived "
     "from acres and values. Variant 0.01 (rent-base widening). Stress 0.004."),
    ("works_ret_from", "The Works keep their own returns for the halls: from", 1917, 1917, "year", "APPROVED (CR-051 §30: the state's dividend left in the Works)", ""),
    ("works_ret_to", "… to", 1927, 1927, "year", "APPROVED (CR-051)", ""),
    ("pat_real", "The Patrimony's real return", 0.045, 0.035, "share", "PROPOSED (CR-057 C), MODEL",
     "Nominal return = MAX(pat_floor, pat_real + the trailing five-year price change)."),
    ("pat_floor", "Floor on the Patrimony's nominal return", 0.02, 0.02, "share", "Model estimate", ""),
    ("pat_abroad_from", "The Patrimony invests abroad from", 1919, 1919, "year", "PROPOSED (CR-057 A2)", "After the Treaty of The Hague."),
    ("pat_abroad0", "… share abroad in the first year", 0.1, 0.1, "share", "PROPOSED (CR-057 A2)", ""),
    ("pat_abroad_max", "… share abroad from pat_abroad_full", 0.5, 0.5, "share", "PROPOSED (CR-057 A2)", ""),
    ("pat_abroad_full", "… year the share abroad reaches its maximum", 1929, 1929, "year", "PROPOSED (CR-057 A2)", ""),
    ("pat_loss", "Loss on the abroad share in 1931-32 (defaults and market value; half each year)", 0.15, 0.25, "share", "Model estimate (CR-057 C)",
     "The German and Latin American defaults of §34, written off in public."),
    ("pat_spend_from", "The Patrimony's spending rule starts", 1910, 1910, "year", "PROPOSED (CR-057 C, author's default: later)", ""),
    ("pat_spend", "Spending rule: share of last year's value paid into the Budget", 0.03, 0.03, "share", "PROPOSED (CR-057 C, author's default: lower)",
     "Earmarked for infrastructure, the Polytechnic and the research institutes: added to receipts and to spending alike (Budget AD, AE)."),
    ("s_tgt", "Target surplus / receipts (tax-cut rule)", 0.02, 0.02, "share", "Model estimate (CR-057 C)",
     "Measured on cash before financing (the budget balance after lending abroad and scheduled debt repayment). Surpluses go to the Reserve "
     "Fund buffer and then to lower taxes."),
    ("cut_speed", "Tax-cut rule: share of last year's gap closed", 0.5, 0.5, "share", "Model estimate (CR-057 C)", "Lagged one year: no circular reference."),
    ("cut_res", "Tax-cut rule: share of the Reserve Fund above its buffer rebated a year", 0.25, 0.25, "share", "Model estimate (CR-057 C)",
     "With the reserve above the buffer no longer invested by the Fund, the excess goes back as lower taxes."),
    ("cut_max", "Tax-cut rule: most of domestic taxes cut", 0.6, 0.6, "share", "Model estimate", ""),
    ("save_cut", "Share of each tax cut saved and invested privately", 0.6, 0.4, "share", "Model estimate (CR-057 C, F)",
     "The money left in private hands. F (the Previsión) raises saving."),
    ("priv_ret", "Lasting rise in output per $1 of private investment from tax cuts", 0.12, 0.06, "share", "Model estimate (CR-056: dev_return 0.30 less the premium 0.18)",
     "The ordinary return; the Patrimony's works keep dev_return."),
    ("crown_row", "Chartered Crown dividends kept: the trunk rights of way and cable landings", 0.2, 0.15, "share", "PROPOSED (CR-057 E, H6), MODEL",
     "The workbook has no railway line, so the rights of way cannot be isolated: this fraction of the chartered industries' Crown dividends stands "
     "for the canal-free equity the state keeps in the trunk rights of way and cable landings; oil, shipping and the concessions abroad are auctioned."),
    ("roy_floor", "Royalty floor on auctioned oil leases (from 1876)", 0.125, 0.125, "share", "PROPOSED (CR-057 E; Mineral Leasing Act 1920 standard, to verify)",
     "Applied only where the current rate is lower; the oil royalty is already one eighth, so it does not bind."),
    ("roy_floor_met", "Royalty floor on mineral leases (from 1876; 0 = the 1849 Mining Law's 5% stands)", 0.0, 0.0, "share", "Variant (CR-057 C widening)",
     "Raising the metal royalty to one eighth would amend the canon 5% of the Mining Law of 1849; a variant only."),
    ("prev_from", "The Previsión opens", 1919, 1919, "year", "PROPOSED (CR-057 F, A2)", "With the peacetime income tax."),
    ("prev_part", "Share of the labour force contributing to the Previsión", 0.25, 0.35, "share", "Model estimate (CR-057 F)", "Stress: a larger deduction cost."),
    ("prev_se", "Share of contributors self-employed (cap $1,500; others $300)", 0.2, 0.2, "share", "Model estimate (CR-057 F)", ""),
    ("prev_mtr", "Marginal income-tax rate on the deduction", 0.05, 0.06, "share", "Model estimate (CR-057 F)", "Reporting only: not deducted from receipts."),
]
# existing levers forced to zero while c57_on = 1
FORCED = ("rb_est", "cb_buy", "dev_share", "dev_bonds", "crown_comp")

# partner official dollar balances in San Francisco, $m (MODEL)
PB_JAPAN = interp({1886: 0, 1890: 10, 1905: 100, 1913: 150, 1919: 500, 1927: 150, 1929: 200, 1932: 150})
PB_PHIL = interp({1886: 10, 1913: 40, 1929: 80, 1932: 80})
PB_OTHER = interp({1899: 0, 1900: 5, 1929: 100, 1932: 100})


# ------------------------------------------------------------------ sheet helper
class Sheet:
    def __init__(self, wb, name: str, after: str, title: str, purpose: str):
        B, P = wb["Budget"], wb["Paths"]
        self.ws = wb.create_sheet(name, index=wb.sheetnames.index(after) + 1)
        self.ws["A1"].value = title
        self.ws["A2"].value = purpose
        self.ws["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. "
                               "Built by finance/build/cr057_economic_order.py; all amounts MODEL.")
        for c, src in (("A1", B["A1"]), ("A2", B["A2"]), ("A3", B["A3"])):
            self.ws[c]._style = copy.copy(src._style)
        self.grp, self.head = B["B4"]._style, B["B5"]._style
        self.year, self.f, self.inp = B["A6"]._style, B["B6"]._style, P["B6"]._style
        self.ws.cell(5, 1).value = "Year"
        self.ws.cell(5, 1)._style = copy.copy(B["A5"]._style)
        for y in YEARS:
            self.ws.cell(row(y), 1).value = y
            self.ws.cell(row(y), 1)._style = copy.copy(self.year)
        self.ws.column_dimensions["A"].width = 8
        self.ws.freeze_panes = "B6"
        self.n = 1
        self.cols: dict[str, str] = {}

    def reserve(self, keys: list[str]) -> None:
        """Fix the letters of columns that later columns refer to before they are written."""
        for i, k in enumerate(keys):
            self.cols.setdefault(k, col(self.n + 1 + i))

    def add(self, key: str, header: str, fn, *, group: str | None = None, note: str = "", is_input: bool = False,
            fmt: str | None = None) -> str:
        self.n += 1
        L_ = col(self.n)
        if key in self.cols:
            assert self.cols[key] == L_, (key, self.cols[key], L_)
        self.cols[key] = L_
        c = self.ws.cell(4, self.n)
        if group:
            c.value = group
        c._style = copy.copy(self.grp)
        h = self.ws.cell(5, self.n)
        h.value = header
        h._style = copy.copy(self.head)
        if note:
            base.note(h, note, 130)
        self.ws.column_dimensions[L_].width = 13
        for y in YEARS:
            v = fn(y, row(y))
            cell = self.ws.cell(row(y), self.n)
            cell.value = v
            cell._style = copy.copy(self.inp if is_input else self.f)
            if fmt:
                cell.number_format = fmt
        return L_

    def __getitem__(self, key: str) -> str:
        return self.cols[key]


def prev(L_: str, r: int, y: int, first: str = "0") -> str:
    return first if y == FIRST else f"{L_}{r - 1}"


# ------------------------------------------------------------------ the Money sheet (H1)
def build_money(wb) -> Sheet:
    M = Sheet(wb, "Money", "Gold & money", "The money block (CR-057 B, H1): partner balances, the money stock and the derived price level ($m)",
              "From price_from the Reserve Bank keeps a working gold cover on its own notes and bank reserves, net of the gold behind partners' "
              "official dollar balances; the money stock follows last year's gold and the price level follows the money stock over the real "
              "output it has to carry. Every input is prior-year or non-price: no circular reference. Feeds Economy!H, Gold & money!I, Budget X.")
    # columns referred to before they are written
    M.reserve(["on", "gold", "gold_av", "pb_jp", "pb_ph", "pb_ot", "pb", "pb_run", "pb_gold", "earmark",
               "c_use", "k_use", "other", "m_free", "m_floor", "m", "binds", "est_real", "p", "dci",
               "liab", "cov_old", "cov_all", "cov_net"])
    g = "Switch and gold"
    M.add("on", "Money rule in force (1 = yes)", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=price_from),1,0)", group=g, fmt="0")
    M.add("gold", "Pacifica's monetary gold, end of year", lambda y, r: f"='Gold & money'!F{r}", note="Gold & money F. Partners' earmarked gold is not in it.")
    G = wb["Gold & money"]

    def gold_av(y, r):
        e = G[f"E{r}"].value
        assert e.startswith("=SUMPRODUCT("), e
        e = e[1:].replace("+'Japan rescue'!D126", "")
        return f"='Gold & money'!B{r}+'Gold & money'!C{r}-({e})-{M['pb_run']}{r}"
    M.add("gold_av", "Gold before the year's external-surplus inflow", gold_av,
          note="Last year's gold plus new gold kept, less gold paid out in the Events (purchases, rescues) and in a run on the balances. Two "
               "flows that depend on this year's GDP are left out, so that the money rule is not circular: the external surplus (Gold & money D; "
               "leaving it out is conservative) and the gold the 1927 Japan rescue pays out (Japan rescue D126, sized on 1927's investment "
               "abroad): the floor test misses it in 1927, the cover check (AO) does not.")
    g = "Partners' official dollar balances in San Francisco (fractional, 50% gold)"
    M.add("pb_jp", "Japan (path)", lambda y, r: round(PB_JAPAN[y], 2), group=g, is_input=True,
          note="MODEL: about $10m 1890, $100m 1905, $150m 1913, $500m 1919 from wartime earnings, back to about $150m by 1927 as they are spent "
               "(CR-025 A12), $200m 1929, $150m 1932. Japan's currency rests on Pacifican deposits (CR-021 H). The 1927 rescue's callable "
               "balances stay in Gold & money I as before (they may overlap this path; not netted).")
    M.add("pb_ph", "Philippine peso reserve (path)", lambda y, r: round(PB_PHIL[y], 2), is_input=True,
          note="MODEL: held in San Francisco from 1886 (CR-029): about $10m rising to $40m 1913 and $80m 1929.")
    M.add("pb_ot", "Korea, the Gulf, China's reserve banks (path)", lambda y, r: round(PB_OTHER[y], 2), is_input=True,
          note="MODEL: from 1900, to about $100m in 1929, under bilateral compacts.")
    M.add("pb", "Partner balances", lambda y, r: (f"=IF(c57_on=1,({M['pb_jp']}{r}+{M['pb_ph']}{r}+{M['pb_ot']}{r})*pb_scale"
                                                  f"*IF($A{r}>=1931,1-pb_run,1),0)"),
          note="× pb_scale; a run in 1931 (pb_run) withdraws a share in gold and the balances stay lower. Zero when c57_on = 0.")
    M.add("pb_run", "Withdrawn in gold in the run of 1931", lambda y, r: (f"=IF(AND(c57_on=1,$A{r}=1931),({M['pb_jp']}{r}+{M['pb_ph']}{r}+"
                                                                          f"{M['pb_ot']}{r})*pb_scale*pb_run,0)"),
          note="Added to gold paid out (Gold & money E).")
    M.add("pb_gold", "Gold behind the partner balances", lambda y, r: f"={M['pb']}{r}*p_cover")
    M.add("earmark", "Partners' earmarked gold (memo, not Pacifica's)", lambda y, r: None, is_input=True,
          note="100% earmarked, withdrawable without notice (CR-057 B). Amount OPEN: not set in this build; it is never Pacifica's gold and never cover.")
    g = "Money stock"
    r13 = row(1913)
    M.add("c_use", "Working cover in use", lambda y, r: (f"=MAX(c_work,${M['cov_net']}${r13}-c_glide*($A{r}-1913),"
                                                         f"IF(AND($A{r}>=ster_from,$A{r}<=ster_to),c_ster,0))"),
          group=g, fmt="0.000",
          note="c_work, gliding down from the cover actually held at the end of 1913 (net of the partners' 50%) by c_glide a year (interpretation: no one-year jump in money in 1914); c_ster in the sterilization years.")
    M.add("k_use", "Notes and reserves / real-output demand", lambda y, r: f"=money_ratio*IF(AND($A{r}>=1930,$A{r}<=1932),k_slump,1)", fmt="0.0000")
    M.add("other", "Other Reserve Bank liabilities (Japan rescue, purchases)",
          lambda y, r: f"='Gold & money'!H{r}+IF(c57_on=1,0,'Energy link'!BE{r})" + ("+'Japan rescue'!$D$131" if y >= 1928 else ""),
          note="As in Gold & money I: the 1927 rescue's callable balances, the Treasury bonds and estate bonds the Bank holds (zero under CR-057). "
               "The rescue item enters the floor from 1928: it is set by 1927's GDP (Japan rescue D21 reads Abroad C), so reading it in 1927 "
               "would be circular. The cover check (AO) counts it in 1927 too. The estate bonds (Energy link BE) are zero under CR-057 (rb_est 0) and are "
               "not read while c57_on = 1: their formula runs through the Fund's lending base, which depends on this year's GDP.")
    M.add("m_free", "Money stock at the working cover", lambda y, r: (
        "=0" if y == FIRST else f"=MAX(0,{M['gold']}{r - 1}-{M['pb_gold']}{r - 1})/{M['c_use']}{r}"),
        note="(gold at end of last year - p_cover × last year's partner balances) / the working cover.")
    M.add("m_floor", "Most money the 40% floor allows (guard 3)", lambda y, r: (
        f"=MAX(0,{M['gold_av']}{r}-{M['pb_gold']}{r})/gold_cover-{M['other']}{r}"),
        note="Gold before the year's surplus inflow, less the partners' cover, over 40%, less the other liabilities: the automatic tightening contracts M to this.")
    M.add("m", "Money stock: notes and bank reserves (M)", lambda y, r: f"=IF({M['on']}{r}=1,MAX(0,MIN({M['m_free']}{r},{M['m_floor']}{r})),Economy!O{r}*money_ratio)",
          note="Before price_from (or with c57_on = 0) the old rule, GDP × money_ratio.")
    M.add("binds", "Floor binds (1 = yes)", lambda y, r: f"=IF(AND({M['on']}{r}=1,{M['m_floor']}{r}<{M['m_free']}{r}),1,0)", fmt="0")
    M.add("est_real", "Estimated real core GDP (1913 $m)", lambda y, r: (
        "=Economy!S6" if y == FIRST else
        f"=Economy!S{r - 1}*Economy!B{r}/Economy!B{r - 1}*(1+Economy!E{r})*Economy!G{r}/Economy!G{r - 1}"),
        note="Last year's real GDP × residents' growth × (1 + real growth per resident) × the output gap's change. No current-year price in it.")
    M.add("p", "Derived price level (1913 = 1)", lambda y, r: f"={M['m']}{r}/({M['k_use']}{r}*{M['est_real']}{r})", fmt="0.000",
          note="M / (money_ratio × k_slump × estimated real GDP). Economy!H takes it from price_from when c57_on = 1.")
    M.add("dci", "Price level for domestic costs in 1913 dollars", lambda y, r: f"=IF({M['on']}{r}=1,Economy!H{r},Paths!B{r})", fmt="0.000",
          note="Atomic R and the Works' deflators. Paths!B when the rule is off. Siberia's price column and the Russian-war events stay on Paths!B: "
               "they feed Gold & money E's sum over the Events column, which the money rule reads, so tying them to the derived level would be circular.")
    g = "Cover (CR-057 B)"
    M.add("liab", "Notes and bank reserves, all (Gold & money I)", lambda y, r: f"='Gold & money'!I{r}", group=g)
    M.add("cov_old", "Gold cover, old basis (gold / notes and reserves)", lambda y, r: f"='Gold & money'!L{r}", fmt="0.000")
    M.add("cov_all", "Gold / (notes and reserves + partner balances)", lambda y, r: f"=IF({M['liab']}{r}+{M['pb']}{r}>0,{M['gold']}{r}/({M['liab']}{r}+{M['pb']}{r}),0)", fmt="0.000")
    M.add("cov_net", "Cover on notes and reserves, net of the partners' 50%", lambda y, r: f"=IF({M['liab']}{r}>0,({M['gold']}{r}-{M['pb_gold']}{r})/{M['liab']}{r},0)", fmt="0.000")
    M.add("req", "Gold required: 40% of notes and reserves + 50% of partner balances", lambda y, r: f"=gold_cover*{M['liab']}{r}+{M['pb_gold']}{r}")
    M.add("room", "Gold above all floors (room for Bagehot lending)", lambda y, r: f"={M['gold']}{r}-{M['req']}{r}",
          note="CR-057 B: the room the lender of last resort has, after the Union rescue and gold credit already paid out.")
    M.add("chk", "Cover met on all liabilities (CR-057)", lambda y, r: f'=IF(c57_on=1,IF($A{r}<1900,"n/a",IF({M["room"]}{r}>=-0.001,"OK","Check")),"n/a")')
    g = "Coupons (MR-01)"
    M.add("infl5", "Trailing five-year price change a year", lambda y, r: (
        "=0" if y < FIRST + 6 else f"=(Economy!H{r - 1}/Economy!H{r - 6})^(1/5)-1"), group=g, fmt="0.0%",
        note="To last year: no circular reference.")
    M.add("cpn_new", "Coupon on new Treasury bonds", lambda y, r: f"=MAX(cpn_floor,r_real+{M['infl5']}{r})", fmt="0.00%")
    M.add("cpn_stock", "Coupon on the stock of public debt at year end", lambda y, r: (
        f"=Paths!Y{r}" if y == FIRST else
        f"=IF(OR(c57_on<>1,$A{r}<=price_from),Paths!Y{r},IF('Debt & cash'!R{r}>0,("
        f"{M['cpn_stock']}{r - 1}*MAX(0,'Debt & cash'!R{r - 1}-'Debt & cash'!C{r}-'Debt & cash'!K{r})+{M['cpn_new']}{r}*('Debt & cash'!H{r}+"
        f"'Debt & cash'!Q{r}+'Debt & cash'!P{r}))/'Debt & cash'!R{r},{M['cpn_new']}{r}))"), fmt="0.00%",
        note="Last year's stock at its coupon less what is repaid, plus this year's issues at the new coupon. Budget X reads last year's value "
             "from the year after price_from; before that Paths!Y.")
    g = "Against the old path"
    M.add("p_old", "Price level before CR-057 (Paths!B; slump_price in 1930-32)", lambda y, r: (
        f"=IF($A{r}>=1930,Paths!B$89+(Paths!B{r}-Paths!B$89)*slump_price,Paths!B{r})"), group=g, fmt="0.000")
    M.add("p_ratio", "Derived / old", lambda y, r: f"=IF({M['p_old']}{r}>0,Economy!H{r}/{M['p_old']}{r},1)", fmt="0.000")
    M.add("real_chk", "Real GDP / its estimate", lambda y, r: f"=IF({M['est_real']}{r}>0,Economy!S{r}/{M['est_real']}{r},1)", fmt="0.000",
          note="How close the money rule's estimate came: it leaves out the talent term (Economy I) and this year's mining, champions and Gulf output.")
    return M


def link_money(wb, M: Sheet) -> None:
    E, G, B, A, W, Sib, Ev = (wb[s] for s in ("Economy", "Gold & money", "Budget", "Atomic", "Works", "Siberia", "Events"))
    Lb, Pt = wb["Labour"], wb["Partners"]
    for y in YEARS:
        r = row(y)
        # Economy H: the derived level
        h = E[f"H{r}"].value
        assert h == f"=IF($A{r}>=1930,Paths!B$89+(Paths!B{r}-Paths!B$89)*slump_price,Paths!B{r})", h
        E[f"H{r}"].value = f"=IF(Money!{M['on']}{r}=1,Money!{M['p']}{r},IF($A{r}>=1930,Paths!B$89+(Paths!B{r}-Paths!B$89)*slump_price,Paths!B{r}))"
        # Gold & money I: the money stock
        i = G[f"I{r}"].value
        assert i.startswith(f"=Economy!O{r}*money_ratio+H{r}"), i
        G[f"I{r}"].value = i.replace(f"=Economy!O{r}*money_ratio", f"=IF(Money!{M['on']}{r}=1,Money!{M['m']}{r},Economy!O{r}*money_ratio)", 1)
        # Gold & money E: the run on the balances leaves in gold
        e = G[f"E{r}"].value
        assert e.startswith("=SUMPRODUCT("), e
        G[f"E{r}"].value = e + f"+Money!{M['pb_run']}{r}"
        # Budget X: the coupon on the stock (last year's) after price_from
        if y > FIRST:
            x = B[f"X{r}"].value
            assert x == f"='Debt & cash'!R{r - 1}*Paths!Y{r}", x
            B[f"X{r}"].value = f"='Debt & cash'!R{r - 1}*IF(AND(c57_on=1,$A{r}>price_from),Money!{M['cpn_stock']}{r - 1},Paths!Y{r})"
        # domestic costs in 1913 dollars follow the derived level
        ar = A[f"R{r}"].value
        assert ar == f"=Paths!B{r}", ar
        A[f"R{r}"].value = f"=Money!{M['dci']}{r}"
        for c in ("W", "AI"):
            v = W[f"{c}{r}"].value
            assert f"/Paths!B{r}" in v, v
            W[f"{c}{r}"].value = v.replace(f"/Paths!B{r}", f"/Money!{M['dci']}{r}")
        # the pulls read Pacifica's lead at US prices
        if y > FIRST:
            t = Lb[f"T{r}"].value
            assert t == f"=Economy!R{r - 1}", t
            Lb[f"T{r}"].value = f"=IF(c57_on=1,Economy!T{r - 1},Economy!R{r - 1})"
            b = Pt[f"B{r}"].value
            assert b == f"=Economy!P{r - 1}", b
            Pt[f"B{r}"].value = f"=IF(c57_on=1,Economy!V{r - 1},Economy!P{r - 1})"
        # real GDP: the domestic part at Pacifica's price level, the world-priced part at the world's
        sv = E[f"S{r}"].value
        assert sv == f"=O{r}/H{r}", sv
        E[f"S{r}"].value = f"=IF(c57_on=1,(J{r}+L{r})/H{r}+(K{r}+M{r}+N{r})/Paths!B{r},O{r}/H{r})"
    base.note(E["H5"], (E["H5"].comment.text + "\n\n" if E["H5"].comment else "") +
              "CR-057 H1: from price_from (1914) with c57_on = 1, the level derived on the Money sheet from the money stock; the slump_price "
              "mechanism goes with it.", 120)
    base.note(G["I5"], G["I5"].comment.text + "\n\nCR-057 H1: from price_from with c57_on = 1, the money stock M of the Money sheet in place of "
              "GDP × money_ratio; the Japan-rescue item stays; the Bank holds no Treasury or estate bonds (cb_buy, rb_est 0).", 120)
    base.note(B["X5"], (B["X5"].comment.text + "\n\n" if B["X5"].comment else "") +
              "CR-057 MR-01: after price_from, last year's coupon on the stock (Money), which blends in new issues at r_real plus the trailing "
              "price change, floored at 2%.", 120)
    base.note(A["R5"], (A["R5"].comment.text + "\n\n" if A["R5"].comment else "") +
              "CR-057: the domestic cost level (Money), the derived price level from 1914 when c57_on = 1.", 120)
    base.note(Lb["T5"], (Lb["T5"].comment.text + "\n\n" if Lb["T5"].comment else "") +
              "CR-057: at US prices (Economy T) when c57_on = 1, so the money rule's lower price level does not read as a smaller lead.", 120)
    base.note(Pt["B5"], (Pt["B5"].comment.text + "\n\n" if Pt["B5"].comment else "") +
              "CR-057: at US prices (Economy V) when c57_on = 1.", 120)
    base.note(E["S5"], (E["S5"].comment.text + "\n\n" if E["S5"].comment else "") +
              "CR-057 (c57_on = 1): non-mining output and the guest workers' at Pacifica's price level (H); mining and oil, the champions and "
              "the Gulf, which sell at world prices, at the world's (Paths!B). With one deflator a lower Pacifican price level would raise "
              "the real value of world-priced output. Identical to O/H before 1914.", 140)
    # Economy T, U, V: reporting and the pulls
    ref = E["S5"]
    persons = lambda r: f"(B{r}+People!V{r}+Labour!L{r})"  # noqa: E731
    for L_, head, f, txt, fmt in (
            ("T", "Pacifica / US per person, at US prices", lambda r: f"=IF(Q{r}>0,V{r}/Q{r},0)",
             "CR-057: GDP per person at US prices (V) over the US's. Equal to R before 1914. The migration pull (Labour T) reads it when c57_on = 1.", "0.00"),
            ("U", "Real GDP, all deflated by H (1913 $m, memo)", lambda r: f"=O{r}/H{r}",
             "The single-deflator measure (Economy S before CR-057).", None),
            ("V", "GDP per person present, at US prices ($)", lambda r: f"=((J{r}+L{r})*Paths!B{r}/H{r}+K{r}+M{r}+N{r})*1000000/{persons(r)}",
             "CR-057: the domestic part converted at the US price level over Pacifica's; world-priced output as it is. The partners' pull "
             "(Partners B) reads it when c57_on = 1.", "#,##0")):
        E[f"{L_}5"].value = head
        E[f"{L_}5"]._style = copy.copy(ref._style)
        E[f"{L_}4"]._style = copy.copy(E["S4"]._style)
        base.note(E[f"{L_}5"], txt, 110)
        E.column_dimensions[L_].width = 13
        for y in YEARS:
            rr = row(y)
            E[f"{L_}{rr}"].value = f(rr)
            E[f"{L_}{rr}"]._style = copy.copy(E[f"S{rr}"]._style)
            E[f"{L_}{rr}"].number_format = fmt or E[f"S{rr}"].number_format


# ------------------------------------------------------------------ the Patrimony (H3)
def build_patrimony(wb) -> Sheet:
    P = Sheet(wb, "Patrimony", "Debt & cash", "The Patrimony (CR-057 C, H3): the state's rents as a sovereign wealth fund ($m)",
              "Rents, not taxes: royalties, the canal, the state's estates, half the guest-worker levy and leased public land leave the Budget "
              "for the Patrimony; it earns a real return, goes abroad from 1919, spends nothing before 1910 and then pays 3% of its value "
              "into the Budget for earmarked works. With the old Development Fund financing off, surpluses go to the Reserve Fund buffer and "
              "then to lower taxes (the tax-cut rule here). The output effect is on Economy D.")
    P.reserve(["on", "roy", "canal", "est", "levy", "land", "inflow", "infl5", "ret", "abroad", "income", "loss", "spend", "value"])
    g = "Inflows (CR-057 C)"
    P.add("on", "The charter in force (1 = yes)", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=pat_start),1,0)", group=g, fmt="0")
    P.add("roy", "Mineral and oil royalties", lambda y, r: f"={P['on']}{r}*(Resources!P{r}+Resources!Q{r})",
          note="Budget D (after the school of mines' share), from 1880.")
    P.add("canal", "Canal net income", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=pat_canal),Paths!S{r}*(1-canal_opcost)*canal_share,0)",
          note="Budget E, from 1900. Counted once: the Crown share holds no canal (Champions' canals abroad are concessions abroad).")
    P.add("est", "The state's estates", lambda y, r: (f"={P['on']}{r}*(Economy!O{r}*Paths!R{r}+IF(AND($A{r}>=works_ret_from,$A{r}<=works_ret_to),0,Atomic!Y{r}))"),
          note="Budget F: state enterprises and concessions (Paths R × GDP) and the Works' direct returns (Atomic Y). In 1917-27 the Works keep "
               "their own returns for the halls (§30, CR-051): that part stays in Budget F, against the halls' cost in Technical programmes. "
               "The Hawaiian hydro board's profits are the Hawaiian crown's and are not in the workbook.")
    P.add("levy", "Half the guest-worker levy", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=levy_from),Labour!Q{r}*levy_pat,0)",
          note="Budget J × levy_pat, from 1890: the rent of the quota. The other half pays for inspection, clinics, schools and a hardship reserve (A2).")
    P.add("land", "Leased public land", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=land_from),land_rent*Economy!O{r},0)",
          note="New receipts from 1900: land_rent × core GDP (placeholder 0.5%). Farmland still goes to settlers on CR-033's instalments (Land Fund).")
    P.add("inflow", "Inflows, total", lambda y, r: f"={P['roy']}{r}+{P['canal']}{r}+{P['est']}{r}+{P['levy']}{r}+{P['land']}{r}")
    g = "Returns and value"
    P.add("infl5", "Trailing five-year price change a year", lambda y, r: ("=0" if y < FIRST + 6 else f"=(Economy!H{r - 1}/Economy!H{r - 6})^(1/5)-1"),
          group=g, fmt="0.0%")
    P.add("ret", "Nominal return", lambda y, r: f"=MAX(pat_floor,pat_real+{P['infl5']}{r})", fmt="0.0%")
    P.add("abroad", "Share invested abroad", lambda y, r: (f"=IF($A{r}<pat_abroad_from,0,MIN(pat_abroad_max,pat_abroad0+(pat_abroad_max-pat_abroad0)"
                                                           f"*($A{r}-pat_abroad_from)/(pat_abroad_full-pat_abroad_from)))"), fmt="0%",
          note="At home to 1919 (railway, mortgage and champions' bonds, a minor share of state bonds); abroad from 1919, never in a defaulting "
               "or negotiating government, no war debts.")
    P.add("income", "Return earned", lambda y, r: "=0" if y == FIRST else f"={P['value']}{r - 1}*{P['ret']}{r}")
    P.add("loss", "Written off in public: 1931-32 losses abroad", lambda y, r: (
        "=0" if y == FIRST else f"=IF(OR($A{r}=1931,$A{r}=1932),{P['value']}{r - 1}*{P['abroad']}{r - 1}*pat_loss/2,0)"))
    P.add("spend", "Paid into the Budget (spending rule)", lambda y, r: (
        "=0" if y == FIRST else f"=IF(AND(c57_on=1,$A{r}>=pat_spend_from),{P['value']}{r - 1}*pat_spend,0)"),
          note="3% of last year's value from 1910: Budget AD (receipt) and AE (earmarked works).")
    P.add("value", "The Patrimony's value, end of year", lambda y, r: (
        f"={P['inflow']}{r}" if y == FIRST else f"={P['value']}{r - 1}+{P['income']}{r}-{P['loss']}{r}-{P['spend']}{r}+{P['inflow']}{r}"))
    P.add("v_gdp", "… / core GDP", lambda y, r: f"=IF(Economy!O{r}>0,{P['value']}{r}/Economy!O{r},0)", fmt="0%")
    P.add("v_abroad", "… held abroad", lambda y, r: f"={P['value']}{r}*{P['abroad']}{r}")
    P.add("v_home", "… held at home", lambda y, r: f"={P['value']}{r}-{P['v_abroad']}{r}")
    P.add("home_inv", "Net new holdings at home (the lending arm's base)", lambda y, r: (
        f"=MAX(0,{P['v_home']}{r})" if y == FIRST else f"=MAX(0,{P['v_home']}{r}-{P['v_home']}{r - 1})"),
          note="The Development Fund, the Patrimony's lending arm at home: the base of its power credit (Debt & cash Z, Energy link AZ).")
    P.add("accum", "Net accumulation", lambda y, r: f"={P['value']}{r}" if y == FIRST else f"={P['value']}{r}-{P['value']}{r - 1}")
    g = "Infrastructure the spending rule pays for"
    P.add("infra", "Infrastructure stock (memo)", lambda y, r: (f"={P['spend']}{r}" if y == FIRST else
                                                                 f"={P['infra']}{r - 1}*(1-dev_dep)+{P['spend']}{r}"), group=g,
          note="Built from the earmarked works; dev_dep a year. A memo like the old Development stock: the output effect uses the yearly flow (Economy D).")
    g = "Tax cuts on domestic taxes (Budget C)"
    P.reserve(["c0", "extra", "gap", "tau", "cut", "share", "pinv", "pstock"])
    slump = lambda r: f"AND($A{r}>=1930,$A{r}<=1932)"  # noqa: E731
    P.add("c0", "Domestic taxes before the cut", lambda y, r: f"=(Economy!J{r}+Economy!L{r}+Economy!M{r}+Economy!N{r})*Paths!P{r}*Paths!Q{r}", group=g,
          note="Budget C's own formula.")
    P.add("extra", "Rebate of the Reserve Fund above its buffer", lambda y, r: (
        "=0" if y == FIRST else
        f"=IF(AND(c57_on=1,$A{r}>=pat_start),cut_res*MAX(0,'Debt & cash'!S{r - 1}-reserve_buffer*Economy!O{r - 1}),0)"),
          note="cut_res of last year's Reserve Fund above its buffer (reserve_buffer × GDP), returned as lower taxes: surpluses fill the buffer "
               "first, then lower taxes. Proportional, so it does not oscillate.")
    P.add("gap", "Last year's room for a cut", lambda y, r: (
        "=0" if y == FIRST else
        f"='Debt & cash'!D{r - 1}-'Debt & cash'!E{r - 1}+{P['extra']}{r - 1}-s_tgt*Budget!M{r - 1}"),
          note="Last year's cash before financing above the cash target (the budget balance after lending abroad and scheduled repayment), "
               "before the rebate, less the target surplus. Lagged: no circular reference.")
    P.add("tau", "Share of domestic taxes cut, from the surplus rule", lambda y, r: (
        "=0" if y == FIRST else
        f"=IF(AND(c57_on=1,$A{r}>=pat_start),MIN(cut_max,MAX(IF({slump(r)},{P['tau']}{r - 1},0),"
        f"{P['tau']}{r - 1}+cut_speed*{P['gap']}{r}/MAX(1,{P['c0']}{r - 1}))),0)"), fmt="0.0%",
          note="Last year's share plus cut_speed × the room over last year's domestic taxes, within 0 and cut_max; cannot fall in 1930-32.")
    P.add("cut", "Tax cut", lambda y, r: (
        f"=MIN(cut_max*{P['c0']}{r},{P['tau']}{r}*{P['c0']}{r}+{P['extra']}{r})" if y == FIRST else
        f"=MIN(cut_max*{P['c0']}{r},IF({slump(r)},MAX({P['tau']}{r}*{P['c0']}{r}+{P['extra']}{r},{P['share']}{r - 1}*{P['c0']}{r}),"
        f"{P['tau']}{r}*{P['c0']}{r}+{P['extra']}{r}))"),
          note="The surplus rule's share × domestic taxes, plus the rebate; in 1930-32 at least last year's share: Pacifica raises no taxes "
               "in the slump (§34); reserves and borrowing carry it.")
    P.add("share", "Share of domestic taxes cut, in all", lambda y, r: f"=IF({P['c0']}{r}>0,{P['cut']}{r}/{P['c0']}{r},0)", fmt="0.0%",
          note="Budget C = its own formula × (1 - this).")
    P.add("pinv", "Saved and invested privately", lambda y, r: f"={P['cut']}{r}*save_cut",
          note="The money left in private hands, at the ordinary return (priv_ret) on Economy D.")
    P.add("pstock", "Private stock from tax cuts (memo)", lambda y, r: (f"={P['pinv']}{r}" if y == FIRST else
                                                                         f"={P['pstock']}{r - 1}*(1-dev_dep)+{P['pinv']}{r}"))
    g = "Output effect (Economy D), decomposed"
    P.add("d_state", "From the state's development investment", lambda y, r: (
        "=0" if y == FIRST else f"=IF(Economy!O{r - 1}>0,dev_return*'Debt & cash'!N{r - 1}/Economy!O{r - 1},0)"), group=g, fmt="0.00%",
          note="dev_return × last year's development investment (Debt & cash N: under CR-057 only the Investment events) / last year's GDP.")
    P.add("d_works", "From the Patrimony's works", lambda y, r: (
        "=0" if y == FIRST else f"=IF(Economy!O{r - 1}>0,dev_return*{P['spend']}{r - 1}/Economy!O{r - 1},0)"), fmt="0.00%")
    P.add("d_priv", "From private investment out of tax cuts", lambda y, r: (
        "=0" if y == FIRST else f"=IF(Economy!O{r - 1}>0,priv_ret*{P['pinv']}{r - 1}/Economy!O{r - 1},0)"), fmt="0.00%")
    P.add("d_new", "Total, within dev_cap", lambda y, r: f"=MIN(dev_cap,{P['d_state']}{r}+{P['d_works']}{r}+{P['d_priv']}{r})", fmt="0.00%")
    return P


def link_patrimony(wb, P: Sheet) -> None:
    B, D, E, X, R = wb["Budget"], wb["Debt & cash"], wb["Economy"], wb["Energy link"], wb["Resources"]
    for y in YEARS:
        r = row(y)
        c = B[f"C{r}"].value
        assert c == f"=(Economy!J{r}+Economy!L{r}+Economy!M{r}+Economy!N{r})*Paths!P{r}*Paths!Q{r}", c
        B[f"C{r}"].value = c + f"*(1-Patrimony!{P['share']}{r})"
        for L_, key, old in (("D", "roy", f"=Resources!P{r}+Resources!Q{r}"),
                             ("E", "canal", f"=Paths!S{r}*(1-canal_opcost)*canal_share"),
                             ("F", "est", f"=Economy!O{r}*Paths!R{r}+Atomic!Y{r}"),
                             ("J", "levy", f"=Labour!Q{r}")):
            v = B[f"{L_}{r}"].value
            assert v == old, (L_, v)
            B[f"{L_}{r}"].value = f"{v}-Patrimony!{P[key]}{r}"
        m = B[f"M{r}"].value
        assert m == f"=SUM(B{r}:L{r})", m
        B[f"M{r}"].value = f"=SUM(B{r}:L{r})+AD{r}"
        yy = B[f"Y{r}"].value
        assert yy == f"=SUM(N{r}:X{r})", yy
        B[f"Y{r}"].value = f"=SUM(N{r}:X{r})+AE{r}"
        B[f"AD{r}"].value = f"=Patrimony!{P['spend']}{r}"
        B[f"AE{r}"].value = f"=Patrimony!{P['spend']}{r}"
        for L_ in ("AD", "AE"):
            B[f"{L_}{r}"]._style = copy.copy(B[f"X{r}"]._style)
        # Debt & cash: the old Fund's financing off
        j = D[f"J{r}"].value
        if y > FIRST:
            assert j.startswith(f"=IF($A{r}>=dev_start,"), j
            D[f"J{r}"].value = j.replace(f"=IF($A{r}>=dev_start,", f"=IF(AND($A{r}>=dev_start,c57_on<>1),", 1)
        D[f"Z{r}"].value = f"=IF(c57_on=1,Patrimony!{P['home_inv']}{r},I{r})"
        D[f"Z{r}"]._style = copy.copy(D[f"I{r}"]._style)
        # Economy D: the output effect
        if y > FIRST:
            d = E[f"D{r}"].value
            assert d == f"=IF(O{r - 1}>0,MIN(dev_cap,dev_return*'Debt & cash'!N{r - 1}/O{r - 1}),0)", d
            E[f"D{r}"].value = f"=IF(c57_on=1,Patrimony!{P['d_new']}{r},{d[1:]})"
        # Energy link: the Fund's lending base, the Patrimony's works as public investment
        for L_ in ("AZ", "AD"):
            v = X[f"{L_}{r}"].value
            assert f"'Debt & cash'!I{r}" in v, (L_, v)
            X[f"{L_}{r}"].value = v.replace(f"'Debt & cash'!I{r}", f"'Debt & cash'!Z{r}")
        au = X[f"AU{r}"].value
        assert au == f"=Budget!R{r}", au
        X[f"AU{r}"].value = f"=Budget!R{r}+Budget!AE{r}"
        # royalty floors on auctioned leases
        q = R[f"Q{r}"].value
        assert q == f"=M{r}*roy_oil", q
        R[f"Q{r}"].value = f"=M{r}*MAX(roy_oil,IF(AND(c57_on=1,$A{r}>=1876),roy_floor,0))"
        p = R[f"P{r}"].value
        assert p == f"=SUM(B{r}:F{r})*roy_metal*0.9", p
        R[f"P{r}"].value = f"=SUM(B{r}:F{r})*MAX(roy_metal,IF(AND(c57_on=1,$A{r}>=1876),roy_floor_met,0))*0.9"
    for L_, head, txt in (("AD", "Transfer from the Patrimony (CR-057)", "Patrimony: 3% of last year's value from 1910, a new receipt."),
                          ("AE", "Earmarked works paid by the Patrimony (CR-057)", "The same amount spent on infrastructure, the Polytechnic and the research "
                           "institutes: budget-neutral. Investment in the account (Energy link AU), not government consumption.")):
        B[f"{L_}5"].value = head
        B[f"{L_}5"]._style = copy.copy(B["X5"]._style)
        B[f"{L_}4"]._style = copy.copy(B["X4"]._style)
        base.note(B[f"{L_}5"], txt, 100)
        B.column_dimensions[L_].width = 13
    B["AD4"].value = "CR-057"
    for L_, txt in (("C", "CR-057: less the tax cut (Patrimony): surpluses go to the Reserve Fund buffer and then to lower taxes."),
                    ("D", "CR-057: less the royalties the Patrimony takes from 1880."),
                    ("E", "CR-057: less the canal's income, the Patrimony's from 1900."),
                    ("F", "CR-057: less the estates' profits the Patrimony takes from 1880 (the Works keep their own returns in 1917-27)."),
                    ("J", "CR-057: less the half of the levy the Patrimony takes from 1890."),
                    ("M", "CR-057: plus the Patrimony's transfer (AD)."), ("Y", "CR-057: plus the earmarked works (AE).")):
        base.note(B[f"{L_}5"], (B[f"{L_}5"].comment.text + "\n\n" if B[f"{L_}5"].comment else "") + txt, 120)
    # the income tax (H7, CT13 adapt): labels only
    assert B["L5"].value == "Tax on income from abroad", B["L5"].value
    B["L5"].value = "Duty on foreign dividends and coupons (to 1914); tax on income from abroad (from 1915)"
    base.note(B["L5"], (B["L5"].comment.text + "\n\n" if B["L5"].comment else "") +
              "CR-057 H7 (CT13 adapt): before 1915 this is a duty on foreign dividends and coupons collected at the paying agent, not an income tax. "
              "Memo: the Realm's first income tax is the War Revenue Act of 1915, once Pacifica is at war (from August 1914), kept at a lower "
              "rate at the peace in 1919 (the Previsión's deduction from 1919, Saving sheet). No numbers change: the workbook's domestic taxes "
              "(C) are one rate on non-mining output and do not separate an income tax.", 160)
    Lv = wb["Levers"]
    rr = int(wb.defined_names["abroad_tax"].attr_text.split("$")[-1])
    assert Lv.cell(rr, 2).value == "Tax on income from abroad", Lv.cell(rr, 2).value
    Lv.cell(rr, 2).value = "Duty on foreign dividends (to 1914), then tax on income from abroad"
    D["Z5"].value = "Development Fund lending base (CR-057)"
    D["Z5"]._style = copy.copy(D["Y5"]._style)
    D["Z4"]._style = copy.copy(D["Y4"]._style)
    base.note(D["Z5"], "CR-057: with c57_on = 1 the Patrimony's net new holdings at home (its lending arm, the Development Fund); otherwise I. "
              "The base of the Fund's power credit (Energy link AZ) and of the energy workbook's (energy/build/extract_finance.py).", 110)
    D.column_dimensions["Z"].width = 13
    base.note(D["J5"], (D["J5"].comment.text + "\n\n" if D["J5"].comment else "") + "CR-057: off while c57_on = 1 (the excess returns as lower taxes).", 110)
    base.note(E["D5"], (E["D5"].comment.text + "\n\n" if E["D5"].comment else "") +
              "CR-057 H3 (c57_on = 1): MIN(dev_cap, (dev_return × (the state's development investment + the Patrimony's earmarked works) + "
              "priv_ret × the private investment from tax cuts) / last year's GDP). Decomposed on the Patrimony sheet.", 130)


def link_crown(wb) -> None:
    C = wb["Champions"]
    for y in YEARS:
        r = row(y)
        bd = C[f"BD{r}"].value
        assert bd == f"=IF($A{r}>=crown_start,(BB{r}*crown_charter+BC{r}*crown_comp)*crown_payout,0)", bd
        C[f"BD{r}"].value = f"=IF($A{r}>=crown_start,(BB{r}*crown_charter*IF(c57_on=1,crown_row,1)+BC{r}*crown_comp)*crown_payout,0)"
        be = C[f"BE{r}"].value
        assert be == f"=IF(BB{r}+BC{r}>0,(BB{r}*crown_charter+BC{r}*crown_comp)/(BA{r}),0)", be
        C[f"BE{r}"].value = f"=IF(BB{r}+BC{r}>0,(BB{r}*crown_charter*IF(c57_on=1,crown_row,1)+BC{r}*crown_comp)/(BA{r}),0)"
    base.note(C["BD5"], (C["BD5"].comment.text + "\n\n" if C["BD5"].comment else "") +
              "CR-057 H6 (c57_on = 1): no stake in competitive industries (crown_comp 0); of the chartered stake only the trunk rights of way and "
              "cable landings (crown_row). The canal and the estates have their own Budget rows and are not here.", 130)


def force_levers(wb) -> None:
    L = wb["Levers"]
    for n in FORCED:
        rr = int(wb.defined_names[n].attr_text.split("$")[-1])
        v = L.cell(rr, 5).value
        assert v == f"=IF(case_sel=1,C{rr},D{rr})", (n, v)
        L.cell(rr, 5).value = f"=IF(c57_on=1,0,IF(case_sel=1,C{rr},D{rr}))"
        base.note(L.cell(rr, 5), "CR-057: 0 while c57_on = 1 (" + {
            "rb_est": "CT15: the power estate's 1930-32 bonds go to savers; the Bank only lends against them",
            "cb_buy": "MR-06: the standing debt is the Bank's collateral, not something it buys",
            "dev_share": "the Patrimony takes rents, not surpluses",
            "dev_bonds": "the standing debt's proceeds stay in the Reserve Fund",
            "crown_comp": "E: no state stake in competitive industries"}[n] + ").", 80)


# ------------------------------------------------------------------ the saving account (H2)
def build_saving(wb, P: Sheet) -> Sheet:
    S = Sheet(wb, "Saving", "Patrimony", "The saving account (CR-057 H2), $m: reporting only",
              "Government, business and household saving, national saving from the investment and consumption account, and the Previsión's "
              "deduction cost. Investment is not yet made to depend on saving: gross domestic investment stays the adopted inv_share path.")
    g = "Government"
    S.add("bal", "Budget balance", lambda y, r: f"=Budget!Z{r}", group=g)
    S.add("ginv", "Public investment inside the Budget", lambda y, r: (
        f"='Energy link'!AU{r}+'Energy link'!AS{r}+'Energy link'!AX{r}+SUMPRODUCT((Events!$B$6:$B$400<=$A{r})*(Events!$C$6:$C$400>=$A{r})"
        f"*(Events!$E$6:$E$400=\"Investment\")*Events!$H$6:$H$400)"),
          note="Public works and the Patrimony's works (Energy link AU), the atomic stations (AS), the Works' dams (AX) and the Investment events: "
               "spending that is saving, not consumption.")
    S.add("pat", "The Patrimony's net accumulation", lambda y, r: f"=Patrimony!{P['accum']}{r}")
    S.add("gov", "Government saving", lambda y, r: f"={S['bal']}{r}+{S['ginv']}{r}+{S['pat']}{r}",
          note="Receipts less government consumption, transfers and interest, plus the Patrimony's accumulation. The brief's narrower measure "
               "(balance + Patrimony) is B + D.")
    g = "Business"
    S.add("bus", "Champions' retained earnings", lambda y, r: f"=Champions!BA{r}*(1-crown_payout)", group=g,
          note="Champions' profits (Champions BA, at home and abroad) less dividends at crown_payout. Other firms' retained earnings are not "
               "modelled and fall into household saving.")
    g = "National saving"
    S.add("gdi", "Gross domestic investment", lambda y, r: f"='Energy link'!AA{r}", group=g)
    S.add("ni", "Net income from abroad", lambda y, r: f"=Abroad!M{r}+Budget!H{r}-Abroad!O{r}-Abroad!V{r}")
    S.add("nfi", "Net foreign investment", lambda y, r: f"='Energy link'!AF{r}+{S['ni']}{r}",
          note="Net exports (Energy link AF) plus net income from abroad.")
    S.add("gold", "New gold kept as money", lambda y, r: f"=Resources!R{r}", note="Outside consumption in the account (Energy link AG).")
    S.add("nat", "National saving", lambda y, r: f"={S['gdi']}{r}+{S['nfi']}{r}+{S['gold']}{r}",
          note="Gross domestic investment + net foreign investment (+ new monetary gold, so that national income less consumption equals it).")
    S.add("nat_gdp", "… / core GDP", lambda y, r: f"=IF(Economy!O{r}>0,{S['nat']}{r}/Economy!O{r},0)", fmt="0.0%")
    g = "Households"
    S.add("hh", "Household saving (residual)", lambda y, r: f"={S['nat']}{r}-{S['gov']}{r}-{S['bus']}{r}", group=g)
    S.add("hh_inc", "Household disposable income (consumption + saving)", lambda y, r: f"='Energy link'!AG{r}+{S['hh']}{r}")
    S.add("hh_rate", "Household saving rate", lambda y, r: f"=IF({S['hh_inc']}{r}>0,{S['hh']}{r}/{S['hh_inc']}{r},0)", fmt="0.0%")
    S.add("cut_saved", "… of it from tax cuts (Patrimony)", lambda y, r: f"=Patrimony!{P['pinv']}{r}")
    g = "The Previsión (CR-057 F), from 1919"
    S.add("prev_n", "Contributors (thousand)", lambda y, r: f"=IF(AND(c57_on=1,$A{r}>=prev_from),Labour!B{r}*prev_part/1000,0)", group=g)
    S.add("prev_c", "Deductible contributions at the caps ($m)", lambda y, r: f"={S['prev_n']}{r}*((1-prev_se)*300+prev_se*1500)/1000",
          note="$300 a year for wage earners, $1,500 for the self-employed (A2, approved), all contributors at their cap.")
    S.add("prev_cost", "Deduction cost to receipts ($m, memo)", lambda y, r: f"={S['prev_c']}{r}*prev_mtr",
          note="Contributions × the marginal rate. Reporting only: not taken out of Budget receipts in this build.")
    return S


# ------------------------------------------------------------------ checks, log, start
def link_checks(wb, M: Sheet) -> None:
    K = wb["Checks"]
    assert K.max_column == 40 and K["AN5"].value.startswith("Identified investment"), K.max_column
    K["AO5"].value = "Gold covers notes (40%) and partner balances (50%) (CR-057)"
    K["AO5"]._style = copy.copy(K["AN5"]._style)
    K["AO4"]._style = copy.copy(K["AN4"]._style)
    K.column_dimensions["AO"].width = K.column_dimensions["AN"].width or 13
    for y in YEARS:
        r = row(y)
        K[f"AO{r}"].value = f"=Money!{M['chk']}{r}"
        K[f"AO{r}"]._style = copy.copy(K[f"AN{r}"]._style)
        s = K[f"S{r}"].value
        assert s.endswith(f'+COUNTIF(AM{r}:AN{r},"Check")'), s
        K[f"S{r}"].value = s + f'+COUNTIF(AO{r},"Check")'


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "5 Nov: CR-057"
    Ch.cell(n, 2).value = "The economic order tightened"
    Ch.cell(n, 3).value = (
        "CR-057 (master lever c57_on; at 0 the CR-051/054/055 workbook exactly). H1 Money sheet: partner balances (Japan, the peso reserve, "
        "the others) covered half in gold; from 1914 the money stock follows last year's gold at a working cover (c_work, gliding from the 1913 "
        "cover by c_glide; c_ster in 1927-28) and the 40% floor's automatic tightening; the price level derived (Economy H; slump_price gone); "
        "notes and reserves = M + the Japan-rescue item; rb_est and cb_buy 0; the new-issue coupon r_real + trailing price change (floor 2%), "
        "blended into the stock (Budget X); the atomic programme's domestic costs (Atomic R, Works) at the derived level; "
        "the migration and partners' pulls at US prices. H3 Patrimony sheet: royalties, canal, estates (the Works keep their own returns in "
        "1917-27), half the levy, leased land out of the Budget; real 4.5% + trailing price change; abroad from 1919; 1931-32 losses; 3% from "
        "1910 into the Budget for earmarked works (AD, AE); dev_share, the reserve above the buffer and dev_bonds off; a lagged tax-cut rule on "
        "Budget C; private investment from tax cuts; Economy D re-based. H6 crown_comp 0, crown_row on chartered dividends, royalty floors. H7 "
        "Budget L relabelled (War Revenue Act 1915, memo). H2 Saving sheet (reporting). New check AO. MODEL.")
    for c in range(1, 4):
        Ch.cell(n, c)._style = copy.copy(Ch.cell(n - 1, c)._style)
    S = wb["Start"]
    r0 = S.max_row + 1
    for i, (nm, txt) in enumerate((("Money", "CR-057 H1: partner balances, the money stock and the derived price level, the cover tests, the coupons."),
                                   ("Patrimony", "CR-057 H3: the Patrimony's rents, returns, spending rule and works; the tax-cut rule; the output effect."),
                                   ("Saving", "CR-057 H2: government, business and household saving, the Previsión (reporting only)."))):
        S.cell(r0 + i, 1).value = nm
        S.cell(r0 + i, 2).value = txt
        for c in (1, 2):
            S.cell(r0 + i, c)._style = copy.copy(S.cell(81, c)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["c57_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true", help="save c57_on = 0 in both cases (identity build)")
    ap.add_argument("--set", action="append", default=[], help="NAME=STORY[,STRESS]: override a CR-057 lever (variants)")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    for s in ("Works", "Electro champions", "Energy link"):
        if s not in wb.sheetnames:
            raise SystemExit("needs the CR-051/054/055 workbook")
    if "Money" in wb.sheetnames:
        raise SystemExit("Money sheet already exists: build from the CR-051/054/055 workbook")
    levers = list(LEVERS)
    for kv in a.set:
        k, v = kv.split("=")
        vals = [float(x) for x in v.split(",")]
        for i, lv in enumerate(levers):
            if isinstance(lv, tuple) and lv[0] == k:
                levers[i] = (lv[0], lv[1], vals[0], vals[-1], *lv[4:])
                break
        else:
            raise SystemExit(f"no CR-057 lever {k}")
    base.add_levers(wb, levers)
    force_levers(wb)
    M = build_money(wb)
    link_money(wb, M)
    P = build_patrimony(wb)
    link_patrimony(wb, P)
    link_crown(wb)
    build_saving(wb, P)
    link_checks(wb, M)
    log(wb, a.off)
    wb.save(a.dst)
    print(f"saved {a.dst}" + (" (c57_on = 0)" if a.off else ""))


if __name__ == "__main__":
    main()
