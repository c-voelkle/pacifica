# Financial workbook, fixed items only (model plan phase 4)

**Status:** built and recalculated, 13 November 2026. The workbook at `finance/` is not replaced: the fixed-only build is a step toward phase 8, and the drafts are unapproved.

**Built by** `finance/build/cr059_068_civil_war.py` from the current workbook (SHA-256 `cba70b31…`, CR-051/054/055), with `population/data/joins_cr059_068.toml` and `finance/build/paths_c_rates_cr059_068.csv`. Recalculated in LibreOffice: 62,294 formulas, no errors, in both cases. The Story-case file is `phase4/Pacifica_financial_model_cr059-068_fixed-only.xlsx` (SHA-256 `13a922c8…`). Rebuilding gives the same workbook (every part identical but the file's own timestamp). The build changes cells on three sheets only: Paths (76), Events (39) and Changes (3).

## Answer to the plan's question

**Do 1859 and 1867 hold with nothing discretionary added? Yes.** The Story case has no failing check in any year (it had none). Stress has 17 failing year-checks, the same 17 in the same years: 1887, 1914–24, 1927 and 1932. None falls in the war or the cession years.

## What the build applies

| Item (register) | Change | Note |
|---|---|---|
| F01 London repaid in 1859 | none to formulas; E01 records the order | The workbook's single debt pool already gives $3.40m at the end of 1858 and $1.59m at the end of 1859, with the Reserve Fund at $3.29m: CT26's targets exactly. What is left is the Treasury's own bonds of 1846–52 |
| P01 Accessions (C1) | Paths D: nothing in 1862–66, 350,036 in 1867 | phase 3 |
| D3 Natural increase | Paths C: the population model's rate after C1 | One pass reaches the fixed point: the model and the sheet now differ by at most 0.001 points a year, and by under 1,600 people in 1932 |
| F10 Compensation | E10 re-dated 1865 → 1866 | amount unchanged ($2m) |
| F04 Vendor credit | E11 1866–72 in sevenths → 1867–72 in sixths | sixths are the placeholder for lever L05 |
| F15 Baja | E13 switched off ($0) | kept for a separate test; restore $1m to run it |
| L13 1867 lending | E14 relabelled: private lending to the Union's bankers and the transit companies | amount unchanged ($10m), until phase 5 |
| L14 Hudson's Bay rights | new E194: $0.65m over 1861–62, paid in gold | the 1869 award as the price (to verify) |
| L04 Sitka | new E195 (garrison and squadron) and E196 (mail), 1867–1900, at $0 | a lever from phase 5 |
| F06, F07 | none: E19 ($25m, 1871–72) and E41 ($6m, 1888–89) already match CR-068 CT28 | checked by the build |
| F02, F03 | none: the war years (Paths AC, 1861–65) and the 1861 army (20,000 regulars, 90,000 reserves) already match | |
| F11 Oregon's customs | none: they leave confederal revenue with Oregon's residents (C1), since customs follow GDP | |

## Results, Story case (the change from the current workbook in brackets)

| End of year | Residents | GDP ($m) | Receipts ($m) | Public debt ($m) | Reserve Fund ($m) | Gold ($m) |
|---|---|---|---|---|---|---|
| 1859 | 1.147m (0) | 269 (0) | 27.8 (0) | 1.6 (0) | 3.3 (0) | 130 (0) |
| 1862 | 1.383m (−178k) | 328 (−20) | 42.7 (−2.6) | 8.8 (+1.7) | 0 (0) | 156 (−0.7) |
| 1864 | 1.524m (−291k) | 419 (−68) | 53.9 (−8.8) | 31.6 (+11.0) | 0 (0) | 177 (−0.9) |
| 1865 | 1.598m (−303k) | 456 (−75) | 58.8 (−9.8) | 27.9 (+14.7) | 0.7 (−1.0) | 189 (−1.1) |
| 1867 | 2.174m (−7k) | 578 (−39) | 72.6 (−4.9) | 24.8 (+21.6) | 0 (−2.6) | 189 (+4.5) |
| 1868 | 2.298m (−7k) | 667 (0) | 84.3 (−0.1) | 12.4 (+12.4) | 3.0 (−14.5) | 192 (+4.5) |
| 1870 | 2.571m (−8k) | 774 (−2) | 98.1 (−1.4) | 0 (0) | 24.7 (−29.4) | 199 (+4.6) |
| 1875 | 3.398m (−12k) | 1,062 (−3) | 132.2 (−1.8) | 0 (0) | 170.1 (−37.6) | 248 (+3.7) |

- **The war years are poorer.** With the held territories outside the count, GDP in 1862–66 is 6–14% lower and receipts $3–10m a year lower. Spending falls less, because the army and the war rows do not shrink with the residents. So the war is financed by borrowing: public debt peaks at $31.6m in 1864 (was $20.6m), and the Treasury borrows $7.2m, $11.8m and $10.9m in 1862–64 (was $5.5m, $8.4m, $5.2m).
- **1867 now borrows.** The first instalment ($6.67m), Alaska ($7.2m) and the 1867 loan ($10m) take $23.9m in gold that year. The Treasury borrows $4.7m (was nothing) and the Reserve Fund ends the year at zero. Debt is repaid by 1869, as before.
- **The cost lasts.** The Reserve Fund stays $28–38m lower in 1869–75, because the war debt was repaid out of the surpluses that used to fill it. Gold is $4–5m higher from 1866 only because the credit's first instalment moves from 1866 to 1867 and the sixths end in 1872.
- **Later years barely move:** residents are 0.1% lower in 1932.

## Headroom: the binding check

The tightest check in the war years is the private-saving test (Sources & uses). Its margin in $m, the current workbook first:

| Year | Story | Stress |
|---|---|---|
| 1862 | 27.8 → 24.2 | 12.2 → 9.4 |
| 1863 | 28.4 → 20.4 | 9.9 → **4.1** |
| 1864 | 37.9 → 26.3 | 16.2 → 7.4 |
| 1865 | 47.1 → 40.5 | 24.8 → 21.1 |
| 1866 | 39.1 → 33.7 | 15.6 → 13.3 |
| 1867 | 42.4 → 35.0 | 16.7 → **8.2** |

Under Stress, 1863 has $4.1m of room and 1867 $8.2m. That room is roughly what the levers in phase 5 compete for: the Richmond credit, the Honolulu package, the garrisons above their head counts and the Juárez credit in 1862–65; the instalment split, Sitka and the 1867 lending in 1867. The cash check passes in every year because borrowing fills the gap; the Reserve Fund is at zero in 1862–64 in both the current workbook and this build.

## Corrections and open points

1. **E20 stays (correction to Q11).** I had recommended dropping E20, $1m a year in 1871–88 replacing Richmond's Mississippi tolls, on the reading that "the draft does not say". Canon §13 (CR-039, approved) says it: "Richmond restores free Mississippi navigation … Pacifica replaces the surrendered toll revenue." Free navigation (CR-068 K21) is Richmond's side of that bargain, and the toll payment is Pacifica's. So the build keeps E20. Dropping it would be a canon change, and would need a tension in CR-068.
2. **Royalties on the held territories' gold.** Resources C counts Comstock, Idaho and Montana output from 1863, "once the territory is Pacifican", and the 5% metal royalty applies to it. With membership from 1867 (Q1), whether held territories pay the royalty before they join is open. The drafts give Washoe its own net-proceeds tax (lever L11) and the Idaho and Montana compacts freight, coin and assay terms, but no royalty. Left unchanged; recommended for phase 5 together with L11.
3. **D1 and D4 from phase 3.** The build takes the recommended readings: the confederal count is the members' (1.60m at the end of 1865; DEM-01's 1.9m read as everyone under the Republic's government), and the treaty nations are outside the count. Both can still be changed.
4. **Levers.** E07 ($6m, 1861), E08 ($5m a year, 1862–64), E09 ($0.8m a year, 1862–64) and E14 ($10m, 1867) stay at the workbook's values, and the new Sitka rows are at zero. Phase 5 replaces them with named levers.

## Files

- `phase4/Pacifica_financial_model_cr059-068_fixed-only.xlsx`: the build, recalculated, Story case.
- `phase4/baseline_*.json`, `phase4/fixed-only_*.json`: the checks and series of the current workbook and this build, both cases (`evaluate.py`).
- `finance/build/cr059_068_civil_war.py`, `finance/build/paths_c_rates_cr059_068.csv`.
