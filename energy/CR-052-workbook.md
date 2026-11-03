# Workbook note, 3 November 2026: the energy workbook (CR-052)

SHA-256 of the energy workbook: `SHA_PLACEHOLDER`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 23,549 formulas, no errors, in all three cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline as integrated on `main`, CR-051 (approved, not yet integrated) for the halls and the Works' dams, and the author's decisions of 3 November 2026 recorded in CR-052.

## Builds

| Build | What changed |
| --- | --- |
| First | Fourteen sheets to the handoff; Story and Stress. |
| Second | After the fresh-context review ([`outputs/CR-052/review.md`](../outputs/CR-052/review.md)): one industrial weight (`ind_w` = 0.5) for factory motors and industrial fuel; the mid-Columbia chain an option (off); Boulder at its historical dates. |
| Third (this note) | The author's sources: the 1917 *Census of Electrical Industries*, Devine (1983) and the 1932 *Minerals Yearbook* (anchors now VERIFIED for US and California 1907–17, factory electrification, oil 1931–32). The approved decisions in the Story case: Realm coal at four times history (CT3 A), all Pacifican-controlled Gulf crude home (B), home oil on the discovery path `oil_c52` (C) with the dry gas fields, and vehicles per person so that California is the most motorized place on earth (CT5). A third case, **Max** (`Levers!E4` = 3): every source Pacifica can reach and every use that can absorb it. |

## Story case (canon with the approved decisions)

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |2.0|13.8|28.6|35.0|44.9|58.2|64.3|60.1|
| Capacity (GW) |1.1|5.9|10.8|12.8|15.9|20.1|22.4|22.7|
| Hydro share |81%|77%|69%|68%|65%|63%|64%|76%|
| kWh per person |191|691|1123|1280|1526|1785|1848|1615|
| × US electricity per person |—|2.35|2.11|2.30|2.26|2.10|1.93|2.03|
| × US utility capacity per person |—|4.82|3.54|3.63|3.23|2.87|2.63|2.21|
| Halls / capacity |0.0%|0.0%|1.6%|2.7%|3.6%|3.5%|2.3%|2.3%|
| Halls / electricity used |0.0%|0.0%|5.8%|9.3%|11.8%|11.0%|7.4%|7.9%|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1153|2791|3954|4299|4872|5533|5894|5304|
| GJ per person |108|140|155|157|165|170|169|143|
| Home oil (m bbl) |70|220|320|360|390|420|450|400|
| Oil imported (m bbl) |6|38|76|71|88|113|113|99|
| Oil share for rail, industry, power |64%|91%|100%|100%|100%|100%|100%|100%|
| Coal mined at home (Mt) |21.3|31.9|36.9|39.3|45.7|52.8|56.9|46.0|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|8%|12%|10%|11%|13%|12%|11%|
| Vehicles per person |0.00|0.04|0.15|0.20|0.24|0.30|0.33|0.33|
| California vehicles per person |0.00|0.05|0.19|0.24|0.30|0.38|0.41|0.41|
| Vehicles to build (thousand) |0|340|1099|1430|1734|2069|2148|1531|
| Northwest hydro beyond own load (TWh) |0.2|1.4|2.2|2.6|2.7|3.0|3.2|6.5|
| Home oil above finance (m bbl) |45|120|205|210|160|167|150|247|
| Power investment ($m) |34|138|325|555|592|564|537|230|
| Power investment / GDP |0.6%|0.8%|0.6%|1.3%|1.1%|0.9%|0.8%|0.4%|
| Electricity revenue ($m) |72|342|960|831|1005|1146|1210|966|
| Checks failing |—|—|—|—|—|—|—|4|

- **Fuel:** the gap of the second build is closed in every year. Railways, industry and power get all the oil they want from 1920 (91–92% in 1910–17). Imports are 7–13% of primary energy in 1913–1932 (Gulf crude 38–113m bbl a year).
- **The multiplier** is unchanged by A–C, which change fuel, not electricity: 1.86–2.30 times US electricity per person in 1920–32. Historical California's central stations already sold about 2.3 times the US per person in 1917 (152 kWh for light and 489 for power, against about 80 and 200; 1917 census).
- **Vehicles:** 0.33 per person in 1929 (California 0.41) needs about 2.1m vehicles built a year by 1929, against the financial workbook's 1.15m.
- **Home oil** runs 45–250m bbl a year above the financial workbook's path: the input its next build must take.

