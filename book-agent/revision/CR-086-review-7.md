# CR-086 review 7 (fresh context, final, 24 November 2026)

I reviewed `CR-086.md` revision 9 as a whole, in a fresh context, without reading any earlier review, proposal, prose check, planning note or writer's note. I read the draft in full, `AGENTS.md`, `CR-083-086-calendar.md`, the storyline lines the draft cites or touches (among them L927, L929, L1177, L1324, L1374, L1379, L1534, L1580, L1597, L1602, L1604, L1612, L1614, L1625, L1651, L1672, L1720, L1728, L1732 to L1758), the ledger entries for the court, the Thalassia settlement, the German debt, the dominions' treaty and New Zealand's guarantee, Victoria's registry profile, and the parts of `CR-083`, `CR-084`, `CR-085` and `CR-087` that bear on July and 1 August 1932 (`CR-083` calendar and `A11`; `CR-084` `A1`, `A3`, `B1`, `B5`; `CR-085` `A3` to `A7`). `preflight.py --draft` exits 0 with 0 errors and 11 warnings: two registry warnings (Soong, Pani), five ledger IDs that belong to the siblings, and four matches of the draft's own "moral cost" pattern, all answered in the draft under `## I`. `cr_facts.py preview` finds one canon passage to revise, L1758, which is the clause `T-6` cuts. Historical claims were not checked against sources; where I say a date is right, that is from memory.

## Verdict

**Ready once the items under Blockers are fixed.** There is one blocker, and it is a matter of three phrases: the draft still says in three places that the Emperor's July ratification covers "the Act", against its own statement and the calendar's that it covers the renewal and the two articles and nothing else. The rest of the dates, travel times, signatories and votes agree with the calendar and the siblings, the two rulings are kept, and the ordered account of 1 August works. The should-fix items are short and most of them concern the last page, which deserves them.

## Blockers

**B1. What the Emperor has ratified by 1 August is stated two ways.**
- *Passage:* L346 "on the one Privy Council advice that covers the renewal and the Act"; L367 "the Emperor's ratification beside the Act"; L577 (row F-15) "one Privy Council advice covering the renewal and the Act". Against L336 "ratifies the renewal and the two articles", L352 "Both crowns have ratified the renewal and the two articles. Julian alone has ratified the Concord's late treaties", L578 (row F-16, H), calendar row "About 14 to 16 July" ("Nothing else is in it") and `CR-085` `A3` ("It covers nothing else").
- *Problem:* The Act annexes the late treaties of July, which Japan ratifies only in the autumn. A ratification "of the Act" laid down in the hall would cover them. L346 sits in the paragraph the draft calls "stated once, here", and L367 is the finale entry most likely to be carried into the storyline, so canon would say both things. F-15 and F-16 are also one item carrying two scopes, both APPROVED; the author's answer of 08:22 was to the wider wording and his approval of H at 10:10 narrowed it.
- *Fix:* In all three places write "the renewal and the two articles" (L367: "the Emperor's ratification of the two articles beside the Act"). In F-15 add "narrowed by H at 10:10 to the renewal, the two articles and the countersignature".

## Should fix

**S1. The Emperor ratifies before anything is signed, and the renewal is never signed at all.**
- *Passage:* L336 "About 16 July … the Emperor ratifies the renewal and the two articles"; L351 "Takahashi and an authorized minister of the Realm exchange the renewal's instruments"; L352 "Both crowns have ratified".
- *Problem:* The dates are approved and I do not reargue them. But the Act is signed on 1 August, and neither the draft nor the calendar has a signature of the renewal: canon's L1734 says ministers "sign and exchange its instruments at Thalassia". As written, Japan's ratification is two weeks older than the signature it ratifies, and the renewal passes from a vote to an exchange with no signature between.
- *Fix:* One sentence in `E1`: the Emperor's instruments are signed in advance on the text fixed at Hayama and take effect when they are laid down and exchanged after signature on 1 August. One clause saying who signs the renewal and when (on 1 August, by Takahashi and the Realm's authorized minister, before they exchange). The same clause is needed in `CR-085` `A3`.

**S2. The last image leaves out three facts it depends on.**
- *Passage:* L367 to L368 "It is the day on which, each year since 1913 … This year she leaves it on"; L304 "Victoria does not enter the chamber"; L400.
- *Problem:* (a) Canon puts Thalassia on Kāneʻohe Bay on windward Oʻahu (L1324). Honolulu is a few miles over the Pali, on the same island, and Victoria took the regency's oath in that city on 1 August 1887 (L929). The draft writes "at Honolulu" as if an ocean lay between; a novelist working from it would too. Her absence from the hall is a choice or a matter of age, and it is half of the image. (b) Canon says only that she switched the set off "the first time" (L1177). "This year she leaves it on", and the author's "for the first time since 1913", need the years between. (c) The draft never says that the founder's voice is broadcast on this 1 August or where it falls in the order; the calendar's step 5 does. Nor does it say whether she has listened to her son read the pledge before it.
- *Fix:* State the three facts and still give no reason: she is at Honolulu, an hour's drive from the hall, and is not in it; she has switched the set off each 1 August since 1913 (and say so in the impact note on L1177, which at L391 names the line without saying what changes); the founder's voice follows the promulgation, and that is what she leaves on. None of this breaks `E4`.

