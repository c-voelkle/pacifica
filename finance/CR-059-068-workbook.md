# Workbook revision, 14 November 2026: the Civil War CRs (CR-059 to CR-065, CR-067, CR-068), Alaska (CR-070) and the members' land (L15)

**Superseded as the current workbook on 15 November 2026 (evening):** CR-056 and CR-057 are now built on top of this package; see [CR-057-on-main-workbook.md](CR-057-on-main-workbook.md).

SHA-256 of the current workbook: `a061a7ba809a1f405260bf6a1ec88982f188f9016611371db2409d80080c864c` (rebuilt on 15 November 2026 for the Legion's pay after the peace; see the fifth addendum at the end, the fourth for Columbia's charter, the third for the Sacramento line, the story assumptions and the Legion, and the second for the phase 9 review's six. The figures in the body are those of 14 November, SHA-256 `c5ebb7bb…`; the first addendum's are those of `9ac9d556…`).

**What it is.** The CR-051/054/055 workbook (SHA-256 `cba70b31…`) with the Civil War CRs' model items, built in two steps by the model plan of 13–14 November 2026 (session `outputs/sessions/20261113-model-register/`). All amounts are MODEL. The new events carry the status "Proposed" until their CRs are integrated, and a workbook label cannot approve a narrative proposal.

**Rebuilding.**

```
python3 finance/build/cr059_068_civil_war.py CR-051-054-055.xlsx step4.xlsx \
    --joins population/data/joins_cr059_068.toml --rates finance/build/paths_c_rates_cr059_068_final.csv
python3 finance/build/cr059_068_levers.py step4.xlsx OUT.xlsx --values finance/build/cr059_068_values.json
python3 /mnt/skills/public/xlsx/scripts/recalc.py OUT.xlsx 600      # LibreOffice; or open and save in Excel
```

Recalculated in LibreOffice: 63,439 formulas, no errors, saved in the Story case (Levers E4 = 1).

The natural-increase rates (Paths C) were iterated with the population model until they stopped changing. In two rounds the largest change fell to 0.000003 a year, and the model and the sheet now agree within 1,200 residents.

## What changed

1. **Fixed items** (`cr059_068_civil_war.py`; register in the session folder). Under the author's Q1–Q3 and Q12, every acceding territory joins at the exchange of 1867 (`population/data/joins_cr059_068.toml`). Also fixed:
   - London repaid first in 1859;
   - the re-dated compensation (E10);
   - the $40m vendor credit over 1867–72 (E11);
   - Baja switched off (E13);
   - the other fixed rows of the register.
