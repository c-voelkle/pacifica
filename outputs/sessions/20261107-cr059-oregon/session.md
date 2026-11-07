---
session: 20261107-cr059-oregon
started: 2026-11-06
updated: 2026-11-07
mode: draft
status: paused-for-author
baseline:
  commit: 221ed91
independence: separate-agents
---

# How Oregon, Washington and Idaho come to Pacifica by 1867, and why Oregon is never a U.S. state

## Brief

- **Desired outcome:** a review of the author's draft timeline for 1848–1867 against canon; an improved plan split into four CRs; then the first of them, CR-059, drafted with all open decisions.
- **Authorization (author, 6–7 November 2026, in a claude.ai session):**
  - review the draft and compare it to canon;
  - write an improved timeline "so we can plan what the 4 CRs … are going to look like";
  - outline the first CR, with the 1859 change "downstream causally from California's changed status … and from its changed Oregon policy", made explicit on the page;
  - outline the 1866 vote, its question and its framing;
  - outline the Native parties;
  - list further levers, "underhanded or sneaky moves are ok too if they work";
  - put Idaho in CR-059 ("I would put it in cr-059");
  - "write up the first draft with all the open decisions."
  
  No decision in the draft is approved. Integration is out of scope.
- **Sources of history:** the author's draft (`source-author-draft-1848-1867.md`); the session's plan and outlines in this folder; web sources listed in CR-059; one fresh-context review.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-06 | compare | Author: "review this proposed timeline and compare it to canon" |
| 2026-11-06 | explore | Author: "write up an improved timeline … so we can plan the 4 CRs" |
| 2026-11-06 | explore | Author: "Let's outline the first cr" |
| 2026-11-07 | draft | Author: "write up the first draft with all the open decisions" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | The 1859 result must follow causally from California's independence and its Oregon policy, explicit on the page | author, 6 Nov | current |
| D2 | decision | Keep "the right argument tainted by Lane's Lecompton background" | author, 7 Nov | current |
| D3 | decision | The exclusion clause as the hinge: Pacifica need not make Oregon change it | author, 7 Nov | current (limited by the floor in the draft, X2–X7) |
| D4 | decision | Underhanded levers are acceptable "if they work"; "some of the optional ones" are good (which ones not stated) | author, 7 Nov | current |
| D5 | decision | Idaho's path belongs in CR-059 | author, 7 Nov | current |
| D6 | decision | John Sherman is swayed by his brother's letters and votes no (106 to 110) | author, 7 Nov | current |
| D7 | decision | Open decisions 1–8 settled as recommended in the claude.ai review of PR #69: P11 adopted with set-off (CT5 amended); P10 moved to 1861–62, open; no V7 push; V12 the declined invitation; Dry Creek included with Billy Chinook as interpreter; the lobby carried into CR-D; P6 never stated; V14 genuinely unauthorized | author, 7 Nov ("I approve the recommendations as proposed") | current |
| D8 | decision | CT14 adapted, with Elias expecting about 55% and his own floor and Native article narrowing it to about 51–49 | author, 7 Nov | current |
| D9 | decision | Wood and Foster keep their places; their motive is the race for settlers, not shipping | author, 7 Nov | current |
| D10 | decision | Research task 19 (the Idaho trade) is the highest research priority before integration | author, 7 Nov | current |
| Q1 | open choice | Open decisions 9–48 in CR-059 (facts to fix) | CR-059 | open |

## Handoffs

| ID | To | Task | Inputs | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Fresh reviewer | Consistency, history, literary and logic review | CR-059.md; master §§8, 10, 12, 13; CR-015 H4–I2; CR-033 A17–A23; CR-055; ledger; AGENTS.md | session notes and outlines | summary in CR-059's final section | done |

## Review judgments

