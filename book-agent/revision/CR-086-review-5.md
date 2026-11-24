# CR-086 review 5 (fresh context, 24 November 2026)

Reviewed: `book-agent/revision/CR-086.md`, revision 6 with the changes of 24 November. Read: the draft in full; `AGENTS.md`; the cited lines of `master_storyline.md` (L892, L929, L1020, L1177, L1281, L1374, L1379, L1503, L1534, L1597, L1602, L1604, L1612, L1614, L1634, L1640, L1643, L1646, L1651, L1655, L1672, L1681, L1695, L1720, L1728, L1732, L1734, L1736, L1738, L1746 to L1758, L1867); the ledger entries the draft amends; the bible's entry for Kaʻiulani; `finance/CR-083-086-workbook.md`; and, for cross-references only, `CR-083` `A10` to `A11`, `CR-084` `A1`, `A3`, `B1`, `B5`, `T-S1`, `T-A2`, and `CR-085` `A3` to `A6`. No earlier review, planning note or session file was opened.

Scripts. `preflight.py --draft` exits with 0 errors and 11 warnings: two registry warnings (Soong and Pani not yet in the registry), five ledger IDs that belong to the siblings, and four matches of the draft's own "moral cost" pattern on lines 49, 74 (twice) and 332, all of them quotations of the author or of the rule. `cr_facts.py preview --tensions` reports "no canon tension carries fact changes". The draft answers four of the five ledger warnings at line 397; `C-1932-ADJUSTABLE-PARITY` (line 127, `CR-085`'s) is not among them.

## Verdict

One more revision. The two articles, the route of consent and the siblings' figures agree, and the canon citations I sampled are sound. Three things stop integration: two decision rows sit in the wrong table, the bulk approval row cannot be applied as written, and the Emperor's ratification cannot reach Thalassia on the dates given.

## Blockers

**B1. Two decision rows are inside the table of signatories.**
- *Passage:* lines 181 and 182, the first two rows of the `C3` table: "| F-13 | Princess Kaʻiulani is the common Foreign minister, named in 1931 …" and "| R-6 | The drafter's PROPOSED additions of revision 6 …". The table's columns are "Signatory | Why it cannot get a weapon soon | What it is paid | Where decided".
- *Problem:* they are three-column decision rows in a four-column table, and the `## Decisions` table (lines 531 to 547) ends at F-12 and holds neither. The two approvals of 24 November are therefore missing from the one place a reader or a script looks for them. The same slip is in all three siblings: `CR-084` `A1` (row R-10), `CR-085` `A4` (row R-7) and `CR-083` `A10a` (row R-12).
- *Fix:* move both rows to the end of `## Decisions` here, and do the same in the three siblings.

**B2. Row R-6 does not say what it approves, and the labels around it contradict each other.**
- *Passage:* line 182: "The drafter's PROPOSED additions of revision 6, as listed under 'The should-fix items … one by one' below | APPROVED … The labels in the body still read PROPOSED where they were written so and are to be read with this row. Proposals made before that revision are not covered".
- *Problem:* (a) The list it points to (lines 569 to 584) mixes cuts, rewordings, things already approved and new proposals, and marks only S2 and S14 as PROPOSED. (b) The author's words of 07:27 name "the pledge holding in war", but line 5 and line 571 date that to revision 5, which the row excludes. (c) Line 159 and line 215 call the pledge in war and the widened bench "approved", while line 561 (item 12, "that the pledge holds in war"), line 571 ("the second is PROPOSED") and line 583 ("S14: the bench is widened for Article I, PROPOSED") still call them PROPOSED. (d) "To be read with this row" makes every PROPOSED label in the body uncertain: a reader cannot tell whether line 175 ("The vote (PROPOSED)"), the non-signatories' footing (line 261) or "It names no place" (line 172) is approved.
- *Fix:* replace the row with an enumerated one. On the quoted words, two items are safe: the pledge holds in war (`C1`) and the bench is widened for Article I complaints (`C5`). Any other addition of revision 6 that the report of 03:35–06:53 marked PROPOSED should be named one by one, with its section. Then correct the labels in the body, item 12 of the PROPOSED list, and S2 and S14, and delete "to be read with this row".

