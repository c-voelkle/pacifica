"""The growth engine (CR-057 follow-up): where Pacifica's lead comes from.

    python3 finance/build/cr057_growth_engine.py IN.xlsx OUT.xlsx [--off] [--set NAME=STORY[,STRESS]]

IN is the CR-057 workbook built on the CR-056 dynamic layer (cr056_dynamics.py, then
cr057_economic_order.py). The script never recalculates; run LibreOffice (xlsx skill
scripts/recalc.py) afterwards. With --off the master lever g_on is saved at 0 in both cases: that
build must reproduce IN's values exactly (the identity check).

Authorization: the author, 6 November 2026, on the growth design note
(finance/CR-057-growth-design-note.md): "Yes that sounds much more accurate"; the answers of 09:18,
09:48 ("aim high ... research directed at industrial goals and close to industry") and 10:06 (steel
24%, the research path to 2%). Nothing in the storyline or the register changes. All amounts MODEL.

One master lever, g_on. At 1:
- Economy D (the Development Fund's 30% return, or CR-057's re-based Patrimony term) is replaced
  by the network premium alone (G6b): g_prem x (1 - coverage) on core network investment (power
  investment from the energy workbook, Energy link H, with homes wired as coverage; AP would close a loop through the Works' price level; rail, ports and the canal at g_core of
  GDP with a coverage path), as a growth increment like the old column;
- Economy J is multiplied by (1 + the engine's level factor) = (1 + G2/G3)(1 + G4)(1 + G6) - 1:
  G2/G3  research stocks (Pacifica, the Union, the rest of the world) per unit of output,
         depreciating at g_dep, entering after an adoption lag (open licensing g_lag_p, exclusive
         licences g_lag_u); the usable share of the patented part (g_open against g_excl);
         absorption of the world stock rising with own research; a quarter of Pacifica's stock
         leaking to the Union; TFP lead = MAX(1, Pacifica's effective stock / the Union's)^g_gamma;
  G4     learning by doing in seven sectors: experience E = own leader's world share
         + g_lbd_x x the rest (Irwin and Klenow 1994), Pacifica's leader against the Union's; the
         cost advantage b x ln(E_P / E_U), b = -log2(1 - learning rate), weighted by each sector's
         gross output / GDP (Hulten); summed;
  G6     capital at the ordinary return: the stock of gross domestic investment (Energy link AA at
         Economy H) depreciating at k_dep; level ((K/Y) / (K/Y)_Union)^(k_alpha / (1 - k_alpha)), the
         Union at g_su / (g_gu + k_dep) (Hall and Jones's levels form); last year's ratio (no circularity).
G1 (Paths!L), G5 (talent, Economy I), G7 (mining, the Gulf) and the champions' block (Economy M)
are unchanged: the champions' R&D is inside the research path, and the research level multiplies
non-mining, non-champion output only (Economy J), so it is not counted twice (G8, simplified).
Research: the state's half (g_pub) beyond the research already in Technical programmes is charged to a new
Budget line AF (g_charge; author's decision 3) and counted in government consumption (Energy link AE).
"""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cr041_russian_war as base  # noqa: E402
import cr051_054_055_champions as c51  # noqa: E402

AUTHOR = "CR-057 growth engine, 6 Nov 2026"
base.AUTHOR = AUTHOR
FIRST, LAST, YEARS, row, interp = c51.FIRST, c51.LAST, c51.YEARS, c51.row, c51.interp

