# Workbook note, 5 November 2026: the dynamic layer (CR-056)

SHA-256 `a579fee526e9e23e45a06dcf3e98987a590c99c6662d7562f677f6746d5dc603`. Built on the CR-051/054/055 workbook (`cba70b31…`) by [`build/cr056_dynamics.py`](build/cr056_dynamics.py) from `energy/build/energy_outputs.csv` (energy workbook `89807a66…`, unchanged), recalculated in LibreOffice (68,494 formulas, no errors). Then [`build/cr056_layers.py`](build/cr056_layers.py) ran six recalculations (Story and Stress × `dyn_mode` 0, 1, 2) and wrote them, with the story tests, as values on a new `Layers` sheet. [`build/cr056_identity.py`](build/cr056_identity.py) confirms that at `dyn_mode` 0 the workbook reproduces every one of the 110,530 cells of `cba70b31…` exactly, in Story and in Stress; the only changed formulas are the six hooks. **Saved at `dyn_mode` 0: merging changes no figure the storyline quotes.** No canon fact changes. All amounts are MODEL.

**Authorization.** Author, 5 November 2026: "Can you please build the model described here?" (the handoff of 5 November). Then, on the design note ([dynamics-design-note.md](dynamics-design-note.md)): "either replace Paths!L after about 1900 with growth derived from capital, power and spillovers, or keep it as the frontier baseline and add the new channels on top. Then compare the result against Pacifica's own story, not against US history." Both are built, on one switch, so they can be compared. Whether "frontier baseline" keeps the design note's rule of counting only Pacifica's lead over the Union (Q1) is a question for you (decision 1); both readings are on a lever. The other recommendations (Q2–Q12) are applied.

**Revised after the fresh-context review.** The first build counted electricity twice in mode 2 (a term for kWh per person beside a capital stock that already holds the power plants), netted the Development Fund against factory drive rather than against the county grids it actually finances, left the extra women outside the labour force, compared services prices with US history instead of the modelled Union, and scored the §34 test on 1929 only. All five are corrected below, and so are the figures that depended on them. The two modes now add much less than the first draft reported (+2.1% and +0.5% in 1929, not +7.1% and +12.6%).

## What changed

