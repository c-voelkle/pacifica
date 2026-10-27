# Workbook revision, 27 October 2026: population, the Land Fund and a larger Events table

`Pacifica_financial_model_1846-1932.xlsx` now carries the population change list (P1–P6) and a Land Fund sheet for draft CR-033. SHA-256: `f7462c1cb998dd3c4da917240e1f02d63604bdc9e9b51ef8ac16f670a98baeef`.

The 23 October CR-031 workbook it replaces is in Git history, and [CR-031-review.md](CR-031-review.md) still describes that version. The edits are made by [`build/cr033_population_landfund.py`](build/cr033_population_landfund.py) from the 23 October file. They were recalculated in LibreOffice: 50,864 formulas, no errors.

Before editing, the unchanged workbook was recalculated in LibreOffice to check that it reproduces the author's saved Excel values. It reproduced all 63,415 numeric cells exactly. The results below therefore compare like with like.

## What changed

| Area | Change |
|---|---|
| **Events** | Every Events range now runs to row 400 instead of 174, so new events are counted. Tested: an event in row 175 reaches Budget. |
| **P1 (Paths C)** | The natural-increase rate now comes from the population model. It works by age, sex and group, with the canon health and fertility paths and the Native Hawaiian and Native Californian paths. It was iterated with the workbook until it stopped changing, and the values are in `build/paths_c_rates.csv`. The model and the sheet now agree on residents in every year. |
| **P2 (Levers `dem01_mult`)** | Arrivals from the Americas, Europe and China in 1848–60 are multiplied by 2.10 (DEM-01). There are 1.21m residents at the start of 1861. |
| **P3 (Levers `xo_*`, People N–R)** | The extra arrivals drawn by Pacifica's lead are split by origin. Japan, China and the Philippines take 0.20/0.10/0.00 before 1914 and 0.32/0.13/0.05 after; the Americas and Europe take the rest. People Q and R are folded into N–P, so nothing is counted twice. |
| **P4 (People Y, Z)** | Memo columns for Native Hawaiians and Native Californians from the population model. They are not part of the totals. |
| **P5 (Checks AJ, AK)** | Two new checks: the Native Hawaiian low falls in 1893–97, and 1861 residents are within 10% of DEM-01's 1.2m. Both pass. |
| **P6** | A note on Levers C8 says that the 170,000 Californians of 1846 include about 150,000 Native Californians. |
| **Land Fund** | A new sheet and Levers `lfund_*`. Its net cash goes into Budget G ("Other receipts (Events, Land Fund)"). |

## Results, Story case

| | 1865 | 1895 | 1918 | 1929 | 1932 |
|---|---|---|---|---|---|
| Residents, m (was) | 1.82 (1.22) | 7.24 (6.53) | 20.3 (17.6) | 29.9 (25.5) | 32.5 (27.3) |
| Asian-origin share (was) | 9.6% (7.6%) | 16.9% (14.6%) | 24.6% (17.2%) | 28.4% (19.4%) | 29.0% (20.0%) |
| Core GDP, $bn (was) | 0.49 (0.34) | 2.90 (2.53) | 33.1 (27.9) | 61.4 (50.8) | 48.4 (39.5) |
| GDP per resident vs the US (was) | 1.85 (1.93) | 1.98 (1.92) | 2.15 (2.07) | 2.32 (2.25) | 3.08 (2.98) |
| Public debt, $m (was) | 13 (94) | 145 (126) | 1,653 (1,393) | 3,068 (2,539) | 2,612 (2,169) |

Checks: 0 problems. The Stress case falls from 17 problems to 11. The private-saving failures of 1861–64, 1867, 1872 and 1920 disappear, and a new one appears in 1887.

Three knock-on effects for the author:

1. **More arrivals.** The workbook's own migration responds to size. Skilled-entry places are a share of residents, and relatives follow the talent stock. So the larger population draws more arrivals: 32.5m at the end of 1932, against the stand-alone model's 30.9m. CR-033 says "about 30 million".
2. **The Civil War costs far less.** With half as many people again in the 1860s, the war years' receipts carry most of the war, and the debt in 1865 is $13m instead of $94m.
3. **The economy is bigger, but output per head barely moves.** GDP rises about 20%, while output per resident against the US rises only slightly.

## Does the Land Fund pay for itself?

