# CR-083 to CR-086: the endgame of 1931–32 in the models (24 November 2026)

**Authorization:** the author, 23 November 2026, 23:52 ("Please run the third review and then proceed to rebuild the models").

**Rebuilt twice on 24 November 2026:** first with the drafter's proposed sizes, then with the author's of 00:12 (the split of 2, 4 and 11 and the contract at 1.0 million tonnes). This note gives the second.

**Status:** the four CRs were approved on 24 November 2026 (13:08) and merged to `main` (pull request 88). The models were rebuilt on `main` the same day on the author's word of 14:56 ("Please proceed to rebuild the workbooks"); what that rebuild changed is in the last section. Every amount is MODEL. Where a CR leaves a band OPEN, the size used here is the drafter's proposal and is marked so.

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
| Tranche 1, Caledonia, near end (1932–33, 1933–34) | 2 annuities, 7.7% of the book, $93m | 2 |
| Tranche 2, the retrenchment, from the end (1974–75 to 1984–85) | 11 annuities, 9.4%, $114m | 13 |
| Tranche 3, the signature, near end (1934–35 to 1937–38) | 4 annuities, 13.9%, $169m | 5 |
| All three | 17 annuities, **30.9% of the book** | 20 annuities, 36.2% |
| The suspended annuity, principal part | $19m | |
| **Written off in 1932** | **$395m** | $702m |
| Britain pays nothing in the annuity years | 1932–33 to 1937–38 | to 1938–39 |
| Britain's last annuity year ends | 1974 | 1972 |

The split of 2, 4 and 11 is the author's (24 November 2026, 00:12). An annuity year runs from 1 July to 30 June, so Britain's next instalment after the moratorium is that of 15 December 1938.

Findings for the drafts:
- **A count of annuities is not a share of the book.** Had all 17 come from the end, as item 84-8 first had it, they would be 16.0% of the book (Story; 19.9% in Stress), not the "~28–38%" the draft then stated: annuities due in the 1970s and 1980s are worth little in 1932.
- **Two near-end annuities for Caledonia are worth about as much as eleven far-end ones for the retrenchment** ($93m against $114m). The signature stays the largest tranche.
- **Britain's part of the claims, six-tenths, has no source.** Every dollar figure above scales with it.

## Events rows

| Row | Years | Category | Story | Stress | What |
| --- | --- | --- | --- | --- | --- |
| E258 | 1871 | Loan (Continental) | $2m | $3m | British Columbia: the loan to the colony with the Puget Sound rail link (`CR-083` `A2`) |
| E259 | 1928–31 | Receipt | $3.1m a year | $2.5m a year | Tokyo station: Tokyo Dentō's site, containment, turbines and grid, 55% of the $22.4m the Atomic sheet enters as Pacifica's (`CR-085` `C1`) |
| E260 | 1932 | Purchase | $0.4m | $0.6m | Fanning and Washington: the plantation buyout (`CR-084` `B4`; no source) |
| E261 | 1932 | Commitment (memo) | $18m | $21.6m | The prairie wheat contract's first harvest, bought by the Patrimony's board: 1.0 million tonnes at $18 (`CR-083` `A11`; Stress 1.2 million) |
| E262 | 1932 | Commitment (memo) | $90m | $120m | The dominion's gold-dollar bonds refunded by private syndicates (`CR-083` `A10`; recalled, to verify) |
| E263 | 1932 | Commitment (memo) | $300m | $400m | Private stabilization credits to Britain and Germany; France sits on gold and asks for none (`CR-086` `B1`, `B3`; no source) |

The Budget, Loans and money sheets do not read the Commitment category, so the three memos move no Treasury cash and no gold. The Events column "Story status" reads Approved for all six since the rebuild on `main`.

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
- **The prairie wheat contract** is sized in a new `[endgame]` block: 1.0 million tonnes a harvest for ten harvests (author, 24 November 2026, 00:12; band 0.8 to 1.2), 18% of Canada's exports of 1931–32, $18m a year at the slump's price.
  - The cabinet's second figure (`CR-083` `A12`): 0 mouths in the Realm; abroad, bread for about 0.95 million on the Realm's diet.
  - Giannini's case: the Realm itself sells 3.0 million tonnes abroad in 1932, so the board's wheat is a third as much again in the same market.
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

