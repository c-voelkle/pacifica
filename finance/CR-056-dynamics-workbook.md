# Workbook note, 5 November 2026: the dynamic layer (CR-056)

SHA-256 `0a9d3ed4a1f9e59f6e47b9511c26a054a8b1a7826ea754c013ad5458ae07b179`. Built on the CR-051/054/055 workbook (`cba70b31…`) by [`build/cr056_dynamics.py`](build/cr056_dynamics.py) from `energy/build/energy_outputs.csv` (energy workbook `89807a66…`, unchanged), recalculated in LibreOffice (67,884 formulas, no errors). Then [`build/cr056_layers.py`](build/cr056_layers.py) ran six recalculations (Story and Stress × `dyn_mode` 0, 1, 2) and wrote them, with the story tests, as values on a new `Layers` sheet. [`build/cr056_identity.py`](build/cr056_identity.py) confirms that the saved workbook at `dyn_mode` 0 reproduces every one of the 110,530 cells of `cba70b31…` exactly; the only changed formulas are the five hooks. **Saved at `dyn_mode` 0: merging changes no figure the storyline quotes.** No canon fact changes. All amounts are MODEL.

**Authorization.** Author, 5 November 2026: "Can you please build the model described here?" (the handoff of 5 November). Then, on the design note ([dynamics-design-note.md](dynamics-design-note.md)): "either replace Paths!L after about 1900 with growth derived from capital, power and spillovers, or keep it as the frontier baseline and add the new channels on top. Then compare the result against Pacifica's own story, not against US history." Both are built, on one switch, so they can be compared. The design note's rule of counting only Pacifica's lead over the Union is withdrawn by that direction; its other recommendations are applied (Q2–Q12 as recommended, with Q1 replaced by the two modes).

## What changed