LEVERS = [
    "— CR-057 growth engine: research, diffusion, learning, capital, networks (6 Nov 2026) —",
    ("g_on", "Growth engine: 1 = on (research, learning, capital, network premium); 0 = the old Economy D and J", 1, 1, "switch",
     "Author's decisions, 6 Nov 2026 (growth design note)",
     "0 reproduces the input workbook exactly. 1 replaces Economy D (the Fund's 30% return or CR-057's Patrimony term) by the "
     "network premium and multiplies Economy J by the engine's level factor (Growth sheet)."),
    ("g_gamma", "G2: TFP elasticity of the effective research stock (relative to the Union's)", 0.12, 0.08, "elasticity",
     "Author 09:48 (research directed at industrial goals); anchored",
     "HMM (2010): firm-level 'from 0.01 to 0.25 but centered on 0.08' (p. 21); G7 country level 0.20-0.22, biased upward. "
     "0.12 = the author's 35% held at the 1900s' intensity, research directed at industrial goals and close to industry."),
    ("g_dep", "G2: research stock depreciation", 0.15, 0.20, "a year", "Anchored",
     "HMM p. 15: 'most researchers use the 15 per cent that Griliches had settled on'; estimates 10-36%."),
    ("g_lag_p", "G2/G3: adoption lag in Pacifica (open licensing)", 3, 4, "years", "Model estimate (anchored)",
     "HMM p. 16: 'a mean lag from 4 to 6 years'; Moser p. 38: licensees took 8-9 years. Open licensing and in-house laboratories shorten it."),
    ("g_lag_u", "G2/G3: adoption lag in the Union (exclusive licences)", 6, 6, "years", "Model estimate (anchored)", "As above."),
    ("g_pat", "G3: patented share of new knowledge", 0.3, 0.3, "share", "Anchored",
     "Moser p. 31: about 20% of US chemical innovations patented (1893, 1915), 44-49% in machinery; 'the majority of innovations "
     "occur outside of the patent system' (p. 40)."),
    ("g_open", "G3: usable share of patented knowledge under open licensing", 0.9, 0.8, "share", "Author 09:18 (decision 3)", ""),
    ("g_excl", "G3: usable share of patented knowledge under exclusive licences", 0.6, 0.6, "share", "Author 09:18 (decision 3)", ""),
    ("g_abs", "G2: absorption, own stock per output at which half the world's stock is usable", 0.05, 0.05, "stock / GDP",
     "Model estimate (anchored)",
     "Mowery and Rosenberg p. 69 (own R&D 'essential to the absorption'); HMM p. 31 ('the absorption capacity of the receiver')."),
    ("g_leak", "G2: share of Pacifica's stock usable in the Union", 0.25, 0.30, "share", "Anchored",
     "Coe and Helpman in HMM p. 30: 'roughly a quarter of the benefits from R&D in G-7 countries accrues to their trading partners'."),
    ("g_gu", "G2: the Union's real output growth (for its stock per output)", 0.04, 0.04, "a year", "Model estimate", ""),
    ("g_gw", "G2: the rest of the world's real output growth", 0.025, 0.025, "a year", "Model estimate", ""),
    ("g_lbd_x", "G4: weight of others' experience against one's own", 0.3, 0.3, "×", "Anchored",
     "Irwin and Klenow (1994): 'α and γ average .28 and .32'; international spillovers as strong as national ones."),
    ("lr_steel_e", "G4: steel learning rate to 1900", 0.24, 0.20, "per doubling", "Author 10:06 (Ohashi 2004)",
     "Ohashi (2004): 'The learning rate obtained is 24 percent' (Japan, 1955-65)."),
    ("lr_steel_l", "G4: steel learning rate by 1929", 0.15, 0.12, "per doubling", "Model estimate",
     "Ghemawat (1985), in Ohashi p. 19: 79 of 97 products at 11-21%."),
    ("lr_car", "G4: motor vehicles", 0.15, 0.12, "per doubling", "Anchored", "Model T 1909-25: 15% real per doubling (McCalley)."),
    ("lr_chem", "G4: chemicals", 0.15, 0.12, "per doubling", "Anchored", "Lieberman (1984): 19% net of capacity, 24-28% gross."),
    ("lr_elec", "G4: electrical equipment", 0.10, 0.08, "per doubling", "Model estimate", ""),
    ("lr_power", "G4: power systems (equipment and fuel rate)", 0.10, 0.08, "per doubling", "Anchored",
     "Mowery and Rosenberg p. 117: coal per kWh from almost 7 lb (1900) to under 0.9 lb (1960s)."),
    ("lr_alu", "G4: aluminium", 0.15, 0.12, "per doubling", "Anchored", "USGS DS140 with the author's prices: 14-18% (1900-29)."),
    ("lr_air_e", "G4: aircraft to 1920", 0.15, 0.12, "per doubling", "Anchored", "Wright (1936): whole airplane 17% falling to 10% (p. 126)."),
    ("lr_air_l", "G4: aircraft by 1929", 0.10, 0.08, "per doubling", "Anchored", "As above."),
    ("g_su", "G6: the Union's gross investment / GDP", 0.21, 0.21, "share", "Model estimate (to verify)",
     "Kuznets: US gross capital formation about a fifth of GNP, 1869-1928 (to verify). The Union's capital / output is "
     "g_su / (g_gu + k_dep), measured the same way as Pacifica's."),
    ("g_prem", "G6: network premium at zero coverage", 0.08, 0.04, "return", "Model estimate (anchored)",
     "Bom and Ligthart (2014): long-run output elasticity of public capital 0.122, 'almost doubled' for core regional "
     "infrastructure; Fernald (1999): 'the interstate system was highly productive, but a second one would not be.'"),
    ("g_core", "G6: rail, port and canal investment outside power", 0.01, 0.01, "share of GDP", "Model estimate", ""),
    ("g_pub", "Research paid by the state", 0.5, 0.5, "share", "Model estimate",
     "The Polytechnic, the institutes, the Works' civilian research; the champions' laboratories pay the rest."),
    ("g_tp_res", "Share of Technical programmes (Budget S, Paths V) that is research", 0.75, 0.75, "share", "Model estimate",
     "Paths V: 'Polytechnic, institutes, testing stations, state works'; the testing stations and state works are the rest."),
    ("g_charge", "Charge the state's research beyond Technical programmes to the Budget (1 = yes)", 1, 1, "switch",
     "Author's decision 3 (6 Nov 2026, 10:45)",
     "Budget AF = g_pub × research × GDP − g_tp_res × the Technical programmes' base (GDP × Paths V), when positive; in "
     "government consumption (Energy link AE)."),
]

