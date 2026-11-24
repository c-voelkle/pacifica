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

## The sizes entered on 24 November 2026, 16:26

**Authorization:** the author, 24 November 2026, 16:26 ("Sounds perfect. Please go ahead and enter it."), to a table of sizes proposed by another assistant and corrected by the drafter against sources. Every size is MODEL. The chain was rebuilt: Story no failed checks, Stress 51; the energy outputs settled on the second pass (largest move on the first, 0.1%). LibreOffice: 83,883 formulas, no errors in either case.

| Item | Story | Stress | Where | Treasury cash |
| --- | --- | --- | --- | --- |
| Great Bear's ore, 1913–32 | 295 t U (5, 10, 15 and 25 t a year from 1913, 1917, 1922 and 1927) at $8.50 a kg | 201 t at $11 | Atomic, through the Endgame sheet's columns D to I | yes |
| Canada's royalty on it | $0.05m a year, $0.10m from 1927 (1913 $) | the same | Atomic, contracts | yes |
| Urgeiriça's dumps and Radium Hill | 15 t in 1926, 10 t in 1927, at $10 a kg | at $12 | Atomic | yes |
| Belgium's revision of 1929 | $5 a kg at Shinkolobwe with the old $0.6m as a floor: $0.65m a year more in 1929–31, nothing more in 1932; $0.10m a year of free radium salt | $6 a kg; $0.15m | Atomic, contracts and radium trade | yes |
| The Indies bond, San Francisco tranche | $20m | $30m | Events E264, memo | no |
| The Guaymas port bonds | $5m | $8m | Events E265, memo | no |
| China's reserve compact | $25m | $40m | Endgame memo | no |
| Singapore: naval works not built | £5.0m ($17.5m at $3.50), of which £2.3m is work in hand; £0.4m a year of upkeep | £5.0m; £0.5m | Endgame memo | no: Britain's |
| New Zealand | £0.60m paid and credited, £0.40m not called | the same | Endgame memo | no: Britain's and New Zealand's |
| Seria's offtake, 1932 | 0.5 million barrels | 0.3 | Endgame memo; energy workbook's Events list | no |

Results (Story):

- **Uranium mined to 1932: 6,124 t** (was 5,804). **In reserve at the end of 1932: 4,939 t** (was 4,619), four fifths of the whole. The storyline now says about 6,100 and about 4,900.
- **The atomic programme's net cost to the Treasury, 1846–1932: $1,010m** in current dollars (was $1,005m). Great Bear costs $3.8m in 1913 dollars over twenty years and Belgium's revision $1.95m more in royalty over 1929–31.
- Monetary gold in 1932 is unchanged at $1,539m.
- **The Gulf floor still holds** with Seria's offtake counted against it: 11.6 million barrels of room in 1932.

Three things differ from the proposal as it arrived:

- **China's reserve compact is not a new balance.** The Money sheet already counts $100m in 1932 for "Korea, the Gulf, China's reserve banks". The $25m is the part of that which moves under China's own compact, so it asks no new gold of the Reserve Bank.
- **Seria is half the proposed size.** The proposal took Seria's exports as about 645,000 t in 1934 and 813,500 t in 1935; the Brunei figures printed in a directory of the time are 371,591 t and 441,744 t, and output began only in the first quarter of 1932.
- **The Malay States had paid £1.2m by December 1929, not £1.6m** (Hansard, 18 December 1929); the £2,113,000 that `CR-084` quotes is the total expected by the end of that financial year. New Zealand's instalment was cut from £125,000 to £100,000 in 1931, which gives about £0.60m paid by March 1932.

Sources fetched on 24 November 2026:
- Hansard, 13 November 1929 (the £2,113,000): https://api.parliament.uk/historic-hansard/commons/1929/nov/13/singapore-base
- Hansard, 18 December 1929 (the three contributions to date): https://api.parliament.uk/historic-hansard/commons/1929/dec/18/singapore-base
- Hansard, 15 February 1933 (about £3,438,000 spent without the floating dock; £2,122,000 contributed): https://api.parliament.uk/historic-hansard/written-answers/1933/feb/15/singapore-base
- Hansard, 26 July 1939 (expenditure and contributions by year to 1929): https://api.parliament.uk/historic-hansard/written-answers/1939/jul/26/singapore-base
- New Zealand Herald, 22 September 1927 (£1,000,000 in eight instalments of £125,000): https://paperspast.natlib.govt.nz/newspapers/NZH19270922.2.132
- Papers Past, 20 May 1932 (the instalment reduced to £100,000): https://paperspast.natlib.govt.nz/newspapers/WC19320520.2.49
- Brunei in the Directory and Chronicle (production from the first quarter of 1932; exports of 1934 and 1935): https://hkintexts.histsyn.com/page/1126605 and https://hkintexts.histsyn.com/page/1134012

Not verified: Eldorado's output in the 1930s; the Kemmerer commission's cover rule. The Guaymas and China sizes are analogies to figures inside the workbook, with no outside source.

### Three figures checked on 24 November 2026 (author, 18:54)

