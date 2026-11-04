# Workbook note, 4 November 2026: the energy workbook (CR-052), fifth build

SHA-256 of the energy workbook: `76e893f6d920a303d16831357186fb8669d6f83dd412bd97fd69bdf5b6541c59`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 23,812 formulas, no errors, in all three cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline as integrated on `main`, CR-051 (approved, not yet integrated) for the halls and the Works' dams, the author's decisions of 3 November 2026 recorded in CR-052, the Max decision of 4 November (the narrowed take of the third review, `outputs/CR-052/review-3.md`) and the CR-053 direction of the same day.

## Builds

| Build | What changed |
| --- | --- |
| First | Fourteen sheets to the handoff; Story and Stress. |
| Second | After the first fresh-context review ([`outputs/CR-052/review.md`](../outputs/CR-052/review.md)): one industrial weight (`ind_w` = 0.5) for factory motors and industrial fuel; the mid-Columbia chain an option; Boulder at its historical dates. |
| Third | The author's sources (the 1917 *Census of Electrical Industries*, Devine 1983, the 1932 *Minerals Yearbook*); the approved decisions in the Story case (Realm coal at four times history, CT3 A; all Pacifican-controlled Gulf crude home, B; home oil found early, C; vehicles so that California is the most motorized place on earth, CT5); a third case, **Max** (`Levers!E4` = 3). |
| Fourth | After the second review ([`outputs/CR-052/review-2.md`](../outputs/CR-052/review-2.md)): home oil from a field-by-field model (22 fields; Kettleman Hills 1923); Northwest water power beyond the Northwest's own load spilled; Max diverges from Story only after 1915. |
| Fifth (this note) | After the third review ([`outputs/CR-052/review-3.md`](../outputs/CR-052/review-3.md)) and the author's decision of 4 November: **the narrowed Max case goes into Story** — M1 electric homes (Ontario level, 96% of homes wired and 1,700 kWh a home by 1929), M6 half the main lines electric by 1929, M7 Boulder Canyon decided 1920 with first power 1926 and ordinary hydro 35% faster after 1915, M8 pressure maintenance and water flooding fifteen years early (every field's primary recovery × 1.3; Story still produces 90% of deliverability), M9 electric boilers in the Northwest mills (5 TWh by 1929). **The mid-Columbia chain is off in every case** (it collides with CR-051 S7). Not taken: M2 (industrial weight, referred to the financial workbook), M3 and M4 (sent back for rework), M5 (held). Stress keeps the fourth build's shape through three new levers (`home_kwh_x`, `nwboil_x`, `hydx_on`). **CR-053's concession crude** (`conc_ven`, `conc_col`, `conc_peru`, `conc_bah`, `conc_kuw`, `conc_mes`) is added to the import ceiling (Fuels `conc`, `imp_max`) in every case. |

## Story case (canon with the approved decisions and the 4 November Max parts)

Fourth-build values in brackets where they changed.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |2.1|14.2 (13.8)|31.0 (28.6)|39.8 (35.0)|53.0 (44.9)|72.7 (58.2)|83.8 (64.3)|84.5 (60.1)|
| Capacity (GW) |1.1|6.0 (5.9)|12.3 (10.8)|15.1 (12.8)|19.5 (15.9)|25.6 (20.1)|29.5 (22.4)|32.0 (22.7)|
| … hydro (GW) |0.4|2.3|5.0 (4.3)|6.3 (5.2)|7.9 (6.3)|10.9 (7.9)|12.8 (8.8)|14.3 (9.8)|
| Hydro share |71%|66%|64% (61%)|64% (61%)|64% (59%)|67% (58%)|71% (59%)|76% (65%)|
| kWh per person |194|712 (691)|1,218 (1,123)|1,456 (1,280)|1,802 (1,526)|2,228 (1,785)|2,407 (1,848)|2,272 (1,615)|
| × US electricity per person |—|2.42 (2.35)|2.29 (2.11)|2.62 (2.30)|2.67 (2.26)|2.62 (2.10)|2.51 (1.93)|2.85 (2.03)|
| × US utility capacity per person |—|4.95 (4.82)|3.89 (3.54)|4.19 (3.63)|3.88 (3.23)|3.68 (2.87)|3.51 (2.63)|3.17 (2.21)|
| Halls / capacity |0.0%|0.0%|1.4% (1.6%)|2.3% (2.7%)|3.0% (3.6%)|2.7% (3.5%)|1.8% (2.3%)|1.6% (2.3%)|
| Halls / electricity used |0.0%|0.0%|5.4% (5.8%)|8.3% (9.3%)|10.0% (11.8%)|8.8% (11.0%)|5.7% (7.4%)|5.6% (7.9%)|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1162|2800|3943|4310|4916|5600|5985 (5868)|5405 (5249)|
| GJ per person |109|140|155|158|167|172|172 (169)|145 (141)|
| Home oil (m bbl) |74|228 (209)|275 (248)|280 (250)|304 (272)|274 (238)|255 (216)|194 (159)|
| Oil imported (m bbl) |6|38|104|130|157 (154)|226 (214)|305 (285)|236 (212)|
| … of it concession crude (CR-053) |0|0|0|0.3|3|12|20|24|
| Oil share for rail, industry, power |68%|94% (85%)|93% (82%)|92% (78%)|93% (78%)|88% (66%)|97% (69%)|70% (42%)|
| Coal mined at home (Mt) |20.8|35.3|49.2|54.6|62.6|69.8|69.9|70.0|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0 (0.5)|0.0 (6.5)|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|8%|16%|18%|20%|25%|31% (30%)|27% (28%)|
| Vehicles per person |0.00|0.03|0.14|0.19|0.24|0.30|0.33|0.33|
| California vehicles per person |0.00|0.03|0.17|0.24|0.30|0.38|0.41|0.41|
| Vehicles to build (thousand) |0|200|1158|1487|1816|2069|2148|1531|
| Northwest hydro spilled (TWh) |0.2|1.3|2.9 (2.2)|3.2 (2.6)|2.7|1.3 (3.0)|0.0 (3.2)|1.4 (6.5)|
| Home oil above finance (m bbl) |49|128 (109)|160 (133)|130 (100)|74 (42)|21 (−16)|−45 (−84)|41 (6)|
| Power investment ($m) |34|145 (138)|436 (325)|756 (555)|827 (592)|918 (564)|922 (537)|484 (230)|
| Power investment / GDP |0.6%|0.8%|0.9% (0.6%)|1.7% (1.3%)|1.6% (1.1%)|1.5% (0.9%)|1.3% (0.8%)|0.9% (0.4%)|
| Electricity revenue ($m) |72|353 (342)|1045 (960)|952 (831)|1202 (1005)|1451 (1146)|1593 (1210)|1379 (966)|
| Checks failing |—|—|—|—|—|—|—|4, 6|