# Research intensity (share of GDP). Pacifica: the author's path (09:18, 1a at 10:06); the Union and the rest of the
# world: Mowery and Rosenberg (research staff 1921-40; federal 12-20% of the 1930s total), MODEL.
RD_P = {1846: 0.0, 1851: 0.0005, 1860: 0.001, 1870: 0.003, 1880: 0.006, 1900: 0.012, 1913: 0.018, 1929: 0.02}
RD_U = {1846: 0.0002, 1880: 0.0005, 1900: 0.001, 1913: 0.0015, 1929: 0.0025}
RD_W = {1846: 0.0005, 1880: 0.001, 1900: 0.002, 1913: 0.003, 1929: 0.004}
RATIO_PU = {1846: 0.01, 1870: 0.04, 1900: 0.10, 1913: 0.18, 1929: 0.30}  # Pacifica's output / the Union's, for the leak
COV_RAIL = {1846: 0.0, 1870: 0.3, 1890: 0.8, 1900: 0.95, 1910: 1.0}

# G4 sectors: (key, label, Pacifica leader's world share, the Union leader's, gross output / Pacifica's GDP, lever(s))
# Shares are MODEL estimates for the alternate history (to verify where historical). Steel: in canon a San Francisco
# syndicate buys Carnegie Steel in 1901 and combines it with the Pacifican mills as Pacifica Steel (master storyline), so
# there is no US Steel: before 1901 the Union's leader is Carnegie (about 3 Mt of a 28 Mt world in 1900); from 1901
# Pacifica's leader is Pacifica Steel (Carnegie's plants plus the Pacifican mills, Champions R) and the Union's is the
# trust formed without Carnegie (about a third of the Union's output). Experience is the firm's, wherever its plants are;
# only the Pacifican mills' output is in Pacifica's GDP (the weight). Ford about a third of world cars in 1913; Alcoa most
# of the world's aluminium before 1900.
SECTORS = [
    ("steel", "Steel", {1870: 0.0, 1890: 0.01, 1900: 0.05, 1901: 0.16, 1913: 0.16, 1929: 0.17},
     {1870: 0.05, 1890: 0.12, 1900: 0.11, 1901: 0.12, 1913: 0.13, 1929: 0.14}, {1870: 0.01, 1900: 0.03, 1929: 0.03}, ("lr_steel_e", "lr_steel_l", 1900, 1929)),
    ("car", "Motor vehicles", {1900: 0.0, 1905: 0.05, 1913: 0.08, 1920: 0.10, 1929: 0.11},
     {1900: 0.0, 1905: 0.10, 1913: 0.33, 1920: 0.45, 1929: 0.23}, {1900: 0.0, 1913: 0.015, 1929: 0.04}, ("lr_car",)),
    ("chem", "Chemicals", "Champions!Y", {1870: 0.01, 1913: 0.03, 1929: 0.05}, {1870: 0.005, 1913: 0.015, 1929: 0.02}, ("lr_chem",)),
    ("elec", "Electrical equipment", "Champions!AD", {1880: 0.0, 1890: 0.15, 1913: 0.20, 1929: 0.15},
     {1880: 0.0, 1890: 0.005, 1913: 0.02, 1929: 0.03}, ("lr_elec",)),
    ("power", "Power systems", {1885: 0.0, 1890: 0.02, 1913: 0.10, 1929: 0.20}, {1885: 0.0, 1890: 0.02, 1929: 0.02},
     {1885: 0.0, 1890: 0.003, 1913: 0.015, 1929: 0.025}, ("lr_power",)),
    ("alu", "Aluminium", {1888: 0.0, 1900: 0.05, 1913: 0.20, 1929: 0.50}, {1888: 0.0, 1890: 0.50, 1900: 0.35, 1913: 0.30, 1929: 0.20},
     {1888: 0.0, 1900: 0.0005, 1913: 0.001, 1929: 0.002}, ("lr_alu",)),
    ("air", "Aircraft", {1910: 0.0, 1915: 0.10, 1929: 0.30}, {1910: 0.0, 1915: 0.10, 1929: 0.15},
     {1910: 0.0, 1915: 0.0005, 1929: 0.002}, ("lr_air_e", "lr_air_l", 1920, 1929)),
]


