# Workbook revision, 14 November 2026: the Civil War CRs (CR-059 to CR-065, CR-067, CR-068), Alaska (CR-070) and the members' land (L15)

SHA-256 of the current workbook: `9ac9d556a0ed6b37a30cc358125c7dc02329cf606e0b623f232c156950e8b9d5` (rebuilt on 15 November 2026 for CR-070's decided wire, Commission and copper; see the addendum at the end. The figures in the body are those of 14 November, SHA-256 `c5ebb7bb…`).

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
     - the instalments as six of $6.67m;
     - Oregon's scrip, $3.2m face;
     - the regional annuities, equal to each region's receipts (D4, MODEL working figures).
   - **People.** 20,000 refugees, deserters and draft evaders a year in 1863–65 (L12).
   - **Alaska (CR-070).** Sitka's garrison and squadron at $2.85m a year in 1867–72, then 40% of that (the settler garrison). The northern mail at $0.3m a year. Receipts:
     - the seal lease, tendered from 1880, with the herd saved;
     - the salmon case tax from 1870;
     - Juneau's gold eight years early (Resources E shifted; the historical path is kept in T);
     - the Seward Peninsula's placers from 1876.
     The Northern Commission and the Chilkoot compact are in at their MODEL costs. The Bering telegraph's cost was in provisionally; the addendum of 15 November replaces it with the wire as decided.
   - **L15, the members' land.** A new sheet, `Members' land`. The new members' farm land from 1867 is taken from the census (1945 Census of Agriculture, Farms and Farm Property, Table 18), with western Montana at a quarter of Montana's. It is sold on the Land Fund's instalments at its floor price, with no purchase cost, because the nations are paid by the regional annuities. Oregon's schools take one-eighteenth of the margin on Oregon's land. The net goes into Budget G beside the Land Fund's: $105m to the Treasury over 1867–1932, $32m of it to 1900, and $1.25m to Oregon's schools. Five OCR-garbled census entries are read as 3 where the scan prints 5; they are listed in the build script and are to verify against the scans.

## Results (MODEL)

| | Before (CR-051/054/055) | This revision |
|---|---|---|
| Story case: failed checks | 0 | 0 |
| Stress case: failed checks (ceiling 17, author) | 17 | 15 |
| Stress: margin of private saving, 1932 | +$7.9m | +$92.4m |
| Stress, with the garrisons above the head counts 25% dearer | | 15 failed; margin +$85.9m |

| Story case | 1867 | 1900 | 1932 |
|---|---|---|---|
| Residents, before → now | 2.18m → 2.23m | 10.32m → 10.75m | 36.75m → 38.44m |
| Real GDP, 1913 $m | 649 → 624 | 7,350 → 7,909 | 41,054 → 44,602 |
| Public debt, $m | 3 → 70 | 279 → 301 | 3,036 → 3,281 |

- **The war.** It now costs Pacifica something: the debt at the end of 1867 is $70m instead of $3m, and 1867's GDP is a little lower.
- **What pays it back.** By 1900 the joins, the refugees, the Oregon works, Alaska's receipts and the members' land have more than made it good.
- **Stress.** The 15 failures that remain are the baseline's own: 1887, 1914–24 and 1927. 1932 now passes every check. The old knife edge (+$3.9m) was the private-saving margin at the story minimum; it is gone.

**Population model** (`population/outputs/`, regenerated on this workbook; tests pass). End of 1932: 38.44m residents, of them 6.11m of Japanese and 5.01m of Chinese origin. Native Hawaiians are 68,000 and Native Californians 131,000. A run with or without `PACIFICA_JOINS` now gives the same figures, because the sheet carries the joins.

## Storyline figures to update at integration (MODEL)

- §-overview (line 41), the population summary, and §37 (line 1294): "about 37 million" by 1932 → **about 38 million**.
- Line 885: Japanese-origin against Chinese-origin, "about 5.7 against 4.9 million of some 37 million" → **about 6.1 against 5.0 million of some 38 million**.
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
| Story: residents at the end of 1932 | 38.435m | 38.443m |
| Story: real GDP in 1932, 1913 $m | 44,602 | 44,612 |
| Story: public debt in 1932, $m | 3,281 | 3,282 |

Walk of the 1932 Stress margin: +92.43 before; +92.03 with the Alaska line in place of the Bering entry, the Commission to 1932, the rent and the railway re-timed; +92.07 with the 1888 cable and the sale; +92.08 with the Aleutian cable; +92.85 with the copper; +91.68 with the Copper River railway. The cables are Investment and raise later output, so they cost the margin almost nothing; the copper railway costs more than the royalty returns to the Treasury.

**Not done.** Paths C was not re-iterated: residents move by about 8,000 in 1932, and the population model and the sheet now agree within about 1,900 residents (1,200 before). The garrisons-25%-dearer test was not rerun. The population outputs were regenerated on this workbook and the tests pass.