**B3. The Emperor's ratification cannot be at Thalassia on 1 August as dated.**
- *Passage:* line 310: "he signs Japan's ratification at Tokyo in the last days of July, on Privy Council advice given on the Act itself and separate from its advice on the renewal, and Prince Chichibu deposits it in the hall. (`CR-085` `A3`)". Lines 306 and 329 repeat the deposit. Line 587 admits the dates are "not tested".
- *Problem:* a paper signed in Tokyo in the last days of July crosses the Pacific by sea, and the fastest liners of 1932 took about nine to fourteen days. Canon has a cable and a radiotelephone to Tokyo and no air service across the ocean. The sibling suite itself counts eleven days from London (`CR-084` `B1`). Second, `CR-085` `A3` has one advice of the Privy Council, in mid-July, on the renewal; it says nothing of a second advice on the Act, so the citation does not support the sentence. Third, the Act's texts are voted by the delegations "in July" (line 304), so the Privy Council would advise on a text that is final only days before.
- *Fix:* choose one. Either the Privy Council gives both advices at its sitting of mid-July, the Emperor signs by about 17 July an instrument that takes effect on signature of the Act, and it sails at once, which means the delegations must vote the two articles in the first half of July; or the Emperor signs at the end of July, Tokyo cables it, and Chichibu deposits a notification of ratification under his full powers with the signed instrument to follow by sea. Either keeps the image of line 329. Write the same account into `CR-085` `A3` and `A5`.

## Should fix

**S1. The one-sentence ending and its own footnote disagree.** Line 84: "the powers that could have sought the weapon give it up, France excepted". Line 197: "The sentence at the head of this file therefore says 'the powers at Thalassia'." It does not. Line 197's wording is the true one, since Vienna (Joachimsthal and the institute), Italy, federal Russia, Belgium and Norway have not signed. *Fix:* "the powers at Thalassia that could have sought the weapon give it up, France excepted".

**S2. The cut offtake is still listed.** Line 560, item 11: "…what the Realm cannot use; the paid offtake of Britain's remaining ore." Lines 4, 198 and 578 say it is cut. *Fix:* delete the phrase, and reduce line 198 to its last clause (see Leftovers).

**S3. Two votes or three.** Line 274: three matters "Julian's government cannot do without", and the aliʻi seats "make Article II their condition for all three". Line 360 (set piece 4): "the price of the two votes that need the aliʻi seats". Line 7 also says "the two votes". *Fix:* "three" in line 360. The same set piece puts Mead's wording in the Senate scene of July; `D1` and `D5` put it in May.

**S4. 1 August is told three ways.**
- Line 313 gives Julian three signatures: the pledge with the custody declaration, "the Realm's guarantee under Article II", and the ratification. Line 329: "He signs once more that day, the ratification". The guarantee is missing from `E3` and from `T-9`.
- Kaʻiulani does not appear in `E3` entry 4 or in set piece 5 (line 361). The approved image, that she signs seated, is only in `E1`.
- Japan's countersignature of the pledge is in `C2a` (line 172), the ledger (line 400) and `CR-085` `A5` ("Chichibu deposits both"), and Britain made it a condition of its own signature (`CR-084` `B5`). `E1` and `E3` have Chichibu deposit the ratification only.
- The order in line 329 has the ratifications before "The Act is signed and promulgated".
- *Fix:* one ordered paragraph in `E3`: the plenipotentiaries and Kaʻiulani, seated, sign the Act; Julian reads the pledge and signs it with the custody declaration and the guarantee; Chichibu lays down the countersignature and the ratification; Julian ratifies; promulgation and the broadcast.

**S5. `D2` claims more than the text of `D1` delivers.** Line 243: "The Realm used food once" and "The third undertaking of `D1` forbids exactly that." Two difficulties. Canon L1374 (PROPOSED) has Julian, in the autumn of 1918, stop the Entente's credit and offer "food to the starving Central Powers for an armistice", so 1919 is not the only use. And the undertakings hold "in peace" (line 237), while the lever of 1919 was pulled under an armistice, "while a peace was being made", toward states still enemies in law. A British or German lawyer would say the article does not reach 1919 at all. *Fix:* define "in peace" in `D1` as toward any signatory with which the Concord is not at war, an armistice counting as peace; and let `D2` say "once in the making of a peace", with 1918 named as a wartime use the article does not reach.

