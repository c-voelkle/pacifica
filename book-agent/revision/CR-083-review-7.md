# CR-083 review 7 (fresh context, 24 November 2026)

I reviewed `book-agent/revision/CR-083.md` as it stands (headed revision 13, with the additions of 08:58 and 09:02: the Governor John Buchan, the vote of 16 April on final terms, the sufficers' objection and Japan's clause moved to March). I read the draft in full, `AGENTS.md`, the storyline lines the draft cites (L91, L705, L708, L892, L927, L1020, L1091, L1093, L1100, L1137, L1139, L1142, L1234, L1265, L1385, L1554, L1593, L1597, L1602, L1604, L1614, L1617, L1651, L1687, L1693, L1695, L1738, L1746–1752, L1881, L1885), and the sibling drafts `CR-084` to `CR-087` only where they cross-refer to this one. I read no earlier review, nothing under `planning/` or `outputs/sessions/`, and no writer's notes. Historical statements below that I make myself are from memory and are marked so.

Scripts: `preflight.py --draft` exits 0 with 0 errors and 7 warnings, all of them that the new persons (Tate, Buchan, Pattullo, Tolmie, Bennett, Kelly, Paull) are not yet in `character_registry.json`. `cr_facts.py preview` reports 11 departures in 4 canon files (the passages the impact notes already name: L91, L708, L1137, L1142, L1554 and their summaries) and 23 findings in the draft itself, which are the draft quoting the old wording and the same unregistered IDs. Nothing unexpected.

## Verdict

**One more revision.** The late additions are sound in outline and mostly carried through: the calendar, `A7`, `A10`, `A10a`, the impact note for L1746 and `CR-085` line 133 all tell March and April the same way. Two things the additions created are not yet resolved: the Governor is silent at the one moment his office would have to speak (his ministers ask a foreign sovereign for a crown), and the Republic is now proclaimed about a week before the treaty it voted for is signed or consented to, which empties the safeguard `A7` promises. The rest is leftovers and labels.

## Blockers

**B1. The Governor and the request for a fourth crown.**
*Passage:* lines 152–155 ("Pattullo's mainland coalition opens talks with Thalassia, and its first request ... to enter Ka Lōkahi as a fourth crown under Julian"; "commissions him on two conditions ... that no request go to London without a vote of the people on a published text"; "*February.* He opens the session ... He refuses: the ministry has the confidence of the House").
*Problem:* Within a fortnight of being commissioned, the King's ministers at Victoria ask a foreign sovereign to take the dominion as his fourth crown, with no vote and no published text. Buchan's schedule does not mention it. His second condition covers only requests to London, so the ministry keeps its letter and breaks its plain purpose at once, and the draft does not say whether he knows, is told, or objects. This is the one act in the season that touches his reserve powers more nearly than anything the Island asks of him: ministers treating to transfer allegiance is not ordinary advice. It also weakens his answer of 13 May ("Lang broke the law and Pattullo has broken none"), which the reader will test against February. As written he is correct only because the hard case is left out.
*Fix:* Decide and state what he knows and does in February. Three workable versions: (a) the second condition reads "no request to London or to any other government"; Pattullo therefore sounds Thalassia informally through the Vancouver members and not as the ministry, and Buchan says so when he hears of it; (b) Pattullo tells him beforehand, Buchan warns in writing that he will not sign a request for union under another crown without a vote and reports to the Dominions Office, and the Senate's refusal spares both men the test; (c) he is not told, learns it from the Island's press, and it is the ground of the Island's dissolution petition, which then has a real argument and a real refusal. Any of the three gives him the scene he lacks (see S8). This is the author's choice (Q1).

