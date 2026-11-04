# Workbook note, 4 November 2026: the energy workbook (CR-052, CR-054 and CR-055), eleventh build

SHA-256 of the energy workbook: `e68b700c189107c091c67d7c29efc19a0dbcbcc511c5e781779d1c768aa8754e`. Built from the financial workbook with SHA-256 `22266bad58ee60da888c9b8de9bcd2c964498a5427d6b453b1f6a5a46f6120b2` (the CR-050 workbook) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 28,765 formulas, no errors, in all three cases. The financial workbook is not changed. All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline with CR-051 integrated (4 November), the author's decisions recorded in CR-052 (CT3 A–C, CT5, CT6, CT9, the narrowed Max decision, the power seat), CR-053, CR-054 (A6 decided) and CR-055.

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
| Tenth | **CR-055 R0 in full: the four purposes the early river serves** (author: "They all seem important. Maybe we need to build more dams?"). **The Columbia–Sierra line** (`tie_mw`, Story: decided 1919, 300 MW in 1924, 600 by 1932; CR-052 F5's "no 1920s line" superseded by the author's direction) carries the river's surplus to the Sierra's district and the halls. **Hydrogenation of heavy residue** at Portland from 1920 on the Columbia's electrolytic hydrogen (35m bbl a year by 1929, 3.5 TWh; the motor fuel gained, about 19m bbl in 1929, is a memo on Fuels and is taken out of the straight-run yield test). **Synthetic rubber** at Tacoma by the carbide–acetylene route from 1923, against the Stevenson scheme (50 kt in 1929, 0.6 TWh). **Electric pig iron** for the yards from 1922 (500 kt in 1929, 1.4 TWh). Two more laddered dams: **McNary** (decided 1922, first power 1927, 1 GW by 1932) and **Chief Joseph** built lower than history's so that it can be laddered (1926/1931). **Result:** the Northwest's spill is zero from 1924 to 1929 (0.5 TWh in 1932 after Chief Joseph), the river is slightly short of its own load in 1927–29 (steam makes up about 1.5 TWh), and the Story case reaches **2.41–3.15× in 1920–32, 2,665 kWh a head in 1929** (93 TWh; hydro 73%). Power investment $0.82–1.12bn a year in 1922–29 (1.4–1.9% of GDP); all checks pass. Max unchanged. |
| Eleventh (this note) | **Consistency with itself and the story** (author, 4 Nov: "make it consistent with itself and the story"). (1) **The Columbia–Sierra line is used.** In the tenth build the Northwest's firm load plus 5 TWh of mill boilers left the line idle from 1925 to 1929, while the halls still drew 106–109 MW from the Sierra grid; now the line takes the river's surplus first (`tie_flow`, at most capacity × `tie_lf` 0.7), the mill boilers take what is left as secondary power (`nwboil_room`; the mills burn fuel for the rest), and the line's delivery counts in the halls' dedicated supply (`tie_halls`, after 8% losses): the halls draw nothing from the grid from 1924. (2) **Hydrogenation at a believable hydrogen consumption with fewer barrels** (author: "fewer barrels"): `h2_kwh` 240 (about 4 kg of hydrogen a barrel, to verify; was 100) and `hyd_bbl` 9m bbl in 1929 (was 35m): 2.2 TWh, 5m bbl of motor fuel gained. (3) **The gaseous-diffusion plant of CR-051** (pilot about 1926, plant 1930–1932) as a strategic load at the Columbia station (`diff_mw`, 150 MW in 1932; site PROPOSED in CR-055 R3). (4) **Wenatchee takes most of Rock Island's output**, as CR-051 says (`alu_wen` 30–32 kt in 1927–29, inside the Columbia's aluminium; the total is unchanged). (5) Stale notes corrected (`nw_spare`, `hilo_src`, `colms_on`). **Result:** Story 2.39–3.17× US electricity per person in 1920–32, 2,532 kWh a head in 1929 (88 TWh); the line carries 1.8–3.7 TWh a year south from 1924; the mill boilers 2.0–2.3 TWh in 1927–29 instead of 3.5–5; all checks pass. |

## Story case (canon with the approved decisions)

