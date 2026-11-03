# Workbook note, 4 November 2026: the energy workbook (CR-052)

SHA-256 of the energy workbook: `6b3ce6b2342bccd8b186bbe3980113b0ff9520e679c2dfeb6f7e6dd256d6b8ea`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 23,722 formulas, no errors, in all three cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline as integrated on `main`, CR-051 (approved, not yet integrated) for the halls and the Works' dams, and the author's decisions of 3 November 2026 recorded in CR-052.

## Builds

| Build | What changed |
| --- | --- |
| First | Fourteen sheets to the handoff; Story and Stress. |
| Second | After the first fresh-context review ([`outputs/CR-052/review.md`](../outputs/CR-052/review.md)): one industrial weight (`ind_w` = 0.5) for factory motors and industrial fuel; the mid-Columbia chain an option; Boulder at its historical dates. |
| Third | The author's sources (the 1917 *Census of Electrical Industries*, Devine 1983, the 1932 *Minerals Yearbook*); the approved decisions in the Story case (Realm coal at four times history, CT3 A; all Pacifican-controlled Gulf crude home, B; home oil found early, C; vehicles so that California is the most motorized place on earth, CT5); a third case, **Max** (`Levers!E4` = 3). |
| Fourth (this note) | After the second review ([`outputs/CR-052/review-2.md`](../outputs/CR-052/review-2.md)): **home oil from a field-by-field model** (22 fields; ramp, peak, decline to their primary recovery; Kettleman Hills 1923), tested against the same fields at historical dates for the financial workbook's own path; **Northwest water power beyond the Northwest's own load is spilled**, not burned in California; Max diverges from Story only after 1915, without double-counting electrification or fuel. |

## Story case (canon with the approved decisions)

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |2.0|13.8|28.6|35.0|44.9|58.2|64.3|60.1|
| Capacity (GW) |1.1|5.9|10.8|12.8|15.9|20.1|22.4|22.7|
| Hydro share |72%|67%|61%|61%|59%|58%|59%|65%|
| kWh per person |191|691|1123|1280|1526|1785|1848|1615|
| × US electricity per person |—|2.35|2.11|2.30|2.26|2.10|1.93|2.03|
| × US utility capacity per person |—|4.82|3.54|3.63|3.23|2.87|2.63|2.21|
| Halls / capacity |0.0%|0.0%|1.6%|2.7%|3.6%|3.5%|2.3%|2.3%|
| Halls / electricity used |0.0%|0.0%|5.8%|9.3%|11.8%|11.0%|7.4%|7.9%|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1154|2772|3919|4269|4849|5497|5868|5249|
| GJ per person |108|139|154|156|165|169|169|141|
| Home oil (m bbl) |74|209|248|250|272|238|216|159|
| Oil imported (m bbl) |6|38|104|130|154|214|285|212|
| Oil share for rail, industry, power |67%|85%|82%|78%|78%|66%|69%|42%|
| Coal mined at home (Mt) |20.8|35.3|49.2|54.6|62.6|69.8|69.9|70.0|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.5|6.5|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|8%|16%|19%|19%|24%|30%|28%|
| Vehicles per person |0.00|0.03|0.14|0.19|0.24|0.30|0.33|0.33|
| California vehicles per person |0.00|0.03|0.17|0.24|0.30|0.38|0.41|0.41|
| Vehicles to build (thousand) |0|200|1158|1487|1816|2069|2148|1531|
| Northwest hydro spilled (TWh) |0.2|1.4|2.2|2.6|2.7|3.0|3.2|6.5|
| Home oil above finance (m bbl) |49|109|133|100|42|-16|-84|6|
| Power investment ($m) |34|138|325|555|592|564|537|230|
| Power investment / GDP |0.6%|0.8%|0.6%|1.3%|1.1%|0.9%|0.8%|0.4%|
| Electricity revenue ($m) |72|342|960|831|1005|1146|1210|966|
| Checks failing |—|—|—|—|—|—|—|4|

- **Oil found early is oil used early.** The field model, with every giant found in the 1880s–1900s (Kettleman 1923), gives 74m bbl in 1900, 209m in 1913 and a peak of about 272m in 1924. Output then falls to 216m in 1929 and, under the oil compact, 159m in 1932. By 1929 that is less than the financial workbook's current path (300m). The cumulative output to 1932 is 7.2bn bbl of 13.5bn primary reserves.
- **The Gulf takes the strain in the late 1920s.** All the Pacifican-controlled Gulf crude comes home, and it binds: 285m bbl in 1929, the ceiling. Imports rise from 8% of primary energy (1913) to 30% (1929). Realm coal reaches its approved ceiling of four times history (70 Mt) from 1927, with 0.5–6.5 Mt imported in 1929–32. **No coal is beyond reach in any year.** Railways, industry and power get 66–85% of the oil they want in 1913–29.
- **The multiplier is unchanged** by A–C, which change fuel, not electricity: 1.86–2.30 times US electricity per person in 1920–32. Historical California already sold about 2.3 times the US per person in 1917 (1917 census).
- **Vehicles:** 0.33 per person in 1929 (California 0.41) needs about 2.15m vehicles built a year by 1929, against the financial workbook's 1.15m.
- **Northwest:** 1.4–6.5 TWh a year of Columbia and Willamette power has no Northwest buyer and is spilled; hydro is 58–67% of generation.
- **The field model's limits.** At historical discovery dates the same fields give 94m bbl in 1913 (history 98) but 401m in 1923 (history 263) and 347m in 1929 (history 293): the flush peaks are generous, so the Story path is generous in its peak years.

