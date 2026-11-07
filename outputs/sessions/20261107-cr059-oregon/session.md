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
| Q1 | open choice | All 46 open decisions in CR-059, especially 1–8 (the optional levers) | CR-059 | open |

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

## Resume here

- CR-059 is a draft on `revision/cr059-oregon`, open for review as draft PR #69. Nothing is approved, and `master_storyline.md`, `change_requests.json` and the ledger are unchanged.
- Research passes 1 (author's audit), 2 (Official Records, vol. 50) and 3 (Congressional Globe, February 1859) are folded in. Still open from the Globe: the preamble roll call member by member; Wood's and Foster's terms. Part II of the Official Records from p. 801 (1864–65) is unread; the page index is in the note.
- Next: the author chooses among open decisions 1–8 and fixes what he wants of 9–46. Then run a second fresh review, approval and integration (storyline §§8, 10, 12; register entry; `cr_facts.py apply`; ledger).
- CR-B (Deseret, Nevada, Montana, Wyoming) must settle CT9 (Nevada) and CT11 (Deseret). CR-C is the Southwest, and CR-D the peace, Alaska and the Senate (see `plan-v2-four-crs.md`).
