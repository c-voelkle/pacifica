# Integration review: CR-083 to CR-087 in `master_storyline.md`

Fresh-context review of branch `integrate/cr083-087-endgame` (HEAD `83e27fa`). Read: `AGENTS.md`, the storyline (sections 33 to 37 in full, the opening overview, the trajectories and closing lists, and every hunk of `git diff d0d2c93`), the shared calendar, and the five decision records by targeted lookup only (not cover to cover). No review files, proposal, prose check, planning or session files were opened. Nothing in the repository was changed.

**Verdict.** The calendar holds: I found no passage that contradicts another on a date, a signer, a ratification, the tranches, the Senate's five votes or the place of the pledge. One finding touches an author's ruling and is listed as a blocker. The rest are label mismatches between writers, three small contradictions of emphasis, repetition in section 37, and a few sentences left stranded by insertions.

Line numbers are those of the storyline at HEAD.

---

## Blocker

**B1. L137 — "give that triumph its unresolved human cost"** (overview, "The novel's larger movement"; an old sentence the integration did not touch).
The author's ruling (CR-086 T-6) is that the cost is shown and never named as unresolved or settled. The integration cut the clause at L1910 but left its twin in the overview. The lint pattern only catches "moral cost", so this one passes the checker.
Fix: end the sentence "...and continuing exclusions stand beside that triumph."

---

## Should fix

### 1. Contradictions between writers (1931–1932)

**S1. L1796 — "only the common Navy's transports remain"** (CR-085) against L1741 "spends part of the lever", L1766 and L1864 "the lever wears away as those fields come in", L1862 "The new blocks produce nothing in 1932" (CR-084).
One writer has the oil lever gone in July 1932; the other has it wearing away over years.
Fix at L1796: "Of the three levers Julian threatened Tokyo with in 1931, the yen is given up now and the oil goes as the Borneo fields come in; in time only the common Navy's transports remain."

**S2. L1882 — "obtains the limiting words ... and the written custody"** (CR-086) against L1788 "what he obtains is that custody of the devices is written down" (CR-085) and L1770 "He loses both".
The same concession to King is won twice for two different arguments: in the winter for his paper against the pledge (L1882), and after May for his third point about the Navy seat (L1788). L1770 says he loses both winter arguments outright.
Fix at L1882: "He loses, and obtains the limiting words "that keeps the article"; the written custody he obtains after May, on his objection to the Navy seat." And at L1770: "He loses both, and keeps one limiting phrase."

**S3. L1844 — "keeps her standing for the one bargain she means to make"** (CR-084) against L1802 "Victoria has used her standing once already that year" (CR-083) and L1792, where in the same July she lets her view on the term be known through the aliʻi seats (CR-085).
Three writers each give Victoria (the old queen) a July or February abstention, and "the one bargain" does not sit with the other two.
Fix at L1844: "Victoria declines to enter the debate." (drop the rest of the sentence; the Charter is told at L1802).

**S4. L1784 — "Julian's cabinet has the offer for five days"** against L1794 "the condition they named in late May" and L1894 "In the last days of May, before Julian sails".
The offer arrives about 28 May; five days of cabinet end about 2 June, the day he sails, yet he takes the finished mandate to the committee in the last days of May. The CR says the committee is "in those days", which the storyline lost.
Fix at L1784: "He takes the mandate to the Senate's committee in those same days, and there..."

### 2. The same sentence written twice

**S5. L1638 — "The reckoning is overtaken in May 1932"** (section 33).
Two writers inserted the same fact back to back: "...it is overtaken: in the last days of May 1932 Britain decides to stop, and Article I of the Final Act of Thalassia ends the race." (CR-086) followed at once by "The reckoning is overtaken in May 1932, when Britain decides to renounce with a separating plant and no device." (CR-084).
Fix: delete the CR-084 sentence and its comment, and end the CR-086 sentence "...Britain, with a separating plant and no device, decides to stop, and Article I of the Final Act of Thalassia ends the race."

**S6. L1588 — "The return rests on that credit"** (section 33).
CR-084's sentence (the credit ends its work on 21 September 1931) is followed by CR-083's (the return rests on that credit, and London leaves gold rather than ask for more). They are in the wrong order and say the exit twice.
Fix: put the CR-083 sentence first and cut "on 21 September 1931, when Britain leaves gold" from the CR-084 sentence, so it reads "After that the credit has done its work; what steadies the floating pound is the sterling..."

### 3. Label sense

**S7. L639 — "Federal cession does not settle Native title or consent."**
The CR-087 insertion ends on `[OPEN — CR-087]`, and this old sentence now reads as part of the open list.
Fix: move the sentence to stand directly after "surveys remain **[PROPOSED]**.", before the `<!-- CR-087: the Lewis crest -->` comment.

