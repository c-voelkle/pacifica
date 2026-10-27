# Population model

A cohort-component model of Pacifica's population: single years of age, two sexes, census groups, 1846–1932. It complements the financial workbook's People sheet, which carries one total with one natural-increase rate.

```
python3 population/historical.py   # validation against our timeline  -> outputs/historical.md
python3 population/canon.py        # canon run against the People sheet -> outputs/reconciliation.md, canon_by_year.csv
python3 population/flows.py        # where the population comes from, and migration vs US immigration -> outputs/flows.md
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

### Counterfactuals the DEM-01 scenario rests on (candidate canon, to confirm)

It needs roughly three times the settlement California gained in our timeline, mostly by keeping people who historically came and left. The candidates:

- **No Foreign Miners' Tax.** The republic administers claims under the inherited Spanish and Mexican mining regime (master storyline §5). So Sonoran, Chilean, Peruvian and Chinese miners stay, where our timeline's California taxed and drove them out from 1850.
- **Assisted passage for women and families from 1852.** This is canon, and it turns sojourning miners into settlers.
- **Secure land titles and a stable republic.** Land titles are an OPEN canon item, so this is a candidate.
- **A Pacific-facing republic,** with Hawaii from 1856 and Pacific shipping, drawing arrivals from Australia and Chile directly.
- **Americans keep moving west** to an independent but open California.

The scenario overshoots DEM-01's second figure, 1.5m in 1865: the model has about 1.74m, because the sheet's 1862–65 joins and arrivals come on top. One of the two needs adjusting.

## Next step: canon divergence factors

The canon run uses our-timeline vital rates on purpose. Its gap to the People sheet is what the canon's own divergences must explain:

- Victoria's health measures and the Hawaiian turn after about 1895;
- the women's and family programmes;
- family migration from 1868 and 1907;
- whatever the author decides for Native Californians.

Each becomes a dated, sourced change to a group's rates or migration profile, recorded in the data files with its canon reference.
