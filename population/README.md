# Population model

A cohort-component model of Pacifica's population: single years of age, two sexes, census groups, 1846–1932. It complements the financial workbook's People sheet, which carries one total with one natural-increase rate.

```
python3 population/historical.py   # validation against our timeline  -> outputs/historical.md
python3 population/canon.py        # canon run against the People sheet -> outputs/reconciliation.md, canon_by_year.csv
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
| `data/assumptions.toml` | Migrant age and sex profiles, joined-territory sex ratio | MODEL, and the only place these live |

## Validation (our timeline)

- **Native Hawaiians, 1853–1896:** with no migration, the calibrated rates reproduce six censuses within about 6%. They also pass an independent test on the share of children. The calibration is weakly identified; see `outputs/historical.md`.
- **California:** each census group closes exactly against the census, which yields historical net migration by group and decade.
- **Native Californians:** losses beyond the worst life-table mortality, 1848–1870, quantified against the scholarly estimates.

## Next step: canon divergence factors

The canon run uses our-timeline vital rates on purpose. Its gap to the People sheet is what the canon's own divergences must explain:

- Victoria's health measures and the Hawaiian turn after about 1895;
- the women's and family programmes;
- family migration from 1868 and 1907;
- whatever the author decides for Native Californians.

Each becomes a dated, sourced change to a group's rates or migration profile, recorded in the data files with its canon reference.