2. **Levers** (`cr059_068_levers.py`; Levers rows 408–460, events E197–E231; rows 408–465 and events to E238 after the addendum). Values come from `finance/build/cr059_068_values.json`: package **D final** of the phase 7 decision sheet, every question approved by the author on 14 November 2026. In brief:
   - **The gold in the war (F18, L17).** No treasure steamers to New York in 1861–65; the gold held back goes east in 1866–67. War bonds may draw idle gold up to 0.12 (Story) or 0.06 (Stress) of notes and bank reserves.
   - **The war and the peace.** All at the package's values:
     - the Richmond credit, $11.7m over 1862–65;
     - the eastern mission, $0.1m a year;
     - the campaigns and garrisons above the head counts;
     - the Honolulu batteries and the second turret ship;
     - the Juárez credit, $16.9m;
     - the Oregon works, $86.9m over 1868–75;
     - private lending to the Union's bankers, $3m in 1867;
     - the instalments as six of $6.67m; the first, in 1867, is net of $5.45m of set-offs (Oregon's scrip at face, $3.2m, and the Northwest's annuities of 1862–66, $2.25m), so it pays $1.22m (E11), and the gold paid to the Union over 1867–72 is $34.55m;
     - Oregon's scrip, $3.2m face;
     - the regional annuities, each at the yearly size of its region's earmarked receipts (D4, MODEL working figures). The annuities run for twenty years (1862–81, 1863–82) and the receipts end in 1866–72, so $19.0m of annuities meet $7.85m of earmarked receipts; from 1873 about $0.95m a year has no earmark.
   - **People.** 20,000 refugees, deserters and draft evaders a year in 1863–65 (L12).
   - **Alaska (CR-070).** Sitka's garrison and squadron at $2.85m a year in 1867–72, then 40% of that (the settler garrison). The northern mail at $0.3m a year. Receipts:
     - the seal lease, tendered from 1880, with the herd saved;
     - the salmon case tax from 1870;
     - Juneau's gold eight years early (Resources E reads the historical path, kept in T, eight years on, capped at 1898). This adds gold rather than moving it: 1891–98 repeat the 1898 value, and with the Seward Peninsula's placers Alaska's gold over 1867–98 goes from $19.8m to $58.8m, with nothing taken away after 1898;
     - the Seward Peninsula's placers from 1876.
     The Northern Commission and the Chilkoot compact are in at their MODEL costs. The Bering telegraph's cost was in provisionally; the addendum of 15 November replaces it with the wire as decided.
   - **L15, the members' land.** A new sheet, `Members' land`. The new members' farm land from 1867 is taken from the census (1945 Census of Agriculture, Farms and Farm Property, Table 18), with western Montana at a quarter of Montana's. It is sold on the Land Fund's instalments at its floor price (`lfund_floor`, $1.25 an acre in Story, $1 in Stress), with no purchase cost, because the nations are paid by the regional annuities. This departs from Q7's "existing rules": the Land Fund prices California's land at the floor or `lfund_share` of the census value per acre, whichever is higher ($1.94 in 1867), so L15 as built understates its receipts. Oregon's customs share after 1867 is not built. Oregon's schools take one-eighteenth of the margin on Oregon's land. The net goes into Budget G beside the Land Fund's: $105m to the Treasury over 1867–1932, $32m of it to 1900, and $1.25m to Oregon's schools. Five OCR-garbled census entries are read as 3 where the scan prints 5; they are listed in the build script and are to verify against the scans.

## Results (MODEL)

| | Before (CR-051/054/055) | This revision |
|---|---|---|
| Story case: failed checks | 0 | 0 |
| Stress case: failed checks (ceiling 17, author) | 17 | 15 |
| Stress: margin of private saving, 1932 | +$7.9m | +$92.4m |
| Stress, 1932: debt within 30% of GDP | 33.1% (fails) | 28.7% |
| Stress, 1932: gold above the cover requirement | −$12.1m (fails) | +$11.1m |
| Stress, with the garrisons above the head counts 25% dearer | | 15 failed; margin +$85.9m |

| Story case | 1867 | 1900 | 1932 |
|---|---|---|---|
| Residents, before → now | 2.18m → 2.23m | 10.32m → 10.75m | 36.75m → 38.44m |
| Real GDP, 1913 $m | 649 → 624 | 7,350 → 7,909 | 41,054 → 44,602 |
| Public debt, $m | 3 → 70 | 279 → 301 | 3,036 → 3,281 |

- **The war.** It now costs Pacifica something: the debt at the end of 1867 is $70m instead of $3m, and 1867's GDP is a little lower.
- **What pays it back.** By 1900 the joins, the refugees, the Oregon works, Alaska's receipts and the members' land have more than made good the war's cost in output and people: 1900's real GDP and residents are higher than before. The debt is not paid back: it stays higher, $301m against $279m in 1900 and $3,281m against $3,036m in 1932.
- **Stress.** The 15 failures that remain are the baseline's own, in 13 years: 1887, 1914–24 and 1927, with 1918 and 1919 failing two checks each (private saving and the Siberian line). No year fails that did not fail before, so the strict rule holds. 1932 now passes every check. The base's two 1932 failures were the debt ratio and the gold cover, not private saving; the tightest 1932 check is now the gold cover, at +$11.1m. (The "+$3.9m knife edge" of the phase 6 notes was a run at the story minimum that the committed scripts no longer reproduce: without `--values` the builder now includes L15.)

**Population model** (`population/outputs/`, regenerated on this workbook; tests pass). End of 1932: 38.44m residents, of them 6.11m of Japanese and 5.01m of Chinese origin. Native Hawaiians are 68,000 and Native Californians 131,000. A run with or without `PACIFICA_JOINS` now gives the same figures, because the sheet carries the joins.

## Storyline figures to update at integration (MODEL)

- §-overview (line 41), the population summary, and §37 (line 1294): "about 37 million" by 1932 → **about 38 million** (after the second addendum: **about 39 million**).
- Line 885: Japanese-origin against Chinese-origin, "about 5.7 against 4.9 million of some 37 million" → **about 6.1 against 5.0 million of some 38 million** (after the second addendum: **about 6.2 against 5.0 million of some 39 million**).
- AGENTS.md's "Residents in 1932 are about 37 million" follows the same change.

## Sources

- Census farm land: [1945 Census of Agriculture, Farms and Farm Property, Table 18](https://agcensus.library.cornell.edu/wp-content/uploads/1945-Farms_and_Farm_Property-TABLES-1179-Table-18.pdf).
- The decisions and runs: the session's `phase6-ranges-packages.md`, `phase7-decision-sheet.md`, `alaska-maxx.md`, CR-070 and `phase8_final.json`.

## Addendum, 15 November 2026: CR-070 as decided (the northern wire, the Commission after 1885, the copper)

The author asked for the model to be rebuilt after CR-070's three fresh-context reviews. Same two build steps and the same package D final; `cr059_068_levers.py` and `cr059_068_values.json` are changed. SHA-256 `9ac9d556a0ed6b37a30cc358125c7dc02329cf606e0b623f232c156950e8b9d5`. Recalculated in LibreOffice: 63,480 formulas, no errors, saved in the Story case. All amounts are MODEL.

**What changed**

- **The Bering telegraph is gone** (CR-070 E1). `cw_ak_telegraph` now switches the Alaska line through British Columbia: E226, $0.4m a year in 1868–70; E227, an operating loss of $0.05m a year in 1871–97; E232, the Sitka–Juneau cable, $0.15m a year in 1872–73; E233, the Lynn Canal line, $0.2m in 1884.
- **The cables** (Investment, like the other cables): E234, the Puget Sound–Sitka cable, $1.5m over 1887–88 (`cw_ak_cable88`); E236, the Aleutian cable to Hakodate, $4.5m over 1900–03 (`cw_ak_aleutian`). The stations' upkeep is not costed.
- **The sale to Canada:** E235, a receipt of $0.25m in 1897 (`cw_ak_bc_sale`).
- **The Northern Commission** (E228) runs to 1932 instead of 1885, at $0.15m a year, until the counties' CR settles Alaska's standing. E237 adds the Sitka ground rent, $5,000 a year from 1869.
- **The Skagway railway** (E230) is built in 1897–99, after the news, not 1896–98.
- **The Chitina's copper** (CR-070 B4, G5): `cw_ak_copper` adds a MODEL path to Resources F in 1900–28 ($2m, then $5m, $9m and $3m a year; about $198m in all, Kennecott's output read about ten years early at a flat value; to verify by year). E238 is the Copper River railway on Development Fund credit, $25m over 1897–1900 (`cw_ak_copper_rail`).

**Results (MODEL)**

| | 14 November | 15 November |
|---|---|---|
| Story case: failed checks | 0 | 0 |
| Stress case: failed checks (ceiling 17) | 15 | 15, the same years |
| Stress: margin of private saving, 1932 | +$92.4m | +$91.7m |
| Stress, 1932: gold above the cover requirement (the tightest 1932 check) | | +$11.1m |
| Story: residents at the end of 1932 | 38.435m | 38.443m |
| Story: real GDP in 1932, 1913 $m | 44,602 | 44,612 |
| Story: public debt in 1932, $m | 3,281 | 3,282 |

Walk of the 1932 Stress margin: +92.43 before; +92.03 with the Alaska line in place of the Bering entry, the Commission to 1932, the rent and the railway re-timed; +92.07 with the 1888 cable and the sale; +92.08 with the Aleutian cable; +92.85 with the copper; +91.68 with the Copper River railway. The cables are Investment and raise later output, so they cost the margin almost nothing; the copper railway costs more than the royalty returns to the Treasury.

**Not done.** Paths C was not re-iterated: residents move by about 8,000 in 1932, and the population model and the sheet now agree within about 1,900 residents (1,200 before). The garrisons-25%-dearer test was not rerun. The population outputs were regenerated on this workbook and the tests pass.

## Fresh-context review, 15 November 2026 (model plan phase 9)

An independent reviewer rebuilt the workbook from the base with the commands above and compared it cell by cell: every formula and defined name is identical and every value agrees within 1e-6 (63,480 formulas, no errors). Story 0 failed checks; Stress 15; the 1932 Stress private-saving margin +$91.683m; residents at the end of 1932 38,443,360; L15 $105.23m to the Treasury ($32.27m to 1900) and $1.251m to Oregon's schools; the population model reproduces `reconciliation.md` byte for byte (−1,854 residents at the start of 1932), with and without `PACIFICA_JOINS`, and its 18 tests pass. Garrisons 25% dearer on this build: Stress 15, margin +$85.8m (+$80.6m with Sitka dearer too). No blocker. The note's wording was corrected above where the reviewer found it wrong (the binding 1932 check, the set-offs, the annuities, the debt, the Alaska gold, L15's price).

**Open for the author** (they change the workbook; all six approved by the author on 15 November 2026 and applied in the second addendum):
1. L15's price: the Land Fund's rule (floor or share of census value, whichever is higher), as Q7 approved, instead of the floor alone.
2. E10 ($2m in 1866, the Navajo and Apache treaties with the peonage compensation): CR-061 A2 puts the compensation under $0.5m, and the annuities have been in E209 since 1862.
3. Whether the 1862–65 Richmond credit (E09, E198, $11.7m) rolls into the $25m refinancing of 1871–72 (E19) or stands beside it (register F06); the workbook has both.
4. CR-059 W9, the Sacramento line to the Siskiyous in 1863–66: no cost row.
5. Canada's 15% of the Pribilof catch is netted over all of 1880–89 (E219); CR-070 D2 has it from 1886.
6. Oregon's customs share after 1867 (register L15) is not built.

**Labels cleaned in the second addendum's rebuild** (no value changes): stale event IDs in the lever notes of `cw_ak_telegraph`, `cw_ak_cable88`, `cw_ak_bc_sale`, `cw_ak_aleutian`, `cw_ak_copper_rail` and E227; Levers G413–G463 status labels ("Lever (start 0)" and similar) and row 408; E195 and E196 still say "at zero until phase 5"; E09's basis still names Logan's mission (now E199); the Changes log row 67; the default `--rates` in `cr059_068_civil_war.py`. Amounts behind switches (E222–E227, E229–E233, the copper path, E237) are hard-coded and do not vary in Stress. The Sitka garrison and the northern mail stop after 1900 (E196, E218).

## Second addendum, 15 November 2026: the review's six decisions (author: "I approve all 6 suggestions")

Same two build steps from the same base; `cr059_068_levers.py`, `cr059_068_values.json` and the Paths C rates are changed. SHA-256 `eb642aa747fcf738f3126ef2160ee18dadb1528709a69fd503cad45ac13eb252`. Recalculated in LibreOffice: 63,491 formulas, no errors, saved in the Story case. All amounts are MODEL.

**What changed**

1. **L15 at the Land Fund's price.** `Members' land` M is now `MAX(lfund_floor, lfund_share × Land Fund T × cw_l15_value_rel)`: the Land Fund's rule, with the new members' farm value per acre at half California's (`cw_l15_value_rel` 0.5; the 1900 census's values per acre in the eight states were roughly a third to two-thirds of California's, to verify). The floor binds to about 1880; the price is about $2.46 an acre in 1900 and $11.23 in 1932 (Story). Story: $530.6m to the Treasury over 1867–1932 (was $105.2m), $66.4m of it to 1900; Oregon's schools $5.1m.
2. **E10 is the compensation only:** $0.5m in 1866 (`cw_peon_comp`; CR-061 A2), down from $2m; the Navajo and Apache treaties' costs are in E209 from 1862.
3. **The Richmond credit stands beside the refinancing.** E19's $25m of 1871–72 is new lending; the war credit (E09, E198) is not rolled into it (E19's note says so). No value change.
4. **The Sacramento line to the Siskiyous** (CR-059 W9) is costed: $8m on Development Fund credit (`cw_or_rail_south`; about 200 miles at about $40,000 a mile, to verify), E240–E243, rising as the line goes north: $1.0m in 1863, $1.5m in 1864, $2.5m in 1865, $3.0m in 1866. An even spread ($2m a year) failed Stress in 1863: that year's private-saving room is about $1.5m.
5. **Canada's 15% from 1886.** E219 now runs 1880–85 at `cw_seal_1880s / 0.85` (before Canada's share) and E239 1886–89 at `cw_seal_1880s` (after it).
6. **Oregon's customs share** (CR-059 V9) is built: from 1867 Budget V adds `cw_or_cust_share × cw_or_cust_base × customs`, a quarter (MODEL; the fraction is CR-059 open decision 21) of the customs attributable to Oregon's residents, held at their 1867 share of the confederation (3.46%). Story: $200m over 1867–1932, $15.9m to 1900, $7.6m in 1932.