def find_col(ws, header: str) -> str:
    for c in range(1, ws.max_column + 1):
        if ws.cell(5, c).value == header:
            return openpyxl.utils.get_column_letter(c)
    raise SystemExit(f"{ws.title}: no column {header!r}")


def build_growth(wb) -> c51.Sheet:
    G = c51.Sheet(wb, "Growth", "Dynamics", "The growth engine (CR-057 follow-up): research, diffusion, learning, capital, networks",
                  "g_on (Levers): 0 = the old Economy D and J; 1 = Economy D is the network premium and Economy J is multiplied by "
                  "(1 + the level factor). See finance/CR-057-growth-design-note.md and finance/CR-057-growth-workbook.md.")
    G.ws["A3"].value = ("Years run down the page. Blue = input you can change · black = formula. "
                        "Built by finance/build/cr057_growth_engine.py; all amounts MODEL.")
    wired = find_col(wb["Dynamics"], "Homes wired (share)")
    rp, ru, rw, rat, cr = interp(RD_P), interp(RD_U), interp(RD_W), interp(RATIO_PU), interp(COV_RAIL)

    g = "G2 and G3: research and diffusion"
    a = G.add("rd_p", "Pacifica's research / GDP", lambda y, r: round(rp[y], 5), group=g, is_input=True, fmt="0.00%",
              note="The author's path: 0.6% (1880), 1.2% (1900), 1.8% (1913), 2% (1929) (09:18; 1a at 10:06). Public and private.")
    b = G.add("rd_u", "The Union's research / GDP", lambda y, r: round(ru[y], 5), is_input=True, fmt="0.00%",
              note="MODEL from Mowery and Rosenberg: 2,775 research scientists and engineers in manufacturing labs (1921), 6,274 (1927), "
                   "27,777 (1940); federal research 12-20% of the 1930s total, $74.1m in 1940 (pp. 21-22, 27).")
    c = G.add("rd_w", "The rest of the world's research / GDP", lambda y, r: round(rw[y], 5), is_input=True, fmt="0.00%",
              note="MODEL: Germany's and Britain's laboratories; Switzerland and Sweden about 0.1% (Gugerli et al. p. 175; Riksdag 1928).")
    d = G.add("ratio", "Pacifica's output / the Union's (for the leak)", lambda y, r: round(rat[y], 4), is_input=True, fmt="0.00")
    gy = G.add("gy", "Pacifica's real growth, last year",
               lambda y, r: 0.03 if y <= FIRST + 1 else f"=IF(Economy!S{r-2}>0,Economy!S{r-1}/Economy!S{r-2}-1,0.03)", fmt="0.0%")
    kp = G.add("kp", "Pacifica's research stock / GDP",
               lambda y, r: (f"={a}{r}/(0.03+g_dep)" if y == FIRST else
                             f"={c51.col(G.n)}{r-1}*(1-g_dep)/(1+{gy}{r})+INDEX(${a}$6:${a}$92,MAX(1,A{r}-1845-g_lag_p))"),
               fmt="0.000", note="Last year's stock less g_dep, over this year's output (last year's growth), plus research g_lag_p years ago.")
    ku = G.add("ku", "The Union's research stock / GDP",
               lambda y, r: (f"={b}{r}/(g_gu+g_dep)" if y == FIRST else
                             f"={c51.col(G.n)}{r-1}*(1-g_dep)/(1+g_gu)+INDEX(${b}$6:${b}$92,MAX(1,A{r}-1845-g_lag_u))"), fmt="0.000")
    kw = G.add("kw", "The world's research stock / GDP",
               lambda y, r: (f"={c}{r}/(g_gw+g_dep)" if y == FIRST else f"={c51.col(G.n)}{r-1}*(1-g_dep)/(1+g_gw)+{c}{r}"), fmt="0.000")
    up = G.add("use_p", "Usable share of own stock, Pacifica (open licensing)", lambda y, r: "=1-g_pat+g_pat*g_open", fmt="0.00")
    uu = G.add("use_u", "Usable share of own stock, the Union (exclusive licences)", lambda y, r: "=1-g_pat+g_pat*g_excl", fmt="0.00")
    ep = G.add("eff_p", "Pacifica's effective stock",
               lambda y, r: f"={kp}{r}*{up}{r}+{kp}{r}/({kp}{r}+g_abs)*{kw}{r}", fmt="0.000",
               note="Own stock × usable share + the world's stock × absorption (own / (own + g_abs)).")
    eu = G.add("eff_u", "The Union's effective stock",
               lambda y, r: f"={ku}{r}*{uu}{r}+{ku}{r}/({ku}{r}+g_abs)*{kw}{r}+g_leak*{kp}{r}*{d}{r}", fmt="0.000",
               note="As Pacifica's, plus g_leak of Pacifica's stock (scaled to the Union's output).")
    rr_ = G.add("R", "Pacifica's effective stock / the Union's", lambda y, r: f"=IF({eu}{r}>0,{ep}{r}/{eu}{r},1)", fmt="0.00")
    l2 = G.add("l2", "G2/G3: TFP lead from research", lambda y, r: f"=IF(g_on=1,MAX(1,{rr_}{r})^g_gamma-1,0)", fmt="0.0%",
               note="MAX(1, R)^g_gamma - 1: only a lead counts (the base path already holds the Union's own technology).")
    rnd = G.add("R_nd", "… the same ratio without open licensing (memo)",
                lambda y, r: f"=IF({eu}{r}>0,({kp}{r}*{uu}{r}+{kp}{r}/({kp}{r}+g_abs)*{kw}{r})/{eu}{r},1)", fmt="0.00")
    G.add("l3", "… of which open licensing (G3, memo)",
          lambda y, r: f"=IF(g_on=1,(MAX(1,{rr_}{r})/MAX(1,{rnd}{r}))^g_gamma-1,0)", fmt="0.0%")

    g = "G4: learning by doing (leader's world share, Pacifica against the Union)"
    terms = []
    first = True
    for key, label, sp, su, wt, lv in SECTORS:
        if isinstance(sp, str):
            sh, cl = sp.split("!")
            P = G.add(f"{key}_p", f"{label}: Pacifica's leader", (lambda sh, cl: lambda y, r: f"={sh}!{cl}{r}")(sh, cl),
                      group=g if first else None, fmt="0.00", note=f"{sp}: the champion's world share.")
        else:
            v = interp(sp, before=0)
            P = G.add(f"{key}_p", f"{label}: Pacifica's leader", (lambda v: lambda y, r: round(v[y], 4))(v),
                      group=g if first else None, is_input=True, fmt="0.00", note="MODEL world share.")
        first = False
        vu = interp(su, before=0)
        U = G.add(f"{key}_u", f"{label}: the Union's leader", (lambda v: lambda y, r: round(v[y], 4))(vu), is_input=True, fmt="0.00",
                  note="MODEL world share (to verify where historical).")
        vw = interp(wt, before=0)
        W = G.add(f"{key}_w", f"{label}: gross output / GDP", (lambda v: lambda y, r: round(v[y], 4))(vw), is_input=True, fmt="0.0%",
                  note="Hulten weight, MODEL.")
        if len(lv) == 1:
            lr = lv[0]
        else:
            e, l_, y0, y1 = lv
            lr = None
        if lr:
            lrf = (lambda lr: lambda y, r: f"={lr}")(lr)
        else:
            lrf = (lambda e, l_, y0, y1: lambda y, r: f"=IF(A{r}<={y0},{e},IF(A{r}>={y1},{l_},{e}+({l_}-{e})*(A{r}-{y0})/{y1 - y0}))")(e, l_, y0, y1)
        LR = G.add(f"{key}_lr", f"{label}: learning rate", lrf, fmt="0%")
        T = G.add(f"{key}_t", f"{label}: cost advantage × weight",
                  (lambda P, U, W, LR: lambda y, r: (f"={W}{r}*-LOG(1-{LR}{r},2)*LN(({P}{r}+g_lbd_x*(1-{P}{r}))/({U}{r}+g_lbd_x*(1-{U}{r})))"))(P, U, W, LR),
                  fmt="0.00%", note="w × b × ln(E_P / E_U), b = -log2(1 - learning rate), E = own share + g_lbd_x × the rest.")
        terms.append(T)
    l4 = G.add("l4", "G4: TFP lead from learning", lambda y, r: "=IF(g_on=1,EXP(" + "+".join(f"{t}{r}" for t in terms) + ")-1,0)",
               fmt="0.0%")

    g = "G6: capital at the ordinary return"
    k = G.add("k", "Capital stock (1913 $m)",
              lambda y, r: (f"=g_su/(g_gu+k_dep)*Economy!S{r}" if y == FIRST else f"={c51.col(G.n)}{r-1}*(1-k_dep)+'Energy link'!AA{r}/Economy!H{r}"),
              group=g, note="Gross domestic investment (Energy link AA: the inv_share path × GDP, public and private alike) at the price "
                            "level, less k_dep. Starts at the Union's ratio × real GDP in 1846.")
    ky = G.add("ky", "Capital / real GDP, last year", lambda y, r: (f"=g_su/(g_gu+k_dep)" if y == FIRST else f"=IF(Economy!S{r-1}>0,{k}{r-1}/Economy!S{r-1},g_su/(g_gu+k_dep))"),
               fmt="0.00")
    kyu = G.add("ky_u", "The Union's capital / real GDP", lambda y, r: "=g_su/(g_gu+k_dep)", fmt="0.00",
                note="Steady state s / (g + δ) at the Union's investment share and growth.")
    l6 = G.add("l6", "G6: level from capital per output against the Union's",
               lambda y, r: f"=IF(g_on=1,({ky}{r}/{kyu}{r})^(k_alpha/(1-k_alpha))-1,0)", fmt="0.0%",
               note="Hall and Jones's levels form, (K/Y)^(α/(1-α)), Pacifica against the Union.")

    g = "Into the Economy sheet"
    lvl = G.add("lvl", "Level factor into Economy J", lambda y, r: f"=(1+{l2}{r})*(1+{l4}{r})*(1+{l6}{r})-1", group=g, fmt="0.0%")
    vr = interp(COV_RAIL, before=0)
    cov = G.add("cov_rail", "Rail, ports and canal: coverage of the planned network", lambda y, r: round(vr[y], 3), is_input=True, fmt="0%")
    dg = G.add("dg", "G6b: network premium, growth increment into Economy D",
               lambda y, r: (0 if y == FIRST else
                             f"=IF(AND(g_on=1,Economy!O{r-1}>0),g_prem*((1-Dynamics!{wired}{r-1})*'Energy link'!H{r-1}"
                             f"+(1-{cov}{r-1})*g_core*Economy!O{r-1})/Economy!O{r-1},0)"),
               fmt="0.00%", note="g_prem × (1 − coverage) on last year's core network investment / last year's GDP: power (Energy link H, the energy "
                                 "workbook's power investment; coverage = homes wired) and rail, ports and the canal (g_core of GDP, coverage path).")

    g = "Memo: who pays for research"
    G.add("rd_cost", "Research spending ($m)", lambda y, r: f"={a}{r}*Economy!O{r}", group=g)
    pub = G.add("rd_pub", "… paid by the state ($m)", lambda y, r: f"=g_pub*{a}{r}*Economy!O{r}")
    tpr = G.add("rd_tp", "… already in Technical programmes ($m)", lambda y, r: f"=g_tp_res*Economy!O{r}*Paths!V{r}",
                note="g_tp_res × GDP × Paths V: the Polytechnic and institutes the Budget already pays for.")
    G.add("rd_charge", "… charged to the Budget beyond them ($m, into Budget AF)",
          lambda y, r: f"=IF(AND(g_on=1,g_charge=1),MAX(0,{pub}{r}-{tpr}{r}),0)")
    return G