**B2. Proclamation comes before the treaty, the guarantee and the refunding, and the safeguard of `A7` no longer works.**
*Passage:* line 178 ("About 12 July both chambers ... vote `CR-084`'s annuity bill ... The Republic of Caledonia is proclaimed about 18 July ... In the last ten days of July the Association Treaty is signed and the Realm's Senate consents to it by two-thirds ... The Concord's guarantee is signed and goes to the crowns and the delegations. Private San Francisco syndicates refund the dominion's bonds"); line 182 ("If Hayama or the Realm's Senate changes anything of substance, the text returns to the legislature; neither does"); `CR-084` line 249 ("the crowns ratify on 1 August").
*Problem:* Since revision 13 the commencement order and Proclamation follow the annuity bill (about 12 and 18 July), but the Association Treaty is signed and voted only after 20 July, the guarantee is ratified by the crowns on 1 August, and the refunding follows Proclamation. For one to two weeks the Republic is outside the Empire with the Governor gone on his cruiser, no signed treaty, no guarantee in force and bonds not yet refunded, depending on two-thirds of the Senate that refused it in February and on aliʻi seats that vote only after Article II. The promise that a changed text "returns to the legislature" cannot be kept after 18 July: there is no dominion to return to and the Severance Act has commenced. Nobody in the draft notices this, and the Island's best argument ("there was no time") gains a better one that is never made.
*Fix:* Either (a) reorder: the Senate's two-thirds on the Association Treaty and the delegations' vote on the guarantee come in the same days as the annuity bill, before the commencement order, on the initialled text, with signature by the Republic on Proclamation Day and ratification on 1 August; or (b) keep the order and say what it is: Pattullo proclaims on an initialled text, the safeguard ends on Proclamation Day, and someone says so aloud (Tolmie in the House, or Buchan at the hand-over, which would give his departure its content). Then amend the sentence at line 182 to match, and tell `CR-086` `E1` where the Association vote falls among the five.

## Should fix

