# CR-083 to CR-086: the endgame of 1931–32 in the models (24 November 2026)

**Authorization:** the author, 23 November 2026, 23:52 ("Please run the third review and then proceed to rebuild the models").

**Status:** the four CRs are drafts on branch `drafts/cr083-086-endgame` and are not canon. These model changes live on that branch with them and go to `main` only with the CRs. Every amount is MODEL. Where a draft leaves a band OPEN, the size used here is the drafter's proposal and is marked so.

Three things changed:
1. **The provisioning model** (`population/provisioning.py`, `population/data/provisioning.toml`): the northern water is withdrawn, and the prairie wheat contract is sized.
2. **The financial workbook**: a new last step, `finance/build/cr083_086_endgame.py`, after `cr081_082_provisioning.py` in `cr057_rebuild_pair.py`. Its master lever is `eg_on`; at 0 the step reproduces its input exactly (110,134 values outside Levers, Events and Changes, none differs).
3. **A new sheet, `Endgame`**, which works Britain's annuities and holds the memos.

The energy workbook's inputs are not changed by this step.

## Britain's annuities

The workbook holds the Treasury's European claims as one balance ($2,023m at the end of 1931), repaid at a flat rate. Britain's part is a lever, `eg_uk_share`, at 0.6 with no source. The 62-year funding of 1923 is worked as level annuities at 3.3%, with 53 left after the moratorium year.

| | Story | Stress |
| --- | --- | --- |
| Britain's part of the claims, end of 1931 | $1,214m | $1,755m |
| Britain's annuity | $48.8m a year | $74.6m a year |
| Tranche 1, Caledonia, from the end of the schedule | 5 annuities, 3.8% of the book, $47m | 6 |
| Tranche 2, the retrenchment, from the end | 6 annuities, 5.5%, $67m | 7 |
| Tranche 3, the signature, from the near end | 6 annuities, 21.6%, $262m | 7 |
| All three | 17 annuities, **30.9% of the book** | 20 annuities, 36.2% |
| The suspended annuity, principal part | $19m | |
| **Written off in 1932** | **$395m** | $702m |
| Britain pays nothing in | 1933 to 1938 | 1933 to 1939 |
| Britain's last annuity | 1974 | 1972 |

Three findings for the drafts:
- **A count of annuities is not a share of the book.** `CR-084` `B1` calls 15 to 20 of 53 annuities "~28–38% of remaining principal". That holds only because the third tranche now comes from the near end (`T-A2`, decided 23 November, 23:52). Had all 17 come from the end, as item 84-8 first had it, they would be 16.0% of the book (Story; 19.9% in Stress): annuities due in the 1970s and 1980s are worth little in 1932.
- **The signature is most of the price.** The six annuities of 1933–38 are worth $262m, more than twice the other two tranches together ($114m). Caledonia's tranche is $47m.
- **The split of 5, 6 and 6** is the drafter's proposal. The author found the band of 15 to 20 "acceptable pending modeling" (23 November, 20:11); the split is his to decide.

## Events rows

| Row | Years | Category | Story | Stress | What |
| --- | --- | --- | --- | --- | --- |
| E258 | 1871 | Loan (Continental) | $2m | $3m | British Columbia: the loan to the colony with the Puget Sound rail link (`CR-083` `A2`) |
| E259 | 1928–31 | Receipt | $3.1m a year | $2.5m a year | Tokyo station: Tokyo Dentō's site, containment, turbines and grid, 55% of the $22.4m the Atomic sheet enters as Pacifica's (`CR-085` `C1`) |
| E260 | 1932 | Purchase | $0.4m | $0.6m | Fanning and Washington: the plantation buyout (`CR-084` `B4`; no source) |
| E261 | 1932 | Commitment (memo) | $27m | $36m | The prairie wheat contract's first harvest, bought by the Patrimony's board: 1.5 million tonnes at $18 (`CR-083` `A11`) |
| E262 | 1932 | Commitment (memo) | $90m | $120m | The dominion's gold-dollar bonds refunded by private syndicates (`CR-083` `A10`; recalled, to verify) |
| E263 | 1932 | Commitment (memo) | $300m | $400m | Private stabilization credits to Britain, Germany and France (`CR-086` `B1`; no source) |