def link_budget(wb, G: c51.Sheet) -> None:
    B, X = wb["Budget"], wb["Energy link"]
    assert B["AF5"].value is None and B["AE5"].value.startswith("Earmarked works"), B["AF5"].value
    B["AF5"].value = "Research beyond Technical programmes (growth engine)"
    B["AF5"]._style = copy.copy(B["AE5"]._style)
    B["AF4"]._style = copy.copy(B["AE4"]._style)
    B.column_dimensions["AF"].width = B.column_dimensions["AE"].width or 13
    base.note(B["AF5"], "The state's half of the research path (Growth sheet) beyond the research already in Technical programmes "
              "(g_tp_res of Budget S's base). 0 at g_on = 0 or g_charge = 0. Author's decision 3, 6 Nov 2026.", 100)
    for y in YEARS:
        r = row(y)
        B[f"AF{r}"].value = f"=Growth!{G['rd_charge']}{r}"
        B[f"AF{r}"]._style = copy.copy(B[f"AE{r}"]._style)
        yv = B[f"Y{r}"].value
        assert yv == f"=SUM(N{r}:X{r})+AE{r}", yv
        B[f"Y{r}"].value = f"=SUM(N{r}:X{r})+AE{r}+AF{r}"
        ae = X[f"AE{r}"].value
        assert ae.startswith(f"=Budget!N{r}+Budget!O{r}+Budget!P{r}+Budget!Q{r}+Budget!S{r}-"), ae
        X[f"AE{r}"].value = ae.replace(f"+Budget!S{r}-", f"+Budget!S{r}+Budget!AF{r}-", 1)


