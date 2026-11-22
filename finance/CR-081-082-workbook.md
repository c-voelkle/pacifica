# CR-081 and CR-082: China's loans and the provisioning doctrine in the workbooks (22 November 2026)

**Authorization:** the author, 22 November 2026, 14:05 ("I approve all as recommended", CR-082 D19, item 6): one task after the merge of PR #84 for CR-081's loans, Chile's loan, the nitrogen plants and the storage works, with the Entente's grain inside the existing advances. All amounts MODEL.

Two changes, rebuilt together by `finance/build/cr057_rebuild_pair.py` and iterated with the energy workbook to a fixed point (five passes; the last moved the energy outputs by at most 4.8e-8):
1. **The nitrogen plants (energy workbook).** `energy/build/energy_inputs.py`, the CR-082 block at the end, re-sizes the paths `eln_kt` (the Columbia's cells) and `haber_kt` (Haber–Bosch on Valley gas). The Electro champions sheet reads them for the value added and the plant.
2. **The Events rows (financial workbook).** `finance/build/cr081_082_provisioning.py` is the last step of the chain, after drink and coffee. Its master lever is `pv_on`: at 0 the step reproduces its input exactly (116,482 values outside Levers, Events and Changes, none differs).

## The nitrogen plants

The home plants now fix two things (CR-082 T9, case B, decided at 13:27 with CR-054's total stated):
- what the Realm's fields take from home, from `population/provisioning.py` (nitrogen used less nitrogen from Chile);
- CR-054's other half: the crowns' sugar and rice, Korea, the China and Manchurian trade, and industry.

Haber–Bosch keeps its share of the earlier path, and the cells make the rest. Tacoma's cyanamide (`fert_gwh`) is beside the new paths and unchanged.

| kt N | 1920 | 1925 | 1929 | 1932 |
| --- | --- | --- | --- | --- |
| The fields' home nitrogen (provisioning model) | 50 | 113 | 152 | 195 |
| Columbia cells, before / **after** | 33 / **66** | 45 / **131** | 60 / **131** | 65 / **159** |
| Haber–Bosch, before / **after** | 0 / **0** | 2 / **6** | 30 / **66** | 35 / **86** |
| **Total fixed** | **66** | **137** | **197** | **245** |

The storyline's "about 200,000 tonnes of nitrogen" in 1929 (§33) is 197 thousand here.

What it changes:
- **Electricity.** The cells' electricity in 1929 rises from 0.78 to 1.71 TWh. Electricity a head is unchanged to the nearest kWh in 1929 (2,656 → 2,657), because the cells run on the river's secondary power.
- **Money.** Power investment moves by under $10m in any year.
- **The energy workbook's checks:** all ten pass in every year (957 of 957).
- **The champions.** Nitrogen's value added in 1929 is $19.5m (was $8.9m), and the nitrogen plant $23.6m (was $8.8m).

## The Events rows

| Row | Years | Category | Story | Stress | What |
| --- | --- | --- | --- | --- | --- |
| E251 | 1891–92 | Loan (Continental) | $10m | $14m | Chile: the regency's loan on the nitrate duty after the armistice (CR-082 D; moved to the copper duty in the mid-1920s, D19) |
| E252 | 1900–20 | Investment | $270m ($12.9m a year) | $405m | Storage works in basins without salmon, lent to the districts on Development Fund credit (`pv_st_acres` 4.5 million × `pv_st_cost` $60; Stress $90) |
| E253 | 1906–32 | Receipt | $6.75m a year | $8.1m a year | The districts' repayments from water rates over 30 years, a quarter never repaid (Stress 40%), as CR-071 C5 |
| E254 | 1908–12 | Loan (Asia) | $13.2m | $16.5m | China: the banner loan of 1908, the Treasury's half of 40 million Haikwan taels at $0.66 (Stress 50 million) |
| E255 | 1928–32 | Loan (Continental) | $25m | $35m | The Gulf: credit for rice, feed and drainage under the provisioning compact (CR-082 R-2) |
| E256 | 1931 | Loan (Asia) | $9m | $9m | China: the wheat credit to the relief commission, 15 million bushels at $0.60 (CR-081 G-10) |
| E257 | 1931–32 | Commitment (memo) | $54m | $72m | The Crown's granary, bought by the Patrimony from its own reserves (3 million tonnes at $18; Stress 4 million). The Budget and Loans do not read the category, so there is no Treasury cash and no new issue (CR-081 G-14) |

The Events column "Story status" reads Approved because the events are approved canon. The amounts are MODEL, and the column is not a canon label.

## Results

| | Before | **After** |
| --- | --- | --- |
| Story / Stress failed year-checks | 0 / 50 | **0 / 51** |
| Residents, end of 1932 | 37.062m | 37.068m |
| Non-mining GDP, 1929 | $25,918m | $25,915m |
| Real GDP, 1929 (1913 $) | $44,156m | $44,170m |
| Domestic taxes, 1900 / 1911 / 1929 / 1932 | $326.7m / $770.7m / $1,649.9m / $1,426.3m | $325.4m / $777.4m / $1,644.9m / $1,425.0m |
| Domestic taxes, 1846–1932, sum | | **+$88.9m** |
| Loans abroad outstanding, 1913 / 1929 / 1932 | $145.1m / $2,414.5m / $2,656.1m | $160.9m / $2,432.5m / $2,695.2m |
| Public debt, 1932 | $1,916.4m | $1,929.1m |

- **The Stress failure.** The one new Stress failure is 1916's market test for Treasury and power-estate bonds (CR-055): bonds placed $591m against a capacity of $588m, a shortfall of $3m. Before, the year passed by $14m, and 1917 already failed. The storage works (E252, $19.3m a year in Stress) tip it.
- **Recalculation.** LibreOffice (the spreadsheet skill's `recalc.py`): 83,733 formulas in the financial workbook, no errors in either case.
- **Financial workbook** SHA-256 `ad6069e0f1e0ff4403d4af63211e7406a801194767fc76ab9759fdfc359a6a1e`.
- **Energy workbook** SHA-256 `886a5ca360257c31dc58940eb2499fd1e7367c59ea9f2247d189f13c18830cc8`.

## Not modelled

- **The Entente's grain (CR-082 F-16):** bought with the Entente advances, which are already E70–E74.
- **The railway bonds of 1896:** the Treasury's part is E53. The rest is San Francisco savers' money.
- **The conservancy of 1891, the Pingxiang credit of 1904 and the Shanghai power bonds of 1929:** China's or a bank's money, not the Treasury's.
- **Chilean buyers' credit** for the British houses' fields: the Realm's banks', not the Treasury's.
- **No cash:**
  - Chile's loan moved to the copper duty in the mid-1920s, a change of security only;
  - New Zealand's crop guarantee of 1931, never called before 1933;
  - the storage compacts with the Akimel O'odham, the Pyramid Lake Paiute and the Pueblos, which give water, not money.
- **The dry-land programme:** inside the growth engine's research flow (Growth sheet).
- **The Realm's grain sales abroad and Chile's nitrate bought for the fields:** the workbook has no commodity trade account.