Tenth-build values in brackets where they changed.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |2.1|14.3|32.4 (32.6)|41.9 (42.4)|56.4 (57.3)|76.4 (79.8)|88.1 (92.7)|93.9 (93.3)|
| Capacity (GW) |1.1|6.1|12.5|15.6 (15.8)|20.3 (20.6)|27.4 (28.4)|31.8 (33.3)|36.3|
| … hydro (GW) |0.4|2.4|5.4|6.7|8.4|11.9|14.4|16.9|
| Hydro share |71%|66%|65%|66%|69% (68%)|73% (70%)|76% (73%)|83% (84%)|
| kWh per person |194|720|1,271 (1,279)|1,534 (1,553)|1,915 (1,946)|2,346 (2,447)|2,532 (2,665)|2,523 (2,507)|
| × US electricity per person |—|2.45|2.39 (2.41)|2.76 (2.79)|2.84 (2.88)|2.75 (2.87)|2.64 (2.78)|3.17 (3.15)|
| × US utility capacity per person |—|5.02|4.09 (4.11)|4.44 (4.49)|4.13 (4.19)|3.91 (4.05)|3.74 (3.91)|3.54|
| Halls / capacity |0.0%|0.0%|1.4%|2.2%|2.8%|2.6% (2.5%)|1.6%|1.4%|
| Halls / electricity used |0.0%|0.0%|5.1%|7.8% (7.7%)|9.4% (9.3%)|8.4% (8.0%)|5.4% (5.2%)|5.1%|
| Halls from the grid (MW avg) |0|0|0|33|0 (106)|0 (109)|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|1.8|2.5|3.1|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.5|1.5|2.0|2.3|7.0|
| Northwest hydro spilled (TWh) |0.2|1.7|3.8|3.8|0.1|0.0|0.0|1.5|
| Primary energy (PJ) |1,156|2,709|3,973 (3,978)|4,348 (4,357)|4,966 (4,982)|5,659 (5,704)|6,063 (6,119)|5,552 (5,544)|
| GJ per person |109|136|156|159 (160)|169|174 (175)|174 (176)|149|
| Home oil (m bbl) |74|228|275|280|304|274|255|229|
| Oil imported (m bbl) |6|38|104|130|157|226|305|236|
| Oil share for rail, industry, power |73%|100%|99%|97%|100%|96% (95%)|100%|94% (95%)|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|9%|16%|18%|19%|24%|31%|26%|
| Vehicles per person |0.00|0.03|0.14|0.19|0.24|0.30|0.33|0.33|
| Vehicles to build (thousand) |0|200|1,158|1,487|1,816|2,069|2,148|1,531|
| Home oil above finance (m bbl) |49|128|160|130|74|21|-45|76|
| Power investment ($m) |34|169|494 (519)|806 (820)|890 (908)|1,109 (1,115)|1,001 (1,075)|678 (612)|
| Power investment / GDP |0.6%|0.9%|1.0%|1.9%|1.7%|1.8%|1.4% (1.6%)|1.2% (1.1%)|
| Checks failing |—|—|—|—|—|—|—|—|

**Fuel security (Story).** Oil demand left unmet is zero in every year; no motor fuel is rationed; no coal is imported; the coal ramp never binds. What the short years cost instead:

| Story |1915|1917|1918|1920|1924|1925|1926|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|---|---|
| Asian exports deferred (m bbl) |10|12|12|14|15|18|20|20|3|18|
| Switched from oil to coal (PJ) |162|266|151|22|0|61|132|62|0|88|
| Motor fuel rationed (PJ) |0|0|0|0|0|0|0|0|0|0|
| Unmet (PJ) |0|0|0|0|0|0|0|0|0|0|
| Stocks (days) |0|0|0|0|0|0|0|0|0|0|

