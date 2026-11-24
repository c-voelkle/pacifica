# CR-085 review 6 (fresh context, 24 November 2026)

I reviewed `book-agent/revision/CR-085.md`, revision 8, in full, in a fresh context. I read `AGENTS.md`; the storyline lines the draft cites (L75 to L1885, about fifty lines, each read whole); the ledger entries `C-1927-CONCORD` and `C-1932-CONCORD-RENEWAL`; the registry only by search; and the sibling drafts `CR-083`, `CR-084`, `CR-086` and `CR-087` by search, for cross-references, dates and figures. I read no earlier review, no planning note and no writer's notes. `preflight.py --draft` exits 0 with 0 errors and 8 warnings, all of them the eight new persons not yet in the registry. `cr_facts.py preview` reports canon lint clean for the 18 fact changes and 13 findings in the draft itself, all the same unknown character IDs. The historical claims about May to July 1932 that the draft marks "from memory" agree with what I know (15 May, Takahashi acting to 26 May, Saitō's cabinet, Araki in both, Hiranuma as vice-president, the London treaty's dates), but I fetched nothing and they still need sources.

## Verdict

**One more revision.** The turn of May is well argued and agrees with the siblings on every date I checked. Two things stop it short of approval: the instruments of July are in an order that cannot work, and the Council at Hayama has no room in which its bargain is struck. Both can be mended in Part A without touching a decided item.

## Blockers

**B1. Japan ratifies on 16 July a renewal whose parts are not yet made or voted.**
- *Passage:* line 102 ("The Emperor signs Japan's ratifications and the countersignature at Tokyo on that advice, about 16 July"); line 145 ("Both crowns then ratify"); line 153 ("at Thalassia from about 27 July ... to sign it"); line 325 (the renewal "Carries ... `C-1932-ADJUSTABLE-PARITY`").
- *Problem:* The mid-July signature is decided and I do not reargue it. The draft does not fit the rest of July round it. (a) The yen's reset is the first thing the cabinet trades the term for (line 104), yet its instrument is negotiated through July and signed by Takahashi after 27 July, eleven days after the Emperor has ratified the renewal that carries it. The Privy Council would be advising on an instrument that does not exist. (b) Line 145 has the crowns ratify after the delegations, and the delegations are still fighting the yen and pool entry "in the choice and instruction of the Senate's thirty delegates"; nothing says they vote before 16 July. (c) The Senate's two-thirds vote is "in July" with no day. If it falls after 16 July, Japan has given up exit while Tate can still win. (d) `CR-084` line 102 has the Concord's other treaties "ratified by both crowns on 1 August", but they are signed at Thalassia in July after Takahashi has sailed, and the advice covers only "the renewal, and the two articles" (line 102). The Emperor cannot ratify on 1 August what is not in the bag.
- *Fix:* One dated order for 25 June to 1 August, stated once in `A6` and used in `A3`, `A7` and the calendar. A workable one: the Senate votes in the first week of July; the parity instrument is initialled by the vice-minister before the Privy Council sits, or is expressly outside the ratified package; the delegations vote before 1 August; Takahashi holds the Emperor's instruments and lays them down only when the parity instrument is signed and the delegations have voted. That gives his carrying them a point. Say which Concord treaties wait for a second advice in the autumn, and bring `CR-084` line 102 into line.

**B2. Nobody can be placed in the room where Hayama's bargain is made.**
- *Passage:* line 108 ("neither Emperor bargains"; Takahashi "settles the text with the three common ministers in the days before and beside the sittings"); line 112 ("without the national ministers"); line 127 ("He asks that the home army come under common command ... Takahashi refuses for the cabinet"); line 106 (the mandate "to refuse the alternating executive, and to ask for the home army"); line 289.
- *Problem:* Three statements do not hold together. Neither Emperor bargains, but Julian carries a mandate to refuse and to ask, and is "himself refused". Takahashi is a national minister and canon shuts him out of the sittings (L1651), so the refusal of Julian is spoken by a man who is not in the Council to a sovereign who does not bargain. And the common ministers cannot settle anything "in the days before": they sail with Julian and land on the eve (lines 95, 107). Who speaks for the Realm is also unclear. The Realm's cabinet writes the mandate and its ministers are excluded; of the three common ministers one is Japanese with his own seat on the table (line 109) and one, Kaʻiulani, signs for both crowns (`CR-084` line 102).
- *Fix:* Decide and say where the bargaining happens. The plainest version: Julian bargains himself, outside the sittings, with Takahashi, and the Council only adopts; strike "neither Emperor bargains" for "the Emperor does not bargain". Or give the Realm an envoy of its own cabinet beside the Council, as Japan has Takahashi. Move the settling of the text to 12–15 June, or have Chichibu and Takahashi's vice-minister prepare it by cable beforehand. Then rewrite set piece 3 to match.

