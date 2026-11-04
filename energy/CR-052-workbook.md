# Workbook note, 4 November 2026: the energy workbook (CR-052, CR-054 and CR-055), tenth build

SHA-256 of the energy workbook: `1e04fb70772768dce2d67599ebf43e34e093d6a3a8dc38079f08d3f1e34d108b`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 28,047 formulas, no errors, in all three cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline as integrated on `main`, CR-051 (approved, not yet integrated) for the halls and the Works' dams, the author's decisions of 3 November 2026 recorded in CR-052, the Max decision of 4 November (the narrowed take of the third review, `outputs/CR-052/review-3.md`), the CR-053 direction, CT6 (Hilo on hydro) and the fuel-security additions of the same day.

## Builds

| Build | What changed |
| --- | --- |
| First | Fourteen sheets to the handoff; Story and Stress. |
| Second | After the first fresh-context review ([`outputs/CR-052/review.md`](../outputs/CR-052/review.md)): one industrial weight (`ind_w` = 0.5) for factory motors and industrial fuel; the mid-Columbia chain an option; Boulder at its historical dates. |
| Third | The author's sources (the 1917 *Census of Electrical Industries*, Devine 1983, the 1932 *Minerals Yearbook*); the approved decisions in the Story case (Realm coal at four times history, CT3 A; all Pacifican-controlled Gulf crude home, B; home oil found early, C; vehicles so that California is the most motorized place on earth, CT5); a third case, **Max** (`Levers!E4` = 3). |
| Fourth | After the second review ([`outputs/CR-052/review-2.md`](../outputs/CR-052/review-2.md)): home oil from a field-by-field model (22 fields; Kettleman Hills 1923); Northwest water power beyond the Northwest's own load spilled; Max diverges from Story only after 1915. |
| Fifth | After the third review ([`outputs/CR-052/review-3.md`](../outputs/CR-052/review-3.md)) and the author's decision of 4 November: **the narrowed Max case goes into Story** — M1 electric homes (Ontario level, 96% of homes wired and 1,700 kWh a home by 1929), M6 half the main lines electric by 1929, M7 Boulder Canyon decided 1920 with first power 1926 and ordinary hydro 35% faster after 1915, M8 pressure maintenance and water flooding fifteen years early (every field's primary recovery × 1.3; Story still produces 90% of deliverability), M9 electric boilers in the Northwest mills (5 TWh by 1929). **The mid-Columbia chain is off in every case** (it collides with CR-051 S7). Not taken: M2 (industrial weight, referred to the financial workbook), M3 and M4 (sent back for rework), M5 (held). Stress keeps the fourth build's shape through three new levers (`home_kwh_x`, `nwboil_x`, `hydx_on`). **CR-053's concession crude** (`conc_ven`, `conc_col`, `conc_peru`, `conc_bah`, `conc_kuw`, `conc_mes`) is added to the import ceiling (Fuels `conc`, `imp_max`) in every case. |
| Sixth | **Fuel security**, after the author's question whether the oil shortfalls meant load-shedding: in a short year the Fuels sheet now draws stocks (`stock_days`), defers the trust's Asian exports (`exp_cut`), switches the coal-capable plant (Paths `dual_share` × `dual_x`), rations motor fuel (`mf_cut`) and only then leaves demand unmet (`unmet`, the real curtailment figure; **check 10** holds it under 2% of the flexible demand and requires no coal beyond reach). Realm coal can rise at most `coal_ramp` a year (10%, plus 1 Mt). The 1932 oil compact is a price floor unless `compact_on` = 1 (Story 0, Stress 1). Check 1 carries the stock and curtailment adjustments. **CT6:** `hilo_src` = 2 in every case; the Hawaiian hydro board's Big Island plants (Paths `h_hilo`, 8 MW in 1922 to 105 MW in 1927 and 115 by 1932, not scaled by `hydro_pace`) carry the smelter; Hawaii's physical potential 250 MW (to verify). |
| Seventh | After Sol's review of the finance note (`claude/finance-investment-share-note.md`, v2): **the Max case's electrified process heat is its own switch** (`heat_el`; Paths `indw_x` applies only with it), so a higher finance weight never stacks on it; **a finance calibration hook** (Paths `ind_idx`, 1 until the financial workbook exports its industrial-output series) scales `ind_w` and `ind_mj` together; **the Development Fund's power credit is capped at the Fund's capacity** (`df_max` × what the Fund invests), the remainder shown as privately financed (`en_power_capex_private`), and check 6 no longer waives the Fund test when the Fund invests nothing; **electricity revenue split** into utility receipts and self-generation valued at utility rates (`self_gen`; `en_elec_revenue_utility`, `en_elec_revenue_selfgen`). Energy results are unchanged; check 6 now passes in every case (in Story the Fund lends $126m of the $140m wanted in 1916 and $111m of $170m in 1932, the rest private). |
| Eighth | **CR-054, the energy-intensive champions reworked** (author, 4 Nov: amounts and the division of labour approved): aluminium about 150 kt in 1929 (Columbia 70, Sierra 60, Hilo 18) with its uses as a memo on Uses (the grid's conductor 35 kt, the Concord fleet's aircraft 7, the Concord pool to Japan 24, civil uses 38, exported beyond the Concord 46); electrolytic ammonia 60 kt N on the Columbia from 1925 beside 30 kt N of Haber–Bosch on Valley gas (BASF licence); electric steel 12%; carbide, chlorine and abrasives × 1.2 from 1920. Story electrochemistry rises from 6.4 to 7.9 TWh in 1929; the multiplier to **2.31–2.94× in 1920–32** (2.56 in 1929); the Northwest's spill is gone from 1927. Max unchanged (it already carried the larger paths). |
| Ninth | **CR-055 R0: the Columbia built early and its power used** (author, 4 Nov: "start building them early, when and wherever it makes sense and putting the energy to use"; the "first main-stem dam" line of CR-051 S7 set aside). Three strategic dams, laddered, not scaled by `hydro_pace`: Bonneville decided 1908, first power 1913 (500 MW by 1922); Rocky Reach 1914/1919 (800 MW by 1929); Wells 1921/1926 (600 MW by 1932). The ordinary Columbia utilities (`h_col`) build less in step. New electrochemistry a decade early: electrolytic zinc at Spokane from 1908 (70 kt in 1929), magnesium from Great Salt Lake brine from 1909 and Tacoma seawater from 1924 (7 kt), ammonia on the Columbia's cells from 1915 instead of 1925 (60 kt N by 1929; the heavy-water residue found 1916–17), furnace phosphorus on the upper Snake from 1915 (30 kt P), electrolytic copper refining at Great Salt Lake from 1905; the Columbia takes CR-054's aluminium growth (100 of 150 kt). The new loads sit in the Northwest balance and the interruptible set. **The river outruns its customers:** even with every plausible 1900s–1920s electrochemical use, the Northwest spills 1–4 TWh a year through the 1920s (first pass, before the utilities were paced back: 6–9 TWh). That spill is the reserve CR-055 names; the diffusion works of the 1930s is its customer. Story: 2.38–2.97× in 1920–32, about 2,490 kWh a head in 1929; all checks pass. |
| Tenth (this note) | **CR-055 R0 in full: the four purposes the early river serves** (author: "They all seem important. Maybe we need to build more dams?"). **The Columbia–Sierra line** (`tie_mw`, Story: decided 1919, 300 MW in 1924, 600 by 1932; CR-052 F5's "no 1920s line" superseded by the author's direction) carries the river's surplus to the Sierra's district and the halls. **Hydrogenation of heavy residue** at Portland from 1920 on the Columbia's electrolytic hydrogen (35m bbl a year by 1929, 3.5 TWh; the motor fuel gained, about 19m bbl in 1929, is a memo on Fuels and is taken out of the straight-run yield test). **Synthetic rubber** at Tacoma by the carbide–acetylene route from 1923, against the Stevenson scheme (50 kt in 1929, 0.6 TWh). **Electric pig iron** for the yards from 1922 (500 kt in 1929, 1.4 TWh). Two more laddered dams: **McNary** (decided 1922, first power 1927, 1 GW by 1932) and **Chief Joseph** built lower than history's so that it can be laddered (1926/1931). **Result:** the Northwest's spill is zero from 1924 to 1929 (0.5 TWh in 1932 after Chief Joseph), the river is slightly short of its own load in 1927–29 (steam makes up about 1.5 TWh), and the Story case reaches **2.41–3.15× in 1920–32, 2,665 kWh a head in 1929** (93 TWh; hydro 73%). Power investment $0.82–1.12bn a year in 1922–29 (1.4–1.9% of GDP); all checks pass. Max unchanged. |

