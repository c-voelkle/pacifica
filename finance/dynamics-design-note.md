# Design note: a dynamic layer for the financial workbook (second- and third-order effects of the investments)

**Status:** superseded in part on 5 November 2026 by the author's direction to build both "replace `Paths!L` after about 1900 with growth derived from capital, power and spillovers" and "keep it as the frontier baseline and add the new channels on top", and to compare them with Pacifica's own story rather than with US history. The rule below of counting only Pacifica's lead over the Union (Q1) is withdrawn; the build and its results are in [CR-056-dynamics-workbook.md](CR-056-dynamics-workbook.md). Kept as the design record. Original status: PROPOSED for the author's approval, 5 November 2026. Written from the handoff of 5 November ("second- and third-order effects of Pacifica's investments"), the workbook at `cba70b31…` (`main` at `961ebae`), the energy workbook at `89807a66…`, `finance/investment-share-note.md` v2, `finance/CR-051-054-055-workbook.md`, `finance/CR-052-workbook.md` and `energy/CR-052-workbook.md`. Every amount the layer produces is MODEL. Anchors marked *verified* were checked in this session or in an earlier one; the rest are *to verify* during the build. CR number to assign (CR-056 is free); this layer changes no canon.

## 1. What the baseline already credits, and what that implies

Reading the formulas, not the descriptions:

- **Growth per resident** is `Paths!L` × `prod_factor` (Economy C) plus the Fund (Economy D = `dev_return` × last year's Development investment flow / last year's GDP, capped at `dev_cap`). `Paths!L` is 1.5% in 1896–1913, 0.8% in 1914–20 and 1.7% in 1921–29: about the Union's own historical growth per person. **I read `Paths!L` as frontier growth at the Union's pace, which already contains the Union's own electrification.** Please confirm (decision Q1); everything below depends on it.
- **The Fund already pays a 30% social return on power.** Its investment flow includes its power credit (Energy link AZ: $363m of the $1,959m it invests in 1929). So cheap power does feed back today, through D, by about 0.15 points of growth a year in the late 1920s. Only the privately financed two thirds of power investment earns nothing beyond `Paths!L`.
- **Talent** raises output per resident as a level (Labour AO, 9.2% in 1929) and the champions' scale (Labour AP → Champions B).
- **The level lead is not a physical story.** In 1929 Pacifica has 2.5 times the Union's real output per person. Its factory motors use 0.48 kWh per 1913 dollar of output against the Union's 0.87 (the energy workbook's `ind_w` = 0.5); even with the electrochemistry, the mill boilers and mining, its industrial power per dollar of output (about 0.95 kWh) is about the Union's. The baseline's 2.4× lead comes from the starting level, the Fund and talent, not from power. A channel that read power *intensity* against the Union would therefore add nothing or take output away.

**Consequence, and the rule I propose for every channel:** a channel counts only the *change since 1900 in Pacifica's physical lead over the Union* (drive share, wired homes, pumped acres and so on), so the Union-pace part stays in `Paths!L` and the pre-1900 level stays where it is. This keeps the layer honest and it keeps it small: my hand estimate is **+1–3% real GDP in 1929 in Story (mid about 2%)**, against the separation chain's −0.47%. The visible differences in daily life come mostly from prices and households (channels 2 and 5), not from GDP.

## 2. Architecture

- **One switch:** lever `dyn_on` (Levers, new block from row 407; Story and Stress columns as usual). 0 = the current model; 1 = the layer.
- **One touch on the existing model:** Economy J (non-mining GDP) gains one factor, `× (1 + dyn_on × Dynamics!<level>)`. At `dyn_on` = 0 this is `× 1`, bit-exact. Every other new formula sits on new sheets and is either reported or reaches GDP only through that factor. Revenue, the Fund's surpluses, migration, the champions' jobs and the Union's losses then move through the workbook's own wiring.
- **No circular references:** the level factor reads only last year's GDP, residents and Fund values, plus imported energy series (constants). Energy and finance iterate only through the scripts.
- **New sheets:** `Dynamics` (the channels, year by year, rows 6–92 like every sheet), `Prices` (sector prices, the consumer deflator), `Life` (the benchmark-year table) and `Layers` (the side-by-side results, written as values by the build script from four recalculations: Story and Stress, each with `dyn_on` 0 and 1).
- **New energy exports** (appended columns, no energy value changes): factory horsepower on electric drive (Uses E), homes and homes wired (P&O AE, Uses B), pumped acres, the average power price (`el_price`), factory motors' GWh, vehicles on the road per person, for Story and Stress.
- **Saved state:** the workbook is saved with `dyn_on` = 0, so every figure the storyline quotes is unchanged until you adopt the layer (Q9).
- **Test of the old path:** the build recalculates with `dyn_on` = 0 and compares every pre-existing cell with `cba70b31…`; the build fails on any difference. Formula count rises; no existing formula changes except Economy J.

## 3. The channels

Notation: year t; P = Pacifica, US = the Union's historical series; `gap(x)` = (x_P − x_US) at t − lag, minus the same in 1900. Parameters: Story mid / Stress low / range.

### C1 Electric drive (TFP in manufacturing) — recommended ON

`level₁ = mfg_share × el_kappa × gap(drive share) × (1 − fund_share)`

- Drive share: energy Uses E (P) against Devine (1983) Table 3 (US: 4.8% 1899, 24.7% 1909, 53.1% 1919, 78.4% 1929, *verified*, in the energy Anchors).
- `el_kappa` **0.8 / 0.5 / 0.5–1.1**. Anchor: David (1990, AER P&P) attributes about half of the roughly 5-point acceleration of US manufacturing TFP growth in 1919–29 (against 1909–19) to secondary electric motors (*verified*); with the drive share rising about 25 points that decade, the top of the range is about 1.1 per unit of share. Fiszbein, Lafortune, Lewis and Tessada (NBER w28076) find rapid, lasting labour-productivity gains with capital deepening and reorganization (qualitative here; magnitudes *to verify*).
- `el_lag` 2 years (factories are rebuilt around unit drive).
- `mfg_share`: manufacturing's share of output, a path (about 0.25 in the 1920s, *to verify* against the US national-income share).
- `fund_share` = the Fund's power credit / power investment, last year (Energy link AZ/AP, about 0.35): **the netting**, because D already pays the Fund-financed part (Q3).
- Pacifica's drive lead is only 4–6 points (0.84 against 0.78 in 1929), so C1 is about **+0.6–1.0% of GDP by 1929**.

**C1b, power per worker — recommended OFF.** In growth accounting the output elasticity of electricity is its cost share (about 0.02–0.04), and per unit of output Pacifica's factories use less power than the Union's (above). The power's productive weight is the reorganization C1 captures.

**C1c, capital deepening — recommended OFF.** Solow arithmetic: 28% investment against Kuznets's 20.6% (*verified*, note v2) raises steady-state output by at most about 18%, but Pacifica's population growth (about 3% a year against the Union's 1.5%) takes most of it back (net about +7%), and that lead is already in the baseline level since the 1880s. Only the change after 1913 (26% → 28%) would count, about +1%; and it would make the `inv_share` test path a driver, which you decided against (CR-052 decision 3).

### C2 Cheap power and relative prices — recommended ON, as a consumer deflator

For good j: `p_j,P = p_j,US (historical, current $) × rel_j`, and a consumer deflator `cpi_rel = Σ w_j × rel_j` that divides household consumption, wages and the life table. **Nominal GDP, the Budget, debt and every check are untouched** (option A). Option B would feed sector prices into the champions' nominal value added (note v2 item 3: nominal GDP, debt ratios, the gold story); I recommend leaving it for later (Q4).

- **Power:** `el_price` (energy, 1913 cents; 1.4 in 1929) against US average revenue (about 1.6 in 1913 money, *to verify*): rel about 0.85 for households; bulk power at `price_strat` 0.5 cents.
- **Power-intensive goods:** `rel = 1 + c_j × (rel_bulk − 1)`, with power's cost share c_j: aluminium 0.2–0.3, arc nitrogen about 0.5, Haber nitrogen about 0.1, steel about 0.02 (*to verify*). Aluminium, fertiliser and electric steel fall clearly; steel hardly.
- **Cars:** no anchor for a Pacifican advantage. Pacifica builds 2.2m a year against the Union's 5.3m, so scale argues for dearer cars, cheap fuel for cheaper motoring. Range 0.9–1.1, mid 1.0 for the car, motor fuel 0.8–1.0 (Q4).
- **Food:** from C4's yield gain, passed through at 0.5–1.0.
- **Services and rent (Balassa–Samuelson), the honesty term:** wages 2–2.5 times the Union's make haircuts, servants and rent dear. `rel_serv = (y_P / y_US)^(1 − θ)`, θ (services' productivity lead) 0.5 / 0.4 / 0.3–0.7. At θ = 0.5 services cost about 1.5 times the Union's.
- **Weights:** the BLS cost-of-living survey of 1917–19 (food about 0.38, housing 0.18, clothing 0.16, fuel and light 0.05, furnishings 0.05, the rest 0.18; *to verify*), with the car and appliances split out.
- **What it shows:** goods fall faster than the general index every year (the technological deflation), and against the Union goods are cheaper and services dearer. My estimate: household consumption per person at Union prices falls from 2.09× (nominal, 1929) to **about 1.6–1.9×** with the services term, or rises to 2.15–2.25× without it. Either way Pacificans are visibly better off; with the term, the page should show a cheap radio and an expensive maid.

### C3 Spillovers from the Works and the power programme — recommended ON, small

`induced R&D_j = ε_RD × the Works' spending in the bottleneck technologies` (vacuum, high voltage, magnets, fluorine: the halls, the feed plant, gaseous diffusion; Works sheet), accumulated with 15% depreciation; then the electrical (Champions AD) and chemical (Y) world shares rise as `share × (1 + γ × ln(1 + R_ind / R_base))`, capped.

- `ε_RD` **0.5 / 0.3 / 0.3–0.6**: Moretti, Steinwender and Van Reenen (*The Intellectual Spoils of War*) find a 10% rise in government-funded R&D brings a 5–6% rise in private R&D in the same industry (*verified*).
- γ 0.1 / 0.05 / 0.05–0.15 (output elasticity of R&D capital; Griliches's surveys, *to verify*); `R_base` = an R&D intensity × the sector's sales (about 2%, *to verify*); the electrical share capped at 0.30, chemicals at 0.20.
- Patents (Champions F) reported with the same factor. Learning-by-doing on the halls' own operation is reported, not credited.
- **Netting:** talent raises every champion's scale (Champions B); C3 enters only two sectors' world shares, through a different mechanism (procurement of bottleneck technology), so the two do not overlap. The shares AD and Y are CR-020 paths that predate CR-051, so they do not already assume the Works.
- About **+0.1–0.3% of GDP by 1929**: part of the separation chain's −0.47% comes back.

### C4 Agriculture — recommended ON

`Δfarm VA = extra pumped acres × (VA per irrigated acre − VA per dry acre) + farm nitrogen × yield response × crop price`

- Extra pumped acres: the energy workbook's `pump_acres` (3.6m in 1929, Story) minus the historical Pacific-states pumped acreage (Census of Irrigation 1920 and 1930, *to verify*).
- Value added per acre: California irrigated against dry farming (Census of Agriculture 1930, *to verify*).
- Valley nitrogen to farms: the share of CR-054's 90 kt not exported or used in industry, at a yield response of about 20–30 kg of grain per kg of N (*to verify*).
- `farm_share` path (the US agriculture share of national income, about a fifth in 1900 and a tenth in 1929, *to verify*; Pacifica's lower).
- **Land Fund:** the implied rise in farm value per acre is a memo; the Land Fund's prices are not moved (they follow "our timeline", and their mechanics are outside this layer).
- About **+0.1–0.4% of GDP by 1929**; food prices 2–5% below the Union's.

### C5 Households — recommended ON (women's work); hours reported, not a driver

`Δwomen's participation = λ × gap(wired share)`; `level₅ = Δparticipation × adult women / residents / lf_rate × rel_f`

- Wired homes: energy (96% in 1929) against the US (68% in 1930, *verified*; earlier years *to verify*).
- λ **0.035 / 0.02 / 0.02–0.08**. Anchor: Vidart (RES 2024) attributes a quarter of the 1880–1940 rise in US women's participation to electrification (*verified*), about 2.7 of roughly 11 points while wiring went from nothing to about 80%. The top of the range follows Greenwood, Seshadri and Yörükoğlu's "Engines of liberation" (RES 2005, *to verify*).
- `rel_f` 0.55–0.6, women's earnings relative to men's (Goldin, *to verify*).
- `lf_rate` itself stays 0.42 in the workbook (guest-worker permits and unemployment read it); the extra workers enter output and the life table only.
- About **+0.2–0.8% of GDP by 1929** and about one more point of women in paid work.
- **Hours** (reported): `h_P = h_US × (y_P / y_US)^(−ε_h)`, ε_h 0.15 / 0.1 / 0.1–0.25, against US manufacturing hours (about 59 in 1900, 48–50 in 1929, Whaples, *to verify*). At 0.15 Pacifica works about 43–44 hours in 1929: the Saturday half-day. As a driver it would take output away; I recommend reading the baseline's output as produced in those hours, i.e. a higher hourly productivity (Q5).
- **Housework, appliances, commuting:** reported in the life table. Housework from the Lebergott series cited by GSY (about 58 hours a week in 1900, *to verify*), shortened by the wiring gap; appliances as the US diffusion curves (radio, washer, refrigerator, iron) shifted by the wiring lead in years; commuting from vehicles per household (0.33 a person against about 0.22, energy Uses AK). Commuting has no good anchor and gets ranges.

### C6 The air arm — recommended: price and order book only

- The aircraft path ($95m 1929, $125m 1932) stays as it is.
- Aircraft prices follow T. P. Wright's learning curve (1936, about 80% per doubling of cumulative output) for the life table and the fleet's costs.
- The fleet's order book enters C7's slump decomposition.
- Civil aviation (air mail, passengers) has no workbook anchor and stays a range in the life table unless you want a services line (Q6).

### C7 The slump — recommended: explain, not add

The baseline already makes the slump mild (output 14% below trend in 1932, against the Union's collapse) through `Paths!M`, `dep_severity` and `slump_price`. The layer **decomposes** that gap rather than adding to it:

- **Demand:** the power estate's investment held up, the naval and air order book, the Reserve Bank's purchases of the estate's bonds (financing, not demand), × a multiplier μ 0.7 / 0.5 / 0.4–1.0 (Barro and Redlick's defence-spending multipliers; Fishback and Kachanovskaya, JEH 2015; *to verify*).
- **Prices:** `slump_price` 0.6, less deflation.
- **The residual:** monetary and banking (gold lent, not hoarded; no bank collapse), with Eichengreen's *Golden Fetters* as the frame (*to verify*).

My estimate: the investment and order book explain 1–2 of the roughly 11 points by which Pacifica's 1932 gap is smaller than the Union's; the rest has to be monetary. Option B would let the demand channel move `Paths!M` and make the slump milder still; it would double count what the baseline already assumes (Q7).

### C8 Third order — mostly automatic

- **Wages:** labour share (about 0.6, *to verify*) × output per worker (Labour C); real, on C2's deflator. Against the Union: Labour BA × BE.
- **Family income:** a one-earner family plus C5's second earners, at the benchmark years.
- **Migration pull:** automatic through Economy R → Labour T. My estimate is +0.1–0.4m residents in 1932, around your 0.3m flag (Q8).
- **Fund feedback:** automatic and stable. Each extra dollar of GDP brings about 11 cents of receipts, 0.7 of the surplus goes to the Fund and earns 0.3, a slowly compounding loop well inside `dev_cap`. The build reports it.
- **Revenue:** automatic (taxes follow non-mining GDP).
- **The Concord partner:** a memo on Dynamics. Japan's saving on the pool aluminium (pool kt × (world − pool price)) and its electrical licences; Japan's GDP in the workbook is not moved.
- **The Union's response:** automatic through Labour BH (champions' business taken) and BB (brain drain); the build reports the change.

## 4. Double counting, in one table

| Already credited | Overlapping channel | Treatment |
| --- | --- | --- |
| `Paths!L` (Union-pace frontier growth, incl. its electrification) | C1, C4, C5 | Channels count only the change since 1900 in Pacifica's lead over the Union |
| `dev_return` on the Fund's power credit | C1 | C1 × (1 − the Fund's share of power investment); D unchanged (alternative: take the power credit out of D and give C1 the whole) |
| Talent → champions' scale (Champions B) | C3 | C3 acts on two sectors' world shares only, through induced R&D |
| Talent → output per resident (Labour AO) | C5 | Women's extra work is not counted in the talent stock; the stock is unchanged |
| The baseline's mild slump (`Paths!M`) | C7 | Decomposition only, no extra stabilization |
| The investment share (test path) | C1c | Off |
| Champions' nominal value added | C2 | Consumer deflator only; nominal accounts untouched |

## 5. Indicative size (hand estimates, Story mid; the build computes the real ones)

| 1929 | Real GDP | Of which |
| --- | --- | --- |
| C1 electric drive | +0.6–1.0% | |
| C3 spillovers | +0.1–0.3% | offsets part of the separation chain's −0.47% |
| C4 agriculture | +0.1–0.4% | |
| C5 women's work | +0.2–0.8% | |
| Feedback (Fund, talent, migration) | × 1.2–1.4 | |
| **Total** | **+1–3% (mid about 2%)** | Stress about +1% |

Residents 1932: +0.1–0.4m. Consumption per person against the Union at its prices: about 1.6–1.9× with the services term (2.09× nominal now). If you read `Paths!L` as Pacifica's growth *without* an electrification wave (Q1, the other answer), C1 against a no-electrification counterfactual would add about 6–8% by 1929; I recommend against it, because 1.7% in the 1920s is the Union's own rate, which the Union reached with its own electrification.

## 6. The energy workbook

**Recommended: the energy workbook keeps reading the baseline** (`dyn_on` = 0) case. The layer values the kilowatt-hours the energy workbook already supplies; most of its extra output comes *from* that power, not on top of it. So no new loop is needed: one pass to add the exports, then a check that `energy_outputs.csv` is unchanged except for the new columns. The one inconsistency is that extra residents would want homes and power; the build reports the implied extra kWh (at the energy workbook's kWh per person) as a check. If you adopt the layer and residents move by more than 0.3m, the energy workbook should then read the dynamic case and the pair iterates as usual (Q10).

## 7. The life table (benchmark years 1900, 1913, 1920, 1924, 1929, 1932)

For a working family and a professional family:

- **Income:** annual earnings, nominal and in 1913 dollars on C2's deflator, against the Union's average annual earnings (HSUS, *to verify*).
- **Prices:** a week's food, a kWh, a radio, an electric iron, a car and a gallon of fuel, a pound of aluminium ware, a cinema ticket, a month's rent, a haircut. Each in dollars and in hours of work, against the Union.
- **The home:** wired or not, kWh a year, appliances.
- **Getting about:** cars per household, the commute (range).
- **Time:** hours worked and housework hours.
- **Work:** women in paid work (all women and married women).
- **The farm:** food's share of the budget.

All MODEL, each column with its anchor and status. This is the table the storyline draws from; nothing in it is canon until you say so.

## 8. Decisions for the author (my recommendation first)

- **Q1** `Paths!L` already contains Union-pace electrification, so channels count Pacifica's lead over the Union. Recommended: **yes**.
- **Q2** Channels on: C1, C2 (deflator), C3, C4, C5 (women's work), C6 (prices and order book), C7 (decomposition), C8 automatic. Off: C1b, C1c. Recommended: **as listed**.
- **Q3** Netting with the Fund. Recommended: **C1 × (1 − the Fund's power share), D unchanged**.
- **Q4** Prices. Recommended: **consumer deflator only (option A), with the services term on**; the car at mid 1.0 and fuel at 0.9 unless you want Pacifican cars cheaper by assumption.
- **Q5** Hours. Recommended: **reported, not a driver**.
- **Q6** The air arm. Recommended: **learning-curve prices and the order book; no civil-aviation output line**.
- **Q7** The slump. Recommended: **decompose, not add**.
- **Q8** Migration. Recommended: **the pull reads the dynamic GDP**; if residents move by more than 0.3m in 1932, I report it and you choose between accepting it (storyline "about 37 million" reviewed) and letting the pull read the baseline.
- **Q9** Saved state. Recommended: **saved with `dyn_on` = 0**, with the Layers sheet showing both. The storyline's figures (residents; §31's atomic cost, which this layer does not move) stay as they are until you adopt it.
- **Q10** Energy reads the baseline. Recommended: **yes**, with the residents check.
- **Q11** Stress gets the same channels at the low end of each range. Recommended: **yes**.
- **Q12** CR number for the build note. Recommended: **CR-056**, as a finance-only CR with no canon change.

## 9. Build plan once approved

1. `finance/build/cr056_dynamics.py` on the current workbook (the chain CR-050 → CR-052 link → CR-051/054/055 → this). Adds the lever block, the four sheets, the Economy J factor and the anchors (with status) on the `Dynamics` sheet's header rows.
2. `energy/build/export_energy.py`: the new columns. One energy pass, then a check that nothing else moves.
3. Recalculate (no errors). Run the `dyn_on` = 0 identity test against `cba70b31…`. Recalculate Story and Stress × 0/1 and write `Layers`.
4. Verify the *to verify* anchors that carry weight (Devine is done; David, Vidart and Moretti are done; next the US wired-home series, women's participation, hours, earnings, the CPI weights, irrigation acreage and the multipliers).
5. `finance/CR-056-dynamics-workbook.md` and a `finance/README.md` entry.
6. Fresh-context review, then PR, CI, and back to you before merging.
