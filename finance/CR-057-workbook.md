# Workbook note, 5 November 2026: CR-057 in the financial workbook (the money block, the Patrimony, the Crown share, the income tax, the saving account)

SHA-256 `76e70aaca293aff913037b2bc573132dba0cf6b17984214339a38371703b7531`. Built on the CR-051/054/055 workbook by [`build/cr057_economic_order.py`](build/cr057_economic_order.py), from `energy/build/energy_outputs.csv` (energy workbook `95607751…`, fifteenth build), then recalculated in LibreOffice: 69,819 formulas, no errors. On every pass the chain is rebuilt in full: CR-050 → CR-052 link → CR-051/054/055 build → this build. The two workbooks were iterated to a fixed point over seven passes (see "The two workbooks together"). **Identity check:** with `c57_on` = 0 the build reproduces every value of `cba70b31` exactly in Story and in Stress (92,621 cells, tolerance 0). Only two labels differ: Budget L and its lever, relabelled under H7. **Story case:** no check fails in any year. **Stress case:** 52 year-checks fail (17 before; see Stress). Status: PROPOSED, for the author's decision before integration. No canon text, register, facts file, character file or ledger is changed. All amounts are MODEL.

**Authorization.** Author, 5 November 2026: "Can you update the energy and financial models accordingly and report back before integrating?" The build carries CR-057 A, A2, B, C, D, E, F and H: H1 (money), H2 (saving), H3 (the Patrimony), H5 (energy), H6 (the Crown share) and H7 (the income tax). It also carries the canon tensions the author approved: CT13 adapt, CT14 amend (the rubber path, in the energy workbook) and CT15 amend (`rb_est` 0). H4, the dynamics workbook of CR-056, is not in this repository and is not built.

## What changed

Everything sits behind one master lever, `c57_on` (Story 1, Stress 1). At 0, every changed formula reduces exactly to the one it replaced.