**The switch to coal is within the coal-capable plant in every year** (266 PJ in 1917 against about 1,300 PJ of switchable demand), so the short years are a managed change of fuel, not a shutdown. **Stocks are exhausted from 1915 and never rebuilt,** because the import ceiling binds in every year after that and the model refills tankage only from surplus: the Realm's real oil reserve in the 1920s is its dual-fuel plant and the Gulf, not its tanks. The deferred exports are home-refined products the trust does not ship to Asia in those years; the Asian contracts are served from Gulf crude instead, which the financial workbook's `asia_home` share should reflect (OPEN). The line's power from 1924 displaces oil-fired steam in California, which is why fewer exports are deferred in 1924 and 1929 than in the tenth build.

- **The multiplier is about two and a half:** 2.39–3.17 times US electricity per person in 1920–32 (1932 is the US slump), about 2,530 kWh a head in 1929. The rise over canon's earlier uses (1.86–2.30) is homes (14 TWh in 1929), the main lines (railways 12 TWh), CR-054's champions and CR-055's river (electrochemistry 13 TWh) and the mill boilers. The eleventh build gives up about 0.14 of the tenth build's 1929 multiplier: the mill boilers yield to the line, and the hydrogenation works is smaller.
- **Hydro carries it:** 14.4 GW in 1929, of which Boulder Canyon 1.3 GW from 1926; hydro is 65–83% of generation in 1920–32. The Northwest spills 3–5 TWh a year in 1919–23 (the river built ahead of its customers, before the line; CR-055), 0.1 TWh in 1924 and nothing in 1925–30; 0.5 and 1.5 TWh in 1931–32 after Chief Joseph, before the diffusion plant reaches full size.
- **The halls (CR-051):** at full size (700 MW, 1925–27) 2.6% of capacity and 8.4% of electricity: a fortieth of capacity and a little under a tenth of electricity, against the storyline's "about a twentieth … a tenth" (CR-052 CT1, OPEN). They draw 33 MW from the Sierra grid in 1922 and nothing from 1924, on the freed arc power, the Works' dams and the line.
- **Oil:** home oil peaks at 304m bbl in 1924 and is 255m in 1929; railways, industry and power get 94–100% of the oil they want in 1913–32. The Gulf binds in 1929 (305m bbl imported, with the concessions' 20m on top of the 285m Gulf ceiling); imports are 31% of primary energy. No coal is imported in any year.
- **Money:** power investment /bin/bash.8–1.1bn a year in 1922–29 (1.4–1.9% of GDP); gross electricity revenue about .7bn in 1929. The Fund's credit is capped at its capacity and check 6 passes in every year; the financial workbook has no power line yet (F12 OPEN).
- **1929 electricity, 78 TWh used:** factory motors 21 TWh, homes 14, railways 12, electrochemistry 13 (aluminium 3.3, hydrogenation 2.2, pig iron 1.4, electric steel 0.9, ammonia 0.8), commerce 7, mining 2.9, mill boilers 2.3, pumping 1.0, the strategic loads 4.6.

## Max case (exploration)

Max keeps the parts Story did not take (process heat electrified through `indw_x`, aluminium at Alcoa's scale, more electrolytic ammonia and electric steel, the Central Valley pumped harder, 100% of the fields' deliverability). Tenth-build values in brackets.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |2.1|15.3|36.3 (36.5)|48.3 (48.9)|65.3 (67.9)|90.2 (95.7)|105.8 (113.0)|108.3 (112.1)|
| Capacity (GW) |1.1|6.5|13.7 (13.8)|17.7 (17.9)|23.2 (24.0)|31.6 (33.3)|37.2 (39.4)|41.0 (42.5)|
| … hydro (GW) |0.4|2.4|5.4|6.7|8.4|11.9|14.4|16.9|
| Hydro share |70%|63%|59% (60%)|59% (60%)|60% (58%)|62% (58%)|64% (60%)|73% (71%)|
| kWh per person |202|767|1,422 (1,430)|1,770 (1,789)|2,218 (2,307)|2,766 (2,937)|3,041 (3,248)|2,912 (3,014)|
| × US electricity per person |—|2.61|2.68 (2.69)|3.18 (3.22)|3.29 (3.42)|3.25 (3.45)|3.17 (3.39)|3.66 (3.79)|
| Halls from the grid (MW avg) |0|0|0|33|0 (106)|96 (109)|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|1.1|0.1|0.0|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.5|0.0|0.0|0.0|3.2|
| Northwest hydro spilled (TWh) |0.1|1.5|3.4|2.6|0.0|0.0|0.0|0.0|
| Home oil (m bbl) |83|254|305|311|338|304|283|254|
| Oil imported (m bbl) |6|32|104|130|157|226|305|236|
| Power investment ($m) |35|176|587 (612)|959 (973)|932 (1,110)|1,173 (1,270)|1,205 (1,281)|783 (642)|
| Checks failing |—|—|—|—|—|—|—|—|

In Max the Columbia's firm loads (more aluminium and ammonia on the river) take the whole river from 1925, so the line carries almost nothing in 1925–29, the mill boilers get nothing, and the halls draw 96 MW from the grid in 1927: Max is an upper bound on use, not a better-balanced Story. The Story–Max gap in 1929 is about 16 TWh: factory process heat about 13, commerce 2, electrochemistry 2.6, less the 2.3 TWh of mill boilers Story keeps.

## Stress case

The lean case: the fourth build's electricity per home (`home_kwh_x` = 0.5), no mill boilers, the hydro pace before M7 (`hydx_on` = 0), Boulder at 1928, the main lines on steam and the financial workbook's oil and vehicle paths; the CR-055 dams and the line as in Story. Tenth-build values in brackets.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |1.7|9.4|19.4 (19.6)|23.8 (24.3)|31.2 (32.1)|40.6 (42.2)|43.8 (45.3)|39.4 (38.8)|
| Capacity (GW) |0.8|4.0|7.4|8.7 (8.9)|10.9 (11.2)|14.2 (14.6)|15.8 (16.2)|15.7 (15.8)|
| … hydro (GW) |0.3|1.7|3.6|4.3|5.3|7.2|8.4|10.1|
| Hydro share |65%|70%|68%|68% (69%)|49% (47%)|77% (81%)|83% (87%)|97% (99%)|
| kWh per person |196|703|1,185 (1,198)|1,379 (1,409)|1,707 (1,757)|2,045 (2,123)|2,092 (2,165)|1,793 (1,767)|
| × US electricity per person |—|2.39|2.23 (2.25)|2.48 (2.53)|2.53 (2.60)|2.40 (2.49)|2.18 (2.26)|2.25 (2.22)|
| Halls from the grid (MW avg) |0|0|0|81|261|0 (210)|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|0.0|2.5|3.1|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Northwest hydro spilled (TWh) |0.1|1.4|3.6|4.2|0.0|3.0|4.0|10.6|
| Home oil (m bbl) |25|100|115|150|230|253|300|180|
| Oil imported (m bbl) |6|23|62|78|96|65 (63)|34 (32)|103 (102)|
| Power investment ($m) |33|133|281 (310)|479 (494)|532 (553)|605 (628)|526|356 (357)|
| Checks failing |3|3|—|2|9|—|—|—|

Failing: check 3 in 1876–1916 (the financial workbook's oil runs ahead of the historical fields), check 2 in 1922 and check 9 in 1923–24 (the halls' grid draw before the line, and 1924 a dry year); check 9 failed in 1923–27 in the tenth build. Stress spills 3–11 TWh a year from 1927 on the Northwest, because it has the CR-055 dams but not their customers.

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
| 9. Strategic loads powered (incl. Hilo on the board's plants) | passes | fails 1923–24 | passes |
| 10. Fuel security (unmet ≤ 2% of flexible demand; no coal beyond reach) | passes | passes | passes |

## The concessions (CR-053)

Entitlement crude added to "Most oil that can be imported", in every case (MODEL): Maracaibo (Lago Petroleum minority, 1923–24) 3m bbl in 1926, 9m in 1929, 12m in 1932; De Mares (Tropical Oil minority, 1920–21) 1, 4, 5; Peru (Lobitos and the northern concessions from 1924, the Union's reciprocal fifth) 4, 7, 7; Bahrain 0.3m in 1932; Kuwait and Mesopotamia nothing before 1932. Together 8m bbl in 1926, 20m in 1929 and 24m in 1932: about 7% of 1929 imports. The Gulf still binds.

## Sensitivity runs (second build, Story before A–C; one change at a time)

Carried from earlier notes for reference; they were run on the second build's Story case and are not re-run on the eleventh.

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
| Levers | 99 levers, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
| Anchors | US series used by formula (population, utility capacity, total generation, primary energy from EIA Table E1) and 85 anchor facts with source and status. |
| Paths | 110 benchmark-year paths (the CR-053 concessions, `dual_share`, `h_hilo`, `ind_idx`, the aluminium-use memos, the three CR-055 dams and the zinc, magnesium, phosphorus and copper lines) and 26 Max-case variants: intensities, shares, tonnages, capacity by basin, the halls' range. |
| People & output | 27 finance series, Story and Stress side by side (red), the active one picked by the case. |
| Hydro | Eight basins, the Works' dams, Rock Island, the Hawaiian hydro board, Bonneville, Rocky Reach, Wells, McNary and Chief Joseph (CR-055), Boulder Canyon and the (off) mid-Columbia chain; output in a normal or dry year; potential used; lead times. |
| Strategic loads | The halls (with the arc power freed, the Works' dams and the Columbia–Sierra line), the feed plant, the Columbia station and Rock Island's balance, the gaseous-diffusion plant (1930–32), the walled college, Hilo and Hawaii's island grid, the navy, the canal; register of sources. |
| Uses | Electricity in 23 sectors (sixteen of them electrochemical, hydrogenation, rubber and pig iron included, plus the Northwest mill boilers) with the aluminium-use memo; fuel in 13; conversion; the use-side primary total. |
| Electricity | Demand, losses, Hawaii's grid, hydro, steam and atomic supply, peak, capacity, reserve, capacity factors, fuel, per person, the multipliers, the halls' shares, the Northwest's own balance (firm load, the line, the mill boilers, spill), the dry-year test. |
| Fuels | Oil allocated where it is available (motor fuel, lamps, the navy, bunkers and the feed plant first); the short-year cascade (stocks, exports deferred, the switch to coal-capable plant, motor-fuel rationing, unmet demand); then Realm coal under its ramp and ceiling, extra wood and imported coal for the rest; gas from the oilfields; the concession crude; the supply-side primary total; import shares; intensity against the US. |
| Finance link | Investment, the Development Fund's credit (capped) and private financing, revenue (gross, utility, self-generation), royalties and fuel trade in money; named columns `en_*`, mapped by payer and recipient in `claude/finance-investment-share-note.md` v2. |
| Events | 58 dated canon commitments, approved discoveries and the CR-053, CR-054 and CR-055 positions. |
| Checks | The nine tests of handoff §7 and the fuel-security test, year by year, and the failing tests. |
| Changes | Revision history. |

## Limits of the model

- **Two systems, one line.** The Northwest's firm load comes first, then the Columbia–Sierra line (Paths `tie_mw`, Story 300–600 MW from 1924, at `tie_lf` 0.7), then the mill boilers; what is left is spilled. When the firm load exceeds the river (Stress 1924), steam or power from the south makes it up in one pooled balance. California and the Northwest are otherwise pooled. A two-system grid with its own peaks is the next refinement.
- The financial workbook does not yet read the `en_*` columns and was not re-run. The Story case needs from it: the home-oil path (with M8), about 2.15m vehicles a year by 1929, power investment of $0.8–1.1bn a year in 1922–29, the concession stakes' cost and dividends (CR-053), the investment-share path and `ind_idx` (M2), and the champions, dams and line of CR-054 and CR-055.
- Hilo is on the Hawaiian hydro board's plants (CT6, approved); Honolulu's grid stays oil-steam.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; the concessions enter only as entitlement crude; no trade block yet for partners' equipment purchases.
- Industrial self-generation is separated from utility receipts only by a share (`self_gen`), not by plant.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, Fowler's Water-Supply Paper 493, and the CR-053 historical anchors (Venezuelan, Colombian and Peruvian output; Holmes's dates; the Red Line shares). [README.md](README.md) lists the downloads.

- Hydrogenation (CR-055) is carried as a load and a motor-fuel memo (5m bbl in 1929); the residue it converts is not taken out of the fuel-oil balance, so its small effect on imports is not shown.