**S3. One APPROVED item is also listed PROPOSED, and one heading claims more than its items give.**
- *Passage:* L607 (PROPOSED item 12) "the route of consent with its five votes, and who ratifies on 1 August"; L578 (F-16) approves G and H; L202 heading "C2a … (APPROVED, items 86-4 and 86-5; King's objection is PROPOSED)".
- *Problem:* The five votes and their dates are calendar decision G, and who has ratified on the day is H; both are APPROVED at L578 and PROPOSED at L607. `C2a`'s heading covers the bullets "Where it is written" (the annex is PROPOSED item 12) and "Who decides the pledge" (PROPOSED item 10), which items 86-4 and 86-5 do not mention.
- *Fix:* Cut the two phrases from item 12. Make the `C2a` heading read "custody and the limiting words APPROVED; the annex, who decides and King's objection PROPOSED".

**S4. The one sentence Britain "gets" in Article II has no date, is missing from the ledger, and promises what the Realm cannot deliver.**
- *Passage:* L265 "Any signatory may buy from the same sellers, on the same published terms, as the Realm's own houses"; L300 "Britain gets that sentence and nothing more"; L440 (ledger line for `C-1932-ARTICLE-II`).
- *Problem:* (a) The text is fixed from 15 June, voted about 9 to 11 July and ratified at Tokyo about 16 July. If the Board of Trade wins the sentence in committee in July, the text changed after it was fixed; if the sentence was in Hayama's text, Britain gets an answer and no sentence. The draft does not say which. (b) The ledger line lists four undertakings and omits it. (c) The Concord cannot bind Argentine or Canadian sellers' terms; it can only promise to take no exclusive right.
- *Fix:* Say that the sentence stood in the text of 15 June and that Simon's delegation is pointed to it. Reword to what the Concord can promise ("the Concord and its houses take no exclusive right from any seller"). Add it to the ledger line.

**S5. Article II is believed because of 1919, and none of 1919's sufferers is a signatory.**
- *Passage:* L273 "Belgium in 1919 was an ally and at peace with the Realm, so the article would have covered what was done to Belgium"; L227 "States not at the conference: Belgium … Austria-Hungary".
- *Problem:* The undertakings run "toward every signatory". Belgium, Vienna and Bohemia are not at Thalassia, so the promise not to do it again is made to everyone except the states it was done to, and Belgium was refused a share of the uranium again in 1928–29 (`A2`). The draft does not notice this. A reader will, and so would a French or German delegate.
- *Fix:* The author's choice between two (see Questions). Either one sentence in `D2` that owns it as a fact, without comment, which suits `E4`; or Belgium accedes to the Act in 1932.

**S6. The calendar's row for 1 August omits two signatories the draft seats.**
- *Passage:* L351 "the dominions by their own plenipotentiaries, the Confederacy, the Gulf Republic, Caledonia by Pattullo"; calendar row "1 August", step (3): "then the Union, Germany, China, the dominions, Caledonia, Mexico and the Netherlands".
- *Problem:* The calendar is approved and is part of the candidate text; the draft's order adds the Confederacy and the Gulf Republic (PROPOSED item 12b). The ledger line at L438 and the table in `C3` agree with the draft.
- *Fix:* Add the two to the calendar's step (3), marked PROPOSED, or say at L351 that they sign as PROPOSED additions to the approved order.

## Minor

**M1.** L265, L267, L273, L306 call the undertaking against conditions "the third"; L9, L593 (F-12), L494, L609 and L619 call it "a fourth undertaking". It is listed third in `D1`, in the ledger line and in `CR-085` `A5`. *Fix:* "the undertaking against conditions (third in the text)" in the decision rows.

**M2.** L275 "Japan … signs as a guarantor"; L303 "a guarantee of the Realm"; L440 "with `PAC` as guarantor"; `CR-085` `A5` "co-guarantor". *Fix:* one usage: the Concord undertakes, the Realm guarantees in addition.

**M3.** L352 "the Concord's late treaties of July" has to include the guarantee of Caledonia, which the delegations vote about 9 to 11 July and which is signed on 18 July (`CR-083` L382: ratified by the Emperor in the autumn). *Fix:* "the Concord's other treaties of July, the guarantee of Caledonia among them".

**M4.** L331 "The British committee of six decides"; L366 "The British cabinet decided in the last days of May"; calendar "The British cabinet decides". `CR-084` `B5` has the committee decide on the cabinet's authority. *Fix:* use `CR-084`'s wording in all three.

**M5.** L129 "In canon London is behind them." This is the draft's proposal and not canon. *Fix:* "Here London is behind them (PROPOSED)." The same bullet group at L132 (Belgium's revision) is PROPOSED item 3 under a heading that reads APPROVED; mark the bullet.

