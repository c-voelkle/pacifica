# Deseret: the gathering and the Saints' birth rate (16 November 2026)

Built by `finance/build/deseret_gathering.py`, the last step of `cr057_rebuild_pair.py` (after the growth engine). Master lever `dg_on`: at 0 the build reproduces the input workbook exactly (checked: no value differs). All amounts MODEL.

**Authorization:** the author, 16 November 2026, 07:02 ("Yes go ahead and add it"), on the proposal of 06:57.

## The story assumption

In this timeline no Edmunds–Tucker Act disincorporates the Church and the Perpetual Emigrating Fund (1887), and confederal law imposes no single marriage system (CR-060). The gathering of converts to Deseret therefore goes on after 1887. Plural marriage itself adds no births. Wives in plural unions had slightly fewer children each than wives in monogamous unions (Smith and Kunz, *Population Studies* 1976). The Utah Population Database shows about one child fewer per wife for each wife added (Moorad, Promislow, Smith and Wade, *Evolution and Human Behavior* 2011). The model therefore adds the gathering and the Saints' higher birth rate, not polygyny.

## What the sheet does

| Column | Content |
| --- | --- |
| B | Convert arrivals a year (input): 2,500 in 1888–99, 3,500 in 1900–14, 1,000 in 1915–18, 3,000 in 1919–25, then 2,000, 1,500 and 1,000 to 1928, none after. The Fund aided about 100,000 emigrants in 1849–87, about 2,600 a year; before 1888 the historical gathering is inside the generic streams. |
| C | Arrivals × `dg_scale` (Story 1, Stress 0.5) |
| D | The Saints joining with Deseret in 1867: 68,932 (`joins_cr059_068.toml`) × `dg_share` (0.95) |
| E | The Saints in Pacifica (memo): last year × (1 + Pacifica's natural increase + `dg_prem`), plus D, plus C net of returns (`dg_ret`, Story 5%, Stress 10%) |
| F | Extra births from the premium (`dg_prem`, Story 0.6 point a year above Pacifica's rate, Stress 0.3) |
| G | The Saints' share of residents |

People E adds C, People D adds F, and People I applies `dg_ret` to the converts instead of the general return rate (Paths I). The population model reads the sheet and carries both as the stream "Deseret" (`population/canon.py`; converts 48% men, `assumptions.toml`).

## Results

| | Before | **With Deseret** |
| --- | --- | --- |
| Residents, end of 1932 | 36.77m | **37.06m** |
| The Saints in 1932 | — | **0.51m** (1.4% of residents; Utah's Church membership historically: 309,400 in 1930) |
| Deseret stream in the population model, 1932 | — | 315,000 (converts and the premium, with descendants) |
| Story / Stress failed year-checks | 0 / 51 | **0 / 51** |
| Output per person against US history, 1929 | 2.30× | 2.30× |
| Cohort model against the sheet, 1932 | 0.3% | **0.2%** |

The storyline's figures hold: about 37 million residents in 1932; about 5.8 against 4.8 million Japanese- and Chinese-origin Pacificans. The energy pair re-converged in five passes. Financial workbook SHA-256 `6bc8d2aa73fff847173fdbd50cea92786e30a98a722289d18ee50d093ecf6f17`, energy `ce927f04…`.

## Not modelled

- **The young men without wives.** Plural marriage in a mostly closed community leaves young men unmarried. In the story they would leave for the Sound, the mines or the cities. The model does not move them out of the Saints' stock.
- **Conversions inside Pacifica.** These move people between faiths and add no residents.
- **Missions in Asia** (Japan from 1901, Hawaii). Their converts are in the Asian streams.

## For the author

The storyline does not yet say that the Fund survives or that the gathering continues. A one-line passage under Deseret (CR-060's section) would carry it, labelled PROPOSED until approved.
