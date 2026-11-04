# Workbook note, 4 November 2026: the financial workbook's energy link (CR-052, with CR-053 to CR-055)

SHA-256 `6840f3811a803c464980eaccded883d220072e129acb362195df2d9b3f98da1c`. Built on the CR-050 workbook (`22266bad…`) by [`build/cr052_energy_link.py`](build/cr052_energy_link.py) from `energy/build/energy_outputs.csv` (energy workbook `846828f3…`), then recalculated in LibreOffice: 54,321 formulas, no errors. No check fails in the Story case in any year; the Stress case fails the same 12 year-checks as before. Paths C was not re-iterated, but **residents still rise**, by 1.1% in 1913 and 1.5% in 1929–32, through the workbook's own migration pull (Labour AL: a richer Pacifica draws more arrivals). All amounts are MODEL.

**Authorization.** Author, 4 November 2026: "Let's rebuild the financial workbook first and assess what this merge would change. Then report back to me before merging please." The approved decisions it carries: CR-052 CT3 C (home oil found with the greatest believable haste), M8 (water flooding fifteen years early) and CT5 (California the most motorized place on earth). The CR-053 stakes and the investment and consumption account carry PROPOSED amounts.

## What changed

| Item | How | Case |
| --- | --- | --- |
| Home oil | The energy workbook's field model (Fuels "Home oilfields") replaces `Resources!I`, the output before any compact. | Story (`en_paths` = 1); Stress keeps the earlier path |
| Motor vehicles built | The CT5 path (energy Uses "Vehicles the finance workbook must build") replaces `Champions!U`. | Story; Stress keeps the earlier path |
| CR-053 stakes | $65m bought in 1920–28 (Tropical Oil $12m, Lago Petroleum $20m, the Peruvian company $24m net of the Union's reciprocal fifth, Holmes's options $1m, the Mesopotamian share $8m) out of ordinary investment abroad (`Abroad!C`) into the champions' assets abroad at book (`Champions!AY`); kept out of the non-oil base of `Capital accounts!C` so that Champion funding does not finance them a second time; a return on the entitlement crude (`conc_div`, 30 cents a barrel) in the champions' earnings abroad and the chartered industries' profits. | Both |
| Power | The energy workbook's power investment, Development Fund credit, utility receipts, royalties and oil imports, as memos on the new **Energy link** sheet. No GDP effect: the utilities are already inside non-mining output. | Both (each case's own figures) |
| Investment and consumption account | `finance/investment-share-note.md` v2, item 1: gross domestic investment on the `inv_share` test path (Story 26% in 1913, 27–29% in the 1920s; Stress five points lower, `inv_gap`), government consumption, net exports, household consumption per person and against the US (1929–32). Reporting only. | Both |
| Industrial index | Item 2, the proportional baseline: the investment share over its 1913 value (Energy link AC), exported to the energy workbook, which reads it only when its lever `ind_src` = 2 (off). | Both |

Not done (OPEN in the note or elsewhere): sector-specific prices (item 3); `asia_home` after 1915; an industrial-output derivation beyond the proportional index; CR-051's costs (the halls, the feed plant, the Columbia station and the Works' dams); the power stations' and the Columbia line's financing in the Budget (the Development Fund's credit is a memo, inside what the Fund already invests).

## Results, Story case (before the change in brackets)

| |1880|1900|1913|1918|1922|1929|1932|
|---|---|---|---|---|---|---|---|
| Oil output (m bbl) |0.05|74 (25)|228 (100)|252 (105)|280 (150)|255 (300)|194 (153)|
| Vehicles built (thousand) |0|0 (0.5)|202 (170)|930 (280)|1,525 (500)|2,177 (1,150)|1,564 (450)|
| Residents, end of year (m) |4.36|10.32 (10.28)|19.45 (19.24)|23.18 (22.90)|26.84 (26.42)|33.92 (33.41)|36.76 (36.19)|
| Champions at home ($m) |26|236 (213)|843 (752)|2,308 (1,820)|2,874 (2,170)|4,661 (4,186)|3,132 (2,580)|
| Core GDP ($m) |1,404|5,585 (5,501)|18,236 (17,804)|39,313 (38,081)|45,129 (43,364)|71,516 (69,318)|56,552 (54,660)|
| × US GDP per person |1.58|2.17 (2.15)|2.29 (2.27)|2.24 (2.20)|2.43 (2.38)|2.39 (2.35)|3.18 (3.13)|
| Real GDP (1913 $m) |1,755|7,348 (7,239)|18,236 (17,804)|23,682 (22,941)|28,563 (27,445)|44,698 (43,324)|41,219 (39,840)|
| Receipts ($m) |188|567 (555)|1,815 (1,762)|4,608 (4,446)|4,760 (4,548)|7,817 (7,568)|5,518 (5,324)|
| Budget balance ($m) |68|100 (94)|374 (353)|1,185 (1,113)|1,066 (988)|1,936 (1,857)|317 (284)|
| Public debt ($m) |0|279 (275)|912 (890)|1,966 (1,904)|2,256 (2,168)|3,576 (3,466)|3,014 (2,937)|
| Reserve Fund ($m) |62|110 (106)|283 (268)|385 (358)|640 (593)|1,236 (1,156)|1,381 (1,293)|
| Development stock ($m) |462|1,327 (1,287)|3,864 (3,681)|5,917 (5,547)|9,441 (8,784)|17,732 (16,701)|18,002 (16,960)|
| National income ($m) |1,411|5,601 (5,518)|18,402 (17,972)|39,595 (38,372)|45,882 (44,121)|72,996 (70,773)|57,513 (55,588)|
| Gross domestic investment ($m) |281|1,396|4,741|8,649|12,636|20,024|13,573|
| Power / investment |0.0%|2.5%|3.6%|3.6%|6.5%|5.7%|5.1%|
| Fund's power credit / the Fund's investment from surpluses |0%|19%|26%|37%|46%|31%|60%|
| Household consumption / GDP |74%|68%|67%|68%|64%|65%|72%|
| Household consumption per person ($) |244|361|619|1,123|1,059|1,335|1,090|
| × US consumption per person |—|—|—|—|—|2.10|2.79|
| Checks failing |0|0|0|0|0|0|0|

**Where the extra output comes from.** In 1929 core GDP is $2.2bn (3.2%) higher. The champions add $0.33bn to GDP (their value added at home is $0.48bn higher: vehicles +$0.51bn, home refining −$0.05bn; GDP takes about 0.69 of it), mining and oil −$0.04bn (less oil in 1929 than the old path, more before) and the guest workers $0.24bn. Non-mining output is $1.66bn higher, for three reasons: about $0.97bn because there are 1.5% more residents (the migration pull of a richer Pacifica), about $0.57bn because output per resident is 0.9% higher (the extra oil royalties, Crown dividends and surpluses of 1900–1927 go into the Development Fund, whose stock is $17.7bn in 1929, $1.0bn more), and about $0.12bn from the extra talent. These are the workbook's own mechanisms, unchanged; the energy link only feeds them.

**Population.** Because the storyline's population figures follow this workbook (AGENTS.md), merging moves them: residents in 1932 are about 36.8 million, not 36.2 (the storyline's "about 36 million" becomes about 37), and the origin shares move with them. The population model (`population/`) is not re-run here.

