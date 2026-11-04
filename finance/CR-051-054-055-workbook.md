# Workbook note, 4 November 2026: the costs and output of CR-051, CR-054 and CR-055

SHA-256 `@SHA@`. Built on the CR-052 workbook by [`build/cr051_054_055_champions.py`](build/cr051_054_055_champions.py) from `energy/build/energy_outputs.csv` (energy workbook `@ESHA@`), then recalculated in LibreOffice: 62,030 formulas, no errors. The CR-052 workbook is itself rebuilt each pass from the CR-050 workbook by `build/cr052_energy_link.py`, so the chain is CR-050 → CR-052 link → this build. The two workbooks were iterated to a fixed point (below). No check fails in the Story case in any year; the Stress case fails 17 year-checks (12 before; see Stress). Residents in 1932 move by about a thousand, not by 0.3 million: the storyline's "about 37 million" stands, and `population/` is not re-run. No storyline canon is changed. All amounts are MODEL.

**Authorization.** Author, 4 November 2026, after PR #63 (CR-052 to CR-055 integrated): "Follow-up task: put the costs and output of CR-051, CR-054 and CR-055 into the financial workbook. Do not change any storyline canon. Report back to me before merging." The amounts used are those the CRs carry (CR-051 M1–M4, S7, S8, open item 5; CR-054 A1, A2, A4, A5, "For the financial workbook"; CR-055 R0, R9, open item 6), with the levers below where the CRs give a range or nothing.

## What changed