| Item | How | Where |
| --- | --- | --- |
| The switch | `dyn_mode`: 0 = the accounting model; **1 = the channels on top of `Paths!L`** (each counted from Pacifica's own 1900 position); **2 = from `dyn_start` (1900) `Paths!L` replaced by growth derived from capital, power and base progress**, with the same channels. Thirty-seven new levers. | Levers 408–444 |
| C1 Unit electric drive | `mfg share × el_kappa × (drive share two years earlier − el_thresh) × (1 − the Fund's share of power investment)`, a level on output per resident. `el_kappa` 0.8 (David 1990: about half of the 5-point 1919–29 acceleration of US manufacturing TFP; verified); `el_thresh` 0.45 (the gain waited for unit drive: Devine's 53% in 1919, verified). Netted by the Fund's share (Energy link AZ/AP, about 0.35) because Economy D already pays those kilowatts. **4.9% by 1929.** | Dynamics, into Economy J |
| C3 Spillovers | The Works' spending on magnets, vacuum and high voltage (the halls, half of diffusion) and on fluorine chemistry (the feed plant, half of diffusion) induces private R&D at `rd_eps` 0.5 (Moretti, Steinwender and Van Reenen: 5–6% per 10%; verified), accumulated at 15% depreciation; the electrical and chemical world shares rise by `rd_gamma` × ln(1 + induced stock / own stock), capped. **Electrical share 0.240 → 0.254 in 1929; chemicals +0.6%.** Patents as a memo. | Dynamics, into Champions AF and Z |
| C4 Farms | Electrically pumped acres (energy workbook, 2.6m in 1929) × `ag_va_acre` ($15) and half the Valley and Columbia nitrogen at 25 t of grain per t of N. **+0.16% by 1929.** | Dynamics, into Economy J |
| C5 Women's work | `w_lambda` 0.035 points of women's paid work per point of homes wired since 1900 (Vidart 2024: a quarter of the 1880–1940 rise; verified) × women of working age × `w_rel` 0.58 / `lf_rate`. **Three more points of women in paid work by 1929; +1.4% of output.** `lf_rate` itself is unchanged. | Dynamics, into Economy J |
| Mode 2 growth | `k_alpha` (0.3) × growth of capital per resident + `e_alpha` (0.03) × growth of electricity per person + `tfp_base` (1.0%, × `prod_factor`). The capital stock starts at `ky_0` (3.0) × real GDP in 1899 and adds gross domestic investment (the `inv_share` path × GDP, so investment becomes a driver) less `k_dep` (4%). The Fund's investment is in the capital stock, so Economy D keeps only its premium over the ordinary return (`dev_return − k_alpha × Y/K`, about 0.18). | Dynamics, into Economy C and D |
| C2 Prices (reported) | Relative prices against the Union, a consumer deflator with 1917–19 budget weights, services and rent at (income lead)^(1 − `bs_theta`) (Balassa–Samuelson), and technological-deflation series. Nominal GDP, the Budget and the checks are untouched. | Prices |
| C6, C7, C8 (reported) | The aircraft learning curve (Wright 1936); the slump decomposed (demand against money and banks); wages, hours (standard hours by income, short time by the output gap), the Japan memo, the Union's lost business. | Dynamics |
| Life table | Benchmark years 1900–1932, for the active case and mode. | Life |
| Side by side | Six recalculations and the story tests, as values. | Layers |
| Energy export | `export_energy.py` also writes factory drive share, homes and homes wired, pumped acres, the power price, kWh a home, vehicles per person and the US's electricity per person. The earlier columns and the energy workbook are unchanged. | `energy/build/` |

**Nothing is counted twice.** The Fund-financed share of power is netted out of C1 (mode 1), and in mode 2 the Fund keeps only its premium, since its investment is already in the capital stock. C3 works on two sectors' world shares, not on the champions' scale, so it does not overlap talent (Champions B). Women's extra work is not in the talent stock. Prices are reported only. The slump is decomposed, not stabilized further. The energy workbook reads the accounting case (design decision Q10), so the physical kilowatt-hours are not changed. The layer values them.

## Results, Story case (accounting · on top · derived)

| | 1913 | 1920 | 1929 | 1932 |
|---|---|---|---|---|
| Real GDP (1913 $m) | 18,217 · 18,333 · 17,638 | 25,911 · 26,538 · 26,720 | 44,487 · **47,633** · **50,102** | 41,054 · 44,277 · 48,975 |
| … against the accounting model | — · +0.6% · −3.2% | — · +2.4% · +3.1% | — · **+7.1%** · **+12.6%** | — · +7.9% · +19.3% |
| Growth of output per resident | 2.17% · 2.17% · 2.13% | 1.58% · 1.59% · 2.34% | 2.53% · 2.53% · 2.88% | 0.18% · 0.19% · 1.69% |
| GDP per person × the Union (money) | 2.49 · 2.50 · 2.42 | 2.68 · 2.75 · 2.79 | 2.73 · 2.92 · 3.08 | 4.02 · 4.33 · 4.81 |
| Consumer prices × the Union | 1.16 · 1.16 · 1.15 | 1.18 · 1.19 · 1.19 | 1.17 · 1.18 · 1.20 | 1.25 · 1.27 · 1.30 |
| Consumption per person × US, at Union prices | | | 1.79 · 1.88 · 1.96 | 2.22 · 2.35 · 2.54 |
| Average earnings ($) | 1,255 · 1,262 · 1,223 | 2,821 · 2,887 · 2,934 | 2,758 · 2,944 · 3,120 | 2,074 · 2,225 · 2,475 |
| Hours a week (Union 55.5, 51.2, 50.6, 38.4) | 50.1 · 50.0 · 50.2 | 46.0 · 45.8 · 45.8 | 45.5 · 45.1 · 44.8 | 38.9 · 38.6 · 38.1 |
| Extra women in paid work (points) | — · 1.1 · 1.1 | — · 2.1 · 2.1 | — · 3.0 · 3.0 | — · 3.1 · 3.1 |
| Residents, end of year (m) | 19.44 · 19.46 · 19.29 | 24.91 · 24.94 · 24.71 | 33.91 · 34.08 · 33.88 | **36.75 · 37.01 · 36.86** |
| Public debt ($m) | 911 · 917 · 882 | 2,656 · 2,720 · 2,739 | 3,559 · 3,811 · 4,008 | 3,036 · 3,252 · 3,483 |
| Budget balance ($m) | 374 · 376 · 362 | 1,680 · 1,726 · 1,740 | 1,921 · 2,044 · 2,136 | 238 · 264 · 299 |
| Development stock ($m) | 3,862 · 3,873 · 3,787 | 8,231 · 8,378 · 8,299 | 16,929 · 17,673 · 18,034 | 17,132 · 17,945 · 18,427 |
| Checks failing | 0 · 0 · 0 | 0 · 0 · **1** | 0 · 0 · 0 | 0 · 0 · 0 |

Debt rises with GDP because the standing debt (`debt_floor` × GDP) does; the Budget is in surplus throughout.

**Reading the results.**
- **Mode 1 adds about 7% by 1929**, almost all of it from unit drive (4.9%) and women's work (1.4%). The farms add little (0.16%), and the electrical share's rise adds about $75m of champions' value added. The rest is the workbook's own feedback (receipts, the Fund, talent and migration). That is roughly fifteen times what the separation chain took away (−0.47%).
- **Mode 2 adds about 13% by 1929 and 19% by 1932, but it is lower before 1914** (−3% in 1913). Capital per resident barely grows while arrivals run at 4–5% a year, so 1900–13 growth (1.97% a year) is below `Paths!L` plus the Fund (2.2%). Mode 2 then grows faster in the war (2.1% against 1.4%: the war takes capital abroad but investment stays 22–24% of GDP) and in the slump (2.1% against 0.5%), because capital keeps accumulating while `Paths!L` stops. In mode 2 the 1930–32 trend keeps rising under the slump.
- **Residents** in 1932: 37.01m (mode 1, +0.25m) and 36.86m (mode 2, +0.11m), both under your 0.3m flag. Mode 2 draws fewer arrivals before 1914 and more after.
- **The atomic programme's cost** in 1913 dollars does not move (§31's $1.4bn). Its 1921 peak is 0.44% of national product in both modes, against 0.45%.

## Against Pacifica's own story (Story case)

| The storyline says | Accounting (0) | On top (1) | Derived (2) |
|---|---|---|---|
| "about 37 million" in 1932 (MODEL); flag a move above 0.3m | 36.75m · holds | 37.01m (+0.25m) · holds | 36.86m (+0.11m) · holds |
| output per person "about 2.24 times the Union's in 1929" (§33, CR-021 comparison) | 2.73× money, 2.33× at Union prices · holds | 2.92×, 2.47× · moves | 3.08×, 2.57× · moves |
| "the Union remains the larger power in real output"; "in 1932 money income briefly puts Pacifica alone ahead" | real 1929 0.97×; money 1932 1.75× · holds | real 1929 **1.03×** · fails | real 1929 **1.06×** · fails |
| "a milder crash than the Union, without escaping collapsing trade" | real GDP 1932/1929 0.923 · holds | 0.930 · holds | **0.978** · holds, barely |
| "a champion has a bad year; the Realm does not" | champions 0.75, GDP 0.85 (1931/1929) · holds | 0.75, 0.86 · holds | 0.75, 0.89 · holds |
| Pacificans "visibly better off" (consumption per person at Union prices, 1929) | 1.79× · holds | 1.88× · holds | 1.96× · holds |
| the atomic peak "0.45 percent of national product, in 1921" (§31) | 0.45% · holds | 0.44% · moves | 0.44% · moves |
| "about 2,600 kilowatt-hours a head in 1929" | 2,614 · holds | 2,601 · holds | 2,617 · holds |
| "Pacifica raises neither tariffs nor taxes; reserves and borrowing fund the response" | surplus, debt 5% of GDP · holds | holds | holds |
| the workbook's checks | none fail | none fail | gold cover 1920 fails |

**Two findings about the accounting model itself.** First, Pacifica's money output already exceeds the Union's in 1929 (1.13×), against the storyline's "in 1932 money income briefly puts Pacifica alone ahead". The sentence holds only in real terms at Union prices (0.97×). Second, the storyline's "2.24 times the Union's" per person (an earlier CR-021 comparison) is 2.73× in money in the current workbook, or 2.33× at Union prices. Neither is caused by this layer.

**What fits the story best.** Mode 1 keeps every test the accounting model keeps except two. "The Union remains the larger power in real output" fails narrowly (1.03× in 1929, at Union prices). The §31 peak moves from 0.45% to 0.44%. Mode 2 moves further:
- the crash almost disappears (−2.2% from 1929 to 1932, against the storyline's "Pacifica is also hurt");
- gold cover fails in 1920;
- it makes the investment-share test path a driver.

## The slump: what explains the milder crash

The Union is 31% below its trend in 1932 and Pacifica 14%. The layer asks how much of that 17-point difference the investment programmes explain. **None of it.** On the energy workbook's paths, power investment falls by half from 1929 to 1931 ($1.04bn to $0.54bn). The naval and air order book ($95m to $125m) does not offset that. Together they run slightly *below* their 1929 share of GDP, so demand closes −0.1 points. All seventeen points rest on prices, money and banks: the gold lent rather than hoarded, the lender of last resort, `slump_price` 0.6. That is what canon's §34 already says of the Reserve Bank. It is not what CR-054's "the naval and air programme … is the order book" suggests, unless that refers to the champions alone (where it is true).

## Life in Pacifica (Story, mode 1)

| | 1900 | 1913 | 1920 | 1924 | 1929 | 1932 |
|---|---|---|---|---|---|---|
| Average earnings, Pacifica ($) | 726 | 1,262 | 2,887 | 2,594 | 2,944 | 2,225 |
| Average earnings, Union ($) | 409 | 558 | 1,180 | 1,129 | 1,194 | 940 |
| … Pacifica / Union, at Union prices | 1.55 | 1.95 | 2.06 | 1.94 | 2.09 | 1.87 |
| Family income, with a working wife's chance ($) | 749 | 1,325 | 3,072 | 2,784 | 3,191 | 2,420 |
| A kWh at home (cents) | 9.1 | 6.0 | 8.2 | 5.6 | 4.5 | 3.8 |
| A basic car ($) | 650 | 550 | 525 | 295 | 450 | 460 |
| A gallon of motor fuel (cents) | 14 | 15 | 27 | 19 | 19 | 16 |
| A pound of bread (cents) | 4.5 | 5.6 | 11.4 | 8.7 | 8.7 | 6.9 |
| A quart of milk (cents) | 6.0 | 8.9 | 16.5 | 13.5 | 14.2 | 10.5 |
| A haircut (cents) | 22 | 38 | 79 | 79 | 80 | 74 |
| A cinema ticket (cents) | 7 | 15 | 39 | 40 | 56 | 46 |
| A radio set ($) | — | — | — | 90 | 108 | 45 |
| A car (hours of work) | 2,425 | 1,090 | 417 | 259 | 345 | 399 |
| A month's power for a wired home (hours) | 6.2 | 3.3 | 3.3 | 4.1 | 4.9 | 5.6 |
| A haircut (hours) | 0.82 | 0.75 | 0.63 | 0.70 | 0.61 | 0.64 |
| A radio (hours) | — | — | — | 79 | 83 | 39 |
| Homes wired, Pacifica / Union | 9% / 5% | 44% / 17% | 72% / 35% | 86% / 50% | 96% / 68% | 97% / 70% |
| kWh a wired home | 220 | 330 | 600 | 1,000 | 1,700 | 2,000 |
| Homes with a radio · washer · refrigerator | — | — | 0 · 10% · 0 | 9% · 17% · 1% | 49% · 34% · 7% | 76% · 35% · 18% |
| Food's share of the budget | 31% | 30% | 29% | 29% | 29% | 27% |
| Motor vehicles per home, Pacifica / Union | 0 / 0 | 0.10 / 0.06 | 0.57 / 0.37 | 0.95 / 0.65 | 1.28 / 0.90 | 1.27 / 0.80 |
| Hours a week, Pacifica / Union | 54.2 / 59.6 | 50.0 / 55.5 | 45.8 / 51.2 | 45.5 / 50.9 | 45.1 / 50.6 | 38.6 / 38.4 |
| Housework hours a week, Pacifica / Union | 57 / 58 | 50 / 54 | 46 / 51 | 45 / 50 | 45 / 48 | 44 / 47 |
| Women in paid work, Pacifica / Union | 21% / 21% | 23% / 22% | 26% / 24% | 27% / 24% | 28% / 25% | 28% / 25% |
| Married women in paid work, Pacifica | 6% | 9% | 11% | 13% | 15% | 15% |

**What the page can say.**
- **Goods cheap, people's time dear.** A Pacifican earns about twice the Union's wage at Union prices. A car costs 345 hours of work in 1929, a radio 83. A haircut or a cinema ticket costs about 1.6 times what it does in the Union.
- **Power gets cheaper, homes use more of it.** The price of a kilowatt-hour halves against the price level from 1913 to 1929, but a month's power takes more hours of work because a wired home uses five times as much: it cooks and heats water electrically.
- **A shorter week.** Pacificans work about 45 hours a week in the 1920s against the Union's 51: the Saturday half-day.
- **1932.** Both work about 38½ hours, Pacificans because their week is shorter, the Union's workers because of short time.
- **More women at work.** Three more women in a hundred work for pay than in the Union by 1929. Married women's paid work is 15% against 12%.
- **Household appliances.** By 1929 half of Pacifica's homes have a radio and a third an electric washer; refrigerators are still rare.

Every US anchor in this table is marked on the `Dynamics` and `Prices` sheets. Verified: manufacturing hours 1900–1929 (Census of Manufactures, Whaples) and homes wired in 1930. **To verify:** earnings, prices, women's work, appliances, housework.

## Stress

Stress takes the low end of each range (`el_kappa` 0.5, `rd_eps` 0.3, `w_lambda` 0.02, `tfp_base` 1.0% × `prod_factor` 0.75). Real GDP in 1929 is +3.2% (mode 1) and +5.3% (mode 2); residents in 1932 are 21.69m and 21.54m (21.64m). The same 17 year-checks fail in every mode, and no new ones. Stress is not meant to match the story, and its story tests are reported on `Layers` only for completeness.

## The two workbooks

The energy workbook is unchanged and reads the accounting case (Q10). The dynamic modes value the same kilowatt-hours rather than demanding more. At mode 1's residents the energy workbook's 1929 electricity is 2,601 kWh a head, so the storyline's "about 2,600" holds without re-iterating. If you adopt a mode, the energy workbook can then read it and the pair iterates as usual. `energy_outputs.csv` gains the new columns; its earlier columns and its energy SHA line are unchanged.

## Decisions for the author

1. **Which mode, if any, becomes the Story case.** I recommend mode 1, because it keeps the story's tests except two.
   - **"The Union remains the larger power in real output"** fails by 3% in 1929. Tuning cannot keep it: even with unit drive switched off (`el_kappa` 0) mode 1 is 0.99×, at 0.5 it is 1.01×. Any second-order gain at all makes Pacifica's real output overtake the Union's by the late 1920s, so the sentence would be amended rather than the model tuned. It is already true only at Union prices.
   - **§31's 0.45% becomes 0.44%.**

   Mode 2 is the honest growth-accounting answer to your first option. It makes the 1900s slower, the war and the slump much faster, and the crash almost vanishes. If you prefer it, the slump would need a deeper `Paths!M` to keep "Pacifica is also hurt", and its gold-cover failure in 1920 would need settling. Until you choose, the workbook stays at mode 0.
2. **The slump.** On the current power paths the investment programmes explain none of the milder crash; the Reserve Bank explains all of it. Keep that (it matches §34). Or make the power estate countercyclical: hold its 1930–32 investment up in the energy workbook, financed by the estate's bonds and the Reserve Bank's purchases that already exist.
3. **The storyline's older figures, independent of this layer.** "2.24 times the Union's" per person (now 2.73× money, 2.33× at Union prices) and "in 1932 money income briefly puts Pacifica alone ahead" (money output is ahead from the 1920s; real output at Union prices only in 1932). These are canon decisions, so the layer only reports them.
4. **The life table's US anchors** (to verify before any figure goes on the page): earnings, CPI, prices, women's work, appliances, housework.

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
