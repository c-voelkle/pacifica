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
  investment from the energy workbook, Energy link H, with homes wired as coverage; rail, ports
  and the canal at g_core of GDP with a coverage path), as a growth increment like the old column;
- Economy J is multiplied by (1 + the engine's level factor) = (1 + G2/G3)(1 + G4)(1 + G6) - 1:
  G2/G3  research in Jones and Williams's flow form (revised after the fresh-context review, M1/M2):
         extra TFP growth each year = g_r x (Pacifica's research / GDP g_lag_p years before x its
         usable share under open licensing x (1 - g_leak x Pacifica's output / the Union's, last
         year) - the Union's research / GDP g_lag_u years before x its usable share under exclusive
         licences), when positive; the lead is the exponential of its running sum;
  G4     learning by doing in seven sectors: experience E = own leader's world share
         + g_lbd_x x the rest (Irwin and Klenow 1994), Pacifica's leader against the Union's; the
         cost advantage b x ln(E_P / E_U), b = -log2(1 - learning rate), weighted by each sector's
         gross output / GDP (Hulten); summed; cars from the vehicles built (Champions U);
  G6     capital at the ordinary return: the stock of gross domestic investment (Energy link AA,
         deflated as GDP is) depreciating at k_dep; level ((K/Y) / (K/Y) in g_kstart)^(k_alpha /
         (1 - k_alpha)) from g_kstart (the base path holds the capital before it); last year's capital over
         last year's trend output (Economy S / G), so a slump does not read as capital deepening.
While g_on = 1, CR-056's mode 2 (Economy C) and C3 (Champions Z, AF) are switched off: G6 and G2
supersede them. C1 and C5 (Economy J's Dynamics factor) stay with dyn_mode.
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
    ("g_r", "G2: social return to research (TFP growth per unit of research / GDP)", 0.35, 0.25, "return",
     "Author 09:18 and 09:48 (35%, research directed at industrial goals); anchored",
     "Jones and Williams (1998): 'estimated TFP growth accounted for by R&D is then r R/Y' (p. 1128), with zero depreciation "
     "as their convention; 'a conservative estimate of the social return of 30 percent' (p. 1121), 0.35-0.37 in their regression "
     "(p. 1131), measured on US industry 1961-89 at about 2% of GDP, the intensity Pacifica reaches in 1929. HMM: case-study "
     "median social return 56% (p. 25). Stress 0.25. Replaces the first build's stock elasticity (review M2)."),
    ("g_lag_p", "G2/G3: adoption lag in Pacifica (open licensing)", 3, 4, "years", "Model estimate (anchored)",
     "HMM p. 16: 'a mean lag from 4 to 6 years'; Moser p. 38: licensees took 8-9 years. Open licensing and in-house laboratories shorten it."),
    ("g_lag_u", "G2/G3: adoption lag in the Union (exclusive licences)", 6, 6, "years", "Model estimate (anchored)", "As above."),
    ("g_pat", "G3: patented share of new knowledge", 0.3, 0.3, "share", "Anchored",
     "Moser p. 31: about 20% of US chemical innovations patented (1893, 1915), 44-49% in machinery; 'the majority of innovations "
     "occur outside of the patent system' (p. 40)."),
    ("g_open", "G3: usable share of patented knowledge under open licensing", 0.9, 0.8, "share", "Author 09:18 (decision 3)", ""),
    ("g_excl", "G3: usable share of patented knowledge under exclusive licences", 0.6, 0.6, "share", "Author 09:18 (decision 3)", ""),
    ("g_leak", "G2: share of Pacifica's research benefits that accrue to the Union", 0.25, 0.30, "share", "Anchored",
     "Coe and Helpman in HMM p. 30: 'roughly a quarter of the benefits from R&D in G-7 countries accrues to their trading partners'."),
    ("g_gu", "G6: the Union's real output growth (memo: its steady-state capital / output)", 0.04, 0.04, "a year", "Model estimate", ""),
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
    ("g_kstart", "G6: first year capital deepening counts (Pacifica's capital / output measured from the year before)", 1900, 1900,
     "year", "Model estimate (review S2)",
     "Paths!L is calibrated to the historical West, which holds its own capital; the dilution of the gold rush and the 1880s "
     "arrivals is inside that base. Counted from CR-056's dyn_start, as CR-056 mode 2 does."),
    ("g_car_lp", "G4: Pacifica's leading carmaker's share of Pacifica's vehicles", 0.5, 0.4, "share", "Model estimate",
     "The moving line comes from the Polytechnic's production-engineering school in 1911 (canon, Champions U note)."),
    ("g_car_lu", "G4: the Union's leading carmaker's share of the Union's vehicles", 0.4, 0.45, "share", "Model estimate",
     "Ford's share of US output was about half in the early 1920s and a third by 1929 (to verify)."),
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
# Motor vehicles built, millions: the Union (historical US production, to verify) and the rest of the world (to verify).
US_VEH = {1899: 0.0, 1900: 0.004, 1905: 0.025, 1910: 0.187, 1913: 0.485, 1916: 1.6, 1920: 2.2, 1923: 4.0, 1925: 4.3, 1929: 5.3,
          1930: 3.4, 1931: 2.4, 1932: 1.4}
ROW_VEH = {1899: 0.0, 1900: 0.005, 1913: 0.1, 1920: 0.15, 1929: 0.75, 1932: 0.5}
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
    ("car", "Motor vehicles", "CARS", "CARS", {1900: 0.0, 1913: 0.015, 1929: 0.04}, ("lr_car",)),
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
    rp, ru = interp(RD_P), interp(RD_U)

    g = "G2 and G3: research and diffusion"
    a = G.add("rd_p", "Pacifica's research / GDP", lambda y, r: round(rp[y], 5), group=g, is_input=True, fmt="0.00%",
              note="The author's path: 0.6% (1880), 1.2% (1900), 1.8% (1913), 2% (1929) (09:18; 1a at 10:06). Public and private.")
    b = G.add("rd_u", "The Union's research / GDP", lambda y, r: round(ru[y], 5), is_input=True, fmt="0.00%",
              note="MODEL from Mowery and Rosenberg: 2,775 research scientists and engineers in manufacturing labs (1921), 6,274 (1927), "
                   "27,777 (1940); federal research 12-20% of the 1930s total, $74.1m in 1940 (pp. 21-22, 27).")
    d = G.add("ratio", "Pacifica's output / the Union's, last year (for the leak)",
              lambda y, r: (0 if y == FIRST else
                            f"=IF(Labour!BK{r-1}>0,((Economy!J{r-1}+Economy!L{r-1})*Paths!B{r-1}/Economy!H{r-1}"
                            f"+Economy!K{r-1}+Economy!M{r-1}+Economy!N{r-1})/Labour!BK{r-1},0)"), fmt="0.00",
              note="Pacifica's GDP at US prices (as Economy V) over the Union's GDP (Labour BK), last year (review M1).")
    up = G.add("use_p", "Usable share of own research, Pacifica (open licensing)", lambda y, r: "=1-g_pat+g_pat*g_open", fmt="0.00")
    uu = G.add("use_u", "Usable share of own research, the Union (exclusive licences)", lambda y, r: "=1-g_pat+g_pat*g_excl", fmt="0.00")
    lp = G.add("rd_p_lag", "Pacifica's research, g_lag_p years before",
               lambda y, r: f"=INDEX(${a}$6:${a}$92,MAX(1,A{r}-1845-g_lag_p))", fmt="0.00%")
    lu = G.add("rd_u_lag", "The Union's research, g_lag_u years before",
               lambda y, r: f"=INDEX(${b}$6:${b}$92,MAX(1,A{r}-1845-g_lag_u))", fmt="0.00%")
    inc = G.add("inc", "Extra TFP growth from research this year",
                lambda y, r: f"=IF(g_on=1,MAX(0,g_r*({lp}{r}*{up}{r}*(1-g_leak*{d}{r})-{lu}{r}*{uu}{r})),0)", fmt="0.000%",
                note="g_r × (Pacifica's usable research less the share leaking to the Union, scaled to the Union's output, less the "
                     "Union's usable research), lagged; only a lead counts (the base path holds the Union's own technology). "
                     "Jones and Williams's flow form: TFP growth from R&D = r × R/Y.")
    cum = G.add("cum", "Cumulative (log) TFP lead from research",
                lambda y, r: (f"={inc}{r}" if y == FIRST else f"={c51.col(G.n)}{r-1}+{inc}{r}"), fmt="0.000")
    l2 = G.add("l2", "G2/G3: TFP lead from research", lambda y, r: f"=EXP({cum}{r})-1", fmt="0.0%")
    incn = G.add("inc_nd", "… the same without open licensing (memo)",
                 lambda y, r: f"=IF(g_on=1,MAX(0,g_r*({lp}{r}*{uu}{r}*(1-g_leak*{d}{r})-{lu}{r}*{uu}{r})),0)", fmt="0.000%")
    cumn = G.add("cum_nd", "… cumulative (memo)", lambda y, r: (f"={incn}{r}" if y == FIRST else f"={c51.col(G.n)}{r-1}+{incn}{r}"),
                 fmt="0.000")
    G.add("l3", "… of which open licensing (G3, memo)", lambda y, r: f"=EXP({cum}{r}-{cumn}{r})-1", fmt="0.0%")
    G.add("ret_m", "Net return on the marginal research dollar (memo)", lambda y, r: "=g_r", fmt="0%",
          note="In the flow form the author's return is the return: constant at Pacifica's intensities, which are within the "
               "range it was measured at (about 2% of GDP).")

    vus, vrw = interp(US_VEH, before=0), interp(ROW_VEH, before=0)
    usv = G.add("veh_u", "The Union's vehicles built (m, input)", lambda y, r: round(vus[y], 4), is_input=True, fmt="0.00",
                note="Historical US motor vehicle production (to verify).")
    rwv = G.add("veh_w", "The rest of the world's vehicles built (m, input)", lambda y, r: round(vrw[y], 4), is_input=True, fmt="0.00")
    wv = G.add("veh_world", "World vehicles built (m)", lambda y, r: f"=Champions!U{r}/1000+{usv}{r}+{rwv}{r}", fmt="0.00",
               note="Pacifica's (Champions U, from the energy workbook) + the Union's + the rest.")

    g = "G4: learning by doing (leader's world share, Pacifica against the Union)"
    terms = []
    first = True
    for key, label, sp, su, wt, lv in SECTORS:
        if sp == "CARS":
            P = G.add(f"{key}_p", f"{label}: Pacifica's leader",
                      lambda y, r: f"=IF({wv}{r}>0,g_car_lp*Champions!U{r}/1000/{wv}{r},0)", group=g if first else None, fmt="0.00",
                      note="g_car_lp × Pacifica's vehicles (Champions U) / the world's (review S6).")
        elif isinstance(sp, str):
            sh, cl = sp.split("!")
            P = G.add(f"{key}_p", f"{label}: Pacifica's leader", (lambda sh, cl: lambda y, r: f"={sh}!{cl}{r}")(sh, cl),
                      group=g if first else None, fmt="0.00", note=f"{sp}: the champion's world share.")
        else:
            v = interp(sp, before=0)
            P = G.add(f"{key}_p", f"{label}: Pacifica's leader", (lambda v: lambda y, r: round(v[y], 4))(v),
                      group=g if first else None, is_input=True, fmt="0.00", note="MODEL world share.")
        first = False
        if su == "CARS":
            U = G.add(f"{key}_u", f"{label}: the Union's leader", lambda y, r: f"=IF({wv}{r}>0,g_car_lu*{usv}{r}/{wv}{r},0)", fmt="0.00")
        else:
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
              lambda y, r: (f"=g_su/(g_gu+k_dep)*Economy!S{r}" if y == FIRST else f"={c51.col(G.n)}{r-1}*(1-k_dep)+IF(Economy!O{r}>0,'Energy link'!AA{r}*Economy!S{r}/Economy!O{r},0)"),
              group=g, note="Gross domestic investment (Energy link AA: the inv_share path × GDP, public and private alike) deflated as "
                            "GDP is (× Economy S / O; review S1), less k_dep. Starts at the Union's ratio × real GDP in 1846.")
    ky = G.add("ky", "Capital / real trend GDP, last year", lambda y, r: (f"=g_su/(g_gu+k_dep)" if y == FIRST else f"=IF(Economy!S{r-1}>0,{k}{r-1}/(Economy!S{r-1}/Economy!G{r-1}),g_su/(g_gu+k_dep))"),
               fmt="0.00")
    kyu = G.add("ky_u", "The Union's capital / real GDP", lambda y, r: "=g_su/(g_gu+k_dep)", fmt="0.00",
                note="Steady state s / (g + δ) at the Union's investment share and growth.")
    l6 = G.add("l6", "G6: level from capital deepening since g_kstart",
               lambda y, r: (f"=IF(AND(g_on=1,A{r}>=g_kstart),({ky}{r}/INDEX(${ky}$6:${ky}$92,g_kstart-1845))"
                             f"^(k_alpha/(1-k_alpha))-1,0)"), fmt="0.0%",
               note="Hall and Jones's levels form, (K/Y)^(α/(1-α)), against Pacifica's own ratio in g_kstart: the base path "
                    "(the historical West) already holds the capital before it, and the Union's ratio is held steady (review S2).")

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
    Ch = wb["Champions"]
    for y in YEARS:  # CR-056 C3 (research spillovers into the champions' shares) is superseded by G2 while g_on = 1 (review S5)
        r = row(y)
        for L_, dc in (("Z", "AX"), ("AF", "AW")):
            v = Ch[f"{L_}{r}"].value
            old_ = f"(1+IF(dyn_mode=0,0,Dynamics!{dc}{r}))"
            assert old_ in v, v
            Ch[f"{L_}{r}"].value = v.replace(old_, f"(1+IF(OR(dyn_mode=0,g_on=1),0,Dynamics!{dc}{r}))")
    for y in YEARS:
        r = row(y)
        if y > FIRST:
            d = E[f"D{r}"].value
            assert d.startswith("=IF(c57_on=1,Patrimony!"), d
            E[f"D{r}"].value = f"=IF(g_on=1,Growth!{G['dg']}{r},{d[1:]})"
        c_ = E[f"C{r}"].value
        assert c_.startswith(f"=IF(AND(dyn_mode=2,$A{r}>=dyn_start),"), c_
        E[f"C{r}"].value = c_.replace(f"=IF(AND(dyn_mode=2,$A{r}>=dyn_start),", f"=IF(AND(dyn_mode=2,g_on<>1,$A{r}>=dyn_start),", 1)
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
