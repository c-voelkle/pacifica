---
session: 20261110-cr068-open-founder
started: 2026-11-10
updated: 2026-11-10
mode: draft
status: paused-for-author
baseline:
  commit: b3de13e
independence: separate-agent   # fresh-context reviewers on revisions 13 and 14; revision 15's fixes are self-reviewed
---

# CR-068 revision 11: the founder in the open

## Brief

- **Desired outcome:** Elias Thorne comes out of the contest with Lincoln as a victor who acts in the open, where revision 10 had him win by concealment.
- **Authorization:** author, 10 November 2026 (chat). The author had revision 10 reviewed from the standpoint of Pindar and judged: "The idea is for Elias to emerge from the contest as a victorious Pindaric hero. The CR has him emerge as a duplicitous villain." He then asked for the discussed changes to be added to the CR on `revision/cr059-oregon`: the blind vote; openness about the reasons; the answer to the legislature; the supporting changes, without the tempter at the high tide; the *Two Houses* paper; the offer of mediation by Elias first; the refuge; the gold, which may keep a creditor's hook; the river; and the honours.
- **Decided by the author in the same conversation:** Victoria's price is not the free-soil rule; the entry policy that keeps fugitives out is hers. Her prices are control of entry at Hawaiian ports (spring 1864) and Hawaii's assent to the peace (November 1864).
- **Out of scope:** integration; canon files, the register, the facts file and the ledger are unchanged. CR-059 to CR-065 are not edited; interfaces are listed in CR-068's canon tensions.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-10 | draft | Author: "please add the discussed Elias-rehabilitating changes … to the revised CR" |

## What was done

- CR-068 revised in place as revision 11 (Parts A, B, C, E, G and H, the storyline blocks, the character notes, the canon tensions, the open decisions, the research list, five samples, Appendix B), and a new Part I that states the rules (O1–O6) and lists the changes (R1–R18).
- Sources supplied by the author for *Two Houses* (G6b): Fellman, *Inside War*; Rose, *Rehearsal for Reconstruction*; Voegeli, *Free but Not Equal*; Foner, *Reconstruction*. Every page reference in G6b and Appendix B rows S36–S51 was checked against the supplied texts. Quotations of Lincoln in those rows are as the books print them and are still to be checked against Basler (research 44, 47).
- `lint_canon.py --only CR-068.md` clean; `cr_facts.py preview`: no fact changes declared.

- **Revision 12 (same day):** the author decided open decisions 1 to 50 in chat (16 and 31 deferred) and asked that no texts be drafted yet. Recorded in the list and applied where they change the text: Lincoln dies in 1871 and the meeting is in 1869; Douglass's judgment (V1) is left out; Pacifica's schools read *Two Houses* and its colleges read Lincoln; L3 loses its sentence on the Native nations and the freedmen; London is cut from G4; the loan passes smaller and shorter; an instrument is suggested for Victoria's entry condition (CT8).

- **Revision 13 (same day):** the author decided open decisions 51 to 73. Applied: the writ of 1871 stands with a ransom article (CT18 decided); Lincoln dies in 1872 (supersedes 1871); the false report is cut; the Confederate mission is not narrowed; no official honours at Lincoln's death; the tension with Victoria's entry policy is left to the reader. Suggestions given for 55, 58, 63, 65 and 71, and *Two Houses* and Lincoln's reply drafted (A12, A13).

- **Revision 14 (same day):** Status columns updated row by row from the author's decisions. A fresh-context reviewer (given revision 13, AGENTS.md, canon, the character bible, CR-049 and CR-059 to CR-066 and the four source texts; withheld: this record and the drafting conversation) found the draft not ready: leftovers, miscounts, and three mechanisms that undid the open founder. Fixed in revision 14 and listed under Review in the CR.

- **Revision 15 (same day):** a second fresh-context reviewer read revision 14 and again found it not ready. Its must-fix items are applied (the second reservation, the blind vote's standing in canon §8, the §13 block, *Two Houses* against CR-059's Oregon exclusion, leftovers and overstated status cells). What is open is now listed at the head of the CR's Open decisions as items 74 to 90.

## Resume here

- **After revision 15:** see CR-068, "Still open after revision 15" (items 74 to 90). The reviewers' strongest advice is item 90, a clean copy of the CR before adoption. Revision 15's own fixes are self-reviewed.

- **After revision 14:** the reviewer's must-fix items are applied. Revision 14's own fixes have not been reviewed by a fresh agent.
- **Waiting on the author:** (1) the reworded second reservation and the dissolution announced beforehand, which change things he had approved; (2) CT25, Victoria and "the policy" of 1871; (3) the items the review found and left for him (listed under Review); (4) the five suggestions and the two drafts A12 and A13; (5) decisions 16 and 31, deferred; (6) whether the 31 rows still marked PROPOSED are approved by default.

- **After revision 13:** all 73 open decisions have an answer except 16 and 31 (deferred). Waiting on the author: his view of the five suggestions (55, 58, 63, 65, 71), of the two drafts (A12, A13) and of the instruments suggested for Victoria's two conditions (CT8; decision 73). Still to do before adoption: update the decision tables' Status columns, run a fresh-context review, and draft storyline text for 1871–72.

