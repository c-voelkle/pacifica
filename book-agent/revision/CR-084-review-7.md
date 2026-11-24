# CR-084 review 7 (fresh context, 24 November 2026)

Reviewed: `book-agent/revision/CR-084.md`, revision 11, in full. Read beside it: `AGENTS.md`; the storyline lines the draft cites (among them L927, L1020, L1234, L1316, L1381, L1385, L1566, L1572, L1575, L1578, L1593, L1597, L1600, L1604, L1609, L1612, L1614, L1640, L1651, L1687, L1693, L1695, L1697, L1720, L1732, L1734, L1738, L1746–L1756, L1861, L1865, L1885); the ledger entries `C-1923-UK-FUNDING`, `C-1931-HOOVER-MORATORIUM`, `C-1932-ANZ-DEFENSE` and `C-1932-CONCORD-RENEWAL`; the registry for the existing IDs; and the sibling drafts `CR-083`, `CR-085`, `CR-086` and `CR-087` by search, for cross-references, dates and figures only. No earlier review, planning note or session file was read. Scripts: `preflight.py --draft` exits 0 with 0 errors and 13 warnings (nine registry entries that must land with the fact changes; four unchecked "line N" mentions inside the author's quoted sheet). `cr_facts.py preview` reports no passage in current canon that would still state an old value and canon lint clean; against the draft itself it reports the nine unregistered IDs, the draft's own Hong Kong pattern matching its own JSON, and one false hit of the draft's own event pattern (S12). History was checked from memory only, and is marked so where used.

## Verdict

**One more revision.** The bargain, the arithmetic of the seventeen annuities and the committee of six hold, and nothing touches the four protected intents. Two things stop it going to the author as it stands: Tizard is given a number that the same section and `CR-086` say no one outside the Works has, and the draft states the approval status of `B5` and of revision 10's additions three different ways. The should-fix items are mostly one-sentence repairs of sequence and of who knows what.

## Blockers

**B1. Tizard knows the sealed count.**
- *Passage:* line 192, "Britain is in the second rank on the day it has one device against fifteen".
- *Problem:* "Some fifteen devices" is the Works' own figure (`L1640`, MODEL) and is nowhere public. The same section says the April paper "gives no figure for what the Works has made" (line 188) and has Tizard say he "cannot say what Thalassia will have built" and that "this is the figure that matters" (line 191). `CR-086` `C2a` has the declaration of custody state "nothing of their number". Tizard's answer to Lindemann, the hinge of the scene, rests on knowledge he cannot have.
- *Fix:* have him argue from what London does know: one late device against a works that has run since before 1924, spent one device in public in 1927 and has not stopped; "against a number he cannot name and must assume is large". That is stronger for the scene than a figure.

**B2. The approval status of `B5` and of revision 10's additions is stated three ways.**
- *Passage:* line 14, "`A2a` and `B5` are the drafter's ... nothing in them is approved"; line 561 (`R-10`), APPROVED for the commencement-order remedy, the coup heard in the committee, Hankey's minute, Lindemann's breach, Churchill's two reasons, Simon's messenger and the cabinet of 8 July; line 562 (`R-11`), APPROVED; line 571 (item 2) and line 580 (item 11), which list the same things as PROPOSED and "in no quoted approval"; line 139 still ends "(PROPOSED)".
- *Problem:* a reader cannot tell what the author is being asked to approve. Beyond the contradiction, `R-10` reaches further than the words it quotes. The sentence the author answered at 07:27 and glossed at 08:22 names three examples, and only one is this CR's: Hawaii as Tonga's guarantor. Whether "the other proposals" covers six further items of `B1` and `B5` is an inference. `R-10` itself concedes the body disagrees with it ("are to be read with this row").
- *Fix:* keep APPROVED on Hawaii as Tonga's guarantor (named in his words), on the order "Republic proclaimed only after the bill" (08:22, "3. yes") and on `R-11`. Mark the rest of `R-10` PROPOSED until he confirms the list (question 1). Then make line 14, the body labels, and items 2 and 11 say the same thing.

## Should fix

**S1. The April accord has no place, no stated content and no public/secret division, and the three drafts tell it differently.**
- *Passage:* line 187, "In April 1932, with the preliminary accord, Kaʻiulani ... hands Simon the draft"; line 162, "a signed preliminary Anglo–Concord agreement (April 1932)"; line 165, "After Britain's preliminary agreement publishes the terms"; calendar, line 245.
- *Problem:* `CR-083` (calendar, April) has the accord initialled "in the last days of April ... in London by Britain and the Concord's Foreign minister, with the Realm's Treasury for the annuities", with a Caledonian chapter that Pattullo's government initials. `CR-086` (line 307) has the draft article "go to London with the preliminary accord". `CR-084` names no place, calls the accord "signed" once and "initialled" elsewhere, and its calendar lists four things the accord authorises and omits the Caledonian chapter, the annuity schedule, the carried suspension and the commencement-order remedy that `B1` attributes to it. It also never says which parts are published. Labuan votes on published terms and the Commons debates in May, while the first article and its tranche must stay secret until the cabinet decides at the end of May. The draft's own list of things not done admits the travel question. It is answerable: London in the last days of April, Thalassia about 14 May, sailing with Julian in the first days of June (`CR-085` `A3`, `A4`), Hayama, back about 25 June.
- *Fix:* one paragraph in `B1`: place and date as `CR-083` has them, who initials, the chapters, what is published (Labuan, Fanning, Tonga, the Caledonian chapter, the first two tranches) and what is handed over separately and secretly (the article and its tranche). Add Kaʻiulani's itinerary in one sentence. In the calendar add the Caledonian chapter to April and, in May, that London receives the legislature's request and consent through the Governor at Victoria (`CR-083` `A6`), on which the Severance bill of June rests. Use "initialled" throughout.

**S2. The second and third triggers are either one event or the hold on Westminster fails.**
- *Passage:* lines 144–145 (separate triggers: ratification of `C-1932-UK-RETRENCHMENT`; ratification of the Final Act); line 150, "Westminster acts three times"; line 200, "what holds it is that the signature's four are cancelled only with the Final Act, to which the treaty is annexed".
- *Problem:* `CR-086` `E` annexes the retrenchment treaty to the Final Act. If ratifying the Act ratifies its annexes, the two triggers fall together and Westminster acts twice, not three times. If they are separate, London can ratify the Act, take the four near annuities and leave the retrenchment treaty and its eleven annuities of 1974–85, which line 200 has just shown to be worth little. Line 200 names the problem and solves it by an assumption that `B1` does not make.
- *Fix:* say in `B1` that the Final Act cannot be ratified without its annexed instruments (or that the third tranche's trigger is ratification of both), and correct "three times".

**S3. The chambers vote "following signing" ten days before anything can be signed.**
- *Passage:* line 126, "The Realm Chambers' Debate (July 1932, following signing; PROPOSED)".
- *Problem:* `CR-083` dates the annuity bill to about 12 July, because the commencement order and the Proclamation of about 18 July wait on it. Line 139 has London's acceptance of the redrafted reverter reach Thalassia about 22 July, so the retrenchment treaty cannot be signed before then. The money bill therefore precedes signature; only the Senate's two-thirds votes can follow it, in the last ten days of July, after Article II (`CR-086` `D5`).
- *Fix:* split `A3` in time: the bill about 12 July, voted on initialled texts, each tranche on its trigger; the Senate's consent after signature in late July. Give the calendar's July row the two dates.

**S4. Britain's four requests win nothing that April had not already given, and the blind answer pays off nowhere.**
- *Passage:* lines 201–205; line 199, "Thalassia therefore does not know Britain's reserve price when it answers".
- *Problem:* request 1 is "Won: the Realm's pledge stands in the article itself", but the April paper already has the Realm pledge "in the same article" (line 188). Request 3 is "Half won" by the write-off of the suspended annuity on signature, which the April accord already carries (line 151) and which the committee already counts in May (line 194). Japan's countersignature is conceded in the text to cost nothing. So Britain loses all four in substance while two are labelled as gains. The secrecy of Simon's bag is built up as a device and then changes no answer. The requests are also numbered 1, 2, 4, 3.
- *Fix:* either make one win real (the April paper has the pledge as a separate declaration, and Britain gets it moved into the article; Hayama must then settle that text, which is possible since Simon's bag reaches Thalassia about 13 June and the cipher cable to Hayama exists), or relabel honestly: Britain asks four things and gets none, and Simon reports that. If the reserve price stays, let Thalassia concede one thing it would have withheld had it known. Renumber.

**S5. "He cannot cable it" does not follow, and the Ottawa clause misreads.**
- *Passage:* line 139, "He cannot cable it, so June's changes go to London ... by King's Messenger"; "its answer is at Thalassia about 22 July, before Baldwin, Chamberlain and Cunliffe-Lister sail for Ottawa".
- *Problem:* what Hayama decided is the Concord's own act and known to Thalassia. A cable that is read gives away nothing when it reports it, and neither does the one word "accept" in reply. What cannot be cabled is Simon's advice and London's instructions. As written the five-week loop, and MacDonald's "no time to do anything else", rest on a constraint that does not apply. Separately, the Ottawa conference opens on 21 July (*Hist.*, as `CR-083` has it), so the ministers sail about 13 July (from memory); 22 July is not before they sail. The cabinet of 8 July is.
- *Fix:* Simon cables the facts in clear and sends his assessment by bag; the cabinet can still decide on 8 July having had the facts since mid-June and his advice since 1 July, and its acceptance is then a choice made with time to refuse, which costs MacDonald more. Or keep the bag and give a reason that holds (the cabinet will not settle a reverter on a cabled summary). Attach "before they sail" to 8 July. Thomas also went to Ottawa (from memory).

**S6. Committee or cabinet: who decides, and who is told.**
- *Passage:* line 197, "The committee decides without waiting ... The Chiefs of Staff are not told, and J. H. Thomas at the Dominions Office is told only in June"; line 199, "In the last days of May the cabinet decides to sign."
- *Problem:* Thomas sits in the cabinet. If the cabinet decides in the last days of May he knows then. If only the six decide, the storyline's and `CR-086`'s "the British cabinet decides" needs the qualification. The Chiefs of Staff are left unexplained: a programme "fully committed" since 1928 has a service owner, and the First Lord is in the room; a works cannot be dismantled before a court's observer without them.
- *Fix:* the committee of six decides with authority delegated by the cabinet, and the cabinet is told the conclusion without the paper (in which case Thomas knows the fact in May and the terms in June); or the full cabinet decides and Thomas is dropped from the sentence. Say when and by whom the Chiefs of Staff are told, in one clause.

**S7. Hoare's line is not on the page.**
- *Passage:* line 196, "Hoare (`T-B5b`) says little"; line 5, "Hoare speaks once"; line 370, Case B, "he speaks once, as written"; Case A, "Chamberlain says that the offer will not improve".
- *Problem:* nothing is written. The tension's Case A implies the line is that the offer will not improve, and the body never gives it to anyone.
- *Fix:* write the one sentence (for instance that he has seen what Thalassia does with a file it holds, and the terms will not be better in a year), or change the tension to "present and silent".

**S8. "Six years of annuities" for the signature.**
- *Passage:* line 192, "an irreversible signature is the only kind Thalassia will pay six years of annuities for".
- *Problem:* the signature's tranche is four (lines 146, 194, 200). Six is the signature's four with Caledonia's two.
- *Fix:* "four years of annuities".

**S9. The words of 19:32 are still not quoted, and one use of them overstates.**
- *Passage:* line 367, "decided by the author on 23 November 2026 at 19:32"; line 191, "The author accepted that the clause tips its readers off (19:32)".
- *Problem:* `CR-086` quotes the words: "I agree with your canon changes except for the final one", the first of those changes being that the British device of 1933–1935 is overtaken. That is a decision and `T-B5a` can quote it. On the tip-off his words are a question ("wouldn't it be too late for the other powers to do anything with that information anyway?"), not an acceptance.
- *Fix:* quote the sentence under `## The author's request` and in `T-B5a`. Remove the working note from line 191, or say that he raised the question and that France is the draft's answer to it (`CR-086` `C4`).

**S10. "Westminster's ratification" is not what Britain does.**
- *Passage:* lines 144–145, 248, 251, 334–337.
- *Problem:* the Crown ratifies treaties on ministers' advice; Parliament passes Acts and, under the Ponsonby rule (restored in 1929, from memory), has treaties laid before it. The tranches hang legally on this trigger, so the word matters. Ceding Labuan, a Crown colony, needs an Act: the historical retrocession of the Dindings, the draft's own precedent, took the Dindings Agreement (Approval) Act of 1934 (from memory, to verify). Detaching Fanning and Washington from the colony is an Order in Council.
- *Fix:* define each trigger as the deposit of the King's ratification, which follows the laying of the treaty and, for Labuan, an approval Act in the autumn session. That gives the diehards a second vote to fight, which the draft can use.

**S11. Kaʻiulani negotiates everything and does nothing.**
- *Passage:* line 187, "Kaʻiulani ... hands Simon the draft ... He hands it over subject to the Council"; Part E.
- *Problem:* the author asked for the minister to be someone who has mattered. She carries every instrument in this CR and has no scene, no choice and no line; the draft's list of things not done says so. "He hands it over" is a leftover of the unnamed minister.
- *Fix:* give her the meeting with Simon in London in April as a set piece: the mediator of 1919 handing Britain a paper whose third clause she has been told only the stated reason for (`CR-086` `C2`). Correct the pronoun.

**S12. The event patterns will fail the lint on honest prose.**
- *Passage:* lines 443–480; preview: "labuan-harbour-lease: canon year is 1932, not 1900" on line 334.
- *Problem:* each pattern takes any year within 120 characters of the instrument's name, across line breaks. The draft's own ledger lines trip it ("Tonga 1900 release ... Labuan Harbour Lease"). After integration any sentence that sets the Batavia Compact beside 1935 or 1937, or the Tonga treaty beside 1900, will be reported as a departure from canon.
- *Fix:* anchor each pattern on a verb ("signed", "initialled", "ratified") between name and year, or shorten the window and exclude newlines.

## Minor

**M1.** Line 219, "the Japanese navy for a fortified pier". `CR-085` `A3` reads canon as leaving Japan no separate navy after 1927. Write "the Japanese naval party" (`L1597`).

**M2.** Line 119, "...when the fleet and not a treaty keeps a strait open; which would make the Realm the policeman of Malaya and the enemy of Nanjing at Hong Kong." The last clause has no antecedent; it belongs to "a base at Singapore". Recast as its own sentence.

**M3.** Line 128, "in a winter when home farms foreclose". The debate is in July. "After a winter".

**M4.** Line 142, one parenthesis says the split "is OPEN" and that it "was decided". Line 150 gives "2, 4 and 11" while the tranches are numbered Caledonia, retrenchment, signature; `CR-083` writes "2, 11 and 4". Use one order.

**M5.** Ledger lists. Line 334 still says "cancelling 15–20" annuities; it is 17, of which this treaty's trigger carries eleven. `C-1932-LABUAN-LEASE` (line 335) omits `UK`, though Britain's consent is written into it and Brunei's foreign relations are Britain's. `SHELL` is listed as a party to two state treaties; "named in" would be truer.

**M6.** `T-P1` and line 268 cite `L1316` only. `L1381` already says "Pacifica and Japan retain Germany's Pacific islands"; cite it, and say whether "and Japan" stands beside "Pacifica's".

**M7.** Working notes left in the body: line 110 ("the drafter's fuller list ..."), line 196 ("so his lines here are a proposal to bring him on"), line 236 ("the meridian has no margin and may be moved to 156° W"). Move them to `## Decisions`; choose 155° or 156° W.

**M8.** Line 212, "Dutch motives (*Hist.*)". The slump and the Chadbourne scheme are history; "what brings The Hague to sign" and the unspoken second reason are the draft's. Split the label.

**M9.** Line 148, "Britain carries that risk for a month", and `CR-083`, "for a month Britain has released a dominion". With the commencement order held back Britain has released nothing; it has passed an Act. The interval is late June to about 12 July, under three weeks.

**M10.** The open item "Tizard's line number (`L1572` or `L1575`)" can be closed: "Tizard reopens his file" is on `L1575`, as cited.

**M11.** Line 244, "Kaʻiulani,)." Stray comma.

**M12.** Line 167, the No-branch: "the cancelled annuity count would have been reduced accordingly". By how many, and from which tranche? If from the eleven far-end annuities, the penalty is close to nothing, which the committee itself says of them.

**M13.** Line 165: the accord is initialled in the last days of April and Labuan votes in May on a new two-year-domicile roll under a three-party commission. Say "late May", or give the roll a source (the Straits Settlements' registers).

## What holds

- The annuity arithmetic: 8 paid, 1 suspended, 53 left (1932–33 to 1984–85); 2 + 4 + 11 = 17; nothing due until 15 December 1938; the last annuity 1973–74; 36 kept. The present values (about $93m, $169m, $114m on a book of about $1.2bn, about 31%) are mutually consistent at a rate near 3.5%, and agree with `CR-083`.
- The cabinet of 5 November 1931 and each minister's office are right (from memory): MacDonald, Baldwin (Lord President), Chamberlain (Exchequer), Simon (Foreign), Cunliffe-Lister (Colonies), Thomas (Dominions), Eyres-Monsell (Admiralty), Hoare (India); Hankey as secretary; Churchill out of office, at the Treasury to June 1929, Lindemann's friend since 1921.
- Agreement with the siblings on: Hayama on 12–15 June; the bill about 12 July and the Proclamation after the commencement order; the Senate's three instruments in one two-thirds vote (`CR-086` `E1`); the Netherlands signing only the straits schedule; the dominions signing for themselves; Kaʻiulani's appointment; Tate's birth about 1866; the oil lever spent in `A2a` and counted in `CR-085`.
- The committee of six as drama: Tizard's missing figure, Lindemann right about the third clause and unanswered, Eyres-Monsell's default proposal and Chamberlain's answer from sterling, the coup read both ways. The losers have names throughout (Eyres-Monsell twice, Lindemann, the oil trust, the aluminium champion, Brooke's neighbour Brunei, Canberra, the Labuan merchants).
- The tensions decided by the author are carried out as decided: no base rights at Singapore, Labuan retroceded on a vote with a No-branch, leased ports without flag or guard, no southern renunciation, the 10° S line honest about Rabaul.
- Weapon design stays off the page; no exclamation marks; no protected intent is touched; Victoria is silent and keeps her one bargain.

## Questions for the author

1. Does "I approve the other proposals as well" (07:27) cover, in this CR, the commencement-order remedy, the coup heard in the committee, Hankey's minute, Lindemann's breach and its cost, Churchill's two reasons, and Simon's messenger with the cabinet of 8 July? Only Hawaii as Tonga's guarantor is named in your words (B2).
2. Should Britain win anything real in June, or lose all four requests and sign anyway (S4)?
3. `T-B5b`: does Hoare speak one line, or sit silent? `T-B5c`: is the dominions' cable at Fanning covered by the rule that a partner is never read?
4. Giannini loses in three CRs in one July. Is that wanted?
5. Your words of 00:12 give Caledonia's annuities as "1933–34" and the signature's as "1935–38"; the draft reads these as the annuity years ending in those calendar years (1932–33 to 1937–38), so that the instalment of 15 December 1932 is among those cancelled. Is that the reading you meant?
