# Workbook change list: population, Civil War CRs (model plan phase 3)

**Status:** proposed, 13 November 2026. Nothing in the workbook is changed; phase 4 applies these changes in `finance/build/cr059_068_civil_war.py`.

**Basis:** the register's fixed population items and the author's decisions of 13 November 2026 (Q1–Q3, Q12, the Vicksburg reading; `session.md`). The figures come from the population model run with the joins file:

```
PACIFICA_JOINS=population/data/joins_cr059_068.toml PACIFICA_POP_OUT=<folder> python3 population/canon.py   # then flows.py, changes.py, neighbours.py
```

The run's reports are in `phase3-run/`; year-by-year values for pasting are in `phase3_by_year.csv`. Residents are counted at the end of each year, as in People column L. Without `PACIFICA_JOINS` the model reproduces the current workbook exactly (checked: every output file is byte-identical to the baseline run).

## Changes to inputs

| ID | Where | Change | Why | Effect |
|---|---|---|---|---|
| C1 | Paths D, 1862–1867 | 1862 177,000 → 0; 1863 85,000 → 0; 1864 25,000 → 0; 1865 10,000 → 0; 1867 50,000 → 350,036 (1856 unchanged, 72,000) | Q1: every acceding territory enters the confederal count at the exchange of 1867. Q12: Baja is switched off, so its residents go too | Residents at the end of 1865 fall from 1.90m to 1.60m (−304,000, −16%); at the end of 1867 they are 6,800 fewer (−0.3%) |
| C2 | Paths D comment | Replace the join list with: "1856 Hawaii (Confederation); 1867 the exchange: Oregon, Washington Territory, Idaho, Washoe, Deseret with southwest Wyoming, western Montana, New Mexico with Arizona and the San Luis Valley, South Park and the upper Arkansas, Alaska. Sizes: population/data/joins_cr059_068.toml." | The comment now describes joins that no longer happen | none |

### The 1867 join, territory by territory

| Territory | Residents, 1867 | Basis |
|---|---|---|
| Oregon | 77,096 | 1860 and 1870 censuses (52,465; 90,923), log-linear |
| Washington Territory | 19,268 | 1860 and 1870 censuses (11,594; 23,955), log-linear |
| Idaho | 17,289 | 1863 territorial census 32,342 less the ~12,000 in the Montana camps; linear to 1870 (14,999) |
| Washoe (Nevada) | 42,941 | the 1870 census, held flat back to 1867 (the rush population was in place by 1863–64) |
| Deseret | 68,932 | 1860 and 1870 censuses (40,273; 86,786), log-linear |
| Southwest Wyoming | 1,000 | story assumption (before the railway of 1868) |
| Western Montana | 18,046 | Edgerton's census of 1864 (15,812) and 1870 (20,595), log-linear |
| New Mexico with Arizona and the San Luis Valley | 101,964 | 1860 census 93,516 (which counts all three); 1870 sum 105,815; log-linear |
| South Park and the upper Arkansas | 1,500 | story assumption ("almost empty") |
| Alaska | 2,000 | ~500 Russians and ~1,500 Creoles at the purchase |
| **Total** | **350,036** | the sheet's 1862–1867 joins were 347,000, Baja included |

All MODEL. The figures follow the censuses' own perimeter, without "Indians not taxed", as the sheet's earlier joins did (see D1).

## Results

| End of year | Residents now | With C1 | Difference | Men 18–45 |
|---|---|---|---|---|
| 1861 | 1,313,954 | 1,313,954 | 0 | 0 |
| 1862 | 1,560,921 | 1,382,961 | −177,960 | −45,122 |
| 1863 | 1,716,211 | 1,451,587 | −264,624 | −67,453 |
| 1864 | 1,814,445 | 1,522,862 | −291,583 | −74,804 |
| 1865 | 1,900,592 | 1,596,898 | −303,694 | −77,964 |
| 1866 | 2,014,738 | 1,708,850 | −305,888 | −78,396 |
| 1867 | 2,181,481 | 2,174,685 | −6,796 | −2,200 |
| 1870 | 2,579,050 | 2,570,150 | −8,900 | −1,130 |
| 1872 | 2,873,114 | 2,862,629 | −10,485 | −1,448 |
| 1900 | 10,327,510 | 10,304,535 | −22,975 | −4,585 |
| 1931 | 35,837,506 | 35,796,931 | −40,575 | −7,913 |

