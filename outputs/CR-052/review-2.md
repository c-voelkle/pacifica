# CR-052 — fresh-context review of the third build (3–4 November 2026)

Independent reviewer, given the third build (the author's sources, CT3 A–C and CT5 in the Story case, and the new Max case), its inputs and build script, the first review and AGENTS.md; no access to the drafting conversation. The dispositions record what the fourth build changed.

## Verdict (reviewer)

Case switching, named ranges and the new formulas are correct, and the Story case behaves as intended. Before the author relies on the numbers: fix the double-counted electrification pace in Max, which drives much of its "4× the US"; derive the oil capability and reserve paths, which were fitted to the Max path and counted barrels that need later technology, so check 3 could not fail; and move Kettleman Hills from 1915. With those fixed, and Max read only from about 1922, Max is a defensible upper bound. The Northwest surplus is best spent on Columbia electrochemistry, electric boilers and pumping, not on a 700-mile tie line.

## Findings and disposition

| # | Finding | Disposition |
| --- | --- | --- |
| MUST 1 | Max multiplies its already raised electrification paths by `elec_pace` 1.15: factories at 83% electric in 1920, homes at 100% from 1924. | Removed: `elec_pace` is 1 in Max. |
| MUST 2 | `oil_cap` was fitted to the Max path; it summed flush peaks as if simultaneous; no decline. | **Replaced by a field-by-field model** (22 fields, canon and historical discovery years, peak, primary recovery): each field ramps (more slowly before 1905, when rigs and markets were few) and declines at the rate its primary recovery allows. `oil_cap` is the model's deliverability; Story produces 90% of it, Max 100% with 30% more recovery from early pressure maintenance and water flooding. The financial workbook's own path is tested against the same fields at their historical years (`oil_caph`). The model at historical years gives 94m bbl in 1913 (history 98), but 401m in 1923 (history 263) and 347m in 1929 (history 293), so its flush peaks are generous; stated in the note. |
| MUST 3 | Kettleman Hills about 1915 needs a 7,000 ft producing well. | Moved to 1923; its gas only from 1923. |
| SHOULD 1 | `oil_known` used modern ultimate recoveries (steam flood). | Primary recovery with 1900–1930 methods only: 13.5bn bbl for all the fields by 1923 (Story); 17.6bn with Max's secondary recovery. Story's cumulative output is 7.2bn by 1932. |
| SHOULD 2 | The output path itself (70m bbl in 1900 above all US output; 420–450m in 1927–31). | Now from the field model. Finding the giants early front-loads the oil: Story peaks at about 272m bbl in 1924 and falls to 216m in 1929 and 159m in 1932. The finance-price value of extra oil is kept as a memo. |
| SHOULD 3 | Max double counts electrified heat against fuel. | Max paths for industrial fuel (`ind_mj`) and home heat (`gj_home`) lowered; Northwest mill boilers subtract 5.1 MJ of fuel per kWh. |
| SHOULD 4 | Aluminium at 280 kt equals world output, with no bauxite named; electrolytic nitrogen needs Japan's market. | Aluminium 180 kt in 1929 (Alcoa's scale), 140 kt on the Columbia; bauxite from Guiana and Bintan through partners (to verify); electrolytic ammonia for the Valley and for Japan. |
| SHOULD 5 | Max at 4.0–4.3× the US in 1913–17 is not believable. | Max now diverges from Story after 1915 (multiplier paths `indw_x`, `hyd_x`; Max paths for 1913 close to Story): 2.6–3.0× in 1913–19, 2.6–3.6× in 1920–32. |
| SHOULD 6 | Northwest: `nw_ord` unused; spare is secondary power; the pooled model burns it in California. | `nw_ord` removed. **Northwest power beyond the Northwest's own load is now spilled** unless a line carries it (`tie_mw` = 0 in every case), in all three cases. Max adds electric boilers in Northwest mills (5 TWh in 1929), all electrolytic ammonia and most aluminium on the Columbia, and a smaller mid-Columbia chain (1.5 GW). |
| SHOULD 7 | Max relaxes the check bands unnecessarily. | Story bands restored for Max. |
| NOTE | Max electric steel before 1907; the note's "about bn" typo; Story primary energy rose with motor fuel; coal no longer binding; vehicles in 1913 high. | Electric steel 0 to 1900; typo fixed; noted; vehicles 0.025 per person in 1913 (about 200,000 built that year). |