Also cleaned: the lever notes' event IDs, the Levers status labels (levers set by the values file read "Package D final"), row 408's header, the notes on E09, E195 and E196, the Changes log entry, and the default `--rates` of `cr059_068_civil_war.py`.

**Paths C** was re-iterated in two rounds: the largest change was 0.000029, then 0.000001, and the population model and the sheet agree within about 100 residents at the end of 1932. The population outputs were regenerated on this workbook and the tests pass.

**Results (MODEL)**

| | First addendum | Second addendum |
|---|---|---|
| Story: failed checks | 0 | 0 |
| Stress: failed checks (ceiling 17) | 15 | 15, the same years (1887, 1914–24, 1927) |
| Stress, 1932: gold above the cover requirement (the tightest 1932 check) | +$11.1m | +$10.0m |
| Stress, 1932: margin of private saving | +$91.7m | +$110.0m |
| Story: residents at the end of 1932 | 38.44m | 38.71m |
| Story: real GDP in 1932, 1913 $m | 44,612 | 45,333 |
| Story: public debt, 1867 / 1900 / 1932, $m | 70 / 301 / 3,282 | 78 / 304 / 3,326 |

- **The land pays; Oregon's share costs.** The land's price is the large gain ($425m more over 1867–1932), much of it after 1900, and it raises growth and residents through the Development Fund. Oregon's customs share costs $200m over the same years and holds the debt up; the Sacramento line adds $8m to the war years' borrowing.
- **The war years are tighter.** With the garrisons 25% dearer, Stress now fails 17 checks, two of them new (1863 and 1864, private saving), where the first addendum's build failed 15: the line uses the room the dearer-garrisons test had in 1863–64. The base case passes the strict rule.
- **Population.** End of 1932: 38.71m residents, of them 6.17m of Japanese and 5.04m of Chinese origin (model). Storyline figures at integration: about 39 million (was about 37; the first addendum's 38.4 rounded to 38), and about 6.2 against 5.0 million.

## Third addendum, 15 November 2026: the Sacramento line later, two story assumptions, the Legion

The author: "Start the Sacramento line later. Make a story assumption for the Oregon census. I suggest Nauvoo is paid by Pacifica only if Pacifica gets something worth the pay in return." SHA-256 `fa26dfaac374b186619f6ba425632e4bb2543a5609494997a71501ab0d6f0b9c`; 63,490 formulas, no errors, saved in the Story case. All amounts MODEL.

- **The Sacramento line** is built in 1865–67 and reaches the Siskiyous in 1867: $2.0m, $3.0m and $3.0m (E240–E242; the same $8m). The war years keep their room.
- **Story assumptions** (author): the new members' farm land is worth about half California's per acre (`cw_l15_value_rel` 0.5), and Oregon's customs share is a quarter of the customs its residents pay (`cw_or_cust_share` 0.25; CR-059 open decision 21). Neither is to be verified against the census; both are labelled as story assumptions.
- **The Nauvoo Legion** is paid only for a decisive deployment (CR-060 D7, CT7; the deployment, M11, is PROPOSED): Lot Smith's cavalry at Bannack in the summer of 1864, $0.1m (E216, `cw_legion_on` 1). Road duty under the Compact is the common defence and is not paid.

| | Second addendum | Third addendum |
|---|---|---|
| Story: failed checks | 0 | 0 |
| Stress: failed checks (ceiling 17) | 15 | 15, the same years |
| Stress, garrisons 25% dearer | 17 (1863, 1864 new) | **15, the same years**; the 1863 private-saving margin is +$0.02m |
| Stress, 1932: gold above the cover requirement | +$10.0m | +$10.0m |
| Stress, 1932: private saving | +$110.0m | +$109.0m |
| Story: residents at the end of 1932 | 38.71m | 38.68m |
| Story: real GDP in 1932, 1913 $m | 45,333 | 45,264 |
| Story: public debt, 1867 / 1900 / 1932, $m | 78 / 304 / 3,326 | 77 / 304 / 3,321 |

Paths C was not re-iterated: one round moves the rates by at most 0.000004, and the population model and the sheet agree within about 700 residents in 1932. The population outputs were regenerated (Japanese-origin 6.17m, Chinese-origin 5.04m) and the tests pass. Storyline figures at integration are unchanged: about 39 million; about 6.2 against 5.0 million. The 1863 margin under dearer garrisons is a knife edge: any further cost in 1863 breaks the adverse test.

## Fourth addendum, 15 November 2026: Columbia's charter (author: "I approve all the suggestions")

Washington Territory accedes as the member Columbia (CR-059 Part IX). SHA-256 `455cf2b7b8e2bbd62772bf63f3913176f41224ecf96158be17a2b82ac23f36ec`; 63,798 formulas, no errors, saved in the Story case. All amounts MODEL.

- **The Legion's pay** stays as in the third addendum: $0.1m in 1864 for the Bannack deployment (E216; CR-060 M11, now approved).
- **Columbia's schools** take one-eighteenth of the margin on Columbia's land, on Oregon's terms (`cw_col_school`; Members' land, new columns "Columbia, sold to date" and "Columbia's schools"): $5.3m over 1867–1932 (Story).
- **The land of the nations without a treaty** (the Chehalis, Cowlitz, Lower Chinook and their neighbours) enters the Land Fund only by purchase. Story assumption: it is a seventh of Columbia's farm land (`cw_col_nontreaty` 0.15). It is bought as it is sold, at the Land Fund's price to the nations (`lfund_price`, $0.10 an acre in Story, $0.25 in Stress), paid as annuities over `lfund_term` (20 years): about 2.0 million acres by 1932, $0.19m in Story ($0.47m in Stress). Both come off Members' land's net to the Treasury.
- **No customs share** for Columbia, and its works are within the Development Fund's ordinary programme, so neither adds a row.