## Story case (canon with the approved decisions and the 4 November Max parts)

Fourth-build values in brackets where they changed.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Everyone present (m) |10.6|19.9|25.5|27.3|29.4|32.6|34.8|37.2|
| Generation (TWh) |2.1|14.3 (13.8)|32.6 (28.6)|42.4 (35.0)|57.2 (44.9)|79.8 (58.2)|92.7 (64.3)|93.3 (60.1)|
| Capacity (GW) |1.1|6.0 (5.9)|12.3 (10.8)|15.1 (12.8)|19.5 (15.9)|25.6 (20.1)|29.5 (22.4)|32.0 (22.7)|
| … hydro (GW) |0.4|2.4|5.4 (4.3)|6.7 (5.2)|8.4 (6.3)|12.0 (7.9)|14.3 (8.8)|16.5 (9.8)|
| Hydro share |71%|66%|64% (61%)|64% (61%)|64% (59%)|67% (58%)|71% (59%)|76% (65%)|
| kWh per person |194|720 (691)|1,279 (1,123)|1,553 (1,280)|1,946 (1,526)|2,447 (1,785)|2,665 (1,848)|2,507 (1,615)|
| × US electricity per person |—|2.45 (2.35)|2.41 (2.11)|2.79 (2.30)|2.88 (2.26)|2.87 (2.10)|2.78 (1.93)|3.15 (2.03)|
| × US utility capacity per person |—|4.95 (4.82)|3.89 (3.54)|4.19 (3.63)|3.88 (3.23)|3.68 (2.87)|3.51 (2.63)|3.17 (2.21)|
| Halls / capacity |0.0%|0.0%|1.4% (1.6%)|2.3% (2.7%)|3.0% (3.6%)|2.7% (3.5%)|1.8% (2.3%)|1.6% (2.3%)|
| Halls / electricity used |0.0%|0.0%|5.4% (5.8%)|8.3% (9.3%)|10.0% (11.8%)|8.8% (11.0%)|5.7% (7.4%)|5.6% (7.9%)|
| Halls from the grid (MW avg) |0|0|0|33|106|109|0|0|
| Primary energy (PJ) |1162|2800|3943|4310|4916|5600|5985 (5868)|5405 (5249)|
| GJ per person |109|140|155|158|167|172|172 (169)|145 (141)|
| Home oil (m bbl) |74|228 (209)|275 (248)|280 (250)|304 (272)|274 (238)|255 (216)|229 (159; the compact a price floor since the sixth build)|
| Oil imported (m bbl) |6|38|104|130|157 (154)|226 (214)|305 (285)|236 (212)|
| … of it concession crude (CR-053) |0|0|0|0.3|3|12|20|24|
| Oil share for rail, industry, power |73%|100% (85%)|99% (82%)|98% (78%)|100% (78%)|95% (66%)|100% (69%)|92% (42%)|
| Coal mined at home (Mt) |20.8|35.3|49.2|54.6|62.6|69.8|69.9|70.0|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0 (0.5)|0.0 (6.5)|
| Coal beyond reach (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|8%|16%|18%|20%|25%|31% (30%)|27% (28%)|
| Vehicles per person |0.00|0.03|0.14|0.19|0.24|0.30|0.33|0.33|
| California vehicles per person |0.00|0.03|0.17|0.24|0.30|0.38|0.41|0.41|
| Vehicles to build (thousand) |0|200|1158|1487|1816|2069|2148|1531|
| Northwest hydro spilled (TWh) |0.2|1.7|3.6 (2.2)|3.3 (2.6)|0.0|0.0 (3.0)|0.0 (3.2)|0.5 (6.5)|
| Home oil above finance (m bbl) |49|128 (109)|160 (133)|130 (100)|74 (42)|21 (−16)|−45 (−84)|41 (6)|
| Power investment ($m) |34|169 (138)|519 (325)|820 (555)|908 (592)|1115 (564)|1075 (537)|612 (230)|
| Power investment / GDP |0.6%|0.8%|0.9% (0.6%)|1.7% (1.3%)|1.6% (1.1%)|1.5% (0.9%)|1.3% (0.8%)|0.9% (0.4%)|
| Electricity revenue ($m) |72|353 (342)|1045 (960)|952 (831)|1202 (1005)|1451 (1146)|1593 (1210)|1379 (966)|
| Checks failing |—|—|—|—|—|—|—|—|

**Fuel security (sixth build, Story).** Oil demand left unmet is zero in every year; no motor fuel is rationed in any year; no coal is imported; the coal ramp never binds (the largest yearly rise is 1917, 37 to 42 Mt). What the short years cost instead:

| Story |1915|1917|1918|1920|1925|1926|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|---|
| Asian exports deferred (m bbl) |10|12|12|14|19|20|21|8|18|
| Switched from oil to coal (PJ) |161|265|150|20|83|154|87|0|123|
| Motor fuel rationed (PJ) |0|0|0|0|0|0|0|0|0|
| Unmet (PJ) |0|0|0|0|0|0|0|0|0|
| Stocks (days) |0|0|0|0|0|0|0|0|0|

Two findings. **The switch to coal is within the coal-capable plant in every year** (265 PJ in 1917 against about 1,300 PJ of switchable demand), so the 1915–18 and 1925–27 shortfalls are a managed change of fuel, not a shutdown. **Stocks are exhausted from 1915 and never rebuilt,** because the import ceiling binds in every year after that and the model refills tankage only from surplus: the Realm's real oil reserve in the 1920s is its dual-fuel plant and the Gulf, not its tanks. The deferred exports are home-refined products the trust does not ship to Asia in those years (8–21m bbl, half of what the financial workbook sells from home crude); the Asian contracts are served from Gulf crude instead, which the financial workbook's `asia_home` share should reflect (OPEN).

- **The multiplier is now about two and a half:** 2.41–3.15 times US electricity per person in 1920–32 (fourth build 1.86–2.30), about 2,670 kWh a head in 1929 (tenth build; CR-054's champions and CR-055's early river with its four purposes add about 0.3 together). The rise is homes (14 TWh in 1929 against 6.5), the main lines (12 TWh against 7.3) and the mill boilers (5 TWh); factory motors are unchanged because M2 was not taken. The halls' shares fall accordingly (CR-051's words still hold: a few per cent of capacity, a twentieth to a tenth of electricity).
- **Hydro carries it:** 12.8 GW in 1929 (8.8), of which Boulder Canyon 1.3 GW from 1926; hydro is 64–76% of generation in 1920–32. Northwest spill falls to nothing in 1929 with the mill boilers, and 1.4 TWh in 1932.
- **Oil, with early water flooding:** home oil peaks at 304m bbl in 1924 (272) and is 255m in 1929 (216); with the sixth build's cascade, railways, industry and power get 95–100% of the oil they want in 1913–29 and 92% in 1932. The Gulf still binds in 1929 (305m bbl imported, with the concessions' 20m on top of the 285m Gulf ceiling); imports are 31% of primary energy. No coal is imported in any year.
- **Money:** power investment 1.3–1.7% of GDP in 1922–29 ($0.76–0.92bn a year), against 0.8–1.3% in the fourth build; electricity revenue $1.6bn in 1929. Since the seventh build the Fund's credit is capped at its capacity and check 6 passes in every year; the financial workbook has no power line yet (F12 OPEN).
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
| Checks failing |—|—|—|—|—|—|—|—|