**The model.** The Republic buys, five years ahead of settlement, the farm land Pacifica needs beyond the old grants. Our timeline's California farm acreage from the census is the measure of that need: 21.6m acres by 1932. Prices and other inputs:
- **Purchase:** 10¢ an acre, as twenty years of annuities in goods.
- **Sale:** $1.25 an acre, the US public-land price, over five years, with 10% never paid.
- **Old grants:** 5% of the grant land is paid in for fast patents and sold.
- **Homeland leases:** 30% of the 7.4m acres of homelands are leased by 1932 at 5¢ an acre, and the Republic keeps 10% of the rent.
- **Survey:** 3¢ an acre.
- **Mounted police:** 300 men in 1852–70 and 150 in 1871–90, at $1,150 a man at 1877 prices (NWMP).
- **Interest:** 5% a year on the balance.

Treaty prices, annuity terms and boundaries are OPEN in canon, so every number here is a lever.

| Case | Land Fund net, $m | Same, value in 1850 | Policy incl. police, $m | Same, value in 1850 | Policy back in credit, with interest | Margin ÷ assisted passage |
|---|---|---|---|---|---|---|
| Story | +21.9 | +4.2 | +11.4 | −0.9 | never | 11% |
| Stress | +11.1 | +1.5 | −1.7 | −4.1 | never | 6% |
| Price paid 50¢ | +13.5 | +2.8 | +3.0 | −2.4 | never | 7% |
| Sale price $2.50 | +46.4 | +9.2 | +35.9 | +4.0 | 1879 | 22% |
| Police doubled | +21.9 | +4.2 | +0.9 | −6.1 | never | 11% |
| No police | +21.9 | +4.2 | +21.9 | +4.2 | 1857 | 11% |

**Findings**

- **The purchases pay for themselves.** The Land Fund is never in deficit and is back in credit by 1857. It nets about $22m by 1932 in the Story case and stays positive in every case tested. Cheap annuities spread over twenty years, against settlers' instalments, carry it. The cold side of the monopoly buyer (A17) is what makes the arithmetic work.
- **The wider policy only breaks even.** The mounted police cost about $10.5m in 1852–90, mostly before the land sales arrive. Counting interest, the policy as a whole is roughly break-even and slightly negative: −$0.9m in 1850 money. It clearly pays only if the Republic sells nearer market value: at $2.50 an acre it is back in credit by 1879. California farm land was worth $5.58 an acre with buildings in 1860 and $12.30 in 1870. Our timeline's militia claims in the 1850s were $1.3m. So in direct cash the police cost more than the volunteer expeditions did, and "cheaper than war" holds only if canon's other reasons count: credit, clean title, the monopoly of force, and the Hawaiian partners.
- **A18 overstates.** The land margin covers about 11% of assisted passage over 1852–1932 (6–22% across the cases), not all of it. CR-033's "the margin pays for assisted passage" would need to become "helps pay for".
- **What the Land Fund doesn't model:** effects of clean titles on credit or output, the treaty commissions themselves, and police beyond the mining districts.

## Sources for the Land Fund inputs

- California land in farms: [1920 Census of Agriculture bulletin, California](https://www2.census.gov/library/publications/decennial/1920/bulletins/agriculture/agriculture-ca.pdf) (1850–1920); [1959 Census of Agriculture, California, Table 1](https://agcensus.library.cornell.edu/wp-content/uploads/1959-California-CHAPTER_A_-_STATISTICS_FOR_THE_STATE-865-Table-01.pdf) (1925–1930).
- 7.4m acres of treaty reservations, 1851–52: [Wikipedia, California Indian Reservations and Cessions](https://en.wikipedia.org/wiki/California_Indian_Reservations_and_Cessions).
- 604 of 813 grant claims confirmed, average 17 years: [Wikipedia, California Land Act of 1851](https://en.wikipedia.org/wiki/California_Land_Act_of_1851). The 8.8m acres of confirmed grant land is a commonly cited figure, still to verify.
- NWMP expenditure of $345,959 in 1877–78: [Tilley's budget speech, 3 March 1885](https://lop.parl.ca/staticfiles/ParlInfo/Documents/Budgets/En/1885-03-03.pdf); 300 men authorised in 1873: [Statistical Year-Book of Canada 1890](https://www66.statcan.gc.ca/eng/1890/189005280512_p.%20512.pdf).
- California militia claims of $1,293,179: [California State Military Museum](https://www.militarymuseum.org/MilitiaandIndians.html).
- Wakefield's land fund for emigration in South Australia: [La Croix, University of Hawaii working paper 19-10](https://www.economics.hawaii.edu/research/workingpapers/WP_19-10.pdf).
- Purchase price, survey cost, default, lease and interest rates: MODEL estimates, marked on Levers.