**Consumption.** Pacificans' household consumption is about two thirds of GDP and about twice the US's per person in 1929 ($1,335 against about $636), 2.8 times in 1932 when the US slump is deeper. On the investment-share note's test, a 27–29% investment share in the 1920s still leaves Pacificans visibly better off than the Union's citizens. The account counts net exports as net foreign investment (private investment abroad less repatriations, the Entente share, public lending, the champions' cash investment abroad net of what foreigners finance) less net income from abroad (including the interest on public loans abroad); it counts the separation halls and weapons, like other military spending, as government consumption, the atomic power stations and the Development Fund's investment events as investment, and new monetary gold outside consumption. The precise ratio depends on these conventions; "about twice" does not. US figures are BEA personal consumption over population (to verify).

**Stress** keeps its earlier paths; only the CR-053 stakes move it, and only a little: the champions' assets abroad are about $65m (1.3%) higher in 1929 and the portfolio about $56m lower, so total private assets abroad change by under 0.1%; receipts are about $1m higher; GDP, debt and residents move by amounts too small to show.

## The two workbooks together

The energy workbook reads this workbook's population, output and industry, and this workbook reads the energy workbook's oil, vehicles and power: the pair was iterated to a fixed point (energy outputs unchanged to six figures on the last pass). This workbook was built last and records the energy workbook it read (`846828f3…`, Energy link A2). The energy workbook records the financial workbook of the previous pass (`f0e743b7…`), whose values it reads are identical to this one's: re-running `extract_finance.py` on this workbook reproduces `energy/build/finance_inputs.csv` exactly. Because each records the other's hash, the pair is checked by values, not by hashes. See `energy/README.md` for the loop.

## Questions for the author

1. **The 1932 oil compact.** This workbook cuts 1932 output by 15% (`oil_compact`, Proposed, CR-020 B6): 194m bbl. The energy workbook's Story case treats the compact as a price floor (`compact_on` = 0, Proposed, CR-052): 229m bbl. One of the two should change; the energy workbook shows the gap as "home oil above finance" (34m bbl in 1932).
2. **The oil price.** The early oil (228m bbl in 1913, about three fifths of world output) is sold at the workbook's historical price path. A Pacifica producing that much would push the world price down; the workbook does not model it, so oil revenue in 1900–1920 is an upper bound.
3. **The investment-share path** (Energy link Y, PROPOSED): adopt the test path as Story? It is reporting only here and moves nothing else. With the energy workbook's `ind_src` = 2 (the proportional industrial index) Story's multiplier is 2.43–3.11× in 1920–32 instead of 2.40–3.17×, and its check 4 (intensity bands) fails in 1932.
4. **CR-053's amounts** ($65m of stakes, 30 cents a barrel) are PROPOSED.
5. **Population.** Accept the migration pull's extra residents (about 37 million in 1932) into the storyline's MODEL figures at integration, or hold them at 36 million by re-iterating Paths C against the population model?

## Review

A fresh-context review (separate agent, 4 November) of this build found the results table and the switches correct and five errors in the first draft of this note and the account: residents do rise; the decomposition credited the wrong mechanism; the CR-053 stakes were financed twice through Capital accounts and Champion funding; net exports left out repatriations, the champions' cash investment abroad and the interest on public loans abroad; and the Stress and SHA statements were wrong. All five are corrected in this version.