## Max case (exploration)

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |3.3|23.8|49.6|60.4|77.1|98.6|111.0|107.8|
| Capacity (GW) |1.7|9.8|18.2|22.0|27.5|35.0|39.4|41.2|
| Hydro share |67%|60%|54%|60%|61%|67%|68%|76%|
| kWh per person |309|1191|1943|2213|2618|3026|3190|2898|
| × US electricity per person |—|4.05|3.66|3.98|3.88|3.55|3.33|3.64|
| × US utility capacity per person |—|8.04|5.98|6.24|5.59|5.00|4.63|4.03|
| Halls / capacity |0.0%|0.0%|1.0%|1.6%|2.1%|2.0%|1.3%|1.3%|
| Halls / electricity used |0.0%|0.0%|3.3%|5.4%|6.9%|6.5%|4.3%|4.4%|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1206|3059|4384|4764|5398|6115|6521|5903|
| GJ per person |113|153|172|174|183|188|187|159|
| Home oil (m bbl) |100|260|360|400|430|470|520|460|
| Oil imported (m bbl) |6|38|73|59|72|75|53|43|
| Oil share for rail, industry, power |94%|100%|100%|100%|100%|100%|100%|100%|
| Coal mined at home (Mt) |15.9|29.6|40.3|42.3|48.9|55.3|59.5|48.5|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|8%|10%|8%|8%|7%|5%|4%|
| Vehicles per person |0.00|0.06|0.19|0.23|0.28|0.34|0.37|0.37|
| California vehicles per person |0.00|0.07|0.24|0.29|0.35|0.42|0.46|0.46|
| Vehicles to build (thousand) |0|474|1335|1584|1901|2249|2338|1717|
| Northwest hydro beyond own load (TWh) |0.1|0.8|0.3|4.2|7.2|12.2|11.8|16.1|
| Home oil above finance (m bbl) |75|160|245|250|200|217|220|307|
| Power investment ($m) |47|224|590|993|1049|1054|992|479|
| Power investment / GDP |0.9%|1.3%|1.2%|2.3%|2.0%|1.7%|1.4%|0.9%|
| Electricity revenue ($m) |117|591|1690|1474|1785|2001|2130|1773|
| Checks failing |—|—|—|6|—|—|—|6|

- **What changes against Story:** electric homes (1,800 kWh a home in 1929), factories fully electric including process heat (`ind_w` 0.75), aluminium at 280 kt in 1929, ammonia from electrolytic hydrogen (150 kt N), 20% electric steel, half the main lines electric, ordinary hydro 35% faster, Boulder decided 1920 (first power 1926), the mid-Columbia chain decided 1918 (3 GW), home oil and vehicles a little faster. The Story case's people and output are kept.
- **The multiplier:** 3.27–3.98 times US electricity per person in 1920–32 (4.0–6.2 against US utility capacity). About 3,200 kWh a head in 1929, against Montana's 3,522 for power alone in 1917.
- **1929 electricity, 98 TWh used:** factory motors and process heat 37 TWh, homes 15, electrochemistry 13 (aluminium 6, electrolytic ammonia 2), railways 12, the rest commerce, mining, pumping and the strategic loads.
- **The Northwest:** 12–16 TWh a year of Columbia and Willamette power beyond the Northwest's own load in 1927–32. The pooled grid counts it as usable in California; no 1920s line could carry it there. It needs about 1.5–2 GW of new Northwest industry or a tie line of about 700 miles.
- **For the financial workbook:** 150–307m bbl a year more home oil than its path, about 2.3m vehicles a year by 1929, about 140 kt more aluminium, power investment of about bn a year in 1922–27.

## Stress case

Unchanged by the third build except for the dry gas fields and the higher share of oilfield gas marketed, which it shares with Story. It keeps the financial workbook's home oil and vehicle paths (`oil_src` = `veh_src` = 1). Electricity per person 1.63–2.24 times the US in 1920–32; halls 10.4–23.6% of electricity in 1920–27; no coal beyond reach.

## The checks

| Test | Story | Stress | Max |
|---|---|---|---|
| 1. Supply = use | passes (largely an identity) | passes | passes |
| 2. Basins within potential; lead times | passes | fails 1922 (the Works' first 100 MW a year early at Stress's lead time) | passes |
| 3. Oilfields within plausible output and known reserves; gasoline yield | passes | passes | passes |
| 4. Electricity per person and energy per dollar within bands | fails 1932 (US slump) | passes | passes |
| 5. Capacity factor, reserve, dry year | passes | passes | passes |
| 6. Power investment within 4% of GDP and the Development Fund's share | fails 1916 | fails 9 years before 1927 | fails 7 years (1914–32): power needs more than 60% of what the Fund invests |
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
| Levers | 84 levers, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 85 anchor facts with source and status. |
| Paths | 77 benchmark-year paths and 19 Max-case variants: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, Boulder Canyon and the optional mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 14 sectors (eight of them electrochemical); fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first), then Realm coal, extra wood and imported coal for the rest; gas from the oilfields; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit, revenue, royalties and fuel trade in money; named columns `en_*`. |
| Events | 33 dated canon commitments and approved discoveries. |
| Checks | The nine tests of handoff §7, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **One mainland grid.** All mainland hydro can serve all mainland demand. No 1920s line could carry Columbia power to California, so the Northwest's hydro is counted where it could not go. This flatters the hydro share and the value of Columbia dams.
- The financial workbook does not yet read the `en_*` columns and was not re-run. Its Story and Stress results are unchanged by this note.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; no trade block yet for partners' equipment purchases.
- Industrial self-generation is not separated from utility supply; revenue prices all of it at the average utility price, which overstates revenue.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, and Fowler's Water-Supply Paper 493 (the file supplied holds only its title and contents). [README.md](README.md) lists the downloads.