## Should fix

**S1. The quota's default has no stated direction, and it moves the Realm's money without a vote.**
- *Passage:* line 116 ("failing agreement, the quota moves to the share the audit of output gives"); line 104 ("a default on the quota that favours Japan"); line 146 ("Tokyo wins a joint audit"); lines 118 and 180 (the yards' and the pool's shares "equal to Japan's share of the quota"); line 156.
- *Problem:* The draft never says whether the audit is expected to lower or raise Japan's 35%. By canon's own figures (the Realm out-producing the Union, Japan the second industrial power) it lowers it. Then Japan pays less, which is the favour, but its yards' and pool shares fall with it, and its claim to the chair weakens under L1595's reasoning. And the Realm's share rises above sixty-five percent by default, with no vote, when the Senate refused the treaty in 1927 over that figure (L1593) and money acts need both chambers (`CR-084` `T-S1`). Tate is given no word on it in `A6`. The draft lists the first half as not done; the second half is new.
- *Fix:* State the expected direction once. Either cap the default (it may move the quota by no more than a stated number of points, and any rise in the Realm's share takes effect on the chambers' vote), or uncouple the yards' and pool shares from the quota and fix them at 35% to 1937. Give Tate the argument.

**S2. Labels in the body contradict the decisions table, and the header is stale.**
- *Passage:* line 12 ("Everything else is PROPOSED"); line 542 (`R-7`, APPROVED, "Body labels that still read PROPOSED on these items are to be read with this row"); lines 89, 98, 106, 153, 197 (the same items marked PROPOSED); line 144 (Victoria's message "(PROPOSED)" under a heading, line 142, that calls her silence APPROVED); line 546 (`P-0a` PROPOSED lists "Wigner's condition as reworded" and `A5`, parts of which `R-7` and `R-8` approve).
- *Problem:* Integration keeps local labels, so the wrong label would enter canon. Line 12 stops at 23:14 and omits the approvals of 00:12, 07:27 and 08:22. The words behind `R-7` are a bulk approval whose three named examples are other CRs' items; that is the author's to confirm item by item if he wishes, but the draft should at least not carry two labels for one item.
- *Fix:* Correct the body labels and line 12; split `P-0a` so that no item appears in both an APPROVED and a PROPOSED row. Quote the 07:31 words for Kaʻiulani ("Yes that works for me", as the siblings do) where line 597 cites them.

**S3. The world's conference sits three weeks without its host, its Foreign minister or its Finance minister.**
- *Passage:* line 107 ("Julian and the three common ministers ... are at Hayama from 12 to 15 June and at sea for nine or ten days each way").
- *Problem:* From about 2 to 25 June the sovereign and all three common ministers are on one cruiser, a fortnight after a coup in which the western squadron's carriers were the danger (L1732). The conference is above all a monetary one and its deadline is 30 June (`CR-084`), five days after they land. King's objection covers Julian's safety and not this. Nobody is named as acting for Julian or as presiding at Thalassia.
- *Fix:* Say who holds the chair at Thalassia and under what authority. Consider leaving the common Finance minister at Thalassia with his deputy at Hayama, since the yen is only "agreed in principle" there; or say why L1651 requires all three.

**S4. Who exchanges the renewal for the Realm, and where Japan's foreign ministry is.**
- *Passage:* line 102 ("He exchanges the renewal's instruments with Kaʻiulani"); line 108.
- *Problem:* The renewal is between the two crowns. Kaʻiulani is the common Foreign minister and signs "for both crowns" in `CR-084`; she cannot be the counterparty to Japan in an instrument between them. Canon also keeps a Japanese foreign ministry beside the common one (L1706, "Shidehara's foreign ministry"; L1720), and the draft gives it no part in May to July. In history Saitō held the portfolio himself until Uchida took it on 6 July (from memory).
- *Fix:* Name the Realm's signatory for instruments between the crowns (`CR-083` already notes the office is OPEN). One sentence on why the finance minister and not the foreign ministry is the cabinet's envoy; Saitō holding the portfolio himself would serve.

**S5. Chiyo knows, and the draft does not say what she did with it.**
- *Passage:* line 105 ("knows before Chichibu comes what Tokyo fears"); line 288 ("she is not surprised").
- *Problem:* Julian "did not expect" the offer and his consort, in private correspondence with Japan's finance minister all winter, did. Either she guessed and kept silent, or she was told, or she prompted it. The three are different books. If she prompted it, the offer is less Japan's own and the manifesto that names her (L1732) has a case; if she only guessed, her part is decoration. It is also a question of who knows what when between husband and wife.
- *Fix:* Choose one and state it. My reading of the draft's intent is that she inferred it and said nothing because the offer had to be Tokyo's; a sentence would do.

**S6. "The navy" is used in three senses.**
- *Passage:* line 98 ("canon as giving Japan no separate navy after 1927"); line 117 ("will be tried by their own service"); line 139 ("loses to the court, the navy and Takahashi"); line 109 (the Navy minister, unnamed and silent).
- *Problem:* If there is no Japanese navy, the naval officers of 15 May are officers of the common Navy, and "their own service" trying them means a Concord court under Julian's appointee trying Japanese officers for killing Japan's premier. That is a gift to the Restoration and is not weighed. "The navy" that beats the army ministry in Tokyo in June has no seat in a Japanese cabinet on this reading. And the man on whom `T-M4` turns has no name, no line and no act at Hayama.
- *Fix:* Say which court tries the naval officers and why. Replace "the navy" in line 139 with whoever speaks (Saitō, as an admiral and premier). Give the Navy minister one thing he does at Hayama, even if his name stays open.

**S7. The rice-riot guard is wider than the claim, and the claim misses the cause.**
- *Passage:* line 424 (the pattern forbids rice riots that "erupt|break out|sweep ... Japan" in any year); line 216 ("preventing physical rice shortage ... so no 1918 Rice Riots from shortage").
- *Problem:* The riots of 1918 came from price, hoarding and the army's buying for Siberia more than from a short crop. Canon has Japan in a Russian war in 1918. A crop 8% larger does not by itself remove that cause, and the pattern would then forbid a riot the storyline might still want.
- *Fix:* Either narrow the pattern to "from shortage" and leave price riots open, or add the mechanism that holds the price in 1918 (the Concord's predecessor compact selling from stock, say) and label it PROPOSED.

**S8. Two industrial terms reach past canon.**
- *Passage:* line 173 (the Nagoya and Ōta line builds "Concord-standard fighters, carrier/patrol aircraft"); line 180 ("a share of the common fleet's and the Concord grid's orders").
- *Problem:* L1600, approved, has Pacifica supply "the common fleet's aircraft"; a Japanese line building carrier aircraft takes that back without a tension. Canon has no Concord grid: the grid is the Realm's (L1560), and 35% of its orders would be a very large gift that Ryan is not shown fighting.
- *Fix:* Say whom the licensed line builds for (the home army's air service and civil transports would keep L1600 whole). Define the second order book or drop "the Concord grid's".

**S9. Edit notes and the older style remain in text that integration will copy.**
- *Passage:* line 89 ("revision 4 tied it to loading the pile ... and the review said so"); line 182 ("would have kept revision 2's form"); lines 363–364 ("as the fourth review found by search", "which revision 4 did not list"); lines 150–164, 188–201 and 207–220 throughout.
- *Problem:* The first group are review labels in the body. Parts `A7`, `B`, `C` and `D` are still in bold run-ins, dashes and stacked parentheses, with phrases such as "zero upfront gold drain", "strictly", "brutal domestic arithmetic" and "without touching a single secret". The draft lists the style as open; it is now the larger part of the file by length.
- *Fix:* Move the revision history out of the body. Rewrite `A7` and Parts B to D in the prose of `A1`–`A6`, with labels in the headings.

**S10. The Emperor gives up a prerogative and has no reason of his own; the best scene is not among the set pieces.**
- *Passage:* line 97 ("The Emperor's stand in May is his own"); line 100; line 104 ("The Emperor's wish is known"); Part F.
- *Problem:* The draft takes care that the court does not propose the surrender, and Hiranuma names what is lost. What Hirohito himself wants, having just faced men who claimed to act for him, is never said, so the central consent is unmotivated. The sharpest conflict in the draft is the cabinet room where Takahashi and Saitō argue and Araki decides not to resign, and Part F has no scene for it.
- *Fix:* One sentence of the Emperor's own reason (the natural one is that a date gives men who act in his name a day to act on). Add the cabinet room to Part F, from Takahashi's side, since canon gives him to the reader.

## Minor

**M1.** *Passage:* line 95 ("Saitō's cabinet confirms it on its second day") against lines 249 and 545 and the author's words ("confirms it on 26 May"). *Problem:* 27 or 26 May. *Fix:* one date.

**M2.** *Passage:* line 99 ("(The deputy is **Mori Kaku** ...)"). *Problem:* the gloss stands before the sentence that mentions a deputy. *Fix:* move it after "a deputy says from the floor".

**M3.** *Passage:* line 144 ("ninety-three or ninety-four"). *Problem:* the registry has Victoria born 1 November 1838, so she is ninety-three in July 1932. *Fix:* "ninety-three", here and in `CR-084`.

**M4.** *Passage:* line 89 ("wins one thing that costs a year"). *Problem:* Tokyo took a year from announcement to ground-breaking (1927 to 1928) and Kansai's site is still OPEN, so May 1933 is no later than the calendar would give anyway. *Fix:* say that the cost is the restart rule and the published shutdowns, not the year.

**M5.** *Passage:* line 208 ("the percentages are this draft's and not `L1885`'s"). *Problem:* `CR-082` states 5%, 8% and 13% itself (its lines 203 and 291). *Fix:* cite them there.

**M6.** *Passage:* line 213 ("succeeding Zusho Hirotake"). *Problem:* Zusho was the college's first head in 1876; I do not think he was Satō's predecessor in 1891. *Fix:* check or cut.

**M7.** *Passage:* line 230 ("three-mile line off Wusong"; Fong "heads the Chinese Maritime Customs"). *Problem:* Wusong lies inside the Yangtze's mouth, far from any three-mile line; the Customs has no authority over telegraph landings. *Fix:* land the cable on a named shore under the Telegraph Administration and give Fong a stated part or none.

**M8.** *Passage:* line 148 ("the bargain ... has hastened the settlement of Ainu land"). *Problem:* the rice programme of 1893 did that, not the bargain of 1932. *Fix:* reword.

**M9.** *Passage:* line 100 (Saionji "says to the Emperor and to the cabinet"). *Problem:* a genrō advises the throne and sees ministers singly. In history he came up to Tokyo in the week after 15 May to recommend the premier. *Fix:* tie his counsel to that errand.

**M10.** *Passage:* line 287 ("days before the May coup"); lines 289–291. *Problem:* sixteen days; the set pieces are numbered 1, 2, 3, 5, 4. *Fix:* "a fortnight before"; renumber.

**M11.** *Passage:* line 607. *Problem:* the May 1932 claims are marked *Hist.* without a fetched source; Mori Kaku and Hiranuma act on the page and have no registry entry or fact change, as the draft itself notes. *Fix:* source and register before integration.

## What holds

- The definition in `A1` of what a refusal in 1937 would have meant removes the old confusion between the union and the trust, and the rest of Part A uses it consistently.
- Meiji practice is respected where it matters: the offer is a cabinet's, the court does not go over its head, the Privy Council advises afterwards on a treaty laid before it, and Araki yields because a resignation would not succeed. His winning the home army in his absence is the draft's best turn.
- Agreement with the siblings: Japan's consent in principle in March through Chichibu with its clause, confirmed only at Hayama (`CR-083` `A10a`, vote of 16 April); 12–15 June everywhere; Takahashi carrying and Chichibu present (`CR-086` `E1`, `E3`); custody outside the common Navy (`CR-086` `C2a`); the oil lever spent in `CR-084` `A2a`; Tate at sixty-six and Ryan at sixty-eight in 1934.
- Travel times hold: the offer cabled about 28 May, five days in cabinet, nine or ten days at sea, the return about 25 June, Takahashi's ten days from 17 July. The announcement of Kansai by radiotelephone fits L1625's rule that the voice link is for the newspapers.
- The arithmetic checks: the yen's 25–33%, the rice percentages and the 0.8% a year, the koku per head.
- Baton Rouge is right for a reason the draft could add: Mobile Bay lies in the rump Confederacy and not in the Gulf Republic (`CR-048`).
- No protected intent is touched, weapon design stays off the page, no exclamation mark appears, and every tension marked decided carries the author's dated words.

## Questions for the author

1. Which way is the audit expected to move the quota, and may a failed review change what the Realm pays without a vote of its chambers (S1)?
2. What did Chiyo know before Chichibu came, and did she keep it from Julian (S5)?
3. Who is the common Navy minister at Hayama, and who holds the seat once it is Japanese by law? You asked for the Foreign minister to be someone who has mattered; Kiyoshi's son is the obvious candidate here, and the choice decides whether the naval party's loss of its squadron has a face.
4. Who signs for the Realm in an instrument between the two crowns, given that the common Foreign minister signs for both (S4)?
5. Does Japan's ratification of 16 July wait on the parity instrument, so that Takahashi holds the Emperor's instruments until the yen is signed (B1)?