**S1. Buchan's appointment: the year, whose advice, and the dominion's name.**
*Passage:* line 153 ("he leaves the Commons in 1930 and comes to Victoria as Governor on Tolmie's advice, a commoner and a Scot sent to a dominion that calls itself Caledonia").
*Problem:* (i) The rule that the King appoints a dominion's representative on the dominion ministers' advice was settled at the Imperial Conference of October–November 1930 and first used for Isaacs in Australia in January 1931 (*Hist.*, from memory). An appointment "in 1930 on Tolmie's advice" is possible only in the last weeks of that year. (ii) In 1930 the dominion is British Columbia; `A8` (line 188) has the name Caledonia taken in 1932. (iii) The biography as stated is correct (born Perth 26 August 1875; Unionist member for the Scottish Universities 1927–35; Governor General of Canada 1935 on Bennett's recommendation). The appointment is plausible: Mackenzie King wanted him for Ottawa in 1926 (*Hist.*, from memory, to verify), which is worth one clause as the reason Tolmie's government could get him.
*Fix:* "named at the end of 1930, the first Governor chosen on the dominion's own advice, and sworn at Victoria early in 1931"; replace "a dominion that calls itself Caledonia" with the old fur-trade name still in use for the northern interior, or drop the clause. Keep 1930/31 PROPOSED.

**S2. "Three times refused" does not match the schedule.**
*Passage:* line 161 ("asks the King's representative three times to stop what followed and is three times refused, correctly"); lines 155–158.
*Problem:* The schedule gives four approaches: the dissolution petition (Tolmie at the head of the Island members; refused), the request to reserve the bills ("the Island asks"; refused), the petition to the King (forwarded by Buchan and refused by London, not by him), and the call to dismiss after 13 May (made by "the Island's press", not by Tolmie). Only the first is Tolmie's by name and only two are Buchan's refusals of a formal request.
*Fix:* Say which three are Tolmie's, or write "the Island asks him three times and London once".

**S3. A leftover in `A7` contradicts the commencement order.**
*Passage:* line 185 ("so for a month Britain has released a dominion on the strength of an initialled accord"), two sentences after "London holds back the Act's commencement order until then, and the Republic is not proclaimed before it".
*Problem:* With the order held back, Britain has released nothing in that month. `CR-084` `B1` (line 148) puts it correctly: Britain carries a risk for a month and has the order as its remedy.
*Fix:* "so for a month Westminster has passed an Act on the strength of an initialled accord, and holds the commencement order as its security."

**S4. Why Vancouver splits, and what Pattullo says about the vote.**
*Passage:* line 175 ("Vancouver splits, on Japan's clause"); line 183 ("Vancouver and the Fraser canneries split nearly evenly (white labour divided over the 8-hour equal-wage article)"); line 239 ("Pattullo answers that it covers residence and not the vote"); line 193 (the floors abolish the disabilities "in voting" for every resident on Proclamation Day, and Japanese subjects who do not take citizenship "keep the floors").
*Problem:* Two reasons are given for the same split, one of them left from before the clause moved into the campaign. And Pattullo's answer is true of the clause and false of the published terms as a whole: the founding articles on the same ballot give every resident, Japanese residents included, the vote. As drafted it even appears that a Japanese subject who declines citizenship keeps the vote, which no state of 1932 would grant and Tokyo did not ask for.
*Fix:* Give Vancouver one account (the clause and the floors together are what labour fights; the equal-wage article divides it). State whether the franchise follows citizenship (then the floor for non-citizens is licences, professions, title and the courts) and let Pattullo's answer be either accurate or a known evasion that the Island's press catches.

**S5. The April accord "initialled in London", ten days after the vote.**
*Passage:* line 175 ("In the last days of April the preliminary accord of `CR-084` is initialled in London ... It has a Caledonian chapter, which Pattullo's government initials").
*Problem:* `CR-084` gives no place for the accord and lists it as unsettled against the travel times (its line 603). From Victoria to London in 1932 is about eleven or twelve days by rail and sea, the vote is on 16 April, the Yukon's returns come by wire, and Buchan must proclaim the result first; nobody who waits for the result reaches London in April. Kaʻiulani in London at the end of April and at Hayama on 12 June is feasible, but only just, and it is not stated.
*Fix:* The dominion's representative already in London (its High Commissioner or agent-general, unnamed) initials on cabled instructions after the proclamation of the result. Agree the place with `CR-084` in the same edit.

**S6. Leftovers of the old order: Hayama "agrees" what it now only confirms, and smaller ones.**
*Passage:* line 177 ("The Hayama Council ... agrees the Concord's guarantee of Caledonia"); line 235 ("agreed at the Hayama Council in mid-June"); line 355 ("agreed at Hayama in mid-June"); against line 176 and `CR-085` line 133 ("which the Council only confirms"). Also line 221 (heading "June–July 1932", though the terms are initialled in March); line 210 ("They do not sign in fourteen weeks", which counted March to the end of June; Proclamation is now about 18 July); line 262 ("Weeks before hosting the Ottawa Imperial Economic Conference", though the treaty is signed in late July, after the conference opens on 21 July); line 144 (heading of `A6`, "September 1931 – February 1932", over a schedule that runs to July).
*Fix:* "confirms" in the three places; adjust the others.

**S7. The Decisions section contradicts itself on what is approved.**
*Passage:* line 549 (R-12: seven groups of rev-12 additions APPROVED, "Body labels that still read PROPOSED on these items are to be read with this row"); line 548 (R-16: the March moves APPROVED); lines 607–612 ("PROPOSED by the drafter (for author sign-off)": item 2 "the sufficers objecting to the guarantee in March", item 5 "the rule that every treaty grant is subject to a compact, the Burrard compact ... Giannini losing on the wheat contract"); line 550 (R-13 cites `A6`; the passage is in `A10`); line 549 (the standstill of October 1931 is in `A10`, not `A6`).
*Problem:* The same items are APPROVED in the table and PROPOSED in the body and in the sign-off list. On integration someone will copy the wrong label into the storyline, which `AGENTS.md` forbids. Separately, R-12 rests on "I approve the other proposals as well" and the author's gloss of 08:22, whose three examples are all from `CR-084` and `CR-086`; none of R-12's seven groups is named in his words.
*Fix:* Correct the body labels and the sign-off list to match the table, fix the two section references, and put R-12's list to the author by name (Q3).

**S8. The Governor has no scene and no cost; the set pieces and impact notes do not know he exists.**
*Passage:* lines 309–313 (set pieces 1–5); lines 302–305 (impact notes for L1738, L1746–1754 and "Other files").
*Problem:* The author asked for the King's representative to have a part. In `A6` every act of his is a correct refusal that costs him nothing, and "He believes in the Empire and writes about it for a living" promises a conflict the schedule never stages. Set piece 1 has Tolmie resign to his cabinet with no Government House in it. The impact notes carry neither him nor the vote of 16 April on published terms, and `character_bible.md` is listed only for Camsell although six people are added.
*Fix:* One set piece for him, at the point where his discretion is real: the commissioning and its conditions, or February (B1), or the hand-over (B2 (b)). Add to the impact note for L1746–1754 the vote on published terms and the Governor's departure; add the bible entries for the new people to "Other files".

## Minor

**M1.** *Passage:* lines 3, 5, 14, 21. *Problem:* The file is "revision 13" with additions "after revision 13"; the status line still says it was revised after the review of revision 10; "Next: the third fresh-context review". *Fix:* call it revision 14 and update the three lines.

**M2.** *Passage:* line 161 ("Tolmie is the loser here by name"); line 262 ("Both truths sit on the page"). *Problem:* These answer a reviewer and are not story. *Fix:* cut the first clause and keep the facts; cut the second sentence.

**M3.** *Passage:* lines 150, 160 ("Premier Simon Fraser Tolmie"; "the premier in office"). *Problem:* A dominion since 1907 would style its head Prime Minister, as New Zealand and Newfoundland did (*Hist.*). "Governor" is right (Newfoundland's style). *Fix:* choose one style and state it once in the note at line 109.

**M4.** *Passage:* lines 155, 159 ("He reports to the Dominions Office"; "He transmits the legislature's request and consent"); line 630. *Problem:* After 1926 the Governor is no longer London's agent; he remains the channel only where the dominion kept that arrangement, as New Zealand and Newfoundland did. And the Statute of Westminster must name this dominion and section 4 must apply to it without the adoption section 10 required of Australia, New Zealand and Newfoundland. *Fix:* one clause each.

**M5.** *Passage:* lines 156, 174. *Problem:* The Governor's March lists the Referendum Act; the calendar's March does not. Nothing says by what act the Convention sits "since February" or whether he assented to it. Nothing says how the Yukon votes in April (winter trail, returns by wire). *Fix:* a clause each.

**M6.** *Passage:* lines 395–396 against 500–539. *Problem:* Tate and Buchan carry no "died"; the others do. Buchan's line 361 gives 1875–1940. *Fix:* add 1940 for Buchan or say why it is left open.

**M7.** *Passage:* line 134 ("the dockyard is already the dominion's own from then"). *Problem:* In 1905 it is a colony's; dominion status is 1907. *Fix:* "the colony's".

**M8.** *Passage:* line 310 (set piece 2, headed "February & July 1932", now contains March).

## What holds

- The March moves are carried through `A7`, `A10`, `A10a`, the calendar's March and May rows, set piece 2, the impact note for L1746 and `CR-085` `A4`; the fortnight between the Senate's refusal and the committee's objection is consistent everywhere.
- Buchan's biography is correct as stated, and his conduct on dissolution, reservation and the Lang comparison is orthodox for a Governor after 1926 and 1930. Lang's dismissal on 13 May is correctly dated and correctly distinguished.
- Dates and ages check: Victoria is ninety-three in February 1932 (L1738); Tate at sixty-six fits L1593 and the rule of sixty-eight; 16 April 1932 is a Saturday; Chamberlain, the gold exit, the Statute, the Ottawa conference and 15 May are right.
- The annuity figures (two near-end annuities, about $93m, 2/4/11) agree with `CR-084` `B1`; the five two-thirds votes agree with `CR-086` `E1`; the map agrees with `CR-087`.
- No protected intent is touched: Pattullo is the President, Julian is not; nothing bears on Noe Ward, the Hawaiian throne or extermination.
- The Senate's third refusal and why Julian obeys it, Tolmie's loss, the Sekani refusal, Paull across the table from the syndicates, and Giannini's real case against the wheat contract give the CR people who want things and do not all get them.
- Citations are in the house form and preflight passes; no exclamation marks.

## Questions for the author

- **Q1 (B1).** What does Buchan know of the request for a fourth crown, and what does he do: is it inside his second condition, is he warned by Pattullo, or does he learn it from the Island?
- **Q2 (B2).** Should the Realm's Senate vote the Association Treaty before the commencement order, or is the Republic proclaimed on an initialled text with the risk said aloud?
- **Q3 (S7).** Do you confirm R-12's seven groups by name? Your words of 07:27 and 08:22 name only examples from the other drafts.
- **Q4 (S4).** Does a Japanese subject who stays Japanese vote in Caledonia, or does the franchise follow citizenship?
- **Q5 (S1).** Is Buchan appointed at the end of 1930 as the first Governor chosen on the dominion's own advice?
