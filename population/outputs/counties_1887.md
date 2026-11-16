# The counties of 1 August 1887 on Pacifica's territory: historical baseline and a regional split

Built by `population/counties_1887.py`. Sections 1 and 3 are our timeline (sources below). Section 2 is MODEL and waits for the author's decision. Nothing here is canon.

## 1. Our timeline: counties, area and people by old unit

Counties whose people would be Pacifican in 1887. "Whole" counts a county if any of it lies on Pacifica's side; "split" lists those the line cuts. Population is the census's, which before 1890 leaves out Indians not taxed.

| Old unit | Counties, 1 Aug 1887 | Area, sq mi | 1880 | 1890 (1887 lines) | 1887 est. | People per county | Median county |
|---|---|---|---|---|---|---|---|
| California | 52 | 158,094 | 864,694 | 1,208,130 | 1,098,904 | 21,132 | 12,613 |
| Oregon | 29 | 96,951 | 174,668 | 313,767 | 265,786 | 9,165 | 7,430 |
| Columbia | 33 | 67,564 | 75,116 | 349,390 | 226,032 | 6,849 | 4,965 |
| Idaho | 15 | 83,597 | 32,610 | 84,079 | 64,289 | 4,285 | 2,673 |
| Western Montana | 9 (1 split) | 43,315 | 32,040 | 96,464 | 69,396 | 7,710 | 5,077 |
| Washoe | 14 | 110,563 | 62,266 | 45,761 | 49,934 | 3,566 | 2,611 |
| Deseret | 24 | 84,896 | 143,963 | 207,905 | 187,345 | 7,806 | 3,983 |
| Deseret (southwest Wyoming) | 2 | 24,365 | 5,440 | 12,355 | 9,781 | 4,890 | 5,676 |
| New Mexico | 14 | 121,590 | 119,565 | 153,593 | 143,072 | 10,219 | 10,152 |
| New Mexico (Arizona county) | 10 | 113,999 | 40,440 | 59,620 | 53,411 | 5,341 | 4,843 |
| The Rockies (Colorado) | 31 (4 split) | 51,020 | 94,822 | 126,086 | 117,717 | 3,797 | 3,710 |
| **Mainland** | **233** | **955,954** | **1,645,624** | **2,657,150** | **2,285,667** | 9,809 | |
| Hawaii | no counties before 1905; 5 island groups | 6,375 | (1884) 80,578 | 89,990 | 85,108 | | |
| Alaska | none; 6 census divisions in 1880 | about 586,000 | 33,426 | | | | |

Hawaii by island, 1884 / 1890: Hawaii 24,991 / 26,754; Maui 15,970 / 17,357; Molokai and Lanai 2,614 / 2,826; Oahu 28,068 / 31,194; Kauai and Niihau 8,935 / 11,859.
Alaska in 1880 by division (Petroff): Southeastern 7,748; Kodiak 4,352; Aleutian 2,451; Kuskokwim 8,911; Yukon 6,870; Arctic 3,094; 430 white and 1,756 Creole residents.

Baja California (the purchase of 1867, PROPOSED in the storyline; switched off in the workbook) is not in this table or in the outline's strawman.

## 2. Where Pacifica's people of 1887 live (MODEL; for decision)

The population model has 5,839,706 residents at the end of 1887 and no regions. Its only regional memory is `joined_territories`, 393,491: the head counts of 1867 with their natural increase and no migrant after 1867. Read literally, the interior and the Northwest hold 7% of the people.