Without the chain the Northwest's spill vanishes earlier (the mill boilers and the Columbia's electrochemistry absorb it) and steam takes the chain's place, so generation is unchanged and the hydro share is 56–62% rather than 58–69%. The Story–Max gap is now entirely M2–M5: about 22 TWh in 1929, of which factory process heat about 13, electrochemistry 4, homes 0.

## Stress case

Unchanged in substance: it keeps the fourth build's electricity per home (`home_kwh_x` = 0.5), no mill boilers, the hydro pace before M7 (`hydx_on` = 0), Boulder at 1928, the main lines on steam and the financial workbook's oil and vehicle paths. Electricity per person 1.72–2.26 times the US in 1920–32 (1.67–2.24); the same checks fail as before (3 in 1876–1916, 2 in 1922, 9 in 1923–27; check 6 passes since the seventh build).

## The checks

| Test | Story | Stress | Max |
|---|---|---|---|
| 1. Supply = use | passes | passes | passes |
| 2. Basins within potential; lead times | passes | fails 1922 (the Works' first 100 MW a year early at Stress's lead time) | passes |
| 3. Oilfields within the field model and primary reserves; gasoline yield | passes | fails 1876–1916 (the financial workbook's oil runs ahead of the historical fields) | passes |
| 4. Electricity per person and energy per dollar within bands | passes | passes | passes |
| 5. Capacity factor, reserve, dry year | passes | passes | passes |
| 6. Power investment within 4% of GDP; Fund credit within the Fund's capacity (capped since the seventh build) | passes | passes | passes |
| 7. Oil and coal imports within reach | passes | passes | passes |
| 8. Navy oil; vehicles per person ≤ 0.5 | passes | passes | passes |
| 9. Strategic loads powered (incl. Hilo on the board's plants) | passes | fails 1923–27 | passes |
| 10. Fuel security (unmet ≤ 2% of flexible demand; no coal beyond reach) | passes | passes | passes |

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
| Levers | 97 levers, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 85 anchor facts with source and status. |
| Paths | 110 benchmark-year paths (the CR-053 concessions, `dual_share`, `h_hilo`, `ind_idx`, the aluminium-use memos, the three CR-055 dams and the zinc, magnesium, phosphorus and copper lines) and 26 Max-case variants: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, the Hawaiian hydro board, Bonneville, Rocky Reach, Wells, McNary and Chief Joseph (CR-055), Boulder Canyon and the (off) mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed and the Works' dams), the feed plant, the Columbia station and Rock Island's balance, the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 23 sectors (sixteen of them electrochemical, hydrogenation, rubber and pig iron included, plus the Northwest mill boilers) with the aluminium-use memo; fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first); the short-year cascade (stocks, exports deferred, the switch to coal-capable plant, motor-fuel rationing, unmet demand); then Realm coal under its ramp and ceiling, extra wood and imported coal for the rest; gas from the oilfields; the concession crude; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit (capped) and private financing, revenue (gross, utility, self-generation), royalties and fuel trade in money; named columns `en_*`, mapped by payer and recipient in `claude/finance-investment-share-note.md` v2. |
| Events | 58 dated canon commitments, approved discoveries and the CR-053, CR-054 and CR-055 positions. |
| Checks | The nine tests of handoff §7 and the fuel-security test, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **Two systems, one line.** Northwest water power beyond the Northwest's own load is spilled unless the Columbia–Sierra line carries it (Paths `tie_mw`, Story 300–600 MW from 1924, CR-055). California and the Northwest are otherwise pooled: steam, the strategic loads and the rest of the interior share one balance. A two-system grid with its own peaks is the next refinement.
- The financial workbook does not yet read the `en_*` columns and was not re-run. Its Story and Stress results are unchanged by this note. The Story case now needs from it: the home-oil path (with M8), about 2.15m vehicles a year by 1929, power investment of $0.76–0.92bn a year in 1922–29, and the concession stakes' cost and dividends (CR-053).
- M3 (aluminium: Hilo the flagship, Arkansas bauxite) and M4 (ammonia) are unchanged in Story pending rework. Hilo is on the Hawaiian hydro board's plants (CT6, approved): 45 MW average for the smelter in 1929 against the board's 49 MW; Honolulu's grid stays oil-steam.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; the concessions enter only as entitlement crude; no trade block yet for partners' equipment purchases.
- Industrial self-generation is separated from utility receipts only by a share (`self_gen`), not by plant.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, Fowler's Water-Supply Paper 493, and the CR-053 historical anchors (Venezuelan, Colombian and Peruvian output; Holmes's dates; the Red Line shares). [README.md](README.md) lists the downloads.

- Hydrogenation (CR-055) is carried as a load and a motor-fuel memo; the residue it converts is not taken out of the fuel-oil balance, so its effect on imports is understated.