- **After revision 12:** decisions 1 to 50 are decided and marked; 16 and 31 are deferred (31: the schoolbook triad is to be more patriotic and must not give the win to another country in its first sentence). Decisions 51 to 73 are open; the author will come to them later. No paper or sample is to be drafted yet. The decision tables' Status columns are not yet updated row by row.

- CR-068 revision 11 is a draft on `revision/cr059-oregon` (PR #69). Nothing is approved or integrated.
- **The author's next decision:** open decision 56 (CT18), the writ of 1871 left standing with a ransom article. It is the one change in revision 11 that the author discussed and did not expressly agree, and it is the largest change to canon (§13's PROPOSED override).
- Then: open decisions 59–73 (the detail of the agreed changes) and canon tensions CT16–CT24.
- **Not done:** a fresh-context review of revision 11, which AGENTS.md requires before adoption and which a revision of this size needs. Storyline text for 1871 and after is not drafted.
- Research open: items 38–54 of CR-068. The most consequential are 38 (how long the Union's election result took to reach Monterey, which sets the window for the blind vote), 50 (whether Elias can be in Texas early in 1863 and at Honolulu by May) and 49 (whether Port Royal, the Missouri war and the Illinois events stand in this timeline).
- The branch is one commit behind `main` (the CR-066 session record); no canon file is edited on it by this session.

## Revision 16 (11 November 2026): the clean copy

**What the author asked.** Whether canon says when the renewal is voted and who the eighteen Council members are, and noted that eighteen can tie. Then: write in the two-thirds vote with California's delegation five to four for the founder; answers to open items 74 to 90; a clean copy.

**What canon says (checked in `master_storyline.md`).** §8: "equal member delegations", no number and no names; the Council appoints a Protector by two-thirds; renewal belongs to the two member legislatures; the Assembly alone revokes. §12: renewals in 1862, 1863 and 1864; the dissolution's dates and procedure OPEN. Late May 1861 is only the working date of the first appointment. Nine members a side and "ten to eight" were the drafter's invention.

**What changed in CR-068.**
- The blind vote is a two-thirds confirming vote of the Council: twelve to six, California five to four, Hawaii seven to two. No amendment to Article XIV; the §8 block is gone (G8, B15, CT17, W1, A9, A11, the §12 block).
- Lincoln dies in November 1872; the Port Townsend convention sends a constitution and a memorial; K5 assumes a formal offer; the readers do not print Lincoln's reply; the four stories are given without the Chronicler's comment; CT25 adapted (the cabinet's controls).
- Suggestions awaiting the author: the test for "will treat" (G8), Bass Reeves as petitioner and the valuation board (G12), the British consul and Lord Lyons (B6).
- Structure: Part I folded into Part H (O1–O6, Victoria's prices); G12 moved into Part G; V1 and CT7 retired; statuses reduced to APPROVED, Suggested, Deferred, OPEN and MODEL; inline revision notes removed. The revision history, decisions 1 to 90 and the reviews moved to `book-agent/revision/CR-068-record.md`.

**How it was built.** Scripts in the session scratchpad (`b16/p1.py` to `p6.py`): exact-match edits that fail loudly, then a regex pass, then a residue check. CR-068.md fell from about 370 KB to about 300 KB.

**Checks.** `lint_canon.py --only` clean on both files; `cr_facts.py preview`: no fact changes declared. No fresh-context review of revision 16.

**Resume here.** The author owes: the drafts A12 and A13; CT2, CT3, CT9 and CT20; the five suggestions. Deferred: K8, W2/A10, and the four mechanism questions of the second review. Then a fresh-context review of the clean copy.

## Fresh-context review of revision 16 (11 November 2026)

The author approved the five suggestions (the inaugural-to-Monterey-to-Vance chain, Bass Reeves, the British consul and Lyons, the valuation board, the instruments) and asked for the review. Reviewer's folder: AGENTS.md, CR-068.md, master_storyline.md, character_bible.md, CR-049, CR-059 to CR-066; told not to argue Lincoln's side against the founder. Verdict: not yet ready, one editing pass short. Its report could not be saved by the reviewer; the findings and what was done are summarized in CR-068's Review section, and the points left for the author are open items 6 to 13 there.

**Resume here.** The author owes: A12 and A13; CT2, CT3, CT9, CT20; open items 6 to 13; a decision on length (the review's list of cuts is in Review).

## The author's answers to the review of revision 16 (11 November 2026)

Written into CR-068 (script `b16/r17.py`): the test for "will treat" is printed in the Council's resolution of 12 November 1864 and runs to 1 May; Richmond's recognition waits on no armistice (canon's treaty of spring 1865 kept as the formal act); Hawaii's delegation acts on Victoria's standing instructions; her price is named before California votes; W1 and B16 closes are an allowed exception; G12 is rebuilt on the founder's hospitality, with the border controls of 1871–72 as the cabinet's reaction, supported by Victoria (CT25 now amended, not adapted; the §13 block replaces two canon sentences); CT2 adapt, CT3, CT9, CT20 amend; CT20 recorded in CR-064. New open item: the war aims of 1861 and California's reasons, for a later CR. CR-065 is to be revised by the author (M1's inaugural; the direct exchange).

**Resume here.** The author owes A12 and A13 and a decision on length. Deferred: K8, W2/A10, the four mechanism questions. The rebuilt round of 1871 has had no fresh-context review.
