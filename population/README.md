# Population model

A cohort-component model of Pacifica's population: single years of age, two sexes, census groups, 1846–1932. It complements the financial workbook's People sheet, which carries one total with one natural-increase rate.

```
python3 population/historical.py   # validation against our timeline  -> outputs/historical.md
python3 population/canon.py        # canon run against the People sheet -> outputs/reconciliation.md, canon_by_year.csv
python3 population/flows.py        # where the population comes from, and migration vs US immigration -> outputs/flows.md
python3 population/changes.py      # workbook change list figures -> outputs/workbook_changes.md, workbook_changes.csv
python3 -m unittest discover -s population/tests -v
```

Needs Python 3.11+ and `openpyxl` (to read the workbook; it is never written).

## How it works

- **Mortality:** Coale–Demeny West model life tables (`cdwest.py`), chosen by life expectancy at birth. Tested against the published level values.
- **Fertility:** total fertility rate spread over ages 15–49 (Coale–Trussell shape).
- **Migration:** the People sheet's streams, each with an age-sex profile.
- **Groups:** as the historical sources record them. US census: white (incl. Californios and Hispanos), Black, Chinese, Japanese, Indian. Hawaii censuses: Hawaiian and part-Hawaiian, plus the other nationalities. Filipino follows the sheet.

## What is sourced and what is not

| File | Content | Status |
|---|---|---|
| `data/census.toml` | Census counts for Hawaii 1853–1900, California by group 1850–1900, other western states 1850–1930, and Native Californian estimates | Each series is labelled verified, identity-checked or estimate, with its source |
| `data/rates.toml` | US white and Black e0 and TFR (Haines) | Verified |
| `data/rates.toml` | Native Hawaiian rates | Calibrated to the census, then tested against age structure |
| `data/assumptions.toml` | Migrant age and sex profiles, joined-territory sex ratio; the Native Californian switch | MODEL, and the only place these live |
| `data/us_immigration.toml` | US immigration by decade and origin, 1841–1930 | Verified (DHS yearbook) |

## Validation (our timeline)

- **Native Hawaiians, 1853–1896:** with no migration, the calibrated rates reproduce six censuses within about 6%. They also pass an independent test on the share of children. The calibration is weakly identified; see `outputs/historical.md`.
- **California:** each census group closes exactly against the census, which yields historical net migration by group and decade.
- **Native Californians:** losses beyond the worst life-table mortality, 1848–1870, quantified against the scholarly estimates.

## The chain (`flows.py`)

Every run uses the same engine, which is linear in population, so differences between runs are exact contributions:

1. the 1846 Californians and their descendants;
2. plus the territories joined;
3. plus each migration stream, with descendants;
4. plus the sheet's flat growth rate, which gives the People sheet.

All four start at zero in 1846. Our timeline on the same territory, from census figures, is the reference line.

## Author decisions (27 October 2026)

1. **Native Californians:** disease without mass killing (`hawaiian_analogue`).
2. **The sheet's 170,000 Californians in 1846** include the Native population.
3. **DEM-01:** about 1.2m in 1861 is preferred, if believable counterfactuals carry it. The scenario multiplies the sheet's 1848–1860 arrivals from the Americas, Europe and China by 2.10 (`[dem01]`).
4. **Japanese immigration predominates over Chinese in absolute terms.** This comes from redirected flows and from emigration increased by the alternate timeline's circumstances (`[extra_origin]`).

### Counterfactuals the DEM-01 scenario rests on (approved by the author, 27 October 2026)

It needs roughly three times the settlement California gained in our timeline, mostly by keeping people who historically came and left. The candidates:

