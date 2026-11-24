# CR-084 review 8 (fresh context, final, 24 November 2026)

I read `CR-084.md` (revision 14) in full, `AGENTS.md`, the shared calendar `CR-083-086-calendar.md`, the storyline lines the draft cites (among them L1020, L1232, L1316, L1334, L1381, L1385, L1551, L1560, L1572 to L1578, L1593 to L1614, L1640, L1651, L1687 to L1695, L1720 to L1756, L1861 to L1885), the ledger entries for `C-1923-UK-FUNDING`, `C-1931-HOOVER-MORATORIUM`, `C-1932-GULF-OIL` and `C-1932-ANZ-DEFENSE`, the registry for the IDs the draft names, and the sibling drafts `CR-083.md`, `CR-085.md` and `CR-086.md` only where they cross-refer (merge order, calendar rows, tranche figures, the 19:32 words, Simon's arrival, the Senate's five votes, the Netherlands' signature). I read no earlier review, proposal, prose check or planning note. `preflight.py --draft` exits with 0 errors and 13 warnings: nine for the new persons not yet in the registry, four for "line NNN" inside the author's quoted words. `cr_facts.py preview` finds no passage in current canon that would still state an old value; its 20 findings are the nine unregistered IDs and the draft's own Hong Kong pattern matching itself. I did not check any historical claim on the web; where I say a date is right or wrong it is from my own memory and is marked so.

## Verdict

**Ready once the items under Blockers are fixed.** There is one blocker, and it is a single sentence: the April paper is said both to carry the pledge as a separate declaration and to carry it inside the article, which undoes the one thing Britain wins in June. The arithmetic of the annuities, the three tranches and their triggers, the travel times and the calendar all hold. The should-fix items are mostly labels that disagree with each other and two points of British practice; S1 to S4 ought to be settled before the author signs, the rest can be done at integration.

## Blockers

**B1. The April paper states the pledge two ways.**
- *Passage:* line 210, "In that draft the Realm's pledge is a separate declaration beside the article"; line 211, "The Realm pledges in the same article never to use the weapon against a signatory that keeps it"; line 226, "It is the one thing Britain gets in June that it did not have in April".
- *Problem:* line 211 describes the paper of April, and puts the pledge inside the article. Lines 210 and 226, the calendar (decision B, approved) and set piece 0 ("The pledge lies beside the article on a separate sheet") all need it outside. As written Britain wins in June what the paper already gave it in April. Simon's case in the committee in May (line 218: "a sentence saying that the weapon will not be used against it, and a court to which a breach can be taken") leans the same wrong way: a court for a breach is what the move into the article buys.
- *Fix:* line 211: "Beside the article, in a declaration of its own, the Realm pledges never to use the weapon against a signatory that keeps it." Line 218: let Simon say that Britain gains the sentence, and that he will ask for it to stand in the article, where the court can reach it. That also gives the first request its motive.

## Should fix

**S1. The Chiefs of Staff are told after everyone else has read it in the newspapers.**
- *Passage:* line 220, "The Chiefs of Staff in London are told in the last week of July … Caledonia's proclamation of 18 July they have read in the newspapers."
- *Problem:* the author's condition at 11:21 was that what they are told must not be something London already knows. By the draft's own calendar the Senate at Thalassia votes the pledge and the text of Article I about 9 to 11 July, and about 12 July both chambers of the Realm pass a bill that cancels four British annuities "for the signature under the first article". The dominion governments have had the terms from Thomas since June (same line). Unless those votes are closed and the bill is worded blind, the Chiefs learn about 13 July, from the press, that Britain is being paid to sign. The draft does not say whether the votes are public, and `CR-086` does not either.
- *Fix:* one of two. Say that the Senate's votes of 9 to 11 July on Article I are taken in closed sitting and that the bill names the third tranche only as "on the deposit of the ratification of the act made at the conference's close", so that 1 August is the first publication. Or keep the votes public and move Eyres-Monsell's telling to the week before them (about 4 to 8 July), still tied to the Act and not to Caledonia. The author should choose; see the questions.

**S2. Two rows of `## Decisions` approve opposite things, and three items carry two labels.**
- *Passage:* line 591 (R-13), "the Chiefs of Staff are told when the plant is dismantled … APPROVED"; line 592 (R-14), "told in the last week of July … APPROVED". Lines 397 to 400 (`T-B5b`), "Recommended: Case B. PROPOSED; not decided", against line 219 and R-13, where Hoare's one line is approved at 10:45; line 305 still reads "(PROPOSED)". Lines 401 to 404 (`T-B5c`), "Recommended: Case A. PROPOSED; not decided", against the author's 10:45 words "Fanning cipher-room reading stays `OPEN`/unstated", R-13 and the OPEN list. Line 608 lists "Churchill's one moment with Lindemann" as PROPOSED while R-10 approves Lindemann's breach and Churchill's two reasons. Line 174 heads the instalments "(PROPOSED)" while R-13 approves the reading that rests on them.
- *Problem:* on approval the decision table and the tensions are copied to the register. R-13 and R-14 cannot both stand. `T-B5c` Case A would write a ban on interception into the trust's charter, which is the opposite of leaving it unstated.
- *Fix:* strike the Chiefs of Staff clause from R-13 and add "superseded by R-14". Mark `T-B5b` "Decided: Case B (author, 24 November 2026, 10:45)" and change line 305. Mark `T-B5c` "Left OPEN by the author (10:45); neither case adopted" and drop the recommendation. In line 608 keep only what R-10 does not cover. In line 174 mark the dates PROPOSED and the reading approved.

**S3. Approvals claimed without the words, or beyond them.**
- *Passage:* line 214, "The author accepted that the clause tips its readers off (19:32)"; lines 208 and 396, "decided by the author on 23 November 2026 at 19:32"; line 604, "the four requests and their answers are approved, R-12 and R-13".
- *Problem:* no words of 19:32 are quoted under `## The author's request` in this file (the draft's own closing list admits it). `CR-086` quotes them: "even if the article's specifications tipped them off, wouldn't it be too late …?" and "I agree with your canon changes except for the final one." The second supports `T-B5a`. The first is a question; it supports the clause, not a statement that he "accepted" the tip-off. For line 604: the calendar's B gives only that Britain wins one request of four, the pledge inside the article. What the other three are (the plant kept as a laboratory, Germany and France, cancellation on signature) and their answers are in no quoted approval.
- *Fix:* quote the 19:32 words here with `CR-086`'s list of the six changes. Reword line 214 without the claim (see M1). In line 604 say that the first request and the count of four are approved and that requests 2 to 4 and their answers are PROPOSED.

**S4. Who accepts on 8 July.**
- *Passage:* line 161, "The committee takes it on 8 July, reports its conclusion to the cabinet and cables the answer the same day … It accepts the redrafted reverter and the Navy seat"; line 274 and the calendar, "The British cabinet accepts".
- *Problem:* the committee of six has the cabinet's authority for the article, whose paper the cabinet has not seen. The redrafted reverter, the lost date of 1937 and the Navy ministry are terms of the retrenchment treaty, which is open cabinet business and was debated in the Commons in May. The body gives them to the committee; the calendar and R-10 ("the cabinet of 8 July") give the day to the cabinet. Simon, one of the six, is at Thalassia.
- *Fix:* "On 8 July the cabinet accepts the redrafted reverter and the Navy seat; the committee, five of the six with Simon away, accepts the article as Hayama left it and tells the cabinet so. One cable carries both answers."

**S5. The Act of Parliament and the date of transfer cover Labuan only.**
- *Passage:* line 168, "an Act approves the cession of Labuan"; line 173; line 278; line 275, "Fanning/Washington buyout and labour compact executed"; line 365, "(June–July 1932 …)".
- *Problem:* Fanning and Washington are annexed territory inside a Crown colony since 1916 by the draft's own account, and they pass to a trust of foreign crowns. By the practice the draft invokes for Labuan they need Parliament's approval as much as Labuan does. The draft also gives the Labuan lease and Tonga's treaty a day of effect (the deposit in the autumn) and gives the atolls none, while Ka Lōkahi buys the estate and offers the workers its charter in June and July, on soil still British.
- *Fix:* "an Act approves the cession of Labuan and of Fanning and Washington". State that the detachment takes effect on the deposit of the King's ratification and that the buyout and the labour compact are executed in July to take effect on that day.

**S6. The merge order leaves more than `B5` hanging.**
- *Passage:* line 14, "this CR merges together with `CR-083` and before `CR-085` and `CR-086` … Until those merge, the storyline carries `B5` as a decision taken in London in late May 1932".
- *Problem:* the interim wording covers `B5` only. Integrated before `CR-085` and `CR-086`, this text also puts into the storyline: Hayama striking the term and the reverter redrafted to "dissolved" (line 161) beside L1734's "renewed to 1937 … Japan may refuse in 1937"; the Navy ministry Japanese by treaty law (lines 161, 252, 261); a Final Act of 1 August as the trigger of the third tranche and the day the suspended annuity is written off; four straits scheduled to an Article II that does not exist; the Emperor's "second advice".
- *Fix:* integrate the four in one pass, which is what the shared calendar already assumes; or extend line 14 to list each of these with its interim wording.

**S7. The Sultan's signature and his voyage.**
- *Passage:* line 187, "signs the Labuan Harbour Lease … He postpones his voyage to England of July 1932 until after the signing"; line 276, "Sultan Ahmad Tajuddin sails for England (*Hist.* delayed slightly from July)".
- *Problem:* the lease is signed in late July (calendar, ledger line 364) and the draft does not say where. If at Thalassia, Brunei to Oʻahu is some three weeks each way and he cannot sail for England in July; if at Brunei Town, someone holding the Concord's full powers must be there, as at Victoria on 18 July.
- *Fix:* say that the lease is signed at Brunei Town by the Sultan and a deputy holding the common Foreign minister's full powers, on the model of Caledonia's guarantee, and that he sails in August.

## Minor

**M1. Notes about the drafting in sections A to E.** Line 130, "the script has no routes or straits, so a routing table is needed"; line 208, "This section owns … Because this CR merges before `CR-086`, the tension is listed here"; line 214, "The author accepted … (19:32); Tizard is the reader"; line 219, "Canon's sentence on Hoare is itself PROPOSED, and the character bible keeps him off the page until now"; line 236, "(figures when the workbook has them)"; line 250, "This section lists only"; line 252, "neither draft gives Labuan a special arrangement"; line 261, "stated here only as what Canberra sees"; lines 161 and 222, "to be sourced", "to verify". *Fix:* move each to `## Decisions` or `## Sources`. The dated approval stamps in the body are labels and can stay, but none belongs in the storyline.

**M2. Tracker IDs used as things in the world.** Line 162, "the Commons debates `OPEN-019-05`"; line 270, "confidential `OPEN-019-05` talks open"; heading of B. *Fix:* "the Pacific retrenchment" or "the accord of April".

**M3. Who is in the talks of November 1931, and where.** Line 159 names Simon, Chamberlain and Cunliffe-Lister; line 270 adds Eyres-Monsell, Hoare and Kaʻiulani. Neither says where they are held, and Kaʻiulani is in London in late April having "crossed two oceans and a continent". *Fix:* one list, and one clause saying the talks run through the Concord's envoy in London until she comes over in the spring.

**M4. The order of the tranches.** The author asked at 10:45 for one order. Lines 173 and 330 use Caledonia, retrenchment, signature (2, 11, 4); lines 164, 169, 172 and 346 use Caledonia, signature, retrenchment. *Fix:* the trigger order everywhere.

**M5. The written-off annuity is outside the sum.** Line 172 values the seventeen at about 31% of the book; the suspended annuity of 1931–32, about $49m more, is forgiven on signature and is in no total. *Fix:* one clause: "with the suspended annuity, about $425m" (MODEL), or say that it is not counted.

**M6. "None but those four".** Line 245: "The schedule binds the powers on the shores and the Concord … none but those four is bound by it." The powers named are three, or four if the Concord's two parties are counted. *Fix:* name them.

**M7. De Jonge is given The Hague's pen.** Line 237 has The Hague concede; line 271 ("De Jonge … conceding two fenced commercial ports") and set piece 4 (line 322, "yielding strictly two … ports", under the title "The BPM Director's Fences") give the concession to the Governor-General, who cannot make a treaty and in 1932 is not BPM's director. *Fix:* "The Hague concedes; de Jonge holds four lines", and retitle.

**M8. Set piece 5.** Line 323, "The cabinet signs away a weapon it could not afford to finish." The committee decides; the cabinet is not shown the paper. *Fix:* "The committee".

**M9. A stale impact note.** Line 298 cites L1374 "for The Hague's 1919 host role without naming Wilhelmina"; nothing in the body cites L1374 or needs it. *Fix:* delete.

**M10. `T-P1` misstates canon.** Line 392: "Canon … does not say who holds Samoa, New Guinea and Nauru after the peace." L1381 and the ledger's `C-1919-HAGUE` say "Pacifica and Japan retain Germany's Pacific islands" (PROPOSED), and L1316 has Australia and New Zealand among the partners who took them. *Fix:* cite L1381, and add to the OPEN list what, if anything, Japan retains.

**M11. Unregistered actors.** MacDonald forms the committee and writes the minute, Baldwin drops Lindemann, Hankey keeps the minute, Thomas tells the dominions; none is in the registry or in line 372's list. *Fix:* add them, or say they are named as incumbents only.

**M12. The Hong Kong and annexation patterns are wider than their messages.** Line 438 forbids "annexed Borneo/Fiji/Java" whoever the subject is, so a later sentence on Britain annexing Fiji in 1874 or the Dutch in Borneo would fail lint. *Fix:* put the subject in the pattern.

**M13. Stale lines in `## Decisions`.** Line 636, "no set piece uses Kaʻiulani" (set piece 0 does); line 631, "`B2` to `B4`, `C1` … still in the older style" (restyled in revision 14); line 3 omits the decisions of 11:21 that R-14 uses; line 660 says the instalment dates were confirmed and line 654 says they are from memory. `A3`, the first bullets of `B1`, `C3` and the calendar table keep the older compressed style (ampersands, plus signs, bold run-ins); that can wait for integration.

**M14. Simon's arrival differs across the suite.** Here and in the calendar, about 12 June; in `CR-085` line 137 and the author's note quoted there, about 14 June. Sailing about 29 May at fourteen days gives 12. *Fix:* in `CR-085`.

**M15. Real-world claims still from memory or unsourced.** The Ottawa sailing of 13 July and who sailed (lines 161, 222; from my own memory the date and the four names are right, and Hailsham and Runciman sailed too); Parliament's practice on cessions and the laying of treaties (line 168); the Lutong pipeline (line 193); the agent-general of 1872 (calendar, A); the instalment dates; the Canadian syndicate's name; the 155° W meridian and the Cook Islands' positions; Churchill leaving the Treasury in June 1929 and his friendship with Lindemann since 1921 (line 221, no entry under `## Sources`); Hankey as secretary; the Dindings; and the list at line 667 (the Tongan agreement of 1905, NKPM, the KPM's monopoly, Sulawesi's nickel, Chadbourne and the Indian duties, the guano bonds). One more, from memory: in history MacDonald, Simon and Chamberlain spent 16 June to 9 July 1932 at Lausanne. If the Thalassia Conference takes Lausanne's place, `CR-086` should say so once.

## What holds

- The annuities: 62 years from 1923–24 leave 53 after the moratorium year; 2 + 11 + 4 = 17, 36 kept; the years, the instalment of 15 December 1938, the fallback of 15 December 1934, and the present values (about $93m, $114m, $169m on a book of about $1.2bn, 31%) agree with each other, with `CR-083` and with a check at about 3.5%.
- The triggers follow K: the second tranche on the retrenchment's ratification, the third on both; and the body draws the right conclusion, that the far-end eleven hold London to nothing and the near-end four do.
- Travel and sequence: Kaʻiulani home by mid-May, Simon out on 29 May and in on 12 June, the cable to Hayama, the messenger to London by 1 July, the answer of 8 July, the full powers on 22 July, all at the calendar's sailing times. The draft's own table agrees with the shared calendar row for row.
- Offices and ages: the British ministers hold their real offices of 1932; Victoria is ninety-three, Kaʻiulani fifty-six, the Sultan of age since September 1931. Parliament approves and the Crown ratifies; the States General approve; the Emperor's two advices follow H.
- The four protected intents are untouched. Weapon design stays off the page. There are no exclamation marks.
- The committee of six is the best scene in the draft: Lindemann is right about the third clause and loses, neither answer meets him and the room knows it, Eyres-Monsell proposes default and is answered with sterling, and Churchill is silenced by his own file of 1926. Every party has a named loss: Canberra, Brooke's neighbour Brunei, the oil trust, the Admiralty, Labuan's Chinese merchants.

## Questions for the author

Needed before approval:
1. **S1.** Are the Realm's votes of 9 to 12 July public? If they are, should the Chiefs of Staff be told before them (about 4 to 8 July) instead of in the last week of July? Your condition of 11:21, that they must not be told what London already knows, decides it either way.
2. **S2, `T-B5c`.** Your words at 10:45 leave the reading of the dominions' cable at Fanning unstated. Does that mean neither case is adopted, so that the recommendation of Case A (a ban in the trust's charter) is withdrawn?
3. **S3.** Requests 2 to 4 and their answers are the drafter's. Do you approve them as written?

Can wait for integration:
4. **S6.** Whether the four drafts are integrated in one pass.
5. Palau, approved under M-2 as half of the southern anchor, still has no section.
6. The meridian of the 10° S protocol, 155° or 156° W, and what Japan retains of the former German islands (M10).