def link(wb, G: c51.Sheet) -> None:
    E = wb["Economy"]
    for y in YEARS:
        r = row(y)
        if y > FIRST:
            d = E[f"D{r}"].value
            assert d.startswith("=IF(c57_on=1,Patrimony!"), d
            E[f"D{r}"].value = f"=IF(g_on=1,Growth!{G['dg']}{r},{d[1:]})"
        j = E[f"J{r}"].value
        old = f"*(1+IF(dyn_mode=0,0,Dynamics!"
        assert old in j and j.endswith(f"*G{r}*H{r}/1000000"), j
        E[f"J{r}"].value = j.replace(f"*G{r}*H{r}/1000000", f"*(1+IF(g_on=1,Growth!{G['lvl']}{r},0))*G{r}*H{r}/1000000")
    base.note(E["D5"], (E["D5"].comment.text + "\n\n" if E["D5"].comment else "") +
              "Growth engine (g_on = 1): the network premium only (Growth sheet). The Fund's 30% return and CR-057's Patrimony term go: "
              "all capital earns the ordinary return through Growth G6.", 120)
    base.note(E["J5"], (E["J5"].comment.text + "\n\n" if E["J5"].comment else "") +
              "Growth engine (g_on = 1): × (1 + the level factor: research and diffusion, learning, capital; Growth sheet).", 120)