- **Light foreign-miner licences instead of a punitive tax.** Canon (§5) has Elias hold the licences to $2 a month for residents and $4 for non-resident foreigners. So Sonoran, Chilean, Peruvian and Chinese miners stay, where our timeline's punitive Foreign Miners' Tax of 1850 drove them out. (Corrected 27 Oct 2026: an earlier wording said "no tax", which contradicted canon.)
- **Assisted passage for women and families from 1852.** This is canon, and it turns sojourning miners into settlers.
- **Secure land titles and a stable republic.** Land titles are an OPEN canon item, so this is a candidate.
- **A Pacific-facing republic,** with Hawaii from 1856 and Pacific shipping, drawing arrivals from Australia and Chile directly.
- **Americans keep moving west** to an independent but open California.

DEM-01's 1865 figure rises to about 1.7m (author): the model reaches 1.74m, with the sheet's 1862–65 joins and arrivals on top of the larger 1861 base. These are approved as model assumptions; putting them into the storyline or historical background would go through a CR.

### Later decisions (27 October 2026)

5. **Generous growth after 1915:** Pacifica becomes a really attractive place to live.
6. **Native populations grow after the initial dip:** fair treatment and a better quality of life than in our timeline.

## Canon rates (`rates_case = "canon"`)

Each group's vital rates follow a dated path, with real-world benchmarks as the ceiling. Pacifica reaches the best levels any population actually achieved in the period, not more.

- **General population:**
  - Mortality follows US white rates until 1888 (Office of Public Measures, §21; Victoria's measures, §23). It then converges to New Zealand's, the world's highest life expectancy, by 1910.
  - Fertility follows US white rates until 1900, then converges to Canada's, the highest among settler societies, by 1915.
- **Native Hawaiians:** calibrated historical rates until Noe's health board (1886, §20), then converging to the general level. The convergence date (1912) is solved so the population turns upward in 1895, as §23 states.
- **Native Californians:** disease without mass killing until 1870, then a protective but unequal deal (draft CR-033: the Republic as sole buyer of Native land).
  - Mortality moves onto the path of New Zealand's Māori by 1891 and follows it: life expectancy about 24 in 1891, 32 in 1911, 41 in 1926 (Te Ara). That leaves a gap of 20–30 years to the general population.
  - Fertility (5.9) is solved so the population turns upward in the later 1890s, as Māori numbers did.
  - Result: low about 99,000 in 1897, about 130,000 by 1932. The dates are MODEL; canon gives none.

`rates_case = "our_timeline"` restores historical rates for comparison.

## Step 2: canon divergence factors (complete)

- **Health measures, the Hawaiian turn, Native recovery, general mortality and fertility:** see Canon rates above.
- **Women's and family programmes:** these act through the assisted-passage share (women and families from 1852) and the migrant sex ratios (Chinese families from 1868, Japanese from 1907). `reconciliation.md` checks the result. The white population runs about 150 men per 100 women in 1856 and evens out to about 100 by 1880, as canon describes.
- **Group-specific rates:** all residents other than Native Hawaiians and Native Californians share the general canon path. This is a decision, not a gap: canon's civic equality and the examined state give no ground for group differences, and no sourced rates for those groups exist here.

Canon text for these decisions: draft CR-033 in `book-agent/revision/drafts/`.

## Step 3: workbook change list (complete, applied 27 Oct 2026)

The workbook now includes the changes (`finance/CR-033-workbook.md`). `[dem01] multiplier` is therefore 1.0 here, and the model and the sheet agree on residents in every year. The workbook's own migration responds to the larger population, so it ends 1932 with 32.5m residents.

[`workbook_change_list.md`](workbook_change_list.md) lists what the People, Paths, Levers and Checks sheets would need to match the approved model. It also lists the knock-on effects to check and the Land Fund rows that apply if CR-033 is adopted. The workbook is unchanged.

**Year convention:** the change list counts residents at the end of each year, as the People sheet does (column L). Elsewhere in this README and in CR-033, "in 1932" means the start of 1932. Before the workbook was revised, the model gave 30.1m at the start of 1932 and 30.9m at the end, using the old sheet's migration. With the revised workbook's migration it gives 31.4m at the start and 32.5m at the end.