The Budget, Loans and money sheets do not read the Commitment category, so the three memos move no Treasury cash and no gold. The Events column "Story status" reads Draft for all six.

## Results

| | Before | **After** |
| --- | --- | --- |
| Story / Stress failed year-checks | 0 / 51 | **0 / 51** |
| Loans abroad outstanding, 1932 | $2,695.1m | **$2,300.6m** |
| European claims outstanding, 1932 | $2,023.3m | $1,628.6m |
| Public debt, 1932 | $1,929.1m | $1,927.1m |
| Monetary gold, 1932 | $1,539.3m | $1,539.3m |
| Residents, end of 1932 | 37.07m | 37.07m |

- The write-off costs the Treasury no cash in the book: the moratorium has already stopped Europe's payments in 1931–32, and the annuities of 1933–38 lie after the book's last year. What the Realm gives up is about $49m a year of receipts for six years after 1932.
- Public debt falls by $2m because Tokyo Dentō pays for part of a station the workbook had charged to Pacifica.
- LibreOffice recalculation: 83,775 formulas, no errors in either case.

## The provisioning model

- **The northern water is withdrawn** (item 83-1). `[century]` loses `water_km3` and its companions, and `century()` no longer counts work 2. The Realm's own works feed 89.0 million a century on (was 115.2 million), 16% of the need. To close the plan the Realm must buy **81%** of what the listed sellers sell abroad (was 76%), about 76% of the world's grain and soybean trade of today. The storyline's "three-quarters or more" (`L1672`) holds.
- **One result moves against a sentence of the report.** Without the Union's grain, every tonne of every other seller now reaches 95% of the need, not 100%. If the storyline or `CR-082` says that the plan can close without the Union, that sentence needs a look on integration.
- **The prairie wheat contract** is sized in a new `[endgame]` block: 1.5 million tonnes a harvest for ten harvests, 27% of Canada's exports of 1931–32, $27m a year at the slump's price.
  - The cabinet's second figure (`CR-083` `A12`): 0 mouths in the Realm; abroad, bread for 1.4 million on the Realm's diet.
  - Giannini's case: the Realm itself sells 3.0 million tonnes abroad in 1932, so the board's wheat is half as much again in the same market. That is a large share, and it makes his objection stronger than the draft lets it be. A band of 1.0 to 2.0 million tonnes is the drafter's proposal.
- Tests: `population/tests/test_provisioning.py`, 13 pass.

## Not done, and why

- **The Atomic sheet** (`CR-086` Part A): Great Bear's 200–350 t, the Portuguese and South Australian purchases and the monazite stock are a memo on the Endgame sheet. The sheet's sources are fixed in `cr049_atomic_programme.py` and `cr050_atomic_retiming.py`; adding a source means reopening both.
- **The energy workbook** (`CR-084`, `CR-085`): the Gulf's lifting share, Seria's offtake, East Borneo's crude, Bintan's bauxite and the stations' fuel loads have no tonnages in the drafts yet.
- **Japan's rice and Hokkaido** (`CR-085` `D1`): the third review's finding that the mechanisms are partly history's own is not yet answered, so the series is not entered.
- **Caledonia's population**: the Realm's count is unchanged; a separate count for the republic is not built.
- **Article II's mouths** (`CR-086` `D6`): the article feeds no one in the Realm, and the Pampas volumes are not modelled.
- **The yen reset** (`CR-085` `A7`): one line on the Endgame sheet (a reset of 20% makes Japan's gold-dollar quota 25% dearer in yen; 25% makes it 33% dearer). The banks' repayments and the Bank of Japan's ceiling are not modelled.
- **The private stabilization credits** are a memo. Entered as private lending they would pass through the gold and money sheets, and those tests would have to be read again.

## How to rebuild

```
python3 finance/build/cr057_rebuild_pair.py WORKDIR --recalc PATH_TO_recalc.py
python3 population/provisioning.py
python3 -m pytest -q population/tests
```