## Rebuilt on main, 24 November 2026

**Authorization:** the author, 24 November 2026, 14:56 ("Please proceed to rebuild the workbooks").

The chain was run again from the CR-050 base with the energy workbook. Story: no failed checks; Stress: 51, as before. The energy outputs did not move (fixed point on the first pass), and no figure in the tables above changed. LibreOffice recalculation: 83,779 formulas, no errors in either case.

What changed:

- **Financial workbook.** The six Events rows E258–E263 read Approved. E263 names Britain and Germany only. The Endgame sheet gains three memos:
  - uranium mined to 1932 on the Atomic sheet, 5,804 t, beside CR-086's "6,000 to 6,200 t" with Great Bear, Urgeiriça and Radium Hill, which stays OPEN;
  - Japan's rescue of 1927: the Treasury's participation of $166m is repaid in five instalments of $33m, 1929 to 1933;
  - a reset of 20% makes the two instalments still due cost Japan about $17m more, counted at the old parity (Story). In Stress the participation is nil, so the memo is nil.
- **Provisioning model** (`population/provisioning.py`, `population/data/provisioning.toml`, report section 5):
  - Japan's home crop after `CR-085` `D1`: 52.6, 62.1 and 68.2 million koku in 1910, 1920 and 1932, which is 5%, 8% and 13% above our timeline's 50.1, 57.5 and 60.3. Against canon's need the gap is nil in 1910 and 1920 and 0.2 million koku (0.3%) in 1932. The storyline's 68.1 is the CR's own rounding.
  - Hokkaido's crop is entered as the CR's band (1.5–1.8, 2.5–3.0 and 3.5–4.0 million koku). How much of it is above our timeline's Hokkaido crop stays OPEN, because that series is not entered.
  - Caledonia's own people in 1932 (`CR-083` Part E): 0.84 million (0.77 to 0.91), about 0.14 million of them on the Island. This is our timeline's census of 1931 for British Columbia and the Yukon (0.70 million) raised by a fifth. The uplift is a story assumption with no source; the author approved it on 24 November 2026, 15:54 ("I approve your population assumption for Caledonia."). The Realm's count is unchanged.
  - Tests: 31 pass.
- **Energy workbook.** No input changed. One reading for `CR-084` `B3.4`: the Gulf crude the model brings home is 285, 266 and 247 million barrels in 1929–31 and 212 million in 1932, which is 80% of the three-year average. The trust's undertaking to the Gulf names "a stated share" of that average and no figure. A share above about four-fifths would already bind in 1932 as the model stands. **The author set the share at three-quarters on 24 November 2026, 15:56 ("I approve three-quarters.").** It is the lever `eg_gulf_floor` in the financial workbook, and the Endgame sheet checks it against the energy workbook's Gulf crude, read when the workbook is built: the floor is 199 million barrels, the liftings of 1932 stand 12 million above it, and the check reads OK. In Stress the energy workbook gives the same ratio, 80%. The series is the Gulf crude the trust can bring home after its Asian sales, used as a stand-in for its whole liftings.

Still not done, and why:

- **No figure in the approved CRs:** the fleet saving from Sembawang's halt; New Zealand's part of the £2,113,000; the Indies treasury bond; the Guaymas port bonds; China's reserve compact; Belgium's higher royalty; Seria's offtake, East Borneo's crude and Bintan's bauxite (the last delivers after 1935, outside the book). Each needs a size from the author or a source before it is entered.
- **The Atomic sheet's sources** (Great Bear, Urgeiriça, Radium Hill, monazite) are still a memo: entering them means reopening `cr049_atomic_programme.py` and `cr050_atomic_retiming.py`, and Great Bear's tonnage is OPEN.
- **The Kansai station** breaks no ground before May 1933, after the book's last year. **The Tokyo station's fuel** is already in the Atomic sheet's energy use.
- **Article II's mouths** (`CR-086` `D6`) and the Pampas volumes: the article feeds no one in the Realm and the schedule's volumes are not in canon.
- **Japan's own nitrogen plants and the Bank of Japan's ceiling** are Japan's books; neither workbook models Japan's home economy.