## Max case (exploration)

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |2.1|15.1|35.7|47.2|64.9|90.1|105.7|105.8|
| Capacity (GW) |1.1|6.4|13.3|17.4|23.3|31.8|37.2|40.0|
| Hydro share |70%|63%|59%|59%|58%|61%|63%|69%|
| kWh per person |202|759|1398|1728|2206|2765|3039|2844|
| × US electricity per person |—|2.58|2.63|3.11|3.27|3.25|3.17|3.57|
| × US utility capacity per person |—|5.22|4.38|4.93|4.74|4.53|4.37|3.90|
| Halls / capacity |0.0%|0.0%|1.3%|2.0%|2.5%|2.2%|1.4%|1.3%|
| Halls / electricity used |0.0%|0.0%|4.6%|6.9%|8.2%|7.1%|4.5%|4.5%|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1162|2822|4050|4462|5131|5834|6226|5615|
| GJ per person |109|142|159|163|174|179|179|151|
| Home oil (m bbl) |83|254|305|311|338|304|283|216|
| Oil imported (m bbl) |6|28|101|130|154|214|285|212|
| Oil share for rail, industry, power |77%|100%|100%|99%|98%|90%|96%|66%|
| Coal mined at home (Mt) |19.4|29.0|38.8|42.0|48.8|61.2|59.7|67.1|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|6%|15%|18%|18%|22%|28%|23%|
| Vehicles per person |0.00|0.03|0.16|0.21|0.27|0.33|0.36|0.36|
| California vehicles per person |0.00|0.04|0.20|0.27|0.34|0.41|0.45|0.45|
| Vehicles to build (thousand) |0|237|1324|1658|2022|2204|2290|1671|
| Northwest hydro spilled (TWh) |0.1|1.1|1.7|4.2|5.1|2.8|0.0|1.2|
| Home oil above finance (m bbl) |58|154|190|161|108|51|-17|63|
| Power investment ($m) |35|152|540|998|1126|1087|1143|553|
| Power investment / GDP |0.6%|0.9%|1.1%|2.3%|2.2%|1.8%|1.6%|1.0%|
| Electricity revenue ($m) |76|376|1205|1139|1491|1821|2026|1739|
| Checks failing |—|—|—|6|—|—|—|6|

- **What changes against Story, after 1915:** electric homes (1,700 kWh a home in 1929), factories fully electric with process heat (industrial weight rising to 0.75 by 1929), aluminium at Alcoa's scale (180 kt in 1929, 140 kt on the Columbia), ammonia from electrolytic hydrogen (150 kt N, all on the Columbia), 20% electric steel, half the main lines electric, electric boilers in the Northwest mills (5 TWh in 1929), hydro 35% faster, Boulder decided 1920 (first power 1926), a 1.5 GW mid-Columbia chain from 1918, and pressure maintenance and water flooding in the oilfields (30% more recovery). Fuel for heat falls where electricity replaces it. People and output are the Story case's.
- **The multiplier:** 2.6–3.0 times US electricity per person in 1913–19, 3.1–3.3 in 1922–29 and 3.6 in 1932 (2.63–3.57 in 1920–32). About 3,000 kWh a head in 1929, about Norway's level, here for 35m people.
- **1929 electricity, 93 TWh used:** factory motors and process heat 34 TWh, homes 14, railways 12, electrochemistry 10.5 (aluminium 4, electrolytic ammonia 2), mill boilers 5, the rest commerce, mining, pumping and the strategic loads.
- **Oil:** 254m bbl in 1913 and 338m at the 1924 peak, 283m in 1929; the Gulf still binds in the late 1920s (285m bbl in 1929).
- **Northwest:** with the mill boilers and the Columbia's electrochemistry, the spill is 4–5 TWh in 1922–24, 2.8 TWh in 1927 and none in 1929.
- **For the financial workbook:** home oil 50–190m bbl a year above its path in 1900–27 (and slightly below in 1929); about 2.3m vehicles a year by 1929; about 40 kt more aluminium than Story; power investment of about .0–1.1bn a year in 1922–29 (1.6–2.3% of GDP).