- **The multiplier is now about two and a half:** 2.29–2.85 times US electricity per person in 1920–32 (fourth build 1.86–2.30), 2,400 kWh a head in 1929. The rise is homes (14 TWh in 1929 against 6.5), the main lines (12 TWh against 7.3) and the mill boilers (5 TWh); factory motors are unchanged because M2 was not taken. The halls' shares fall accordingly (CR-051's words still hold: a few per cent of capacity, a twentieth to a tenth of electricity).
- **Hydro carries it:** 12.8 GW in 1929 (8.8), of which Boulder Canyon 1.3 GW from 1926; hydro is 64–76% of generation in 1920–32. Northwest spill falls to nothing in 1929 with the mill boilers, and 1.4 TWh in 1932.
- **Oil, with early water flooding:** home oil peaks at 304m bbl in 1924 (272) and is 255m in 1929 (216); railways, industry and power get 88–97% of the oil they want in 1913–29 (66–85%). The Gulf still binds in 1929 (305m bbl imported, with the concessions' 20m on top of the 285m Gulf ceiling); imports are 31% of primary energy. No coal is imported in any year.
- **Money:** power investment 1.3–1.7% of GDP in 1922–29 ($0.76–0.92bn a year), against 0.8–1.3% in the fourth build; electricity revenue $1.6bn in 1929. Check 6 (the Development Fund's share) fails in 1916 and now also in 1932, when the Fund's credit shrinks in the slump; the financial workbook has no power line yet (F12 OPEN).
- **1929 electricity, 74 TWh used:** factory motors 21 TWh, homes 14, railways 12 (main lines about 7), commerce 7, electrochemistry 6.4 (aluminium 3.1), mill boilers 5, mining 2.9, pumping 1.0, the strategic loads 4.6.

## Max case (exploration, after the 4 November narrowing)

Max keeps the parts Story did not take (process heat electrified through `indw_x`, aluminium at Alcoa's scale, electrolytic ammonia, electric steel, the Central Valley pumped harder, 100% of the fields' deliverability) and loses the mid-Columbia chain.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |2.1|15.1|35.7|47.2|64.9|90.1|105.7|105.8|
| Capacity (GW) |1.1|6.4|13.3|17.4|23.3|31.4 (31.8)|36.7 (37.2)|39.4 (40.0)|
| … hydro (GW) |0.4|2.3|5.0|6.3 (6.9)|7.9 (9.1)|10.9 (12.3)|12.8 (14.1)|14.3 (15.9)|
| Hydro share |70%|63%|59%|59%|56% (58%)|56% (61%)|56% (63%)|62% (69%)|
| kWh per person |202|759|1,398|1,728|2,206|2,765|3,039|2,844|
| × US electricity per person |—|2.58|2.63|3.11|3.27|3.25|3.17|3.57|
| Home oil (m bbl) |83|254|305|311|338|304|283|216|
| Oil imported (m bbl) |6|28|101|130|157|226|305|236|
| Northwest hydro spilled (TWh) |0.2|1.1|1.7|1.0 (4.2)|0.0 (5.1)|0.0 (2.8)|0.0|0.0 (1.2)|
| Power investment ($m) |35|152|540|920 (998)|1044 (1126)|1081|1137|548|
| Checks failing |—|—|—|—|—|—|—|6|

Without the chain the Northwest's spill vanishes earlier (the mill boilers and the Columbia's electrochemistry absorb it) and steam takes the chain's place, so generation is unchanged and the hydro share is 56–62% rather than 58–69%. The Story–Max gap is now entirely M2–M5: about 22 TWh in 1929, of which factory process heat about 13, electrochemistry 4, homes 0.

## Stress case

Unchanged in substance: it keeps the fourth build's electricity per home (`home_kwh_x` = 0.5), no mill boilers, the hydro pace before M7 (`hydx_on` = 0), Boulder at 1928, the main lines on steam and the financial workbook's oil and vehicle paths. Electricity per person 1.72–2.26 times the US in 1920–32 (1.67–2.24); the same checks fail as before (3 in 1876–1916, 6 in 1900–26, 2 in 1922, 9 in 1923–27).

## The checks

| Test | Story | Stress | Max |
|---|---|---|---|
| 1. Supply = use | passes | passes | passes |
| 2. Basins within potential; lead times | passes | fails 1922 (the Works' first 100 MW a year early at Stress's lead time) | passes |
| 3. Oilfields within the field model and primary reserves; gasoline yield | passes | fails 1876–1916 (the financial workbook's oil runs ahead of the historical fields) | passes |
| 4. Electricity per person and energy per dollar within bands | fails 1932 (US slump) | passes | passes |
| 5. Capacity factor, reserve, dry year | passes | passes | passes |
| 6. Power investment within 4% of GDP and the Development Fund's share | fails 1916 and 1932 | fails 9 years before 1927 | fails 1916 and 1932 |
| 7. Oil and coal imports within reach | passes | passes | passes |
| 8. Navy oil; vehicles per person ≤ 0.5 | passes | passes | passes |
| 9. Strategic loads powered | passes | fails 1923–27 | passes |

## The concessions (CR-053)

Entitlement crude added to "Most oil that can be imported", in every case (MODEL): Maracaibo (Lago Petroleum minority, 1923–24) 3m bbl in 1926, 9m in 1929, 12m in 1932; De Mares (Tropical Oil minority, 1920–21) 1, 4, 5; Peru (Lobitos and the northern concessions from 1924, the Union's reciprocal fifth) 4, 7, 7; Bahrain 0.3m in 1932; Kuwait and Mesopotamia nothing before 1932. Together 8m bbl in 1926, 20m in 1929 and 24m in 1932: about 7% of 1929 imports. The Gulf still binds.

## Sensitivity runs (second build, Story before A–C; one change at a time)

Carried from the fourth build's note for reference; they were run on the second build's Story case.

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

## What is in the workbook

| Sheet | Contents |
|---|---|
| Start | Purpose, conventions, case, the financial workbook's SHA, key results for the benchmark years, the §8 questions and how each is carried. |
| Levers | 86 levers, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 85 anchor facts with source and status. |
| Paths | 89 benchmark-year paths (six of them the CR-053 concessions) and 26 Max-case variants: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, Boulder Canyon and the (off) mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 16 sectors (nine of them electrochemical, plus the Northwest mill boilers); fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first), then Realm coal, extra wood and imported coal for the rest; gas from the oilfields; the concession crude; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit, revenue, royalties and fuel trade in money; named columns `en_*`. |
| Events | 39 dated canon commitments, approved discoveries and the CR-053 positions. |
| Checks | The nine tests of handoff §7, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **Two systems, no tie line.** Northwest water power beyond the Northwest's own load is spilled (Paths `tie_mw` = 0). California and the Northwest are otherwise pooled: steam, the strategic loads and the rest of the interior share one balance. A two-system grid with its own peaks is the next refinement.
- The financial workbook does not yet read the `en_*` columns and was not re-run. Its Story and Stress results are unchanged by this note. The Story case now needs from it: the home-oil path (with M8), about 2.15m vehicles a year by 1929, power investment of $0.76–0.92bn a year in 1922–29, and the concession stakes' cost and dividends (CR-053).
- M3 (aluminium: Hilo the flagship, Arkansas bauxite) and M4 (ammonia) are unchanged in Story pending rework; Hilo's power source (`hilo_src`) stays OPEN (CT6, review-3 finding 9).
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; the concessions enter only as entitlement crude; no trade block yet for partners' equipment purchases.
- Industrial self-generation is not separated from utility supply; revenue prices all of it at the average utility price, which overstates revenue.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, Fowler's Water-Supply Paper 493, and the CR-053 historical anchors (Venezuelan, Colombian and Peruvian output; Holmes's dates; the Red Line shares). [README.md](README.md) lists the downloads.
