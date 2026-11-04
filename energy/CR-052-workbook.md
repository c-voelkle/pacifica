# Workbook note, 4 November 2026: the energy workbook (CR-052, CR-054 and CR-055), fourteenth build

Built from the financial workbook with its CR-052 energy link (SHA-256 recorded on the Start sheet; `finance/CR-052-workbook.md`) by [`build/extract_finance.py`](build/extract_finance.py) and [`build/build_energy_workbook.py`](build/build_energy_workbook.py), then recalculated in LibreOffice: 29,029 formulas, no errors, in all three cases. The two workbooks read each other and were iterated to a fixed point (README, "Reproduce"). All amounts are MODEL estimates; every input is a blue cell with its basis beside it.

The model follows the handoff (`claude/energy-workbook-handoff.md`), the storyline with CR-051 integrated (4 November), the author's decisions recorded in CR-052 (CT1, CT2, CT3 A–C, CT5, CT6, CT9, the narrowed Max decision, the power seat, Northwest capacity), CR-053, CR-054 (A6 decided) and CR-055.

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
| Eleventh | **Consistency with itself and the story** (author, 4 Nov: "make it consistent with itself and the story"). (1) **The Columbia–Sierra line is used.** In the tenth build the Northwest's firm load plus 5 TWh of mill boilers left the line idle from 1925 to 1929, while the halls still drew 106–109 MW from the Sierra grid; now the line takes the river's surplus first (`tie_flow`, at most capacity × `tie_lf` 0.7), the mill boilers take what is left as secondary power (`nwboil_room`; the mills burn fuel for the rest), and the line's delivery counts in the halls' dedicated supply (`tie_halls`, after 8% losses): the halls draw nothing from the grid from 1924. (2) **Hydrogenation at a believable hydrogen consumption with fewer barrels** (author: "fewer barrels"): `h2_kwh` 240 (about 4 kg of hydrogen a barrel, to verify; was 100) and `hyd_bbl` 9m bbl in 1929 (was 35m): 2.2 TWh, 5m bbl of motor fuel gained. (3) **The gaseous-diffusion plant of CR-051** (pilot about 1926, plant 1930–1932) as a strategic load at the Columbia station (`diff_mw`, 150 MW in 1932; site PROPOSED in CR-055 R3). (4) **Wenatchee takes most of Rock Island's output**, as CR-051 says (`alu_wen` 30–32 kt in 1927–29, inside the Columbia's aluminium; the total is unchanged). (5) Stale notes corrected (`nw_spare`, `hilo_src`, `colms_on`). **Result:** Story 2.39–3.17× US electricity per person in 1920–32, 2,532 kWh a head in 1929 (88 TWh); the line carries 1.8–3.7 TWh a year south from 1924; the mill boilers 2.0–2.3 TWh in 1927–29 instead of 3.5–5; all checks pass. |
| Twelfth | **Northwest capacity for both the line and the boilers** (author: "add NW capacity and keep both"): Columbia second units in the Bonneville and Rocky Reach powerhouses (`h_col2`, decided 1923: 450 MW in 1925, 1.1 GW by 1929; `cf_col2` 0.35 on the freshet's secondary water; `col2_on`, Stress 0). The mill boilers get their full path in every year (5.0 TWh in 1929) and the line its full capacity. **The financial workbook's energy link** (`finance/CR-052-workbook.md`): this workbook's home oil and vehicles now drive the financial workbook's Story case, whose output is 3.2% higher in 1929; this workbook re-reads it (iterated to a fixed point), so the "home oil above finance" row is zero in every year: the 1932 compact is a price floor in both workbooks (author, 4 Nov 2026). `export_energy.py` writes what the financial workbook reads; `ind_src` (off) reads the financial workbook's industrial index. **Result:** Story 2.40–3.17× US electricity per person in 1920–32, 2,617 kWh a head in 1929 (93 TWh); no oil demand unmet; all checks pass. |
| Thirteenth | **Re-read after the financial workbook's CR-051/054/055 build** (`finance/CR-051-054-055-workbook.md`); formulas and inputs unchanged. The financial workbook's output is 0.3% lower in 1929 and its Development Fund invests less in 1920–24 and in the slump, so the Fund's power credit is smaller (Story $95m in 1932, was $126m) and more is privately financed; every other result moves by under 0.2% (2,614 kWh a head in 1929, was 2,617; the multiplier 2.40–3.17 unchanged); all checks pass. `export_energy.py` now also writes the series the financial build reads (the strategic dams' capacity, the halls, the feed plant, the station, the diffusion plant, Rock Island's balance, the aluminium memo and the CR-054/055 quantities). The tables below are the twelfth build's. |
| Fourteenth (this note) | **The strategic dams costed as decided** (author, 4 Nov 2026, the financial workbook's PR #64 decisions 4 and 5): the five Columbia dams (Bonneville, Rocky Reach, Wells, McNary, Chief Joseph) at plant plus bulk lines (`cost_bulk` $30/kW, no distribution: about $1.0bn current in 1908–32 instead of $1.45bn) and the Columbia second units at `col2_cost` 0.4 of a new plant (about $0.19bn instead of $0.48bn). Power investment in Story is $1.04bn in 1929 (was $1.15bn); energy results are unchanged; all checks pass. Re-iterated with the financial workbook to a fixed point. The tables below are the twelfth build's. |

## Story case (canon with the approved decisions)

Eleventh-build values in brackets where they changed.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |2.1|14.5 (14.3)|33.0 (32.4)|42.7 (41.9)|57.4 (56.4)|79.4 (76.4)|92.6 (88.1)|95.4 (93.9)|
| Capacity (GW) |1.1|6.2 (6.1)|12.6 (12.5)|15.9 (15.6)|20.7 (20.3)|28.6 (27.4)|33.6 (31.8)|37.2 (36.3)|
| … hydro (GW) |0.4|2.4|5.4|6.7|8.5 (8.4)|12.6 (11.9)|15.5 (14.4)|18.0 (16.9)|
| Hydro share |71%|66%|64% (65%)|65% (66%)|69%|73%|76%|82% (83%)|
| kWh per person |194|720|1,273 (1,271)|1,535 (1,534)|1,914 (1,915)|2,396 (2,346)|2,617 (2,532)|2,522 (2,523)|
| × US electricity per person |—|2.45|2.40 (2.39)|2.76|2.84|2.81 (2.75)|2.73 (2.64)|3.17|
| × US utility capacity per person |—|5.02|4.08 (4.09)|4.43 (4.44)|4.12 (4.13)|4.01 (3.91)|3.89 (3.74)|3.57 (3.54)|
| Halls / capacity |0.0%|0.0%|1.4%|2.2%|2.8%|2.4% (2.6%)|1.6%|1.4%|
| Halls / electricity used |0.0%|0.0%|5.0% (5.1%)|7.6% (7.8%)|9.3% (9.4%)|8.1% (8.4%)|5.2% (5.4%)|5.0% (5.1%)|
| Halls from the grid (MW avg) |0|0|0|33|0|0|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|1.8|2.5|3.1|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.5|1.5|3.5 (2.0)|5.0 (2.3)|7.0|
| Northwest hydro spilled (TWh) |0.2|1.6 (1.7)|3.7 (3.8)|3.6 (3.8)|0.0 (0.1)|0.1 (0.0)|0.0|4.6 (1.5)|
| Primary energy (PJ) |1,166 (1,156)|2,723 (2,709)|4,058 (3,973)|4,452 (4,348)|5,078 (4,966)|5,797 (5,659)|6,214 (6,063)|5,670 (5,552)|
| GJ per person |109|135 (136)|157 (156)|160 (159)|169|175 (174)|176 (174)|150 (149)|
| Home oil (m bbl) |74|228|275|280|304|274|255|229|
| Oil imported (m bbl) |6|38|104|130|157|226|305|236|
| Oil share for rail, industry, power |72% (73%)|100%|95% (99%)|93% (97%)|97% (100%)|93% (96%)|100%|89% (94%)|
| Coal imported (Mt) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Would have to import |3%|9%|16%|18%|19%|24%|30% (31%)|25% (26%)|
| Vehicles per person |0.00|0.03|0.14|0.19|0.24|0.30|0.33|0.33|
| Vehicles to build (thousand) |0|202 (200)|1,179 (1,158)|1,525 (1,487)|1,845 (1,816)|2,106 (2,069)|2,177 (2,148)|1,564 (1,531)|
| Home oil above finance (m bbl) |0 (49)|0 (128)|0 (160)|0 (130)|0 (74)|0 (21)|0 (-45)|0 (76)|
| Power investment ($m) |35 (34)|170 (169)|503 (494)|820 (806)|910 (890)|1,146 (1,109)|1,148 (1,001)|696 (678)|
| Power investment / GDP |0.6%|0.9%|0.9% (1.0%)|1.8% (1.9%)|1.7%|1.8%|1.6% (1.4%)|1.2%|
| Checks failing |—|—|—|—|—|—|—|—|

**Fuel security (Story).** Oil demand left unmet is zero in every year; no motor fuel is rationed; no coal is imported; the coal ramp never binds. What the short years cost instead:

| Story |1915|1917|1918|1920|1924|1925|1926|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|---|---|
| Asian exports deferred (m bbl) |10|12|12|14|18|18|20|20|14|18|
| Switched from oil to coal (PJ) |199|304|196|78|56|131|202|133|0|162|
| Motor fuel rationed (PJ) |0|0|0|0|0|0|0|0|0|0|
| Unmet (PJ) |0|0|0|0|0|0|0|0|0|0|
| Stocks (days) |0|0|0|0|0|0|0|0|0|0|

**The switch to coal is within the coal-capable plant in every year** (304 PJ in 1917 against about 1,300 PJ of switchable demand; more than in the eleventh build because the financial workbook's higher output wants more oil), so the short years are a managed change of fuel, not a shutdown. **Stocks are exhausted from 1915 and never rebuilt,** because the import ceiling binds in every year after that and the model refills tankage only from surplus: the Realm's real oil reserve in the 1920s is its dual-fuel plant and the Gulf, not its tanks. The deferred exports are home-refined products the trust does not ship to Asia in those years; the Asian contracts are served from Gulf crude instead, which the financial workbook's `asia_home` share should reflect (OPEN). The line's power from 1924 displaces oil-fired steam in California.

- **The multiplier is about two and a half:** 2.40–3.17 times US electricity per person in 1920–32 (1932 is the US slump), about 2,620 kWh a head in 1929. The rise over canon's earlier uses (1.86–2.30) is homes (14 TWh in 1929), the main lines (railways 12 TWh), CR-054's champions and CR-055's river (electrochemistry 13 TWh) and the mill boilers (5 TWh). With the financial workbook's industrial index (`ind_src` = 2, off) it would be 2.43–3.11, and check 4 fails in 1932.
- **Hydro carries it:** 15.5 GW in 1929, of which Boulder Canyon 1.3 GW from 1926 and the Columbia second units 1.1 GW; hydro is 64–82% of generation in 1920–32. The Northwest spills 3–5 TWh a year in 1919–23 (before the line), almost nothing in 1924–29, and 1.2–4.6 TWh in 1930–32, when the slump, Chief Joseph and the second units leave the river ahead of its customers until the diffusion plant grows (CR-055 R3).
- **The halls (CR-051):** at full size (700 MW, 1925–27) about 2.4–2.8% of capacity and 8–9% of electricity (CT1: the storyline's wording is amended at integration). They draw 33 MW from the Sierra grid in 1922 and nothing from 1924.
- **Oil:** home oil peaks at 304m bbl in 1924 and is 255m in 1929; railways, industry and power get 89–100% of the oil they want in 1913–32 before the switch to coal-capable plant, and no demand goes unmet. The Gulf binds in 1929 (305m bbl imported, with the concessions' 20m); imports are 30% of primary energy. No coal is imported in any year.
- **Money:** power investment /bin/bash.8–1.15bn a year in 1922–29 (1.6–1.9% of GDP); the financial workbook now carries it inside gross domestic investment (about 6% of it in the late 1920s) and the Development Fund's credit as a share of what the Fund invests (31% in 1929). Check 6 passes in every year.
- **1929 electricity, 82 TWh used:** factory motors 21.6 TWh, homes 14.2, railways 12.2, electrochemistry 13 (aluminium 3.3, hydrogenation 2.2, pig iron 1.4, electric steel 0.9, ammonia 0.8), commerce 7.4, mill boilers 5.0, mining 2.9, pumping 1.0, the strategic loads 4.6.

## Max case (exploration)

Max keeps the parts Story did not take (process heat electrified through `indw_x`, aluminium at Alcoa's scale, more electrolytic ammonia and electric steel, the Central Valley pumped harder, 100% of the fields' deliverability). Eleventh-build values in brackets.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |2.2 (2.1)|15.5 (15.3)|37.0 (36.3)|49.4 (48.3)|66.6 (65.3)|91.8 (90.2)|107.7 (105.8)|113.3 (108.3)|
| Capacity (GW) |1.1|6.5|13.9 (13.7)|18.0 (17.7)|23.6 (23.2)|32.4 (31.6)|38.2 (37.2)|43.1 (41.0)|
| … hydro (GW) |0.4|2.4|5.4|6.7|8.5 (8.4)|12.6 (11.9)|15.5 (14.4)|18.0 (16.9)|
| Hydro share |69% (70%)|63%|59%|59%|59% (60%)|63% (62%)|66% (64%)|73%|
| kWh per person |202|767|1,426 (1,422)|1,776 (1,770)|2,222 (2,218)|2,770 (2,766)|3,044 (3,041)|2,995 (2,912)|
| × US electricity per person |—|2.61|2.68|3.19 (3.18)|3.29|3.25|3.18 (3.17)|3.76 (3.66)|
| Halls from the grid (MW avg) |0|0|0|33|9 (0)|0 (96)|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|0.9 (1.1)|1.8 (0.1)|2.2 (0.0)|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.5|0.0|0.0|0.0|5.7 (3.2)|
| Northwest hydro spilled (TWh) |0.1|1.5|3.2 (3.4)|2.4 (2.6)|0.0|0.0|0.0|0.0|
| Home oil (m bbl) |83|254|305|311|338|304|283|254|
| Oil imported (m bbl) |6|36 (32)|104|130|157|226|305|236|
| Power investment ($m) |35|177 (176)|599 (587)|978 (959)|957 (932)|1,204 (1,173)|1,283 (1,205)|810 (783)|
| Checks failing |—|—|—|—|—|—|—|—|

In Max the Columbia's larger firm loads (aluminium and ammonia on the river) take most of the river even with the second units: the line carries 0.9–2.2 TWh in 1924–29 rather than Story's 1.8–3.1, the mill boilers get nothing until 1930, and the halls draw 9 MW from the grid in 1924 (the eleventh build's 96 MW in 1927 is gone). Max is an upper bound on use, not a better-balanced Story (author: "Yikes, but ok").

## Stress case

The lean case: the fourth build's electricity per home (`home_kwh_x` = 0.5), no mill boilers and no second units, the hydro pace before M7 (`hydx_on` = 0), Boulder at 1928, the main lines on steam and the financial workbook's own (pre-CR-052) oil and vehicle paths; the CR-055 dams and the line as in Story. Eleventh-build values in brackets.

| |1900|1913|1920|1922|1924|1927|1929|1932|
|---|---|---|---|---|---|---|---|---|
| Generation (TWh) |1.7|9.4|19.4|23.8|31.2|40.6|43.8|39.4|
| Capacity (GW) |0.8|4.0|7.4|8.7|10.9|14.2|15.8|15.7|
| … hydro (GW) |0.3|1.7|3.6|4.3|5.3|7.2|8.4|10.1|
| Hydro share |65%|70%|68%|68%|49%|77%|83%|97%|
| kWh per person |196|703|1,185|1,379|1,707|2,045|2,092|1,793|
| × US electricity per person |—|2.39|2.23|2.48|2.53|2.40|2.18|2.25|
| Halls from the grid (MW avg) |0|0|0|81|261|0|0|0|
| Columbia–Sierra line, south (TWh) |0.0|0.0|0.0|0.0|0.0|2.5|3.1|3.7|
| Northwest mill boilers (TWh) |0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
| Northwest hydro spilled (TWh) |0.1|1.4|3.6|4.2|0.0|3.0|4.0|10.6|
| Home oil (m bbl) |25|100|115|150|230|253|300|180|
| Oil imported (m bbl) |6|23|62|78|96|65|34|103|
| Power investment ($m) |33|133|281|479|532|605|526|356|
| Checks failing |3|3|—|2|9|—|—|—|

Failing: check 3 in 1876–1916 (the financial workbook's oil runs ahead of the historical fields), check 2 in 1922 and check 9 in 1923–24. Stress spills 3–11 TWh a year on the Northwest from 1927, because it has the CR-055 dams but not their customers (accepted by the author).

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
| Levers | Every lever, Story, Stress and Max, each with a named range, status and basis; `case_sel` in E4. |
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

- **Two systems, one line.** The Northwest's firm load comes first (the Columbia second units add secondary water), then the Columbia–Sierra line (Paths `tie_mw`, Story 300–600 MW from 1924, at `tie_lf` 0.7), then the mill boilers; what is left is spilled. When the firm load exceeds the river (Stress 1924), steam or power from the south makes it up in one pooled balance. California and the Northwest are otherwise pooled. A two-system grid with its own peaks is the next refinement.
- The financial workbook reads this workbook's home oil, vehicles, power memos and concession crude through `export_energy.py` (`finance/CR-052-workbook.md`). Not yet carried there: the CR-054 and CR-055 champions' output, the power stations' financing beyond the Fund's credit memo, `asia_home` after 1915, sector prices.
- Hilo is on the Hawaiian hydro board's plants (CT6, approved); Honolulu's grid stays oil-steam.
- Partners' own energy, and production abroad (Emba, Baku, Grozny–Maikop) except as oil the trust can ship home; the concessions enter only as entitlement crude; no trade block yet for partners' equipment purchases.
- Industrial self-generation is separated from utility receipts only by a share (`self_gen`), not by plant.
- The Columbia second units are costed at `col2_cost` (0.4) of a new plant with its lines, and the five strategic Columbia dams at plant plus bulk lines (`cost_bulk`), since the fourteenth build; other hydro at plant plus lines and distribution.
- The atomic stations' cost stays in the financial workbook's Atomic sheet.

## Anchors

Verified in the sessions: US primary energy by source 1850–1935 (EIA Annual Energy Review Table E1, from Schurr and Netschert); US central stations 1907, 1912 and 1917 and California, Washington, Montana and the Pacific division in 1917 (*Census of Electrical Industries 1917*, supplied by the author); manufacturing's electric drive 1899–1929 (Devine 1983, Table 3, supplied by the author); crude output by state 1931–32 and California's leading fields (*Minerals Yearbook 1932–33*, p. 472, supplied by the author); US electricity in 1930 (Construction Physics); California oil in 1895 and 1900. Carried from the CR-051 power check: California hydro 1922, PG&E 1911, Oak Ridge 1945. Still TO VERIFY: the 1920s US series, Norway, Canada, Switzerland, most state coal and oil series, Fowler's Water-Supply Paper 493, and the CR-053 historical anchors (Venezuelan, Colombian and Peruvian output; Holmes's dates; the Red Line shares). [README.md](README.md) lists the downloads.

- Hydrogenation (CR-055) is carried as a load and a motor-fuel memo (5m bbl in 1929); the residue it converts is not taken out of the fuel-oil balance, so its small effect on imports is not shown.