**S6. Article II is offered as part of the price of Article I, which the third undertaking forbids and France disproves.** The `C3` table lists "the food order" under "What it is paid" for Britain, China, Mexico, the Gulf and the Confederacy. Line 218 has Kaʻiulani answer the German delegate "that the pledge and Article II are what the other side receives for it". France signs Article II and not Article I (line 202) and receives the food order in full. *Fix:* take the food order out of the price column and let Kaʻiulani answer with the pledge and the debts; add one sentence that Article II is given to every signatory of the Act whatever it does about Article I. That strengthens the article.

**S7. "To honour the scheduled contracts" covers contracts the Concord is not party to.** Line 235 undertakes it without limit. The schedule (lines 249 to 258) holds four kinds: the state's own instruments; the prairie contract, whose buyer is the board "which the Crown cannot direct" (`CR-083` `A11` says the schedule "binds neither the board nor the Agency"); private houses' contracts; and the straits, whose shores are British and Dutch (`CR-084` line 212: "The schedule binds the powers on the shores and the Concord"). `D4` (line 261) explains only the non-signatory sellers. The ledger line 401 repeats "the scheduled contracts are honoured". *Fix:* word the second undertaking as "to honour its own scheduled instruments and to interrupt none of the others", and say in `D3` on which footing each row stands. Say also why the Netherlands signs the schedule of an article it does not sign (line 196); an article that costs it nothing and guards its own straits is one it would sign.

**S8. Germany's signature is not argued against France's freedom.** `B4` has Hahn object to the third clause. Nobody in Berlin objects that Germany renounces while France stays free, receives Germany's renunciation "for nothing" (line 204) and sits on the bench that judges Germany (line 217). Britain's cabinet has that argument (`CR-084` `B5`, Eyres-Monsell's dissent); Germany's needs it more. *Fix:* two sentences in `B4`: who says it in Berlin, and what answers him (the pledge France does not have, the debt settlement, a French judge who cannot sit when France is a party). Also: line 202 says of France's reasons "neither is pride", and the first reason (line 203, "it had been watched being wrong") is injured pride with a scientific argument attached. Drop the disclaimer.

**S9. France's credit.** Line 140: France "asks for no credit". The workbook's row E263 is "Private stabilization credits to Britain, Germany and France (`CR-086` `B1`; no source)", and line 593 speaks of syndicates that "carry three great powers". *Fix:* make the memo Britain's and Germany's, or give France a credit line it does not draw.

**S10. The pledge in war is approved and never argued.** Line 159: the pledge "holds in war as in peace" and ends "only when the court has found it in breach", and breach means a separating plant, a test or kept fuel. A signatory could then make conventional war on the Realm and keep its immunity. The Senate's debate (line 175) repeats King's peacetime argument only. A two-thirds vote that never hears this is hard to believe. *Fix:* give the provisioners the sentence in the chamber and give the answer (the fleet, oil and credit remain; Article II holds only in peace; a pledge that fell away in war would be worth nothing to London). On the bench (line 215), say whether Japan's judge sits when the Realm complains, since Japan countersigns the pledge.

**S11. The header is a day behind.** Line 3 dates the revision to "the author's decisions of 00:12"; line 9, "Approved so far", stops at 23:14 and says "The rest of the wording of both articles and everything else is the drafter's", which omits 23:21, 23:52, 00:12 and the three decisions of 24 November; line 14 names a review asked for at 23:21, where the latest request is that of 07:37.

**S12. A drafting instruction sits in the body beside the fact it guards.** Line 310: "She chaired the peace during which relief was made a lever, and she signs the act that forswears it; the draft says nothing of what she knew in 1919, and no sentence on integration should." The first half is the kind of pointing sentence an integrator will copy into the storyline; the second half is a rule and belongs in `E4`. *Fix:* keep the facts in `E1` (who she was in 1919, that she signs seated) and move the rule to `E4`, next to the rule on the cost.

## Minor

- Line 453 (`T-8`): "`D1`'s three undertakings are…" describes the text before the decision; add "as then drafted". `T-8` and `T-9` stand after the note that there is no `T-3` (line 452); move the note to the end.
- Line 223 marks "charges nothing and pays nothing (PROPOSED)"; F-2 (line 534) and item 86-3 approve "carried free, nothing paid".
- Line 170: the heading of `C2a` reads APPROVED for the whole section; the annexed declaration and what it says are item 12 of the PROPOSED list.
- Line 172: the declaration "names no place" and speaks of "the two keys of the archive"; line 171 says "the Thalassia archive". Have the declaration name the keys by their holders.
- Line 272: the heading "The pledge binds the Realm: the chambers' vote" uses "pledge" for Article II and "chambers" for a vote that only the Senate takes (line 273).
- Line 237: "Mead has it narrowed" gives a man "holding no office" (line 275) the power to amend; and "The words are the cabinet's and Mead's" sits oddly with line 276, where he fights the third undertaking and loses.
- Line 237: "treaties in force on 1 August 1932" does not cover the dominions' defense treaty of July, which carries New Zealand's guarantee and is unratified that day. "Signed on or before" would.
- The calendar (lines 295 to 307) has no row for May's narrowed text of Article II, the second of the three steps.
- The `C3` row for Caledonia omits the pledge that every other signatory receives.
- Line 310 ends "(`CR-085` `A3`)." after the full stop.
- Impact notes: nothing for the passage where Kaʻiulani's appointment of 1931 will be told, for L1374 (the seated echo), for L1651 and L1734 (Chichibu's deposit), or for L1746 ("joins the arbitration court's new charter") on the widened bench.
- Line 397 answers four ledger warnings; preflight gives five.
- `E2` (Guaymas) stands between the calendar and the finale. It reads better in Part B.

