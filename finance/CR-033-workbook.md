# Workbook revisions, 27–28 October 2026: population, the Land Fund, a larger Events table and skilled entry from 1856

## 28 October 2026: CR-034 A24, skilled entry from 1856

SHA-256 of the current workbook: `061d6c34e23084123ced0a961c13eb4b491bf06f1b5d9772e8fff2677acfd89a`. It is the 27 October revision below plus one change, made by [`build/cr034_skilled_entry.py`](build/cr034_skilled_entry.py) at the author's decision of 28 October 2026 (CR-034 A24, adopted with CR-033 to CR-036):

- **Levers "First year of the skilled-entry programme": 1856** (was 1880), in both cases. The places cap, a share of residents, ramps the programme with the population; no separate ramp was added.
- **Paths C re-iterated.** The population model and the workbook were iterated until the natural-increase rates stopped changing (two rounds; [`build/paths_c_rates.csv`](build/paths_c_rates.csv)).
- **DEM-01 multiplier unchanged** at 2.10: residents at the start of 1861 are 1.24m, still "about 1.2 million" and inside the 10% check.
- Recalculated in LibreOffice: 51,127 formulas, no errors. **Story case: no failed checks. Stress case: 11 failed checks, the same as before A24.** The Land Fund results below do not change, because they rest on farm acreage, not population.

| Story case | 1865 | 1895 | 1918 | 1929 | 1932 |
|---|---|---|---|---|---|
| Residents, m (27 Oct) | 1.90 (1.82) | 8.33 (7.25) | 22.9 (20.4) | 33.4 (30.1) | 36.2 (32.6) |
| Asian-origin share | 10.4% | 18.5% | 25.2% | 28.8% | 29.4% |
| Core GDP, $bn | 0.53 | 3.49 | 38.1 | 69.6 | 54.9 |
| GDP per resident vs the US | 1.91 | 2.07 | 2.20 | 2.36 | 3.14 |
| Public debt, $m | 13 | 174 | 1,903 | 3,479 | 2,943 |

From the population model on this workbook (end of year): Japanese-origin 5.59m and Chinese-origin 4.77m in 1932 (Japanese arrivals overtake Chinese in 1901, the Japanese-origin population in 1923); Native Californians low 99,000 in 1896, 131,000 in 1932; Native Hawaiians low 42,000 in 1895, 68,000 in 1932. The author chose these workbook figures for the storyline (28 October 2026); DEM-01 in `war_base_assumptions.md` replaces the CR-015 range of 4–6.5m for 1895.

## 27 October 2026: population, the Land Fund and a larger Events table

This revision added the population change list (P1–P6) and a Land Fund sheet for CR-033. Its SHA-256 was `6342b6c25301c50f7973c132549bbbac86fa1cc9e6cae76436574310454eefde` (sale price tied to land values; see below); the 28 October revision above supersedes it.

The 23 October CR-031 workbook it replaces is in Git history, and [CR-031-review.md](CR-031-review.md) still describes that version. The edits are made by [`build/cr033_population_landfund.py`](build/cr033_population_landfund.py) from the 23 October file. They were recalculated in LibreOffice: 51,127 formulas, no errors.

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
| Residents, m (was) | 1.82 (1.22) | 7.25 (6.53) | 20.4 (17.6) | 30.1 (25.5) | 32.6 (27.3) |
| Asian-origin share (was) | 9.6% (7.6%) | 16.9% (14.6%) | 24.6% (17.2%) | 28.4% (19.4%) | 29.0% (20.0%) |
| Core GDP, $bn (was) | 0.49 (0.34) | 2.91 (2.53) | 33.4 (27.9) | 61.9 (50.8) | 48.9 (39.5) |
| GDP per resident vs the US (was) | 1.85 (1.93) | 1.99 (1.92) | 2.16 (2.07) | 2.34 (2.25) | 3.10 (2.98) |
| Public debt, $m (was) | 13 (94) | 146 (126) | 1,668 (1,393) | 3,097 (2,539) | 2,634 (2,169) |

Checks: 0 problems. The Stress case falls from 17 problems to 11. The private-saving failures of 1861–64, 1867, 1872 and 1920 disappear, and a new one appears in 1887.

Three knock-on effects for the author:

1. **More arrivals.** The workbook's own migration responds to size. Skilled-entry places are a share of residents, and relatives follow the talent stock. So the larger population draws more arrivals: 32.6m at the end of 1932, against the stand-alone model's 30.9m. CR-033 as adopted says about 36 million, after A24.
2. **The Civil War costs far less.** With half as many people again in the 1860s, the war years' receipts carry most of the war, and the debt in 1865 is $13m instead of $94m.
3. **The economy is bigger, but output per head barely moves.** GDP rises about 20%, while output per resident against the US rises only slightly.

## Does the Land Fund pay for itself?

**The model.** The Republic buys, five years ahead of settlement, the farm land Pacifica needs beyond the old grants. Our timeline's California farm acreage from the census is the measure of that need: 21.6m acres by 1932. Prices and other inputs:
- **Purchase:** 10¢ an acre, as twenty years of annuities in goods.
- **Sale:** settlers pay over five years, and 10% is never paid. The sale price follows land values (see below).
- **Old grants:** 5% of the grant land is paid in for fast patents and sold.
- **Homeland leases:** 30% of the 7.4m acres of homelands are leased by 1932 at 5¢ an acre, and the Republic keeps 10% of the rent.
- **Survey:** 3¢ an acre.
- **Mounted police:** 300 men in 1852–70 and 150 in 1871–90, at $1,150 a man at 1877 prices (NWMP).
- **Interest:** 5% a year on the balance.