def log(wb, off: bool) -> None:
    Ch = wb["Changes"]
    n = Ch.max_row + 1
    Ch.cell(n, 1).value = "6 Nov: CR-057 growth"
    Ch.cell(n, 2).value = "The growth engine"
    Ch.cell(n, 3).value = ("Master lever g_on (at 0 the input workbook exactly). Growth sheet: research stocks for Pacifica, the Union and the "
                           "world with lags, open licensing, absorption and leakage (G2/G3); learning by doing in seven sectors (G4); capital "
                           "at the ordinary return (G6); the network premium (G6b). Economy D = the premium; Economy J × (1 + level). MODEL.")
    for c_ in range(1, 4):
        Ch.cell(n, c_)._style = copy.copy(Ch.cell(n - 1, c_)._style)
    S = wb["Start"]
    r0 = S.max_row + 1
    S.cell(r0, 1).value = "Growth"
    S.cell(r0, 2).value = "The growth engine: research, diffusion, learning, capital and the network premium (CR-057 follow-up)."
    for c_ in (1, 2):
        S.cell(r0, c_)._style = copy.copy(S.cell(81, c_)._style)
    if off:
        L = wb["Levers"]
        rr = int(wb.defined_names["g_on"].attr_text.split("$")[-1])
        L.cell(rr, 3).value = 0
        L.cell(rr, 4).value = 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--off", action="store_true", help="save g_on = 0 in both cases (identity build)")
    ap.add_argument("--set", action="append", default=[], help="NAME=STORY[,STRESS]: override a lever of this script")
    a = ap.parse_args()
    wb = openpyxl.load_workbook(a.src)
    for s in ("Dynamics", "Patrimony", "Money"):
        if s not in wb.sheetnames:
            raise SystemExit("needs the CR-057 workbook built on the CR-056 layer")
    if "Growth" in wb.sheetnames:
        raise SystemExit("Growth sheet already exists")
    levers = list(LEVERS)
    for kv in a.set:
        k_, v = kv.split("=")
        vals = [float(x) for x in v.split(",")]
        for i, lv in enumerate(levers):
            if isinstance(lv, tuple) and lv[0] == k_:
                levers[i] = (lv[0], lv[1], vals[0], vals[-1], *lv[4:])
                break
        else:
            raise SystemExit(f"no growth lever {k_}")
    base.add_levers(wb, levers)
    G = build_growth(wb)
    link(wb, G)
    link_budget(wb, G)
    log(wb, a.off)
    # The CR-057 money block and the 1927 Japan rescue close a loop (Money N from 1928 reads the rescue's callable balances,
    # the rescue's private share reads 1927 investment abroad, which reads 1927 output). LibreOffice reports it as Err:522
    # once the engine changes the path; iterative calculation resolves it (no value moves at g_on = 0).
    wb.calculation.iterate = True
    wb.calculation.iterateCount = 200
    wb.calculation.iterateDelta = 1e-7
    wb.save(a.dst)
    print(f"saved {a.dst}" + (" (g_on = 0)" if a.off else ""))


if __name__ == "__main__":
    main()