| | Third addendum | Fourth addendum |
|---|---|---|
| Story: failed checks | 0 | 0 |
| Stress: failed checks (ceiling 17) | 15 | 15, the same years |
| Stress, garrisons 25% dearer | 15 | 15, the same years; 1863 margin +$0.016m |
| Stress, 1932: gold above the cover requirement | +$10.0m | +$10.1m |
| Story: members' land to the Treasury, 1867–1932 | $530.6m | $525.2m |
| Story: residents at the end of 1932 | 38.68m | 38.68m |
| Story: real GDP in 1932, 1913 $m | 45,264 | 45,256 |

Paths C was not re-iterated: the change is a few million dollars over sixty-five years; the population model and the sheet agree within about 800 residents at the start of 1932. The population outputs were regenerated and the tests pass.

## Fifth addendum, 15 November 2026: the Legion paid after the peace (author, on review B1: "Young acts; paid after")

The fresh-context review of the candidate storyline found that the Legion's deployment, as first written, had Elias order it and pay for it in 1864, against canon's "Elias orders no operation" and "sends no money … before the vote". The author chose that Young sends Lot Smith's cavalry to Bannack on Deseret's own decision and that Pacifica pays the Legion only in 1865, once the peace keeps western Montana. E216 moves from 1864 to 1865 at the same $0.1m (`cw_legion_on` × `cw_legion_pay`; CR-060 D7, M11). SHA-256 `a061a7ba809a1f405260bf6a1ec88982f188f9016611371db2409d80080c864c`; 63,798 formulas, no errors, saved in the Story case. All amounts MODEL.

| | Fourth addendum | Fifth addendum |
|---|---|---|
| Story: failed checks | 0 | 0 |
| Stress: failed checks (ceiling 17) | 15 | 15 (1887, 1914–24, 1927), the same years |
| Stress, garrisons 25% dearer | 15 | 15, the same years; 1863 margin +$0.016m |
| Stress, 1932: gold above the cover requirement | +$10.1m | about +$10.1m |
| Story: residents at the end of 1932 | 38.68m | 38.68m |

The cost moves a year later; no new Stress failure appears up to 1900, and the 1865 Stress margin stays positive (+$2.7m). Paths C was not re-iterated. The population outputs were regenerated in the adoption branch and the tests pass.