**S8. Britain's programme: PROPOSED in one writer, APPROVED in the other.**
- Britain four years in with a separating works: `[PROPOSED — CR-084]` at L1668 ("by the spring of 1932 it has a separating works") and L1856 ("is four years in"); `[APPROVED]` at L1638 (CR-084), L1860 ("the small separating plant it has built"), L1868 and L1884 (CR-086, "four years into copying").
- Britain's ore enough for one late device and no second: `[PROPOSED — CR-084]` at L1856 (Tizard); `[APPROVED — CR-086]` at L1640 and L1884.
- The three undertakings of Article I and the pledge: `[PROPOSED — CR-084]` at L1856 ("A signatory outside the Concord undertakes"); `[APPROVED — CR-086]` at L1876.
Fix: at L1856 and L1668 mark these three facts APPROVED and leave PROPOSED on what is CR-084's own (Tizard's and Lindemann's speeches, the money voted, the default proposal).

**S9. L1802 — "in February she opposed a fourth crown"** is `[PROPOSED — CR-083]`; L1812 "Victoria opposes it from Honolulu" is `[APPROVED — CR-083]`.
Fix at L1802: label the first clause APPROVED and put `[PROPOSED — CR-083]` before "and the allies she gathered then".
The same applies one step back: the coalition's request for a fourth crown is `[PROPOSED]` at L1810, while Julian's asking the Senate on that request is `[APPROVED]` at L1812 and L1110. One of the two labels should give way.

**S10. L1739 — "Britain leaves gold on 21 September 1931"** opens a `[PROPOSED — CR-084]` run; the same fact is `[APPROVED — CR-083]` at L1723 and unlabelled canon at L1719 and L1721.
Fix: cut the sentence at L1739 (it is the fourth telling in section 34) and begin "After the election of 27 October...", with "Britain still owes its annuities in gold dollars" folded into the later sentence on why it deals.

**S11. L2015 — "OPEN-019-01–02, 06–08 and 10–13 remain ... Dominions treaty"** against L1872 `[APPROVED — CR-082, OPEN-019-06]` and L115 "(OPEN-019-06 decided)".
The integration edited this entry for 05 and left 06 listed as open.
Fix: "OPEN-019-05, British payment in kind, is decided by CR-084, and OPEN-019-06, the Dominions treaty, by CR-082 and CR-084. OPEN-019-01–02, 07–08 and 10–13 remain: ..." and drop "Dominions treaty" from the list.

### 4. Repetition at length in section 37 (which to trim)

**S12. The commencement-order safeguard, told three times.** L1818 (end: "comes into force only by a commencement order, which London holds back"), L1820 ("About 15 July London makes the commencement order ... only after the bill and the order") and L1846 ("The April accord gives it one remedy ... not proclaimed before the order").
Trim L1846 (CR-084): cut from "Caledonia's tranche is earned in June" to "before the order." and keep one clause, "Britain carries that risk for about three weeks."

**S13. Caledonia's tranche valued twice.** L1818 "of about $49 million each, some $93 million at present value" and L1846 "about $49 million a year ... about $93 million in 1932".
Trim L1818: cut the `[MODEL — CR-083]` figures; L1846 holds the whole schedule.

**S14. The July-to-autumn sequence, told three times.** L1842 ("The Council at Hayama adopts ... second advice of the Privy Council"), L1868 (the whole paragraph, same writer) and L1904 (CR-086); L1900's last sentence ("In the last days of July the component treaties are signed ... as their signers arrive") repeats L1868's first.
Trim L1842: delete that one sentence. Trim L1900: delete its last sentence. Keep L1868 and L1904.

**S15. Article I's text, told twice.** L1856 sentences 2 to 4 (CR-084) and L1876 (CR-086) give the three undertakings and "Atomic power stays lawful" almost word for word.
Trim L1856 to: "The paper Kaʻiulani left in London asks more of Britain than ships: the three undertakings of the first article, the Realm's pledge beside it, and a tranche of the annuity schedule for the signature."

