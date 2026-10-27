---
name: pacifica-population
description: Model Pacifica's population by age, sex and census group (1846-1932) and reconcile it with the financial workbook's People sheet. Use for manpower, crews, labour force, school-age and electorate questions, the Native Hawaiian and Native Californian populations, and testing whether a CR's demographic claims hold.
---

# Pacifica population

Turn canon events and the People sheet's migration into an age-sex-group population, and report where the sheet's single total and flat growth rate diverge from what the age structure implies. Companion to [Chryseis](../chryseis/SKILL.md): Chryseis prices things; this model says who is there to do them.

Apply the [shared authority and scope rules](../../../docs/authority-and-scope.md) (R1–R7).

## Run

```
python3 population/historical.py   # our-timeline validation
python3 population/canon.py        # canon run and reconciliation with the People sheet
python3 population/flows.py        # chain from 1846 by source, and migration against US immigration
python3 population/changes.py      # figures for the workbook change list (workbook_change_list.md)
python3 -m unittest discover -s population/tests
```

Read `population/outputs/flows.md` and `reconciliation.md` before answering. Native Californians follow the switch in `data/assumptions.toml` (an OPEN canon question; say which setting a number uses); quote its numbers with their labels.

## Rules

- Inputs live only in `population/data/`: census counts and sourced rates (`census.toml`, `rates.toml`) and MODEL assumptions (`assumptions.toml`). Never put a number in code. Every new value carries its source and status (verified, identity-checked, estimate, calibrated, MODEL).
- Historical series test the engine; they are not canon. A canon divergence (better health, family migration, a different Indigenous history) is a dated change to a group's rates or migration profile, recorded with its CR or storyline reference.
- Groups follow the historical sources' own categories (US census: white, Black, Chinese, Japanese, Indian; Hawaii censuses: Hawaiian, part-Hawaiian and nationalities). Don't invent groupings.
- The workbook is read, never written. A gap between the model and the sheet is a finding for the author, not a correction to apply. Report it as: what the sheet implies, what the age structure implies, which canon factor could explain the difference.
- Where canon is OPEN (for example Indigenous claims), show labelled bounds, not one answer.
- Life tables can't represent killing, famine or war: report such losses as excess loss beyond the worst West table, not as a rate.
- Don't add probabilities or scores. Compare cases (baseline vs a CR) rather than predict the one true 1932.

## Extending

To add a canon factor: add the dated rate or profile change to the data files with its canon reference, rerun both scripts, and state how the gap to the sheet changed. To add a region or group: source its census counts first (status "verified" or "identity-checked"), then add it. Keep runs under a minute.