**M6.** Notes about the document in body sections A to E: L121 "Canon left three questions for this CR"; L134 "Part C depends on this sentence"; L143 "this CR does not decide it"; L160 "Nothing more is decided here"; L162 "are not invented here"; L199 "is not decided here"; L227 "The sentence at the head of this file therefore says"; L236 "No sentence in this CR says how it ends"; L345 "stated once, here"; L371 "No sentence in this CR, and none added …". None says "the drafter" or "revision", so the rule's letter is kept. *Fix:* move the scope notes to `## Decisions` or the OPEN list; keep `E4` as the instruction it is, but outside the lettered body, so that its sentence naming Kaʻiulani and 1919 cannot be copied into the storyline.

**M7.** L248 "as patiently as she chaired the Danubian commission in 1919 … Article II she does not offer as payment". This keeps the letter of the ruling of 07:37: no sentence says what she knew. It is the draft's closest approach to it, since the Danubian commission is where Vienna and Bohemia negotiated with Hoover (L1379). See Questions.

**M8.** L115 "binds itself never to withhold bread" is wider than the article: "in peace", and L306 "It does not promise the Realm's own crop to anyone". *Fix:* "never to make bread a weapon in peace", or keep it knowingly as the headline.

**M9.** L367 "The Act is promulgated in the Senate's hall": by whom is not said. Canon has Concord acts promulgated at Thalassia (L1651). *Fix:* name Julian.

**M10.** L357 "Alberto J. Pani … signs for Mexico" stands under "The charter", as if he signed a domestic act. *Fix:* "signs the Final Act for Mexico".

**M11.** *Hist.* claims still "from memory": Herriot's government formed 3 June 1932 (L232); the Vienna Final Act of 9 June 1815 (L314); France's gold in 1932 (L172). Both dates are right as far as I know. *Hist.* claims with no entry under `## Sources`: the Halibut Treaty of 1923 and the conference of 1926 (L225); Calles as the power in Mexico in 1932 (L356); Britain importing most of its bread (L300). The Travancore source is a blog, as the draft says. The Ottawa closing date is given as 18 August at L672; I believe it was 20 August.

**M12.** Cross-reference, not this draft's fault: `CR-085` `A3` (its L137) has Simon arrive "about 14 June"; the calendar and `CR-084` `B5` say about 12 June. `CR-085` also sends the Navy minister and the Foreign minister's deputy to Hayama, where the calendar names the Finance minister only.

## What holds

- **Dates and travel.** Every date of April to autumn 1932 in the body, the draft's own table, the set pieces and the decision rows agrees with the calendar, apart from B1. The sea times work from Oʻahu: Simon 29 May to 12 June, Julian 2 to 12 June and back by 25 June, the messenger 8 to 22 July, Takahashi 17 to 27 July, Pattullo 18 to 25 July.
- **Authority.** The Senate's five two-thirds votes are the same five in `D5`, `E1`, the calendar, `CR-083`, `CR-084` `A3` and `CR-085` `A6`, four about 9 to 11 July and one in late July, with the money bill by majority in both chambers. Kaʻiulani signs for both crowns and so does not exchange; the Emperor does not travel; Chichibu does not sign; Parliament approves and the King ratifies.
- **Identities and ages.** Victoria is ninety-three until 1 November; Kaʻiulani fifty-six; Mead seventy-four; Vance has held the second key since 1915 (L1256); the anniversary is the forty-fifth.
- **Knowledge.** Only Hoover in the conference room knows what the fuel is; the foreign delegates cite no figure for the stock; the Realm cannot complain on what the cipher room reads. Weapon design stays off the page.
- **Protected intents.** None is touched.
- **The two rulings.** No sentence says what Kaʻiulani knew in 1919 (but see M7). No sentence says the cost is unresolved or settled; the pattern's four matches are quotations of the clause being cut.
- **Literary.** The losers have names and lose in their own months (King, Szilárd, Mead, Tate, Hahn, Lindemann, the French delegate). Julian acts on the day. The bargain's weak joints are stated by the people who see them: the court that releases the Realm, France on the bench, Tate's ally on a signatory at war. The order of 1 August is clear, and ending on Victoria after the public crescendo is the stronger choice once S2 is done.

## Questions for the author

Needed before approval:
1. **Victoria on 1 August (S2).** Thalassia and Honolulu are on one island. Is she invited and stays home, or too old to cross the Pali, or is only the fact stated? And did she switch the set off every year from 1913 to 1931?
2. **The simile at L248 (M7).** Does "as patiently as she chaired the Danubian commission in 1919", in the sentence before she declines to offer the food order as payment, stay within your ruling, or should the reference to 1919 go?

Can wait for integration:
3. **Belgium (S5).** Own in one sentence that the promise runs to none of 1919's sufferers, or bring Belgium into the Act?
4. **The renewal's signature (S1).** Who signs the renewal for the Realm on 1 August; `CR-085` leaves the minister OPEN.
5. Already deferred by you and still open: Vance's death (L1736) and the second key in August; how France's reservation ends.