| ID | Judgment | Finding | Location | Disposition |
| --- | --- | --- | --- | --- |
| F1 | consistency | The §8 arithmetic did not carry the bill | CR-059 storyline §8 | repaired |
| F2 | literary | The Mississippi motive did not survive the Senate vote of May 1858 | H3 | repaired |
| F3 | consistency | Deseret's status contradicted §10 | Part V, W10 | repaired; CT11 |
| F4 | consistency | Individuals held a veto; Elias had no price; a "no" vote was a dead end | V1 | repaired |
| F5 | consistency | Which body governed occupied Oregon was unclear | W2, W11 | repaired |
| F6 | consistency | The public domain conflicted with CR-033's Land Fund | N2, V9 | repaired; CT13 |
| F7 | literary | The restraint policy (P5) contradicted the levers | Part I | repaired ("Who decides, and when") |
| F8–F17 | mixed | The consider items | various | repaired or carried to open decisions 40–46 |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `python3 book-agent/revision/lint_canon.py --only book-agent/revision/CR-059.md` | pass |
| X2 | `python3 book-agent/revision/cr_facts.py preview book-agent/revision/CR-059.md` | pass; no canon passage states an old value |
| X3 | Event patterns tested against the draft's own prose | all five match |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-11-06 | Review of the author's draft; plan v2 | requested comparison complete |
| 2 | 2026-11-06 – 07 | Outlines 1–4 and the levers | usable proposals |
| 3 | 2026-11-07 | CR-059 draft, fresh review, repairs | blocked on author choices (Q1) |
| 4 | 2026-11-07 | Author's research audit folded in: Walla Walla mechanism, war-claims act and bonds, 1860 county returns (Marion as the swing), margin about 51–49, Nesmith's turn (V7a), Chinese counts, migration unquantified | blocked on author choices; next research pass: the 1859 Globe speeches and the 1862 Walla Walla correspondence |
| 5 | 2026-11-07 | Official Records vol. 50 read (Part I complete, Part II pp. 1–800; note `research-official-records-vol50.md`). Walla Walla mechanism rebuilt on the October 1861 order sending the regulars east, the January 1862 report and Halleck's refusal of coin; the convention moved to July 1862 | blocked on author choices; next research pass: the 1859 Globe speeches |
| 6 | 2026-11-07 | Congressional Globe, 10–12 February 1859, and the Stephens and Hughes pamphlets read (note `research-congressional-globe-1859.md`). Lamar, Nichols and Thayer spoke for admission, so the six changed votes are now Barksdale, McRae, Horton, Leiter, Wood and Foster, all silent historically (H3–H5, §8 prose); Hughes added as the historical voice of "admit to bind"; Thayer's "non-resident Government" proposed as a scene for 1866 | blocked on author choices (open decisions 35, 43 updated); the H changes need a fresh look |
| 7 | 2026-11-07 | Second fresh review (facts and hard blockers): five blockers repaired (Sherman's vote, Lamar wording, CT14 for the conditional article placed in the 1865 armistice convention, Buchanan's Sausalito demand labelled PROPOSED, the 1861 convention's meeting); factual corrections (68 per cent, coin, Article I §35, Mullan, Fort Benton timing, Colorado, state count, CT8's 1887 knock-on) | blocked on author choices |
| 8 | 2026-11-07 | Author's research: 42,862 confirmed as a contemporary estimate (OHQ 1926, 2019); $1,090,850 confirmed as bonds issued by 1866 (Treasury reports 1866, 1871), year of issue not established (E2, open decision 42) | blocked on author choices |
| 9 | 2026-11-07 | Author approved the recommendations of the PR #69 review: open decisions 1–8, CT5, CT14 and the Maine motive written into CR-059 and the §8 and §12 drafts; task 34 added (war claims by county); task 19 made the top research priority | blocked on research task 19 and decisions 9–48 |
| 10 | 2026-11-07 | Research task 19 (the Idaho trade) read online (note `research-idaho-trade.md`): river-company traffic and rates, Portland treasure, Idaho and Boise Basin output, supply routes. Folded into CR-059 Part V and I11 (the summer of 1866, PROPOSED) | blocked on decisions 9–48; archival part of task 19 open |
| 11 | 2026-11-07 | Author supplied Johansen (1941) and Throckmorton (1961). Research note section 6 (river-company finances by year, retail-price shares, the 1866 squeeze, the Montana push, gold against greenbacks, Corbett, Bolino's series) and section 7 (ten proposed set pieces). CR-059 Part V corrected (48% in 1861, not 1862; Columbia's lead 1862–64 only) and "coin cuts both ways" added (PROPOSED) | set pieces await the author |

## Resume here

- CR-059 is a draft on `revision/cr059-oregon`, open as draft PR #69. The author has chosen among open decisions 1–8 and decided CT5, CT14 and the Maine motive (7 November; CR-059 "Author's choices of 7 November 2026"). The CR is not approved, and `master_storyline.md`, `change_requests.json` and the ledger are unchanged.
- **Task 19, the Idaho trade, is done in part** (round 10; `research-idaho-trade.md`). Still open within it: Owyhee and northern output by year, tonnage by route and the river company's yearly earnings, for which the archives below are the remaining sources:
  - University of Oregon Special Collections, John C. Ainsworth papers (Coll 250), boxes 5–10: OSN business records.
  - Whitman College and Northwest Archives, OSN Wallula agency records (WCMss.532), 1861–62: the Wallula office's manifest book.
  - Oregon Historical Society Research Library: OSN corporate records and the Transportation Collection.
  - Dorothy O. Johansen, "The Oregon Steam Navigation Company: An Example of Capitalism on the Frontier", *Pacific Historical Review* (June 1941), 179–188; Johansen and Gates, *Empire of the Columbia* (1957); Randall V. Mills, *Stern-Wheelers up Columbia* (1947). The Oregon Encyclopedia, citing these, gives about 100,000 passengers and 60,000 tons upriver from Celilo in roughly two years after 1862, and a profit near 50 per cent in 1862.
  - Gold output: Waldemar Lindgren, "The Mining Districts of the Idaho Basin and the Boise Ridge", USGS 18th Annual Report, part 3 (1898), which estimates the Idaho City camp at about $44.7 million for 1863–96; Rossiter W. Raymond, *Statistics of Mines and Mining in the States and Territories West of the Rocky Mountains* (from 1869), and J. Ross Browne's report of 1868 for the 1860s by year; the Director of the Mint's annual reports for Idaho deposits; Bancroft, *History of Washington, Idaho and Montana* (1890).
- Also open: task 34 (war claims by county, for P11's weight in the south); decisions 9–48; a fresh review of the 7 November choices; then approval and integration (storyline §§8, 10, 12; register entry; `cr_facts.py apply`; ledger).
- CR-B (Deseret, Nevada, Montana, Wyoming) must settle CT9 (Nevada) and CT11 (Deseret). CR-C is the Southwest, and CR-D the peace, Alaska and the Senate, now also carrying the appropriation lobby (see `plan-v2-four-crs.md`).