## Literary effect

The design works. Julian reading the pledge in the hall of the Senate that refused him in February is the right act for the last day, and it is his only speech. Kaʻiulani seated, as canon has her at The Hague ("She presides seated, and the conference knows why", L1374), carries 1919 into the room without a word about it. Victoria leaving the set on (line 361) is the best single image in the draft and says what the author wants unsaid. I found no sentence that states the cost as unresolved or settled, and none that says what Kaʻiulani knew in 1919; line 310 is the closest and is dealt with in S12.

What weakens the close is arrangement. `E3` entry 4 is a list of procedures in the wrong order, and it leaves out the seated signature (S4). The page of 1 August also dwells on what is not yet done: line 314, "No other signatory has", and the Union's signature riding on November. Those are honest and should stay in `E1`; the fourth entry should hold only what happens in the hall. The draft offers candidates for the last image and does not choose. For the crescendo the author asked for, the order that builds is: the signatures, Julian's voice, Chichibu's two papers, then the founder's voice on the air and Victoria's set left on. France's delegate in the hall, signing the Act and not the article, is enough shadow.

## Leftovers from earlier revisions

The accumulated notes do make the draft hard to read. About eighty lines stand before the first sentence of substance, and about thirty-five lines of review bookkeeping stand at the end of `## Decisions`.