Treaty prices, annuity terms and boundaries are OPEN in canon, so every number here is a lever.

**The sale price follows land values** (author decision, 27 October 2026). It is the larger of a floor and a share of the census value of California farm land and buildings per acre in that year.
- **The floor** is $1.25 an acre, the US public-land price across the border; from 1862 the Homestead Act gave land away free.
- **The share** is 20%. Raw, unsurveyed land is worth a fraction of an average farm with its improvements and buildings, and the better districts go at auction.
- **The resulting path:**

  | Year | 1861 | 1870 | 1880 | 1890 | 1900 | 1920 |
  |---|---|---|---|---|---|---|
  | Sale price, $ an acre | 1.25 | 2.46 | 3.16 | 6.51 | 4.91 | 20.93 |

  The average over all sales is $5.48.
- **Earlier draft:** it used a flat $1.25 for the whole period, which ignored land values rising from $5.58 an acre in 1860 to $24.56 in 1900.

| Case | Land Fund net, $m | Same, value in 1850 | Policy incl. police, $m | Same, value in 1850 | Policy back in credit, with interest | Margin ÷ assisted passage |
|---|---|---|---|---|---|---|
| Story (share 20%) | +97.9 | +12.5 | +87.4 | +7.3 | 1882 | 47% |
| Stress (share 10%, floor $1, dearer purchases and police) | +38.8 | +3.3 | +26.0 | −2.3 | never | 21% |
| Share 10% | +48.7 | +6.5 | +38.2 | +1.3 | 1896 | 24% |
| Share 30% | +147.9 | +18.9 | +137.4 | +13.7 | 1877 | 72% |
| Flat $1.25 (earlier draft) | +21.9 | +4.2 | +11.4 | −0.9 | never | 11% |
| Price paid 50¢ | +89.5 | +11.0 | +79.0 | +5.9 | 1886 | 43% |
| Police doubled | +97.9 | +12.5 | +76.9 | +2.2 | 1898 | 47% |
| No police | +97.9 | +12.5 | +97.9 | +12.5 | 1857 | 47% |

**Findings**

- **The purchases pay for themselves.** The Land Fund is never in deficit and is back in credit by 1857. It nets about $98m by 1932 in the Story case. Cheap annuities spread over twenty years, against sales at a rising price, carry it. The cold side of the monopoly buyer (A17) is what makes the arithmetic work.
- **The whole policy pays too.** The police cost about $10.5m in 1852–90, mostly before the land sales arrive. Even so, the policy is +$7.3m in 1850 money and back in credit, with interest, by 1882. It stays positive at a 10% share, with the police doubled, and when paying five times as much for the land. It fails only in the Stress case, and with a flat $1.25 price.
- **"Cheaper than war."** Our timeline's militia claims in the 1850s were $1.3m. In the 1850s the police cost more than those expeditions did, but over the period the land margin more than repays them.
- **A18 is half true.** The margin covers about 47% of assisted passage over 1852–1932 (21–72% across the cases). The author chose "helps pay for" on 28 October 2026.
- **What the Land Fund doesn't model:** effects of clean titles on credit or output, the treaty commissions themselves, and police beyond the mining districts.

## Sources for the Land Fund inputs

- California land in farms and average value of farm land and buildings per acre: [1920 Census of Agriculture bulletin, California](https://www2.census.gov/library/publications/decennial/1920/bulletins/agriculture/agriculture-ca.pdf) (1850–1920); [1959 Census of Agriculture, California, Table 1](https://agcensus.library.cornell.edu/wp-content/uploads/1959-California-CHAPTER_A_-_STATISTICS_FOR_THE_STATE-865-Table-01.pdf) (1925–1930).
- 7.4m acres of treaty reservations, 1851–52: [Wikipedia, California Indian Reservations and Cessions](https://en.wikipedia.org/wiki/California_Indian_Reservations_and_Cessions).
- 604 of 813 grant claims confirmed, average 17 years: [Wikipedia, California Land Act of 1851](https://en.wikipedia.org/wiki/California_Land_Act_of_1851). The 8.8m acres of confirmed grant land is a commonly cited figure, still to verify.
- NWMP expenditure of $345,959 in 1877–78: [Tilley's budget speech, 3 March 1885](https://lop.parl.ca/staticfiles/ParlInfo/Documents/Budgets/En/1885-03-03.pdf); 300 men authorised in 1873: [Statistical Year-Book of Canada 1890](https://www66.statcan.gc.ca/eng/1890/189005280512_p.%20512.pdf).
- California militia claims of $1,293,179: [California State Military Museum](https://www.militarymuseum.org/MilitiaandIndians.html).
- Wakefield's land fund for emigration in South Australia: [La Croix, University of Hawaii working paper 19-10](https://www.economics.hawaii.edu/research/workingpapers/WP_19-10.pdf).
- Purchase price, survey cost, default, lease and interest rates: MODEL estimates, marked on Levers.