The variants below fix Hawaii at one and a half times its historical population (Japanese settlement; MODEL) and Alaska at 40,000 (Petroff's count plus the garrison of settlers; MODEL), set each acceded unit at a multiple of its historical 1887 population, and give California the rest.

| Old unit | History 1887 | V1 interior as in history | V2 interior one and a half times history | V3 interior twice history | V4 every region in proportion | Strawman counties (I2) |
|---|---|---|---|---|---|---|
| California | 1,098,904 | 4,485k (77%) | 3,892k (67%) | 3,299k (56%) | 2,727k (47%) | 41 |
| Oregon | 265,786 | 266k (5%) | 399k (7%) | 532k (9%) | 660k (11%) | 14 |
| Columbia | 226,032 | 226k (4%) | 339k (6%) | 452k (8%) | 561k (10%) | 14 |
| Idaho and western Montana | 133,685 | 134k (2%) | 201k (3%) | 267k (5%) | 332k (6%) | 9 |
| Washoe | 49,934 | 50k (1%) | 75k (1%) | 100k (2%) | 124k (2%) | 5 |
| Deseret | 187,345 | 187k (3%) | 281k (5%) | 375k (6%) | 465k (8%) | 9 |
| New Mexico | 143,072 | 143k (2%) | 215k (4%) | 286k (5%) | 355k (6%) | 9 |
| Arizona | 53,411 | 53k (1%) | 80k (1%) | 107k (2%) | 133k (2%) | 6 |
| The Rockies | 127,498 | 127k (2%) | 191k (3%) | 255k (4%) | 316k (5%) | 6 |
| Hawaii | 85,108 | 128k (2%) | 128k (2%) | 128k (2%) | 128k (2%) | 5 |
| Alaska | 33,426 | 40k (1%) | 40k (1%) | 40k (1%) | 40k (1%) | 5 |

**What each variant does to the Senate of 1888** (123 county senators; the strawman's counts; California's 41 include San Francisco):

| | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| California's share of the people | 77% | 67% | 56% | 47% |
| California's share of county senators | 33% | 33% | 33% | 33% |
| People per Californian county | 109k | 95k | 80k | 67k |
| People per county elsewhere on the mainland | 16k | 25k | 33k | 41k |
| Counties California would have by population alone (of 124) | 95 | 83 | 70 | 58 |

## 3. Sources and checks

- **Counties, dates and areas:** Atlas of Historical County Boundaries (Newberry Library; CC0), every county whose boundary version covers 1 August 1887 (`data/counties/newberry_1887.csv`).
- **County populations:** census totals as given in each county's English Wikipedia article, read on 16 November 2026 (`data/counties/census_by_county_raw.txt`). Status: identity-checked for 1880 where the state sums close.
- **1887:** log-linear between the censuses of 1880 and 1890, each state scaled to its own interpolated total; counties created between August 1887 and 1890 are folded into their parents (`overrides.toml`). An estimate.
- **The line in Montana, Wyoming and Colorado:** `[pacifica_share]` in `overrides.toml`; the split counties' fractions are guesses.

| State | Counties | Sum of counties 1880 | Census 1880 | Difference | Sum 1890 | Census 1890 | Difference |
|---|---|---|---|---|---|---|---|
| AZ | 10 | 40,440 | 40,440 | 0 | 59,620 | 88,243 | 28,623 |
| CA | 52 | 864,694 | 864,694 | 0 | 1,208,130 | 1,213,398 | 5,268 |
| CO | 42 | 193,883 | 194,327 | 444 | 411,838 | 413,249 | 1,411 |
| ID | 15 | 32,610 | 32,610 | 0 | 84,079 | 88,548 | 4,469 |
| MT | 15 | 38,989 | 39,159 | 170 | 132,159 | 142,924 | 10,765 |
| NM | 14 | 119,565 | 119,565 | 0 | 153,593 | 160,282 | 6,689 |
| NV | 14 | 62,266 | 62,266 | 0 | 45,761 | 47,355 | 1,594 |
| OR | 29 | 174,668 | 174,768 | 100 | 313,767 | 317,704 | 3,937 |
| UT | 24 | 143,963 | 143,963 | 0 | 207,905 | 210,779 | 2,874 |
| WA | 33 | 75,116 | 75,116 | 0 | 349,390 | 357,232 | 7,842 |
| WY | 8 | 20,789 | 20,789 | 0 | 57,816 | 62,555 | 4,739 |

1880: Colorado (444), Montana (170) and Oregon (100) do not close and are to be traced. 1890: the census totals include Indians on reservations, whom the county figures leave out, so the differences are expected; San Francisco, Ormsby and Alturas for 1890 are unverified (`overrides.toml`).