- Lines 4 to 8: five paragraphs of "What changed". Keep revision 6's; the rest belong in the commit history.
- Line 198: "Revisions 3 to 5 had the Works offer a paid contract for it. That is cut: it would have paid Britain twice". Keep only that Britain keeps its ore and that Tizard's estimate answers it.
- Line 279: "Earlier drafts carried a figure with no source; it is removed."
- Line 459: "(As first written this case said 'his only signature that day'; he also ratifies, which the fourth review pointed out.)"
- Lines 569 to 603: the item-by-item answers to three earlier reviews. Fold what is still open into the OPEN list (Britain's ore quantities, the syndicates' capacity, `L1736`, the Council of the Seal's membership, the one foreign voice on Article II) and cut the rest.
- Line 206 ("No sentence in this CR says how it ends") and line 323 ("the draft says so") are notes to the reader of the draft and not statements of what happens.

No label of the form "(Fixes B4)" and no exclamation mark is in the draft.

## The drafts together

- **Votes and ratification.** `E1`'s five two-thirds votes match `CR-084` `A3` and `T-S1` (the two counter-signatures and `C-1932-ANZ-DEFENSE` in one vote), `CR-083` `A10` (the Association Treaty, given "only after Article II has been voted first") and `CR-085` `A6` (the striking of the term). The annuity bill by majority in both chambers matches. Article II as the sufficers' fifth condition matches `CR-084` `A3`.
- **Britain's price.** The split of 2 near-end, 4 near-end and 11 far-end, the six years without payment and the clause for L1754 agree across `CR-084` `B1`, `T-A2`, the workbook and line 350.
- **Britain's fourth request.** `CR-084` `B5` has Thalassia answer "that France has no ore, no separating plant and no pledge". This draft gives France Madagascar's ores (lines 100 and 209). One of the two must change; "little ore" would do.
- **Japan.** `CR-085` `A5` agrees on Japan's place, custody and the countersignature. It differs on the Privy Council (B3) and on what Chichibu deposits (S4).
- **June.** Kaʻiulani sits at Hayama on 12–15 June as a common minister (L1651), about eleven days' sailing each way. `CR-084` `B5` has Thalassia answer Simon's four requests "in June" and a messenger reach London for the cabinet of 8 July, which means leaving by about 27 June. That is possible only if the cabinet at Thalassia answers on a cable from Hayama; say so in one of the two drafts. `CR-084` `B5` also has her hand Simon the draft in April without saying where, and then says "He hands it over".
- **Caledonia, the wheat, the straits.** `CR-083` `A11` and `CR-084` lines 150 and 212 agree with `C3` and `D3`, subject to S7.
- **The misplaced approval row** is in all four drafts (B1).

## Approvals against the quoted words

- F-1 (19:16), F-2 (19:32 and item 86-3), F-3 (19:32 and 86-1), F-4 (19:32, 19:35), F-4a (19:55), F-4b (20:11), F-4c (items 86-2 and 86-4 to 86-7) and F-12 (23:52) rest on quoted words. The draft is candid that the sheet's wording is the author's "by adoption".
- F-5 and F-8 rest on "Yes to both" (23:21) and are correctly limited; the tonnage and the July date stay open.
- F-13 rests on 07:31 and 07:37. "Named in 1931", handing Simon the draft and answering the delegates follow from the office.
- The pledge in war and the widened bench rest on 07:27, which names both. Their labels are inconsistent (B2).
- R-6 is not clear enough (B2). "I approve the other proposals as well" answers a sentence about things "marked PROPOSED" in one report, with three examples. It cannot carry anything the row does not name.
- Labels that reach further than the words: the heading of `C2a` (minor, above). `T-9` Case B covers reading the pledge and signing the custody declaration; signing the guarantee under Article II and ratifying are rightly PROPOSED in item 12.
- The decisions of 00:12 concern the siblings except the Hayama dates, which the calendar follows.

## History checked

On the web, 24 November 2026: Herriot's third ministry ran from 3 June to 18 December 1932 (confirmed, so line 202 need no longer say "from memory"). The Ottawa conference opened on 21 July 1932; the page gives its close as both 18 and 20 August, as the draft notes, and names Baldwin as Britain's delegate. The Urgeiriça page confirms working from 1913 and does not carry the idle years of 1926–29 or the sale of August 1929; those rest on the draft's second source, which I did not open.

From my own knowledge, consistent with the draft: the Final Act of Vienna, 9 June 1815; the customs gold unit of 1 February 1930; T. V. Soong at Finance from 1928 to 1933, with a short resignation in mid-1932 that is worth a look since the protocol is signed in July; Soong's and Pani's years of birth and death; Pani at the Treasury from February 1932; Justo in office from 20 February 1932; Calles as the power in Mexico, and a Sonoran born at Guaymas; France's large gold stock in 1932; Britain off gold on 21 September 1931; China on silver until 1935; Simon at the Foreign Office; Mead born in 1858. One caution: the Statute of Westminster did not apply to Australia and New Zealand until they adopted it (1942 and 1947), so line 195's "after the Statute of Westminster a dominion makes its own treaties" is exact only for Canada; the two could sign in their own names in any case, and canon L1752 already uses the phrase. The sea time across the Pacific in B3 is from memory. Not checked: Radium Hill's and South Terras's dates, the monazite trade, Travancore, Madagascar's output.