The war years carry about 300,000 fewer people, and about 75,000 fewer men of military age. From 1867 the difference is small: Baja's residents go, the territories come in a little larger than the sheet's sizes, and five years of their natural increase are lost. By 1932 the total is 0.1% lower.

## Knock-on effects to check (no input change proposed)

| ID | Where | What to check |
|---|---|---|
| D1 | DEM-01 (`war_base_assumptions.md`) | DEM-01 reads "~1.9m at the end of 1865" (author, 28 October 2026: the workbook figures govern the prose). With C1 the confederal count at the end of 1865 is 1.60m. **Recommended:** keep 1.60m as the members' count, which the finance uses, and read DEM-01's 1.9m as the people under the Republic's government: members plus the territories it holds under compact or occupation (Oregon and Washington from 1861, the Rio Grande and Arizona from 1862, Deseret associated from 1862, Idaho and Montana's camps, Washoe from 1864). That count comes to about 1.9m at the end of 1865. The storyline itself states only the 1861 figure (1.2m, unchanged), so no storyline text changes. An author decision; written here, not applied. |
| D2 | Economy J; Budget; Labour B | Non-mining GDP, the labour force and the assisted-arrival cost all scale with residents, so in 1862–66 they fall by up to 16%. The gold the held territories send to San Francisco (F12) is counted in Resources and does not move. This is the main question phase 4 answers: whether 1862–67 still holds. |
| D3 | Paths C (natural-increase path) | The plan's risk list notes that Paths C was not re-iterated in the last build. The joined territories' natural increase now starts in 1867, not 1862. The model's implied rate for 1862–66 rises slightly (fewer frontier-age joiners). Recommended: re-iterate Paths C once in phase 4, after C1. |
| D4 | Native nations | The census basis leaves out the treaty nations of the new territories (the Diné, Apache, Ute, Shoshone, Bannock, Paiute, the Northwest nations, Alaska's peoples). The model counts Native Californians and Native Hawaiians as residents. Whether the treaty nations count as residents from 1867 is a question for the author; the model can carry them as a separate group if so. Not applied. |
| D5 | Refugees (L12) | The draft-evader and refugee stream is at zero in this phase, as the plan says. It is sized in phase 6, and it partly offsets the war-year shortfall: they settle in members' counties as well as in Oregon. |

## Memo items (no input)

- **Pacifica's own war deaths, 1862–1866,** as the drafts give them: the second Valverde and the Fort Craig investment, Apache Pass, Bear River (a limited action, about 300 men engaged; CR-060 D8), the Owyhee killings and the prosecution (1865–66), the Black Hawk war's first season (1865) and the Hispano revolt of 1866. No draft gives casualty totals; they are small and are not put into the engine.
- **Neighbours.** `neighbours.py` starts in 1870 and projects the rump from the 1870 census, so the war's casualty changes have no input there: Shiloh (Union about 11,500, Confederate about 8,000, against 13,047 and 10,699), Vicksburg (about 12,500 escape and about 15,000 surrender, the reading taken for C4), the Overland campaign (more than 60,000) and Atlanta untaken. Kentucky and Delaware still slave states in 1866 leave the post-1898 rump unchanged. The run confirms `neighbours_by_year.csv` is unchanged.
- **Groups.** Hispano and Pueblo residents enter with the joined territories at white vital rates, as the model's census groups do. The Chinese floor (P06) and the entry controls (P07, P09) are memo items until a stream is sized.

## Checks

| Check | Result |
|---|---|
| Default run (no joins file) against the baseline run | identical, all eight output files |
| `python3 -m unittest discover -s population/tests` | 18 tests pass (three new ones on the joins file) |
| The same with `PACIFICA_JOINS` set | 17 pass, 1 skipped: the gap decomposition against the sheet, which by design no longer shares the sheet's joins |
| `neighbours_by_year.csv` with the joins file | unchanged |

## Code changes

- `population/canon.py`: `PACIFICA_JOINS` replaces the sheet's territory joins by a joins file; `PACIFICA_POP_OUT` writes the reports to another folder. Without them the run is the canon run, unchanged.
- `population/flows.py`, `changes.py`, `neighbours.py`: write to the same folder; `flows.py` builds its our-timeline comparison from the joins file when one is set.
- `population/data/joins_cr059_068.toml`: the 1867 joins and their bases.
- `population/tests/test_population.py`: three tests on the joins file.