## Stress case

It keeps the financial workbook's home oil and vehicle paths (`oil_src` = `veh_src` = 1) and shares the dry gas fields with Story. Electricity per person is 1.63–2.24 times the US in 1920–32, and the halls are 10.4–23.6% of electricity in 1920–27. Check 3 now tests the financial workbook's oil against the fields at their historical dates, and **fails in 1876–1916**: the current financial path (25m bbl in 1900, 100m in 1913) already runs ahead of the fields history found by then. CT3 C replaces that path.

## The checks

| Test | Story | Stress | Max |
|---|---|---|---|
| 1. Supply = use | passes (largely an identity) | passes | passes |
| 2. Basins within potential; lead times | passes | fails 1922 (the Works' first 100 MW a year early at Stress's lead time) | passes |
| 3. Oilfields within the field model and primary reserves; gasoline yield | passes | fails 1876–1916 (the financial workbook's oil runs ahead of the historical fields) | passes |
| 4. Electricity per person and energy per dollar within bands | fails 1932 (US slump) | passes | passes |
| 5. Capacity factor, reserve, dry year | passes | passes | passes |
| 6. Power investment within 4% of GDP and the Development Fund's share | fails 1916 | fails 9 years before 1927 | fails 4 years (1916–32) |
| 7. Oil and coal imports within reach | passes | passes | passes |
| 8. Navy oil; vehicles per person ≤ 0.5 | passes | passes | passes |
| 9. Strategic loads powered | passes | fails 1923–27 (124–261 MW of the halls from the grid) | passes |

## Sensitivity runs (second build, Story before A–C; one change at a time)

| Change | × US electricity per person, 1920–32 | Halls / electricity, 1920–27 | Hydro share 1929 | Coal beyond reach, all years (Mt) | Worst year (Mt) | Halls from grid, 1925 (MW) |
|---|---|---|---|---|---|---|
| As built | 1.86–2.30 | 6–13% | 64% | 130 | 17.7 (1917) | 153 |
| Mid-Columbia chain on (option) | 1.86–2.30 | 6–13% | 79% | 120 | 17.7 (1917) | 153 |
| No main-line electrification | 1.73–2.20 | 6–14% | 69% | 148 | 17.9 (1917) | 153 |
| All Pacifican-controlled Gulf crude shipped home | 1.86–2.30 | 6–13% | 64% | 75 | 14.7 (1917) | 153 |
| Realm coal at 4× history instead of 3× | 1.86–2.30 | 6–13% | 64% | 3 | 1.8 (1917) | 153 |
| No home oil sold in Asia | 1.86–2.30 | 6–13% | 64% | 101 | 16.2 (1917) | 153 |
| Works' dams 30% larger (about 650 MW) | 1.86–2.30 | 6–13% | 65% | 129 | 17.7 (1917) | 73 |
| Industrial weight 0.7 | 2.14–2.62 | 5–11% | 56% | 190 | 20.3 (1917) | 153 |
| Industrial weight 1.0 (US-type dollar, the first build) | 2.56–3.10 | 4–10% | 47% | 295 | 24.5 (1918) | 153 |

The coal gap is mostly the size of the `coal_mult` lever, not a ceiling the model derives: at four times historical western output it nearly vanishes. The multiplier depends mainly on the industrial weight.

## What is in the workbook

| Sheet | Contents |
|---|---|
| Start | Purpose, conventions, case, the financial workbook's SHA, key results for the benchmark years, the §8 questions and how each is carried. |
| Levers | 83 levers, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 85 anchor facts with source and status. |
| Paths | 83 benchmark-year paths and 26 Max-case variants (oil from the field model in energy_inputs.py): intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, Boulder Canyon and the optional mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 16 sectors (nine of them electrochemical); fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first), then Realm coal, extra wood and imported coal for the rest; gas from the oilfields; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit, revenue, royalties and fuel trade in money; named columns `en_*`. |
| Events | 33 dated canon commitments and approved discoveries. |
| Checks | The nine tests of handoff §7, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **Two systems, no tie line.** Northwest water power beyond the Northwest's own load is spilled (Paths `tie_mw` = 0). California and the Northwest are otherwise pooled: steam, the strategic loads and the rest of the interior share one balance. A two-system grid with its own peaks is the next refinement.
- The financial workbook does not yet read the `en_*` columns and was not re-run. Its Story and Stress results are unchanged by this note.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; no trade block yet for partners' equipment purchases.
- Industrial self-generation is not separated from utility supply; revenue prices all of it at the average utility price, which overstates revenue.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, and Fowler's Water-Supply Paper 493 (the file supplied holds only its title and contents). [README.md](README.md) lists the downloads.