- **The Singapore base's whole estimate.** The scheme in the Navy Estimates is £7,750,000 (First Lord, 23 November 1927; Civil Lord, 15 March 1932, Vote 10 item 64). With the Army's and the Air Ministry's works the whole was put at £11.6m in December 1929: £9.0m on Navy Votes, £2.0m on Army funds and £0.6m on Air funds. The work actually in hand under the Imperial Conference's decision of 1930 is smaller: an estimate of £5,145,000 for the contract and contingent services (£4,036,000 to the contractor and £1,043,516 of departmental works), with the floating dock, £971,000, beside it; the dockyard's workshops, the generating station and the completion of the graving dock were deferred to a review in 1935. About £3,438,000 was spent by February 1933 without the dock, and the vote for 1932 was £690,000, so about £2.8m was spent by the spring of 1932.
  - **The £5.0m stands**, as £7.75m less £2.8m, on the reading that the £7.75m does not include the floating dock. The Hansard pages do not say so in terms; if it does include the dock the figure is £4.0m.
  - **Only £2.3m of it is work in hand** (£5.145m less £2.8m). The other £2.7m was already deferred in 1930, so in 1932 it is a saving against the plan and not against the estimates. The Endgame sheet shows the split. The Stress lever of £6.0m had no support and is now £5.0m.
- **The Indies' dollar issues.** Three in New York in 1922, all at 6%: $40m of 25-year bonds in January, $40m of 40-year sinking-fund bonds in March, and $20m more of the 40-year bonds in April. That is $100m in 1922. The loan of June 1923 was not a dollar issue: £6m at 5% underwritten in London beside a loan raised in Holland (Evening Post, 16 June 1923). The proposal's total of $150m in dollars is therefore not right; the dollar issues of 1922–23 come to $100m. The $20m tranche is a fifth of the 1922 borrowing.
- **The pound.** Dated quotations in New York for 1932: $3.50 in mid-January, $3.82 at the end of March, $3.30 in late October, $3.34 on 22 December. The Bank of England's history of the Exchange Equalisation Account gives $3.61 when the Account began in the summer and a low of $3.14½ on 29 November. $3.50 is a fair figure for the summer of the Act. The year's average of about $3.51 is recalled from the Federal Reserve's *Banking and Monetary Statistics*; the table itself was not reached.

Sources fetched on 24 November 2026:
- Hansard, 23 November 1927: https://api.parliament.uk/historic-hansard/commons/1927/nov/23/singapore-base
- Hansard, 17 December 1929: https://api.parliament.uk/historic-hansard/written_answers/1929/dec/17/singapore-naval-base
- Hansard, 9 March 1932: https://api.parliament.uk/historic-hansard/written-answers/1932/mar/09/singapore-base
- Hansard, 15 March 1932 (Navy Estimates): https://api.parliament.uk/historic-hansard/commons/1932/mar/15/navy-estimates-1932
- Hansard, 22 February 1933: https://api.parliament.uk/historic-hansard/commons/1933/feb/22/singapore-base
- New Zealand Herald, 7 January 1922: https://paperspast.natlib.govt.nz/newspapers/NZH19220107.2.42
- Star (Christchurch), 16 March 1922: https://paperspast.natlib.govt.nz/newspapers/TS19220316.2.52
- Evening Public Ledger (Philadelphia), 21 April 1922: https://panewsarchive.psu.edu/lccn/sn83045211/1922-04-21/ed-1/seq-25.pdf
- Evening Post, 16 June 1923 (not readable): https://paperspast.natlib.govt.nz/newspapers/EP19230616.2.59
- Southland Times, 18 January 1932: https://paperspast.natlib.govt.nz/newspapers/ST19320118.2.37
- Bay of Plenty Times, 30 March 1932: https://paperspast.natlib.govt.nz/newspapers/BOPT19320330.2.24
- Dominion, 27 October 1932: https://paperspast.natlib.govt.nz/newspapers/DOM19321027.2.72
- Bank of England, the Exchange Equalisation Account: https://www.bankofengland.co.uk/-/media/boe/files/archive/ww/boe-1939-1945-partii-appendix.pdf

Still not done, and why:

- **Entered since** (see the section above): the Singapore saving, New Zealand, the Indies bond, the Guaymas bonds, China's reserve compact, Belgium's royalty, Seria's offtake, and Great Bear, Urgeiriça and Radium Hill on the Atomic sheet.
- **After the book's last year:** East Borneo's crude and Bintan's bauxite deliver after 1935. **The monazite stock** has no tonnage in canon.
- **Seria's offtake is a memo.** It is sold in Asia and does not enter the home fuel balance; half a million barrels is a thousandth of the year's refinery runs.
- **The Kansai station** breaks no ground before May 1933, after the book's last year. **The Tokyo station's fuel** is already in the Atomic sheet's energy use.
- **Article II's mouths** (`CR-086` `D6`) and the Pampas volumes: the article feeds no one in the Realm and the schedule's volumes are not in canon.
- **Japan's own nitrogen plants and the Bank of Japan's ceiling** are Japan's books; neither workbook models Japan's home economy.