| Item | How | Where |
| --- | --- | --- |
| The switch | `dyn_mode`: 0 = the accounting model; **1 = the channels on top of `Paths!L`**; **2 = from `dyn_start` (1900) `Paths!L` replaced by growth derived from capital and base progress**, with the same channels. `dyn_vs_us` (saved 1): in mode 1, C1 and C5 count only Pacifica's lead over the Union, because `Paths!L` already holds the Union's own electrification; 0 counts Pacifica's whole gain since 1900. Thirty-seven new levers. | Levers 408–444 |
| C1 Unit electric drive | `mfg share × el_kappa × (Pacifica's drive share two years earlier above el_thresh, less the Union's)`. `el_kappa` 0.8 (David 1990: about half of the 5-point 1919–29 acceleration of US manufacturing TFP; verified); `el_thresh` 0.45 (Devine's 53% in 1919, verified); the Union's drive share is Devine's Table 3 (verified). Not netted by the Fund: factories buy from the power estate and their own plants. **1.4% by 1929** (in 1927, the lagged year, Pacifica's drive share is 0.80 against the Union's 0.73). | Dynamics, into Economy J |
| C3 Spillovers | The Works' spending on magnets, vacuum and high voltage (the halls, half of diffusion) and on fluorine chemistry (the feed plant, half of diffusion) induces private R&D at `rd_eps` 0.5 (Moretti, Steinwender and Van Reenen: 5–6% per 10%; verified), accumulated at 15% depreciation; the electrical and chemical world shares rise by `rd_gamma` × ln(1 + induced stock / own stock), capped. **Electrical share +5.9% in 1929.** Patents as a memo. | Dynamics, into Champions AF and Z |
| C4 Farms | Electrically pumped acres (energy workbook, 2.6m in 1929) × `ag_va_acre` ($15) × (1 − the Fund's share, since the farm lines are county-grid credit), and half the Valley and Columbia nitrogen at 25 t of grain per t of N. **+0.13% by 1929.** | Dynamics, into Economy J |
| C5 Women's work | `w_lambda` 0.035 points of women's paid work per point of homes wired since 1900 (Vidart 2024: a quarter of the 1880–1940 rise; verified), less the Union's own wiring gain (mode 1), × (1 − the Fund's share). The extra women **join the labour force** (Labour B) and produce `w_rel` 0.58 of the average worker's output. **0.9 points more women in paid work than in the Union by 1929; +0.27% of output.** | Dynamics, into Economy J and Labour B |
| Mode 2 growth | `k_alpha` (0.3) × growth of capital per resident + `tfp_base` (1.0%, × `prod_factor`). Electricity has no term of its own: it is an input, the plants are in the capital stock, and unit drive is C1 (counted here from Pacifica's own position, since `tfp_base` is the pre-electric rate). The capital stock starts at `ky_0` (3.0) × real GDP in 1899 and adds gross domestic investment (the `inv_share` path × GDP, so investment becomes a driver) less `k_dep` (4%). Economy D keeps only the Fund's premium over the ordinary return (`dev_return − k_alpha × Y/K`, about 0.18). | Dynamics, into Economy C and D |
| C2 Prices (reported) | Relative prices against the modelled Union: a consumer deflator with 1917–19 budget weights, services and rent at (GDP per person against the Union)^(1 − `bs_theta`) (Balassa–Samuelson), a GDP deflator (households at the consumer ratio, government at the services ratio, investment and net exports at 1) for comparing real output, and technological-deflation series. Nominal GDP, the Budget and the checks are untouched. | Prices |
| C6, C7, C8 (reported) | The aircraft learning curve (Wright 1936); the slump decomposed, Pacifica's gap now against its own 1920s trend like the Union's; wages, hours (standard hours by real income against the Union, short time by the output gap), the Japan memo, the Union's lost business. | Dynamics |
| Life table | Benchmark years 1900–1932, for the active case and mode. | Life |
| Side by side | Six recalculations and the story tests, as values. | Layers |
| Energy export | `export_energy.py` also writes factory drive share, homes and homes wired, pumped acres, the power price, kWh a home and vehicles per person (and two series not yet read: industry's motors and the US's electricity per person). The new columns sit before the Stress block, so the old Stress columns move; every reader goes by header. The earlier columns, their values and the energy workbook are unchanged. | `energy/build/` |

**What is not counted twice.** The Fund-financed share of power (about 0.35) is netted out of the channels that ride on the county grids (C4's pumping, C5), because Economy D already pays those at `dev_return`; in mode 2 the Fund keeps only its premium, since its investment is in the capital stock. Mode 1 counts only Pacifica's lead in electric drive and wiring, because the frontier holds the Union's. Mode 2 has no electricity term beside capital. C3 works on two sectors' world shares, not on the champions' scale, so it does not overlap talent (Champions B). Women's extra work is not in the talent stock. Prices are reported only. The energy workbook reads the accounting case (design decision Q10), so the physical kilowatt-hours are not changed. The layer values them.

## Results, Story case (accounting · on top · derived)

| | 1913 | 1920 | 1929 | 1932 |
|---|---|---|---|---|
| Real GDP (1913 $m) | 18,217 · 18,261 · 16,563 | 25,911 · 26,203 · 24,419 | 44,487 · 45,433 · 44,704 | 41,054 · 41,905 · 43,506 |
| … against the accounting model | — · +0.2% · -9.1% | — · +1.1% · -5.8% | — · +2.1% · +0.5% | — · +2.1% · +6.0% |
| Trend growth per resident (before the slump and talent) | 2.17% · 2.17% · 1.84% | 1.58% · 1.58% · 2.05% | 2.53% · 2.53% · 2.66% | 0.18% · 0.19% · 1.63% |
| Growth of real GDP per resident, actual | 1.89% · 1.92% · 1.56% | 1.22% · 1.38% · 2.35% | 2.54% · 2.56% · 3.21% | -3.73% · -3.60% · -2.28% |
| GDP per person × US history (Economy R) | 2.29 · 2.30 · 2.12 | 2.42 · 2.45 · 2.34 | 2.38 · 2.42 · 2.45 | 3.17 · 3.23 · 3.44 |
| GDP per person × the modelled Union (money) | 2.49 · 2.49 · 2.30 | 2.68 · 2.71 · 2.58 | 2.73 · 2.78 · 2.79 | 4.02 · 4.10 · 4.33 |
| GDP prices × the Union | 1.15 · 1.15 · 1.14 | 1.17 · 1.18 · 1.16 | 1.17 · 1.18 · 1.18 | 1.30 · 1.30 · 1.32 |
| Consumer prices × the Union | 1.18 · 1.18 · 1.16 | 1.21 · 1.21 · 1.20 | 1.21 · 1.21 · 1.21 | 1.33 · 1.33 · 1.35 |
| Consumption per person × US, at Union consumer prices | — · — · — | — · — · — | 1.73 · 1.76 · 1.78 | 2.09 · 2.13 · 2.23 |
| Average earnings ($) | 1,255 · 1,253 · 1,154 | 2,821 · 2,836 · 2,693 | 2,758 · 2,798 · 2,798 | 2,074 · 2,103 · 2,218 |
| Hours a week (Union 55.5, 51.2, 50.6, 38.4) | 49.4 · 49.4 · 49.9 | 45.2 · 45.2 · 45.4 | 44.6 · 44.5 · 44.5 | 37.8 · 37.7 · 37.4 |
| Women in paid work above the Union (points) | — · 0.7% · 0.7% | — · 1.1% · 1.1% | — · 0.9% · 0.9% | — · 0.8% · 0.8% |
| … the driver, net of the Fund (points) | — · 0.5% · 0.7% | — · 0.7% · 1.3% | — · 0.6% · 1.9% | — · 0.5% · 2.0% |
| Unit drive C1 · farms C4 · women C5 (level, mode 1) | 0.0% · 0.1% · 0.2% | 0.7% · 0.1% · 0.3% | 1.4% · 0.1% · 0.3% | 1.3% · 0.1% · 0.2% |
| Residents, end of year (m) | 19.44 · 19.45 · 19.06 | 24.91 · 24.93 · 24.28 | 33.91 · 33.99 · 33.08 | 36.75 · 36.86 · 35.90 |
| Public debt ($m) | 911 · 913 · 828 | 2,656 · 2,686 · 2,503 | 3,559 · 3,635 · 3,576 | 3,036 · 3,094 · 3,118 |
| Budget balance ($m) | 374 · 374 · 341 | 1,680 · 1,700 · 1,572 | 1,921 · 1,960 · 1,922 | 238 · 246 · 251 |
| Development stock ($m) | 3,862 · 3,865 · 3,658 | 8,231 · 8,298 · 7,518 | 16,929 · 17,190 · 16,238 | 17,132 · 17,404 · 16,551 |
| Checks failing | 0 · 0 · 0 | 0 · 0 · 0 | 0 · 0 · 0 | 0 · 0 · 0 |

Debt rises with GDP because the standing debt (`debt_floor` × GDP) does; the Budget is in surplus throughout.

**Reading the results.**
- **Mode 1 adds about 2% by 1929.** Unit drive gives 1.4% (Pacifica's lead in drive share is seven points, not the 35 points above the threshold the first build counted), women's work 0.27%, the farms 0.13%; the electrical share's rise adds about $50m of champions' value added, including the scale feedback. The rest is the workbook's own feedback (receipts, the Fund, talent and migration). That is about four times what the separation chain took away (−0.47%). Residents in 1932 are 36.86m (+0.10m).
- **With `dyn_vs_us` 0** (Pacifica's whole electrification on top of the frontier) mode 1 adds +9.0% in 1929 (48,494), with residents 37.05m in 1932 (+0.29m, just under your flag) and real output at Union prices 1.04× the Union's in 1929: this is the first build's reading, now with the other corrections.
- **Mode 2 is slower before the war and faster after it, and ends near the accounting model.** Capital per resident barely grows while arrivals run at 4–5% a year, so 1900–13 growth is well below `Paths!L` plus the Fund: real output is 9.1% lower in 1913 and 5.8% lower in 1920. It catches up in the 1920s, when unit drive (7.6%, counted from Pacifica's own position) and capital deepening add up: +0.5% in 1929. In the slump it keeps accumulating capital while `Paths!L` stops, so it is 6.0% higher in 1932. Residents in 1932 are 35.90m (−0.85m), beyond your 0.3m flag: fewer prosperous years before 1914 mean fewer arrivals. The result leans on `ky_0`: at 2.5 instead of 3.0, 1929 real output is +8.7% (48,365) against the accounting model.
- **Trend and actual growth differ in the slump.** The "trend" row is Economy E, before the output gap and talent; actual growth of real GDP per resident in 1932 is −3.7% (mode 0), −3.6% and −2.3%.
- **The atomic programme's cost** in 1913 dollars does not move (§33's $1.4bn). Its 1921 peak stays 0.45% of national product in mode 1; mode 2 makes it 0.48%, because 1921 output is lower.

## Against Pacifica's own story (Story case)

"Fails": a sentence of the story no longer fits. "Re-sync": a MODEL figure in the storyline to update.

| The storyline says | Accounting (0) | On top (1) | Derived (2) |
|---|---|---|---|
| "about 37 million" in 1932 (MODEL); flag a move above 0.3m | 36.75m · holds | 36.86m (+0.10m) · holds | 35.90m (−0.85m) · re-sync |
| output per person "about 2.24 times" in 1929 (§33; Economy R, against US history, as in CR-031); within 10% | 2.38× · holds | 2.42× · holds | 2.45× · holds |
| "the Union remains larger in real output" in 1932 (§34; at Union GDP prices) | 1929 0.97×, **1932 1.35×** · fails | 0.99×, 1.38× · fails | 0.96×, 1.39× · fails |
| "in 1932 money income briefly puts Pacifica alone ahead" (§34) | **ahead from 1924** · fails | from 1924 · fails | from 1927 · fails |
| "a milder crash than the Union, without escaping collapsing trade" (Union real GDP 1932/1929 about 0.75) | 0.923; per resident 0.850 · holds | 0.922; 0.849 · holds | 0.973; 0.895 · holds |
| "a champion has a bad year; the Realm does not" | champions 0.75, GDP 0.85 (1931/1929) · holds | 0.75, 0.85 · holds | 0.75, 0.89 · holds |
| Pacificans "visibly better off" (consumption per person × US at Union consumer prices, 1929) | 1.73× · holds | 1.76× · holds | 1.78× · holds |
| the atomic peak "0.45 percent of national product, in 1921" (§33, MODEL) | 0.45% · holds | 0.45% · holds | 0.48% · re-sync |
| "about 2,600 kilowatt-hours a head in 1929" | 2,614 · holds | 2,608 · holds | 2,680 · holds |
| "Pacifica raises neither tariffs nor taxes; reserves and borrowing fund the response" | surplus, debt 5% of GDP · holds | holds | holds |
| the workbook's checks | none fail | none fail | none fail |

**The accounting model already departs from §34.** Pacifica's money output passes the Union's in 1924 (1.00×, then 1.04× in 1925), not "briefly" in 1932, and its real output at Union prices passes the Union's in 1930 (1.04×; 1.14× in 1931; 1.35× in 1932), so "the Union remains larger in real output" is false of 1932 in every mode. Both come from the Union's collapse in the model (its money output halves from 1929 to 1932) more than from Pacifica's growth. The layer neither causes nor cures this. The storyline's "2.24 times" holds on the measure it was taken from (Economy R, 2.38×); against the modelled Union it is 2.73× in money and 2.32× at Union GDP prices.

Two cautions on the tests. The crash test is on total real GDP; per resident the fall is 15% (mode 0), 15% (mode 1) and 10% (mode 2), so mode 2 makes the crash about two thirds as deep, not absent. The champions test is lenient: real GDP per resident falls 12% from 1929 to 1931 in mode 0, which sits awkwardly beside "the Realm does not".

**What fits the story best.** Mode 1 keeps every test the accounting model keeps and changes no storyline figure beyond rounding. Mode 2 moves residents by 0.85m and the atomic peak to 0.48%, slows the 1900s and softens the crash.

## The slump: what explains the milder crash

The Union is 31% below its trend in 1932 (BEA's real GDP against a 2.5% trend). Measured the same way, against its 1920–29 growth, Pacifica's real output is 22.9% below (mode 0; 21% per resident). The first build measured Pacifica against the model's own trend, which is flat in 1930–32, and so overstated the difference. The layer asks how much of the 8-point difference the investment programmes explain. **None of it.** On the energy workbook's paths, power investment falls by half from 1929 to 1931 ($1.04bn to $0.54bn); aircraft output rises from $95m to $125m, but the navy bill falls from $183m to $173m. Together they run slightly *below* their 1929 share of GDP, so demand closes −0.1 points. About 8 points rest on prices, money and banks: the gold lent rather than hoarded, the lender of last resort, `slump_price` 0.6. That is what canon's §34 already says of the Reserve Bank. It is not what CR-054's "the naval and air programme … is the order book" suggests, unless that refers to the champions alone (where it is true).

## Life in Pacifica (Story, mode 1)

| | 1900 | 1913 | 1920 | 1924 | 1929 | 1932 |
|---|---|---|---|---|---|---|
| Average earnings, Pacifica ($) | 726 | 1,253 | 2,836 | 2,509 | 2,798 | 2,103 |
| Average earnings, Union ($) | 409 | 558 | 1,180 | 1,129 | 1,195 | 941 |
| … Pacifica / Union, at Union prices | 1.55 | 1.90 | 1.98 | 1.84 | 1.94 | 1.68 |
| Family income, with a working wife's chance ($) | 749 | 1,313 | 3,002 | 2,670 | 3,000 | 2,259 |
| A kWh at home (cents) | 9.1 | 6.0 | 8.2 | 5.6 | 4.5 | 3.8 |
| A basic car ($) | 650 | 550 | 525 | 295 | 450 | 460 |
| A gallon of motor fuel (cents) | 14 | 15 | 27 | 19 | 19 | 16 |
| A pound of bread (cents) | 4.5 | 5.6 | 11.4 | 8.7 | 8.7 | 6.9 |
| A quart of milk (cents) | 6.0 | 8.9 | 16.6 | 13.5 | 14.2 | 10.5 |
| A haircut (cents) | 22 | 39 | 82 | 83 | 83 | 81 |
| A cinema ticket (cents) | 7 | 16 | 41 | 42 | 58 | 51 |
| A radio set ($) | — | — | — | 90 | 108 | 45 |
| A car (hours of work) | 2,419 | 1,084 | 418 | 263 | 358 | 412 |
| A month's power for a wired home (hours) | 6.2 | 3.3 | 3.3 | 4.2 | 5.0 | 5.7 |
| A haircut (hours) | 0.82 | 0.78 | 0.66 | 0.74 | 0.66 | 0.73 |
| A radio (hours) | — | — | — | 80 | 86 | 40 |
| Homes wired, Pacifica / Union | 9% / 5% | 44% / 17% | 72% / 35% | 86% / 50% | 96% / 68% | 97% / 70% |
| kWh a wired home | 220 | 330 | 600 | 1,000 | 1,700 | 2,000 |
| Homes with a radio · washer · refrigerator | 0% · 0% · 0% | 0% · 0% · 0% | 0% · 10% · 0% | 9% · 17% · 1% | 49% · 34% · 7% | 76% · 35% · 18% |
| Food's share of the budget | 31% | 30% | 29% | 29% | 29% | 26% |
| Motor vehicles per home, Pacifica / Union | 0.00 / 0.00 | 0.10 / 0.06 | 0.57 / 0.37 | 0.95 / 0.65 | 1.27 / 0.90 | 1.27 / 0.80 |
| Hours a week, Pacifica / Union | 54.0 / 59.6 | 49.4 / 55.5 | 45.2 / 51.2 | 44.8 / 50.9 | 44.5 / 50.6 | 37.7 / 38.4 |
| Housework hours a week, Pacifica / Union | 57 / 58 | 50 / 54 | 46 / 51 | 45 / 50 | 45 / 48 | 44 / 47 |
| Women in paid work, Pacifica / Union | 20.6% / 20.6% | 22.7% / 22.0% | 24.8% / 23.7% | 25.1% / 24.0% | 25.6% / 24.7% | 25.8% / 25.0% |
| Married women in paid work, Pacifica | 5.6% | 8.2% | 10.1% | 11.1% | 12.4% | 12.8% |

**What the page can say.**
- **Goods cheap, people's time dear.** A Pacifican earns about 1.9 times the Union's wage at Union prices; this is an upper bound, because earnings are labour's share of output per worker including mining and oil. A car costs 358 hours of work in 1929, a radio 86. A haircut or a cinema ticket costs about 1.7 times what it does in the Union.
- **Power gets cheaper, homes use more of it.** The price of a kilowatt-hour falls by half against the price level from 1913 to 1929, but a month's power takes more hours of work because a wired home uses five times as much: it cooks and heats water electrically.
- **A shorter week.** Pacificans work about 44½ hours a week in the late 1920s against the Union's 51: the Saturday half-day.
- **1932.** Both work about 38 hours, Pacificans because their week is shorter, the Union's workers because of short time.
- **Somewhat more women at work.** About one more woman in a hundred works for pay than in the Union by 1929: the Union's own wiring already carries most of electrification's effect. Married women's paid work is 12.4% against 11.5% (this assumes about three fifths of the extra workers are married, as married women are about three fifths of women).
- **Household appliances.** By 1929 half of Pacifica's homes have a radio and a third an electric washer; refrigerators are still rare.

Every US anchor in this table is marked on the `Dynamics` and `Prices` sheets. Verified: manufacturing hours 1900–1929 (Census of Manufactures, Whaples), factory drive shares (Devine) and homes wired in 1930. **To verify:** earnings, prices, women's work, appliances, housework.

## Stress

Stress takes the low end of each range (`el_kappa` 0.5, `rd_eps` 0.3, `w_lambda` 0.02, `tfp_base` 1.0% × `prod_factor` 0.75). In Stress Pacifica's factories electrify more slowly than the Union's, so with `dyn_vs_us` 1 unit drive is negative (−0.7% in 1929) and mode 1 is −0.3% in 1929; mode 2 is −5.7%. Residents in 1932 are 21.65m and 21.12m (21.64m). Mode 1 fails the same 17 year-checks as the accounting model; mode 2 adds two in 1932 (private saving capacity, interest within 15%). Stress is not meant to match the story, and its story tests are reported on `Layers` only for completeness.

## The two workbooks

The energy workbook is unchanged and reads the accounting case (Q10). The dynamic modes value the same kilowatt-hours rather than demanding more. At mode 1's residents the energy workbook's 1929 electricity is 2,608 kWh a head, so the storyline's "about 2,600" holds without re-iterating. If you adopt a mode, the energy workbook can then read it and the pair iterates as usual.

## Decisions for the author

1. **How to read "keep it as the frontier baseline and add the new channels on top".** If `Paths!L` is the Union-pace frontier with the Union's electrification inside it (the design note's Q1), mode 1 counts only Pacifica's lead: +2.1% in 1929 (`dyn_vs_us` 1, saved). If you meant every channel on top of the frontier in full, mode 1 is +9.0% (`dyn_vs_us` 0), which credits the Union's own electrification to Pacifica a second time. I recommend 1.
2. **Which mode, if any, becomes the Story case.** I recommend mode 1 with `dyn_vs_us` 1: it keeps every test the accounting model keeps and moves no storyline figure. Mode 2 is the growth-accounting answer to your first option. Without the double-counted electricity it ends near the accounting model in 1929, after a slower 1900s and before a softer slump, and it moves residents by −0.85m; it also rests on an uncertain starting capital ratio. Until you choose, the workbook stays at mode 0.
3. **§34, independent of this layer.** In the accounting model Pacifica's money output passes the Union's in 1924 and its real output at Union prices in 1930, so "in 1932 money income briefly puts Pacifica alone ahead; the Union remains larger in real output" fails in every mode. Either the sentences are amended (for example: Pacifica's money income passes the Union's in the mid-1920s, and in the slump it passes in real output too), or the Union's modelled collapse is revisited. These are canon decisions, so the layer only reports them.
4. **The slump.** On the current power paths the investment programmes explain none of the milder crash; about 8 points rest on the Reserve Bank. Keep that (it matches §34). Or make the power estate countercyclical: hold its 1930–32 investment up in the energy workbook, financed by the estate's bonds and the Reserve Bank's purchases that already exist.
5. **The life table's US anchors** (to verify before any figure goes on the page): earnings, CPI, prices, women's work, appliances, housework.

## Known limits

- C3 treats the Works' halls, feed plant and diffusion spending as public R&D. It is production spending, and the public-to-private ratio (about 10 in 1920) is far outside the range the elasticity was estimated on. The effect is small (the electrical share +5.9%).
- Real output against the Union uses a GDP deflator built from the consumer ratio; investment goods are taken at the Union's price.
- Consumption "at Union consumer prices" divides a ratio against US history by a price ratio against the modelled Union.
- The Prices sheet's "1913 Pacifican prices" consumption series mixes Pacifica's GDP price level with the consumer ratio; it is reported only and not quoted here.

## Not done

Out of scope, as the handoff says:
- a world oil-price response;
- Paths C;
- `halls_after`;
- `asia_home` after 1915;
- the Fund's power share and the royalty (CR-052 F12);
- the Columbia dams' royalties.

Also not done:
- **Sector prices in the nominal accounts** (option B): prices are reported only, so the gold-standard story's price effects are not in the Budget or debt.
- **Civil aviation as an output line.**
- **A commute measure.** No anchor; the life table gives vehicles per home.
- **Japan's GDP.** The Concord pool is a memo only.
- **The population model (`population/`)**, which is not re-run.