| Item | How | Where |
| --- | --- | --- |
| The magnet halls (CR-051 M2) | `halls_y12` × Y-12's construction cost (`y12_build`, $110m in 1913 $; to verify): Story 2.75, Stress 3.0, on M2's timetable (decided 1917, first halls 1919, second stage 1922, twice Y-12 in 1923 with the copper rewind, the full plant 1925–26): **$302m (1913 $)**. Operation by the energy workbook's draw × `halls_op` ($35k a MW-year): $25m a year at 700 MW. Replaces CR-050's $130m construction, its $60m enlargement of 1928–30 (after 1927 the output rises through gaseous diffusion, M4) and its $6–10m operation. | Works → Atomic AD |
| The feed plant (M1) | Ralston College's columns with their oil-fired powerhouse, 1920–22, larger 1924–25 ($32m); their 0.4–0.75 Mt of oil at the oil price, and staff ($3–5m a year). | Works → Atomic AD |
| The Columbia station (S7) | Towns bought out 1919–20, piles, the separation plant, the company town, Roslyn steam ($40m, 1919–27; the CR-049/050 research installation of 1921 is taken as its first pile and not counted twice); operation $1–5m a year; the experimental breeder 1930–32 ($8m). | Works → Atomic AD |
| Gaseous diffusion (M4) | Pilot 1925–27 ($3m), plant 1930–32 ($50m), operation by its 150 MW. | Works → Atomic AD |
| The Works' dams and Rock Island (M2, S7) | Built by a hydro company of the Works on the Treasury's account: capacity from the energy workbook × `works_kw` ($130/kW, CR-051's "about $100m" for 400–500 MW), spread over the three years to first power; Rock Island with its 80-mile line. $94m (1913 $), $154m current. **Investment**, like the atomic stations. | Works → Atomic AF |
| The compacts (S8) | The White Bluffs fee with the river accord's share ($0.15m a year from 1920) and the royalty on Rock Island's and the Works' dams' kilowatt-hours (the energy workbook's `roy_mill`, size OPEN under CR-052 F12), paid by the Works, so in the Budget. The five Columbia dams' royalties are the power estate's and outside the Budget. | Works → Atomic AE |
| Rock Island's sales (S7) | Its output beyond the station to the Wenatchee smelter, the orchards and the pumps at `works_price` (0.4 cents 1913): about $3m a year. | Works → Atomic AG (returns) |
| The Mint's silver (M3) | 3,000 t lent 1918, returned 1923: about $95m at 1918–19 prices. A memo; no cash flow. | Works |
| Aluminium (CR-054 A1, A4) | 150 kt in 1929 by destination: the Realm and the Concord (the grid, the fleet's aircraft, the pool to Japan, civil uses) at the pool's price, the third beyond the Concord at the world price, 30% lower in 1931 and 35% in 1932 (`alu_x31`, `alu_x32`); purchased inputs `alu_inp`; first fabrication. With the aircraft and engines (an explicit path) it **replaces the input path in Champions!AO**. | Electro champions → Champions AO |
| Arkansas bauxite and the alumina refinery (A1) | Alumina from the Gulf: 290 kt and $14m in 1929, inside aluminium's inputs; the refinery and the royalty are the Gulf's. Memo. | Electro champions |
| Nitrogen, electric steel (A2, A5) | 90 kt N in 1929 (Columbia cells and Haber–Bosch on Valley gas) at the nitrogen price; electric steel (an eighth of steel) at a premium over ordinary steel. | Electro champions → Champions BF |
| The Columbia's electrochemistry (CR-055 R0) | Zinc, magnesium, phosphorus, copper refining, Tacoma's rubber (50 kt), the Portland hydrogenation works (5m bbl of motor fuel gained) at historical prices; electric pig iron (0.5 Mt) a memo, a change of process inside steel. Rubber and hydrogenation never below zero value added; their losses at world prices in 1931–32 (about $10m a year) are shown, not hidden. | Electro champions → Champions BF, AP, BC |
| Copper | 300 kt refined in 1929 is worth $120m, 43% of copper and other metals (Resources!F); 25–60% in every year. Reconciled: the series is not changed. | Electro champions |
| Plant | New output above the best of the last ten years × a plant cost per unit (`inv_*`): $580m 1908–32, of which hydrogenation $240m and rubber $110m. | Electro champions → Energy link AT |
| Power investment, counted once (R9) | The energy workbook's memo (H) becomes the account's first component: its generic cost of the Works' dams and Rock Island ($310m) out, their CR-051 cost ($154m) in; the second units at `col2_cost` = 0.4 of a new plant ($290m out); the Columbia–Sierra line added ($60m, 1920–24, which the energy workbook does not cost). The five dams stay inside H, shown separately (AQ) so they are not added again. Then the atomic stations, the CR-054/055 works, public works and the rest of investment as a residual that must not be negative (a new check). | Energy link AL–AW |
| Financing power (R9) | The Treasury builds the Works' dams (Atomic); the Development Fund lends `en_dev_share` (0.35) of the rest within `en_df_max` × what it invests (inside the Fund's investment, not additional); **the power estate's bonds** finance its five dams, the second units and the line beyond the Fund's credit to it ($1.1bn issued, $960m outstanding in 1932, outside public debt); **the Reserve Bank buys half the estate's issues in 1930–32** (`rb_est`; $146m held in 1932), added to notes and bank reserves (Gold & money I); a new check tests the Treasury's and the estate's bonds against the market. | Energy link AX–BJ, Gold & money I, Checks AM–AN |

**Nothing is counted twice.** The CR-050 hall rows come out of Atomic!O (the weapon engineering, the security and the tests stay); the separation chain, the compacts and the dams are new Atomic columns inside its total cost (× `atom_scale`, as before) and reach Budget *Technical programmes*; Rock Island's sales reach *State enterprises*. The dams are investment in the account (government consumption now excludes Atomic AF as it excludes P), and the energy workbook's generic cost of the same dams is taken out of power investment. The 1921 research installation is the station's first pile. The uranium quantities are unchanged (the storyline quotes 5,800 t mined and 4,600 t in reserve); the piles' loading is inside the existing research and weapons buckets.

## Results, Story case (before the change in brackets)

| |1913|1920|1922|1924|1927|1929|1931|1932|
|---|---|---|---|---|---|---|---|---|
| Residents, end of year (m) |19.44 (19.45)|24.91|26.83 (26.84)|28.81|31.81|33.92|35.79|36.76|
| Core GDP ($m) |18,221 (18,236)|53,137 (53,130)|45,076 (45,129)|54,041 (54,171)|62,867 (63,070)|71,273 (71,516)|60,828 (61,033)|56,410 (56,592)|
| Real GDP (1913 $m) |18,221 (18,236)|25,920 (25,917)|28,529 (28,563)|33,358 (33,439)|39,789 (39,918)|44,546 (44,698)|41,606 (41,747)|41,115 (41,247)|
| Receipts ($m) |1,813 (1,815)|6,287 (6,286)|4,754 (4,760)|5,674 (5,684)|6,882 (6,898)|7,798 (7,817)|6,153 (6,169)|5,512 (5,525)|
| Technical programmes ($m) |163|585 (520)|550 (425)|607 (478)|611 (562)|705 (710)|640 (587)|599 (544)|
| Budget balance ($m) |374|1,695 (1,760)|937 (1,066)|1,215 (1,345)|1,734 (1,786)|1,937 (1,936)|545 (598)|266 (320)|
| Public debt ($m) |911 (912)|2,657 (2,656)|2,254 (2,256)|2,702 (2,709)|3,143 (3,153)|3,564 (3,576)|3,150 (3,149)|3,028 (3,014)|
| Reserve Fund ($m) |283|511 (516)|621 (640)|736 (769)|976 (1,023)|1,189 (1,236)|1,312 (1,363)|1,326 (1,381)|
| Development stock ($m) |3,862 (3,864)|8,250 (8,318)|9,160 (9,441)|10,899 (11,400)|14,155 (14,819)|17,109 (17,732)|17,701 (18,343)|17,343 (18,004)|
| Atomic programme, cost ($m) |8|150 (85)|180 (54)|165 (36)|93 (42)|103 (105)|120 (65)|110 (55)|
| Champions at home ($m) |829 (843)|2,626 (2,616)|2,856 (2,874)|3,471 (3,463)|4,236 (4,198)|4,707 (4,661)|3,518 (3,463)|3,237 (3,156)|
| … aluminium and aircraft ($m) |8 (28)|30 (60)|26 (80)|55 (100)|98 (145)|134 (180)|141 (133)|156 (110)|
| … electrochemistry and metals ($m) |6 (—)|41 (—)|37 (—)|52 (—)|85 (—)|93 (—)|49 (—)|36 (—)|
| Investment share of GDP |26%|27%|28%|28.4%|29%|28%|25%|24%|
| Power investment, counted once ($m) |170 (170)|517 (503)|825 (819)|870 (909)|1,123 (1,144)|1,084 (1,149)|598 (599)|695 (697)|
| Other investment / gross domestic investment |89%|89%|86%|87%|87%|87%|85%|84%|
| Power estate's bonds outstanding ($m) |26|186|249|285|537|731|843|960|
| … held by the Reserve Bank ($m) |0|0|0|0|0|0|78|146|
| Gold cover |0.75|0.41|0.55|0.52|0.46|0.46|0.54 (0.54)|0.56 (0.58)|
| Household consumption per person ($) |618 (619)|1,319 (1,321)|1,055 (1,059)|1,170 (1,176)|1,223 (1,229)|1,330 (1,335)|1,178 (1,183)|1,086 (1,091)|
| Checks failing |0|0|0|0|0|0|0|0|

The investment share is the adopted test path and does not move; power investment in brackets is the energy workbook's memo as before.

**The atomic programme over 1846–1932:** $1,247m in 1913 $ (was $678m), $1,957m current (was $1,047m), direct returns $210m (was $167m), net cost to the Treasury **$1,747m (was $881m)**; the peak is 0.41% of real GDP in 1921 (was 0.18%). Of the Works sheet's $761m (1913 $) for the separation chain, the halls' construction is $302m and their operation $229m; the dams add $94m and the compacts $20m.

**Reading the results.**
- **The money is in 1919–1926.** The halls are built in the dearest dollars of the period; the Budget surplus is $65–130m a year lower in 1920–24, and because the Development Fund invests most of every surplus, its stock is $0.6bn (3.5%) lower in 1929 and real GDP 0.34% lower. That is the whole GDP effect of CR-051: the model credits the programme with no spillovers.
- **The champions add little value, much power.** Aluminium's value added at 1920s prices is small ($39m in 1929 on 150 kt), so Champions!AO falls below its old, unexplained path in 1913–29 ($134m against $180m in 1929) and rises above it in 1931–32 ($156m against $110m), when the naval and air programme is the order book. The electrochemistry adds $93m in 1929, electric steel's premium half of it. Net, the champions at home are about 1% higher in the late 1920s and 2.6% higher in 1932.
- **1931 is a champions' bad year, not the Realm's.** The export third loses $5–6m of price a year in 1931–32, the rubber and hydrogenation works lose about $10m at world prices, the pool and the order book hold; champions' value added at home falls 25.3% from 1929 to 1931, against 25.7% in the old build.
- **Debt is practically unchanged** (+$14m in 1932): the Story case pays the Works from surpluses. The Reserve Fund is $55m lower in 1932.
- **The estate's bonds** are about 1.7% of GDP by 1932, the Reserve Bank's share of them $146m: gold cover in 1932 0.56 instead of 0.58, well above the rule.
- **Residents** are 36.76 million in 1932 in both builds (−1,066 people): the migration pull hardly feels a 0.3% GDP difference.

## Stress

Stress takes the halls at three times Y-12, `atom_scale` 1.5 (as before) and its own energy paths. Its atomic programme costs $308m in 1922 (was $80m) and its Budget is in deficit in 1922–24 (−$82m in 1922, was +$164m). Public debt is **$5.0bn in 1932 (was $3.4bn)**, the Development stock $1.35bn in 1929 (was $1.95bn), GDP 0.4% lower in 1929, residents unchanged (21.65m). Checks failing: 17 year-checks (was 12): the old ones (private saving capacity 1887 and 1914–20, the Siberian line 1918–19, the Japan FX buffer 1927, gold cover 1932), plus **private saving capacity in 1921–24** (the Treasury borrows to build the halls) and **debt over 30% of GDP in 1932** (30.0%). Stress is the lean case; the failures say that the halls at the top of CR-051's range with Stress's cost overrun are not affordable without borrowing in the early 1920s.

## The two workbooks together

The energy workbook reads this workbook's population, output, industry and the Fund's investment; it was rebuilt from each pass (its formulas unchanged) and iterated with this build to a fixed point: on the last pass the energy outputs moved by under one part in a million, and re-running `extract_finance.py` on this workbook reproduces `energy/build/finance_inputs.csv` to within 1e-6. This workbook was built last and not recalculated afterwards; Energy link A2 records the energy outputs it read. The energy workbook's results hardly move (electricity per person 2,614 kWh in 1929, was 2,617; the multiplier unchanged at 2.40–3.17); its Development Fund credit is smaller in the slump (Story $103m in 1932, was $126m) because the Fund invests less. `energy/build/export_energy.py` now also writes the CR-051/054/055 series this build reads (the strategic dams' capacity, the halls, the feed plant, the station, the diffusion plant, Rock Island's balance, the aluminium memo and the CR-054/055 quantities); the earlier columns are unchanged.

## Decisions for the author

1. **The halls' cost level.** Story 2.75 × Y-12 ($302m in 1913 $, about $520m current): 2.5 would be $275m, 3.0 $330m. `y12_build` ($110m in 1913 $) rests on Y-12's $0.48bn to 1946 and a construction-cost index, both to verify.
2. **Where the costs sit.** As built: the separation chain (halls, feed, station, breeder, diffusion) is government consumption, as CR-052's account already counts the halls; the Works' dams and Rock Island are investment built on the Treasury's account through the Atomic sheet, and their royalty a Budget cost. The alternative is a self-financing hydro company of the Works (its own bonds, power sold to the halls at cost), which would take about $154m out of the Budget in 1920–26 and put a capital charge into the halls' operation.
3. **The second units.** `col2_cost` 0.4 of a new plant's cost ($193m instead of $482m). The energy workbook still costs them in full in its own memo and check 6.
4. **The five dams' cost.** The energy workbook's generic rule ($160/kW plant + $110/kW lines and distribution) puts them at **$1.45bn current** in 1908–32, against CR-055 R9's "about $0.5bn". They are inside its power investment, counted once here, and not changed: lowering them is an energy-workbook change.
5. **The Reserve Bank's share** of the estate's slump issues (`rb_est` 0.5) and whether the estate's bonds carry a Treasury guarantee (none is modelled).
6. **Rubber and hydrogenation after the Stevenson scheme:** about $10m a year lost at world prices in 1931–32; who bears it (the fleet's contracts, the champion, a subsidy) is open.
7. **Champions!AO before 1929** falls below the old path. The aircraft path ($95m in 1929, $125m in 1932) is a MODEL input; raise it if the air arm should weigh more.
8. **Stress:** accept the two new failures, or lower Stress's `halls_y12` to 2.5.

Not done, as asked: the industrial-output derivation (`ind_src` = 2), sector-specific prices, `asia_home` after 1915, a world oil-price response, Paths C, `halls_after`, the Development Fund's power share and the royalty's size (CR-052 F12). Also left: the arc plants' war nitrogen (inside munitions), carbide, chlorine and abrasives (inside Chemicals), the alumina refinery's ownership, and the five Columbia dams' royalties.

## Review

@REVIEW@