| Item | How | Where |
| --- | --- | --- |
| Partner balances (B, MR-03) | Official dollar balances held in San Francisco, as paths × `pb_scale` (Stress 1.25): Japan ($10m 1890, $100m 1905, $150m 1913, $500m 1919, $150m 1927, $200m 1929, $150m 1932), the Philippine peso reserve ($10m 1886, $40m 1913, $80m 1929) and the others (from 1900, $100m by 1929). They are fractional liabilities with 50% gold cover (`p_cover`). Earmarked partner gold is a memo column with no amount (OPEN): it is never Pacifica's gold and never cover. A Stress run takes `pb_run` (0.3) of the balances out in gold in 1931 (Gold & money E). | Money |
| The money stock (H1) | From `price_from` (1914): M(y) = (gold at end of y−1 − 0.5 × partner balances(y−1)) / the working cover in use. The working cover starts at the cover actually held at the end of 1913 (0.79 net of the partners' 50%), falls by `c_glide` (0.025) a year, and reaches `c_work` (0.5) in 1925. In the sterilization years 1927–28 it is `c_ster` (0.55; MR-02). **Guard 3:** M can never exceed what the 40% floor allows: gold before the year's surplus inflow, less the partners' cover, divided by 0.4, less the Bank's other liabilities. Notes and bank reserves are M plus the Japan-rescue item (Gold & money I). | Money, Gold & money I |
| The price level (H1) | P(y) = M(y) / (`money_ratio` × `k_slump` in 1930–32 × estimated real GDP). The estimate is last year's real GDP × residents' growth × (1 + real growth per resident) × the output gap's change. It uses only prior-year or non-price values, so there is no circular reference. It replaces Economy H, and the `slump_price` mechanism with it. | Money, Economy H |
| Real GDP | The domestic output (non-mining and the guest workers') is deflated by Pacifica's price level. The world-priced output (mining and oil, the champions, the Gulf) is deflated by the world's (Paths B). With one deflator, a lower Pacifican price level would raise the real value of output sold at world prices. Economy U keeps the single-deflator measure as a memo. | Economy S, U |
| The pulls at US prices | The migration pull (Labour T) and the partners' catch-up (Partners B) read Pacifica's lead at US prices (new Economy T and V). Without this, the lower price level would look like a poorer Pacifica and would cut immigration. | Labour T, Partners B |
| The Bank buys nothing (MR-06, CT15) | `cb_buy` and `rb_est` are 0 while `c57_on` = 1, so the power estate's 1930–32 bonds go to savers (Energy link BF, in the private-saving test). | Levers |
| Coupons (MR-01) | New-issue coupon = MAX(2%, `r_real` 3% + the trailing five-year price change). The coupon on the stock blends new issues in and repaid bonds out. Budget X reads last year's coupon after 1914; before that it reads Paths Y. | Money, Budget X |
| Domestic costs | The atomic programme's 1913-dollar costs (Atomic R, the Works' deflators) follow the derived level. | Atomic R, Works W, AI |
| The Patrimony (C, H3) | Royalties (from 1880), the canal (from 1900), the state's estates (from 1880), half the guest-worker levy (from 1890) and leased land (`land_rent` 0.5% × core GDP, from 1900) leave the Budget. The Works' own returns (Atomic Y) stay with the Works for the halls in 1917–27. Return: a real 4.5% (`pat_real`) plus the trailing five-year price change, floored at 2%. Abroad: 10% in 1919, rising to 50% in 1929. Losses of 15% on the abroad share in 1931–32 (half each year), written off in public. Spending rule: nothing before 1910, then 3% of last year's value paid into the Budget (AD) and spent on earmarked works (AE), which are budget-neutral and counted as investment (Energy link AU). The works build an infrastructure stock (memo, `dev_dep`). | Patrimony, Budget D, E, F, J, M, Y, AD, AE |
| The old Fund off | `dev_share` and `dev_bonds` are 0, and the reserve above the buffer is no longer invested (Debt & cash J). The Fund's lending base for power is now the Patrimony's net new holdings at home (Debt & cash Z, read by Energy link AZ and by the energy workbook). | Levers, Debt & cash J, Z |
| Tax cuts (C) | A lagged rule on domestic taxes. The share cut rises by `cut_speed` (0.5) × last year's cash surplus above a 2% target (after lending abroad and scheduled repayment, over last year's domestic taxes). To that is added a rebate of a quarter of the Reserve Fund above its buffer (`cut_res`). The cut is at most 60%, and the share cannot fall in 1930–32: no tax rise in the slump (§34). | Patrimony, Budget C |
| Private investment from tax cuts | 60% of each cut (`save_cut`) is saved and invested privately at `priv_ret` 0.12 (CR-056: 0.30 less the premium 0.18). | Patrimony |
| Output effect (H3) | Economy D = MIN(`dev_cap`, (0.30 × (the state's development investment + the Patrimony's works) + 0.12 × the private investment from tax cuts) / last year's GDP). The decomposition is on the Patrimony sheet. | Economy D |
| The Crown share (E, H6) | `crown_comp` is 0. Of the chartered stake, `crown_row` (0.2) of the dividends stands for the trunk rights of way and cable landings: the workbook has no railway line in which to isolate them. Royalty floor of one eighth on auctioned oil leases (`roy_floor`); it does not bind, because the oil royalty is already one eighth. A floor on minerals (`roy_floor_met`) exists only as a variant. | Champions BD, BE, Resources P, Q |
| The income tax (H7, CT13 adapt) | Budget L is relabelled "Duty on foreign dividends and coupons (to 1914); tax on income from abroad (from 1915)". A memo on the War Revenue Act of 1915 is added. No number changes. | Budget L, Levers |
| The saving account (H2) | Government saving (the budget balance plus public investment in the Budget plus the Patrimony's accumulation), business saving (the champions' retained earnings), national saving (investment plus net foreign investment plus new monetary gold), household saving as the residual, and the household saving rate. The Previsión's deduction cost is computed from 1919 (`prev_part` 0.25 × the labour force × the $300 and $1,500 caps × `prev_mtr` 5%). **Reporting only:** investment does not yet depend on saving, and the deduction is not taken out of receipts. | Saving |
| A new check | Gold covers 40% of notes and reserves plus 50% of partner balances. | Checks AO, Money |

## Results, Story case (the current workbook `cba70b31` in brackets)

| |1913|1920|1922|1925|1929|1932|
|---|---|---|---|---|---|---|
| Price level (1913 = 1) |1.000 (1.000)|1.048 (2.050)|1.244 (1.580)|1.465 (1.650)|1.326 (1.600)|1.512 (1.372)|
| Core GDP ($m) |14,019 (18,217)|21,492 (53,117)|26,709 (45,053)|37,552 (58,230)|42,104 (71,179)|42,362 (56,327)|
| Real GDP (1913 $m) |14,019 (18,217)|19,487 (25,911)|21,094 (28,514)|25,414 (35,291)|31,312 (44,487)|28,375 (41,054)|
| × US per person (Economy R) |1.93 (2.29)|1.06 (2.42)|1.57 (2.43)|1.73 (2.42)|1.56 (2.38)|2.69 (3.17)|
| … at US prices (Economy T) |1.93|1.98|1.96|1.93|1.86|2.20|
| Residents, end of year (m) |17.72 (19.44)|22.70 (24.91)|24.25 (26.83)|26.67 (29.79)|30.27 (33.91)|32.33 (36.75)|
| Receipts ($m) |1,234 (1,813)|2,653 (6,284)|2,828 (4,752)|3,725 (6,108)|3,991 (7,787)|3,525 (5,503)|
| Domestic taxes ($m) |739 (1,131)|1,696 (4,249)|1,762 (3,037)|2,281 (3,930)|2,223 (5,111)|2,103 (3,816)|
| Tax cut ($m; share of domestic taxes) |128 (15%)|0|28 (2%)|243 (10%)|788 (26%)|764 (27%)|
| Budget balance ($m) |12 (374)|383 (1,680)|262 (918)|227 (1,306)|−62 (1,921)|−1,051 (238)|
| Public debt ($m) |701 (911)|1,075 (2,656)|1,335 (2,253)|1,878 (2,911)|2,105 (3,559)|2,420 (3,036)|
| Reserve Fund ($m) |562 (282)|223 (510)|669 (618)|1,735 (801)|2,160 (1,176)|0 (1,310)|
| The Patrimony ($m) |3,180|5,715|6,971|10,052|14,349|15,536|
| … paid into the Budget ($m) |86|158|187|265|412|456|
| Infrastructure stock ($m, memo) |283|1,043|1,335|1,908|3,069|4,099|
| Private stock from tax cuts ($m, memo) |1,033|923|893|1,054|2,284|3,502|
| Gold cover, old basis (gold / notes and reserves) |0.91 (0.75)|0.87 (0.41)|0.75 (0.55)|0.62 (0.51)|0.55 (0.46)|0.50 (0.56)|
| Gold / (notes and reserves + partner balances) |0.73|0.62|0.59|0.53|0.49|0.45|
| Notes and bank reserves ($m; with the Japan-rescue item from 1927) |981 (1,275)|1,435 (3,718)|1,831 (3,154)|2,612 (4,076)|3,150 (5,231)|3,270 (4,295)|
| Household consumption per person × US |—|—|—|—|1.38 (2.09)|2.34 (2.78)|
| kWh a head (energy workbook) |703 (720)|1,286 (1,273)|1,507 (1,535)|2,061 (2,087)|2,592 (2,614)|2,590 (2,519)|
| Checks failing |0|0|0|0|0|0|

Household consumption per person at US prices is 1.66 × the US's in 1929 and 1.89 in 1932.

**Reading the results.**
- **Output falls by a fifth because the Fund's investment of surpluses is gone.** Before 1914 the price level is unchanged, so the 23% lower real GDP in 1913 is pure output. The old Fund invested 70% of each surplus, the reserve above the buffer and the standing debt's bonds: about 2.75% of GDP a year by 1929, at a 0.30 social return, which added about 0.6–0.8 points a year to growth from 1880. The new mechanism adds 0.2–0.4 points. The Patrimony's works are about 1% of GDP at 0.30, and the private investment from tax cuts is about 1.1% of GDP at 0.12 in 1929 and less before. Over fifty years the gap compounds to −21% in real GDP per resident in 1929 ($1,035 against $1,312) and −12% in residents in 1932, through the workbook's own migration pull. This is the trade-off CR-057 C names. The model credits the private investment with the ordinary return only.
- **Prices.** The derived level stays near 1.0 through the war (the US's is 2.05 in 1920). It then rises to 1.47 in 1925, because the working cover glides from 0.79 to 0.5 and the gold held above the cover becomes money. It falls in 1926–28 under the sterilization (1.21 in 1928), and in the slump it rises from 1.33 in 1929 to 1.60 in 1931 and 1.51 in 1932. Real output falls 9% from 1929 to 1932 while gold holds, so money per unit of output rises. Prices fall from 1929 to 1932 only if money demand rises by more than about 13% (`k_slump`; at 1.10 the 1932 level is still 2% above 1929's). **The rule as set does not give MR-01's falling prices.** That is a decision for the author (below).
- **Money income against the Union** (World sheet): Pacifica's nominal output is 0.62 of the Union's in 1929 (1.13 before) and 1.22 in 1932 (1.75). **Real output** in 1932 is $28.4bn against the Union's $28.6bn (1913 $, the Union deflated by Paths B); before CR-057 it was $41.1bn against $26.3bn.
- **Coupons.** The trailing price change makes the new-issue coupon 9.3% in 1925, after the 1920–25 rise, and 2.0% (the floor) in 1929. The coupon on the stock is 4.3% in 1920, 6.6% in 1925 and 5.7% in 1932 (Paths Y: 4.9–5.0%). Interest is 2.7% of receipts in 1925 and 3.8% in 1932.
- **The budget.** About $0.38bn of 1929 receipts (royalties, the canal, the estates, half the levy) moves to the Patrimony, $0.21bn of new land rents goes to it directly, and $0.15bn of Crown dividends disappears. The transfer of $412m comes back and is spent on works. The surplus rule cuts domestic taxes by 26% by 1929. In the slump no tax rises, so the budget runs deficits of $0.9–1.1bn in 1931–32, the Reserve Fund is spent ($2.2bn in 1929, nothing at the end of 1932) and debt rises to $2.4bn (5.7% of GDP).

## The money block (B's three questions)

| |1919|1920|1921|1927|1929|1930|1931|1932|
|---|---|---|---|---|---|---|---|---|
| Working cover in use |0.64|0.615|0.59|0.55|0.50|0.50|0.50|0.50|
| Money stock M ($m) |1,346|1,435|1,621|2,767|2,901|3,060|3,273|3,022|
| Most the 40% floor allows ($m) |2,105|2,282|2,466|3,878|3,366|3,626|3,300|3,197|
| Partner balances ($m) |622|584|546|318|380|363|347|330|
| Cover net of the partners' 50% |0.66|0.67|0.64|0.46|0.49|0.50|0.43|0.45|
| Gold above all floors ($m) |344|382|386|177|270|313|102|155|

- **Where the cover binds:** nowhere in the Story case: the floor never limits M (Money "Floor binds" is 0 in every year). In Stress it binds in 1931 and 1932, after the run on the balances, and the price level falls to 0.55 in 1932.
- **1920:** cover on the old basis is 0.87 (0.41 before): the 1920 cover does not bind and brings on no 1920–21 correction. The price level rises from 1.05 to 1.21 in 1921 as the working cover glides down. On all liabilities, partner balances included, cover is 0.62.
- **The lender of last resort's room in 1931** (gold above all floors) is **$102m**, after the Union rescue's first tranche ($240m) has left in gold. CR-057 B's "$631m above the floors" was the current workbook's gold above the 40% rule alone ($631m), without partner balances and with the larger gold stock of the larger economy. The weekly rate step does not tighten in the slump in Story; in Stress it does in 1931–32.

## The Patrimony against C's rough figures

| ($m) |1900|1913|1920|1929|1932|
|---|---|---|---|---|---|
| Royalties |12|26|69|52|30|
| Canal |0|10|12|18|13|
| The state's estates |10|34|43|94|105|
| Half the levy |20|59|111|219|147|
| Leased land |24|70|107|211|212|
| Inflows |66|199|343|595|508|
| Return earned |23|199|250|437|868|
| Written off (abroad) |0|0|0|0|569|
| Paid into the Budget |0|86|158|412|456|
| **Value** |494|**3,180**|**5,715**|**14,349**|**15,536**|
| … / core GDP |10%|23%|27%|34%|37%|

C's rough figures (5% from 1880) were $3.2bn, $6.9bn, $15.3bn and $18.5bn, with $90m, $180m, $420m and $525m paid. The workbook gives $3.2bn, $5.7bn, $14.3bn and $15.5bn, with $86m, $158m, $412m and $456m. The levy and land rents are smaller than C's $323m and $356m in 1929 because the economy is smaller. The 1931–32 write-offs are $563m and $569m. The Patrimony's share of GDP is higher than C's 22% because GDP is lower.

## Output short of the story: the rent base widened (triggered)

Real GDP per resident in 1929 is 21% below the current model and Economy R 34% below, so the author's instruction applies: widen the rent base first and report back. Each variant was built on the final CR-051/054/055 workbook with the same energy outputs (the energy workbook was not re-iterated for them). **None is picked; the saved workbook is at the default.**

| Run | Real GDP 1929 ($m) | … per resident ($) | Economy R 1929 | … at US prices | Residents 1932 (m) | The Patrimony 1929 ($m) | Transfer 1929 ($m) | Story checks |
|---|---|---|---|---|---|---|---|---|
| Current workbook | 44,487 | 1,312 | 2.38 | 2.38 | 36.75 | — | — | 0 |
| CR-057 default | 31,312 | 1,035 | 1.56 | 1.86 | 32.33 | 14,349 | 412 | 0 |
| `land_rent` 1.0% | 31,680 | 1,045 | 1.57 | 1.88 | 32.38 | 18,668 | 535 | 0 |
| The levy's share 75% | 31,312 | 1,035 | 1.56 | 1.86 | 32.31 | 16,586 | 475 | 0 |
| Royalty floor of one eighth (minerals too; oil is already one eighth) | 31,533 | 1,040 | 1.57 | 1.87 | 32.38 | 15,609 | 449 | 0 |
| All three | 31,902 | 1,052 | 1.57 | 1.89 | 32.41 | 22,120 | 635 | 0 |

The rent base moves output per resident by +0.4% to +1.7%: the gap is about −20% in every variant. The levy variant changes only how the rent is split between Budget and Patrimony: it moves money, not output, within a decade. The oil floor does not bind, so the royalty variant raises the metal royalty from the Mining Law's 5% to 12.5%; that would amend canon. The CR names the other levers (a higher spending rule, a slower Pacifica with lighter taxes), and they were not used.

## Sensitivities (not variants of the rent base)

| Run | Price 1929 | Price 1932 | Economy R 1929 | World: Pacifica / Union, 1929 and 1932 | Real GDP 1929 ($m) |
|---|---|---|---|---|---|
| Default (`c_work` 0.5 reached by a glide of 0.025 a year) | 1.326 | 1.512 | 1.56 | 0.62, 1.22 | 31,312 |
| `k_slump` 1.05 | 1.326 | 1.430 | 1.56 | — | 31,312 |
| `k_slump` 1.10 | 1.326 | 1.356 | 1.56 | — | 31,312 |
| Hold the 1913 cover (`c_glide` 0) | 0.685 | 0.712 | 0.87 | 0.36, 0.63 | 32,643 |
| `c_work` 0.5 at once in 1914 (no glide) | 1.496 | 1.727 | 1.75 | 0.70, 1.38 | 31,090 |
| Economy D read on the stocks (0.30 × infrastructure stock + 0.12 × private stock) | 0.914 | 1.029 | 1.73 | — | 58,390 |

- With no glide the price level jumps 55% in 1914 (1.55): the Bank prints the gold above a 50% cover at once.
- Holding the 1913 cover gives MR-01's falling prices: 0.79 in 1920 and 0.69 in 1929, 30% below 1913. Money income is then below the Union's per person (Economy R 0.87 in 1929).
- Read literally on the stocks, Economy D sits at `dev_cap` (1.2 points a year) from the 1910s, and real GDP in 1929 is 31% *above* the current model. The column has always used the yearly flow (dev_return × the Fund's investment), with the stock as a memo. A stock in a growth-rate formula would count the return on the whole stock again every year, so the build keeps the flow.

## The saving account (reporting only)

| ($m) |1913|1920|1929|1932|
|---|---|---|---|---|
| Budget balance |12|383|−62|−1,051|
| Public investment in the Budget (public works and the Patrimony's works, the atomic stations, the Works' dams, Investment events) |368|594|1,282|1,589|
| The Patrimony's net accumulation |313|434|620|351|
| Government saving |692|1,411|1,840|888|
| Champions' retained earnings |198|500|969|619|
| National saving (investment + net foreign investment + new monetary gold) |3,994|6,974|13,260|10,124|
| … / core GDP |28.5%|32.4%|31.5%|23.9%|
| Household saving (residual) |3,104|5,063|10,450|8,617|
| Household saving rate |24.9%|27.3%|27.6%|22.2%|
| Previsión: contributors (thousand) and deduction cost ($m) |—|2,343; 63|3,125; 84|3,360; 91|

The household rate is the residual of an imposed investment path (`inv_share`) and is high (22–28%) for that reason; other firms' retained earnings fall into it. Investment is not made to depend on saving in this build (CT7 adapt; H2's derivation is the next step).

## The storyline's MODEL figures

| Figure | Workbook | |
|---|---|---|
| About 37 million residents in 1932 | 32.33 million (36.75 before) | **re-sync** (about 32 million), or restore output |
| 2.24 times the Union per person in 1929 (Economy R) | 1.56 (2.38 before); 1.86 at US prices | **re-sync** |
| About 2,600 kWh a head (1929) | 2,592 (energy workbook) | **holds** |
| §34: "money income briefly puts Pacifica alone ahead in 1932" | Pacifica / Union nominal 0.62 in 1929, 1.22 in 1932 (World) | **holds** (it failed before: 1.13 in 1929) |
| §34: "the Union remains larger in real output" | 1932: $28.6bn against Pacifica's $28.4bn (1913 $) | **holds**, by 0.7%, a margin within the model's error (it failed before: $26.3bn against $41.1bn) |
| "Pacifica raises neither tariffs nor taxes" | Tariff paths unchanged; the tax-cut share cannot fall in 1930–32 (26.2% in 1929, 26.6% in 1932) | **holds** |
| The atomic programme, peak 0.45% of national product in 1921 | 0.61% in 1921. The cost stays $1,399m in 1913 $ ($1,394m before); in current dollars it is $1,841m ($2,190m), net to the Treasury $1,652m ($1,980m) | **re-sync** the peak (the 1913-dollar cost holds) |
| Tacoma's rubber, about 50,000 tonnes in 1929 | 25 kt in 1929, a 5 kt standby line from 1930 (energy workbook, CT14) | **re-sync** as G17. G17's "half its peak" holds only against the old 50 kt: the path's own peak is 40 kt in 1928 |

## Stress

Stress takes the less favourable end of each new lever: a real return of 3.5%, land rents of 0.4%, losses of 25% abroad, `save_cut` 0.4, `priv_ret` 0.06, `crown_row` 0.15, `k_slump` 1.10, partner balances × 1.25, a 30% run on them in 1931, `r_real` 3.5% and a Previsión take-up of 0.35. **52 year-checks fail (17 before):**
- private saving capacity in 1887 and 1914–32 (was 1887 and 1914–24);
- the bond markets in 1916–20 and 1931–32 (new), with the CR-055 bond test in the same years;
- debt over 30% of GDP in 1918–28 and 1930–32 (was 1932);
- interest over 15% of receipts in 1931–32 (new);
- the Siberian line in 1918–19 and the Japan FX buffer in 1927 (as before).

The 1932 gold-cover failure of the old Stress case is gone, because the Bank buys no bonds. The new failures come from **nominal commitments fixed in historical dollars against a smaller nominal economy**: the $8.5bn Entente credit, the Siberian war (on Paths B) and the rescues. Stress's price level is 0.79 in 1920 against Paths B's 2.05, so public debt is $4.4bn in 1920 on a $8.7bn GDP. The floor binds in 1931–32 after the run on the balances, and the price level halves from 1929 to 1932 (1.12 to 0.55).

## The two workbooks together

The pair was rebuilt seven times. Each pass ran energy export → CR-052 link → CR-051/054/055 build → this build → extract → energy build, and each workbook was recalculated in LibreOffice with no errors. The energy outputs changed by at most 3e-4 on pass 5, 9e-6 on pass 6 and under 1e-6 on pass 7. On the last pass, re-running `extract_finance.py` on this workbook reproduces `energy/build/finance_inputs.csv` line for line. This workbook records the energy workbook it read (`95607751…`, Energy link A2). The energy workbook records the financial workbook of the previous pass (`e657ccd3…`), whose extracted values are identical to this one's. `energy/build/extract_finance.py` now reads the Fund's lending base from Debt & cash Z when CR-057 has built it. The fleet's payments under CR-055 decision 7 (Electro champions → Budget O) re-ran with the new rubber path: $0.5m, $2.9m and $1.8m in 1930–32 (were $1.1m, $8.5m and $9.6m).

## Decisions for the author

1. **The working cover.** The default reaches the brief's `c_work` 0.5 by a glide from the 1913 cover. This restores §34's two sentences, but it gives rising prices in 1920–25 and in the slump, not MR-01's falling prices. Holding the 1913 cover gives falling prices, but Pacifica's money income falls below the Union's per person. A path between the two, a different `money_ratio`, or less gold retained are the other levers. Which does the author want?
2. **Output.** CR-057 as specified costs about a fifth of output per resident by 1929, and the rent-base variants do not close the gap. The CR's other levers are a higher spending rule, a slower Pacifica with lighter taxes, or crediting the Patrimony's lending at home or the private investment with more than the ordinary return. Alternatively, accept the smaller Pacifica (about 32 million in 1932) and re-sync the storyline's figures.
3. **The literal stock reading of Economy D.** It is shown above but not used. Confirm the flow reading.
4. **House heating.** House heating gets nothing once the storage heaters have the winter surplus (energy note). Does the author want heating served first in winter? The total absorbed is the same either way.
5. **The Japan path and the 1927 rescue.** The rescue's callable balances in Gold & money I may overlap the Japan path ($150m in 1927). They are not netted.
6. **Stress.** The 35 new year-checks are a finding about fixed nominal commitments under a money rule. Accept them, or price the Entente credit and the Russian war in the derived level (which needs Gold & money E restructured; see Known limits).

## Known limits and interpretations

- **Circularity guards.** The floor test (guard 3) leaves out three things: the external surplus's gold (Gold & money D, which is conservative); in 1927 the gold the Japan rescue pays out, and from 1928 it counts the rescue item; and the estate bonds the Bank holds (zero under CR-057). Each of these depends on this year's GDP. The cover check (AO) counts them all.
- Siberia's price column and the Russian-war events stay on Paths B. They feed Gold & money E's sum over the whole Events column, which the money rule reads, so tying them to the derived level would be circular. The Electro champions' input costs also stay on Paths B.
- Land rents are the brief's placeholder (0.5% × GDP), not derived from acres and values. They are not charged against private incomes. Leasing rather than selling spares the buyers' capital; the workbook models neither.
- The Works' "retained dividend" is taken as the Works' own direct returns (Atomic Y, $6–12m a year) kept in Budget F in 1917–27 against the halls' cost, which stays in Technical programmes.
- The Crown's trunk-rights-of-way stake is a fraction (0.2) of the chartered industries' dividends, because no railway line exists.
- Earmarked partner gold has no amount (OPEN).
- The Previsión's deduction is reported, not deducted.
- Business saving covers only the champions.
- Investment is not derived from saving.
- The tax rule is a controller, not a law. With small budgets in the 1880s it cuts up to its 60% cap and then lets the reserve run down by 1895.
- The energy workbook does not value Tacoma's acetylene chemicals and cyanamide, so the rubber's small value added ($4m in 1929) is not replaced in the champions' accounts.
- Paths C (the population path) was not re-iterated; `population/` was not re-run.