**S16. The annuity debate of 12 July, told twice.** L1820 (CR-083: Giannini and Tate's bloc object, "the money should go to the mortgages") and L1844 (CR-084: Giannini, the Industrial Board's senators and Tate's bloc attack the same bill).
Keep L1844 as the debate. Trim L1820 to the vote and the ministers' answer with the map, which is unique to it: cut the sentence "Giannini and Harlan Tate's interior bloc object ... an Act of a foreign parliament." or reduce it to "Giannini has the figure: two annuities given for an Act of a foreign parliament."

**S17. Canada's signature and Great Bear, told twice.** L1830 ("London cannot ask Ottawa a second time ... to divert the ore"; "Canada's signature is not bought with the board's contract") and L1884 ("cannot be asked by London to divert the ore; its signature is not bought with the prairie wheat contract").
Trim L1884 to: "Canada signs for itself, and Australia and New Zealand sign on the same footing."

**S18. New Zealand's rebate, told three times** by one writer: L1848 (end), L1866 (last sentence) and L1872 ("London credits Wellington with its contribution").
Trim L1872: delete that `[PROPOSED — CR-084]` sentence.

---

## Minor

**M1. L1902 and L1912 — "the founder's voice is broadcast, as every year"** appears in both. The second is the last image and should be the first time the reader meets the phrase.
Fix at L1902: end the paragraph "It is the day on which, each year since 1913, the press estate broadcasts the founder's voice."

**M2. "ninety-three" five times** (L1776, L1802, L1812, L1844, L1912). It dulls the last image. Fix: drop "at ninety-three" at L1812 and L1844.

**M3. L1908 — "Its signature under the Final Act is still unratified"** is inserted between "have checked the loss of its talent" and "The check comes late", which answers the earlier sentence.
Fix: move the CR-086 sentence to the end of the paragraph and begin it "The Union's signature".

**M4. L1735 — "In 1932 it still buys about a quarter"**. After the inserted sentence about the trust and the Republic, "it" has lost the Realm as its subject. Fix: "In 1932 the Realm still buys".

**M5. L1407 — "cancelled under that head"**. The sentence before is now about sterling. Fix: "In 1932 the first annuities cancelled in that settlement".

**M6. L1154 — "A customs line stands at the Rockies now"**. "now" reads as a comparison with the retired history, and the sentence repeats the Canadian Pacific, the Montreal banks and the bonded wheat from the sentence before. Fix: "A customs line stands at the Rockies, and the bonded route still pulls the Prairies away from reciprocity with the Union."

**M7. L1888 — "France, a non-signatory, sits on the bench"** against L1886 "France signs the Final Act and Article II". Fix: "France, which has not signed Article I,".

**M8. L1818 — "puts the Hayama Council off to mid-June"**. Section 36 never says the Council had an earlier date; there the date follows from the offer of 28 May. Fix: "The coup at Tokyo on 15 May leaves everything waiting on the Hayama Council of mid-June, the Act and the proclamation with it."

**M9. L1792 — order inside the paragraph.** July (Senate, delegations), then "In the Diet in June Mori Kaku", then July again. Fix: move the Mori Kaku sentence to the head of the paragraph.

**M10. L1870 — the November election paragraph** stands before the whole account of the Final Act and 1 August (L1874 to L1904). Fix: move it to follow L1904, which ends "rides on the election of November".

**M11. "About" days labelled unevenly.** L1894 marks "about 9 to 11 July" `[PROPOSED — CR-086]`; the same days stand under `[APPROVED]` at L1792, L1820, L1844 and the Emperor's "About 16 July" at L1792. The closing lists (L2041 to L2047) say all "about" days are PROPOSED, so nothing is wrong in substance; either drop the inline label at L1894 or add it elsewhere.

**M12. Spelling.** L1842 has "counter-signature" and "countersignature" in one sentence; "counter-signature(s)" also at L1848, L1894, "countersign-" everywhere else. Pick one.

**M13. Closing lists and trajectories not carried forward.**
- L2002 "final scenes ... remain to be developed": add "the last image is settled by CR-086."
- L2041 lists "which northern nation refuses in 1932" as open; L1826 names the Sekani of McLeod Lake (`[PROPOSED]`).
- L1920 (Victoria) and L1932 (Julian) say nothing of 1932 beyond the Charter: no refusal of the fourth crown, no Final Act. Not a contradiction; a one-clause addition each would bring them level with Takahashi, Hirohito and Kiyoshi's son, which were updated. Kaʻiulani has no trajectory entry at all.

**M14. L1743 — "his loss after the first review of 1937"** is said in March 1932, three months before Hayama creates that review. Fix: "his loss once the annex's bar ends in 1937".

**M15. L1651 and L1662** both tell the announcement of 29 April 1932 (same writer). Trim L1651 to a clause or cut it.

**M16. Implied comparison with real history.** L1386 "no cabinet in Tokyo falls to riots over a shortage of rice" only means something against the historical record. Older canon uses the same form ("There is no boycott of Japan in 1931"), so this is within house practice; noted only.

---

## Checked and found sound

- **Calendar order.** Late April accord (L1745, L1818); early May sailing; Labuan's and the legislature's votes in May; 15 May; 26 to 28 May; London's committee and Simon's sailing about 29 May; Hayama 12 to 15 June; Simon about 12 June and his cable; the Severance Act in the last week of June; 30 June; 8 July cable and the full powers about 22 July; Senate and delegations about 9 to 11 July; annuity bill about 12 July, "four days after" the cable; commencement order about 15 July; Emperor about 16 July and Takahashi's arrival about 27 July; Proclamation about 18 July and Pattullo's arrival about 25 July; late treaties 22 to 30 July; yen agreement about 28 or 29 July; 1 August; autumn deposits. Sea times agree with the calendar's.
- **Who signs what.** April accord: Simon, Kaʻiulani, the Realm's Treasury, the High Commissioner for the Caledonian chapter. Association Treaty: Pattullo and the Realm's envoy. Guarantee: Pattullo and the Foreign minister's deputy, with Takahashi's countersigned full powers. Trilateral Treaty: Kaʻiulani, Pattullo, Bennett's plenipotentiary. Renewal: Takahashi and an authorized minister of the Realm, not Kaʻiulani. Final Act order: Julian, Takahashi, Simon first of the powers, Kaʻiulani last and seated. Consistent at L119 to L123, L1798, L1820, L1830, L1842, L1902.
- **Ratification.** Both crowns: the renewal and the two articles. Julian alone on 1 August: the late treaties. Emperor's second advice in the autumn. King's ratification deposited in the autumn; Parliament approves and does not ratify. Consistent at L1792, L1820, L1842, L1846, L1868, L1904.
- **Annuities.** Sixty-two years from 1923, fifty-three remaining, seventeen cancelled (2, 11, 4), thirty-six standing; years 1932–33 and 1933–34, 1934–35 to 1937–38, 1974–75 to 1984–85; the suspended annuity written off on signature; nothing paid until 15 December 1938; triggers as calendar K. The arithmetic and the 31 per cent check. Consistent at L119, L1407, L1741, L1818, L1846, L1856, L1858, L1860, L1868, L1906.
- **The Senate's five two-thirds votes.** Four about 9 to 11 July with Article II first, the fifth in the last days of July; neither article to the Chamber; the annuity bill by majority in both. Consistent at L1628, L1792, L1812, L1820, L1842, L1844, L1872, L1882, L1894.
- **The pledge.** A separate declaration in April, moved into Article I at Hayama on Britain's first request; the other three requests refused. Consistent at L1745, L1856, L1860, L1876, L1902.
- **Custody and keys.** Two keys, the Sovereign's and the Polytechnic chief's; the Navy minister holds none. L1790, L1880, L1882 agree (apart from S2 on when King won the written statement).
- **What Hayama agreed.** L1786, L1790, L1820, L1842, L1860, L1876, L1894, L1662 are consistent; Kaʻiulani takes part by cable; Hirohito does not bargain.
- **Kaʻiulani and Victoria.** Never confused. Kaʻiulani is fifty-six and Foreign minister throughout; Victoria is at Honolulu; "Victoria" as the city is always clear from context.
- **High Commissioner** (L1818, once) and **the Governor John Buchan** (L117, L1810 to L1820): consistent.
- **Rulings and protected intents.** No sentence says what Kaʻiulani or Victoria knew in 1919 about the food lever. The last image is the final paragraph of section 37 (L1912), gives no reason and says nothing of the years between. No murderer of Noe Kaʻanoe Ward; Julian is never President ("provisional President" at L1820 is Pattullo); no throne abeyance; no extermination; no weapon design (process words only).
- **Retired history.** No British Columbia in Confederation, no Canadian Pacific coast, no northern water diversion, no renewal "to 1937", no Japanese right to refuse in 1937 except as the winter's fear (L1770) and what Japan gives up (L1788, L1860). The Western line meets the 49th parallel only on the Lewis crest (L125, L639). "Britain is managed through debt" (L1906) is qualified at once by the schedule.
- **House style.** No exclamation marks, no drafting or review labels in body sentences, no "in our timeline". Codes such as "T-6" and "T-R3" occur only inside hidden comments.
- **Stitched old sentences** in L718, L1576, L1786, L1796 and L1798 read as sense.

---

## What was done with this review (24 November 2026)

Applied in the storyline: B1; S1 to S18 (S9's second point, the label on the coalition's request, is left as the decision record has it); M1, M2 (two of the five), M3, M4, M5, M7, M10, M12 and the first point of M13. Not applied: M6, M8, M9, M11, M14, M15, M16 and the rest of M13 (the trajectories of Victoria and Julian, and a trajectory entry for Kaʻiulani), which are left for the rewrite of the text.
