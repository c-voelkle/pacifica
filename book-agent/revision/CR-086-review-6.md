# CR-086 review 6 (fresh context, 24 November 2026)

I reviewed `book-agent/revision/CR-086.md`, revision 7, in full (641 lines), in a fresh context and without any earlier review, planning note or session record. I read `AGENTS.md`; the storyline lines the draft cites for its last year (L929, L1177, L1593, L1597, L1602, L1604, L1612, L1614, L1640, L1646, L1651, L1728, L1732–L1738, L1746–L1758, and L1374 for The Hague); the ledger entries `C-1919-ARBITRATION-COURT` and `C-1932-THALASSIA`; and, in the sibling drafts `CR-083`, `CR-084`, `CR-085` and `CR-087`, only the passages that bear on July and 1 August 1932 (`CR-083` `A6`–`A10a` and its calendar; `CR-084` `A1`, `A3`, `B1`, `B5`; `CR-085` `A3`–`A7` and its calendar). `preflight.py --draft` exits with 0 errors and 11 warnings (two registry IDs to land with the commit, five sibling ledger IDs, four matches of the draft's own forbidden pattern); the draft answers all of them under `## I`. `cr_facts.py preview` finds one passage in canon (L1758, the clause T-6 retires) and eleven matches in the draft itself, all quotations of that clause or the two new IDs. No exclamation marks. I ran nothing else and edited nothing.

## Verdict

**One more revision.** The bargain, its losers and its texts hold, and the approved decisions are followed almost everywhere. Two things still do not fit together: what Japan's instruments of mid-July can cover against what the suite says is ratified on 1 August, and when Article II becomes binding and by whose doing. Both are matters of a few sentences and a dated calendar, not of design.

## Blockers

**B1. What the Emperor's instruments cover, and "the Concord has ratified it".**
*Passage:* line 319, "on the one Privy Council advice that covers the renewal and the Act"; line 323, "The Act is signed, and the Concord has ratified it"; line 315, calendar row for 1 August; line 313, "July | The Concord's delegations vote the component treaties and the texts of the two articles".
*Problem:* Three drafts give three scopes. `CR-085` `A3` (line 102) says the advice of mid-July covers "the renewal, and the two articles of the Final Act in the text settled there", signed by the Emperor about 16 July, Takahashi sailing the next day. `CR-086` says it covers "the Act", and that the Concord has ratified the Act on the day. `CR-084` `A1` (line 102) says its four Concord treaties are "ratified by both crowns on 1 August (`CR-086` `E1`)". But the Act annexes instruments to which Japan is a party and which did not exist on 16 July: the Trilateral Treaty ("late July", `CR-083`), the Caledonian guarantee as signed, the parity agreement Takahashi himself signs after 27 July (`CR-085` `A7`), China's protocol (July). An instrument of ratification cannot cover a treaty not yet signed, and full powers "to confirm any change of wording" do not ratify. There is a second fault of order: canon has the delegations vote and "both crowns then ratify" (L1602, L1734; `CR-085` `A6`), yet nothing in the calendar puts the delegations' vote on the renewal and the articles, or the Senate's striking of the term that must precede it, before about 14 July. As dated, the Emperor ratifies before the delegations have voted. (That he signs in mid-July on one advice is decided, F-15; this finding is about what that one advice can reach and what follows from it.)
*Fix:* State the scope once, here, in `CR-085`'s words: the renewal, the two articles, the countersignature. Give days: the Senate's votes on Article II and on the term, then the delegations' vote on the renewal and the two articles, by about 12–14 July and cabled to Tokyo. Say that the component treaties signed after 16 July are voted by the delegations in the last days of July, ratified by Julian on 1 August and by Japan in the autumn with the others. Change line 323 to what is then true: the Concord has ratified the two articles and the renewal; the annexed instruments signed in late July await Japan's ratification. Correct `CR-084` line 102 to match.

**B2. Article II: when it becomes binding, and whose doing that is.**
*Passage:* line 246, "In July the sufficers make it their condition that the text be voted as law and as a guarantee of the Realm (`D5`). The words are the cabinet's and Mead's; that they bind is the sufficers' doing"; line 285, "loses on the form in July"; line 319, "Both articles are treaties of the Concord"; line 306, "a declaration of the Concord's practice of never denying, which becomes Article II".
*Problem:* The draft never says when the declaration "binding no one" becomes an article of a treaty. If Hayama agrees it in June as an article of the Concord's treaty (line 319; `CR-085` `A5`, where the army ministry objects in June to being bound and the matter is "closed by Japan's own ratified word"), then it binds by the delegations' vote and the crowns' ratification whatever the Senate does, and the sufficers in July add only the Realm's separate guarantee. If instead it is still a declaration until the sufficers' condition in July, then the Emperor's instrument of 16 July, given on the text "settled" at Hayama, ratifies a form that was not yet decided. Either way "that they bind is the sufficers' doing" and Mead "loses on the form in July" cannot both stand with `E1`. This is the hinge of the second half of the ending ("Victoria's school writes the limit into her son's triumph"), so it has to be exact.
*Fix:* Choose one. (a) The sufficers' condition is made in May, with their draft before the Senate's committee, and Julian carries the article form to Hayama because he needs their votes in July; July is where they collect, by having Article II taken first. Or (b) Hayama makes it an article of the Concord, and what the sufficers win in July is the Realm's own guarantee, voted as law, which stands even if the Concord ends or a common minister reads the article narrowly; then line 246 reads "that the Realm stands behind them alone is the sufficers' doing" and Mead loses on the guarantee, not on the form. Align line 306 and `CR-084` `A3`'s fifth condition with the choice.

## Should fix

**S1. A sentence that runs against the author's decision of 07:37.**
*Passage:* line 319, "She chaired the peace during which relief was made a lever, and she signs the act that ends its use"; against line 341 and F-13, "no sentence mentions what she knew in 1919 about the food lever".
*Problem:* The sentence does not use the word "knew", but it puts Kaʻiulani and the lever in one sentence and draws the irony for the reader, which is what the decision keeps off the page. It also overstates: by `D2` the article would not have reached 1919.
*Fix:* Cut the sentence. "Mediator … at The Hague in 1919 … She signs seated, as she presided then" already carries it.

**S2. `D2`'s gloss on 1919 undoes T-8.**
*Passage:* line 252, "It would not have reached 1919 itself, which was an armistice"; "Article II is the promise not to do it again in peace".
*Problem:* T-8 Case B was decided so that the Realm "gives up in law the lever that won it half its ore". The draft then says the article would not have applied to the occasion on which the lever was pulled. And the gloss is wrong for the case that matters: Belgium, from which Shinkolobwe came, was an ally in 1919, at peace with the Realm; only Vienna and Bohemia were on the other side of an armistice. As written, "why it is believed" rests on a forswearing the text does not make.
*Fix:* Say what "in peace" means: between the Concord and that signatory. Then the article would have reached Belgium in 1919 and not Vienna before the treaty was signed, and `D2` can say so in one sentence without pretending more.

**S3. Who signs on 1 August is incomplete, and what Julian signs is unclear.**
*Passage:* line 322, "Who signs on 1 August"; line 338, entry 4.
*Problem:* The list names the Concord, Julian, Britain, the dominions and the Union. It does not say who signs for Germany, France (and where its reservation is entered on the day), China (Soong signed the protocol in July; is he the plenipotentiary?), Mexico (Pani?), Caledonia (Pattullo signs the Trilateral Treaty in `CR-083`; a republic a fortnight old signs its first general act), the Gulf Republic, the Confederacy and the Netherlands. Separately, `CR-084` `B5` has Britain win that "the Realm's pledge stands in the article itself and is not a separate declaration", while here Julian signs "the pledge with the declaration of custody" as if it were a paper of its own, after the Act has been signed.
*Fix:* One line per signatory, names where canon or the siblings have them and "delegate, name OPEN" otherwise. Say that Julian signs the Act itself at the pledge, as Sovereign of Pacifica, and separately the annexed declaration.

**S4. The order of 1 August pays Britain after it has signed, and the day has no last image.**
*Passage:* line 338, "The plenipotentiaries sign the Act … Julian reads the Realm's pledge aloud … Takahashi lays the Emperor's countersignature beside the pledge, which is the condition Britain made … Julian ratifies for his crowns. The Act is promulgated … carried by radio and by television".
*Problem:* As an order of acts it is clear and lawful. As an ending it runs downhill: the high point (Julian, refused by this Senate in February, reading the pledge in its hall) comes second of six, and the account closes on ratification, promulgation and broadcasting arrangements. Simon signs before the pledge is read and before the countersignature Britain made its condition is on the table, so the one visible exchange of the day is out of order. France's reservation, the day's only refusal, has no place in the sequence. The founder's voice, which T-9 Case A offered as the last sound, is mentioned as a fact about the date and not placed. Victoria, whose school wrote Article II, appears only in `G5` as a candidate. No viewpoint is assigned.
*Fix:* Reorder within what is decided: Julian reads the pledge and signs; Takahashi lays the countersignature beside it; then the powers sign, Simon first, France with its reservation, Kaʻiulani last and seated; Julian ratifies; promulgation. Say where the founder's voice falls. Name the closing image as PROPOSED (see the questions) so that the entry ends on a person and not on a transmitter.

**S5. `CR-084` gives a foreigner the Works' figure.**
*Passage:* line 122, "No foreigner in this CR cites a figure for the Works' stock … They argue from an arsenal whose size the Realm will not state"; `CR-084` line 192, Tizard: "one device against fifteen".
*Problem:* Fifteen is the Works' own MODEL figure (L1640) and nothing published gives it; two lines earlier in `CR-084` Tizard "cannot say what Thalassia will have built". The suite contradicts itself on who knows what.
*Fix:* In `CR-084`: "one device against however many Thalassia has". Note the correction here.

**S6. The ore-per-device ratio in the body.**
*Passage:* line 113, "some sixty tonnes of uranium to a device (250 tonnes by 1927 for about four devices, `L1646`; the same line read with `L1640`'s fifteen devices gives a different figure, and the workbook must settle it)".
*Problem:* It is a drafter's working note inside the story's text, it derives a quantity per weapon that canon does not state, and it contradicts itself in the same parenthesis. The house rule keeps weapon design off the page; a per-device material figure is on the wrong side of it.
*Fix:* Keep "enough in time for one device, late and small, and not for a second (quantities OPEN)". Move the ratio to `## H`.

**S7. Labels out of step with the Decisions table.**
*Passage:* line 186, "The vote (PROPOSED)"; line 246, "stand as written (PROPOSED)"; line 232, "charges nothing and pays nothing (PROPOSED)" against F-2, "carried free, nothing paid" APPROVED; line 573, item 12, "that the pledge holds in war"; lines 583 and 595, "the second is PROPOSED", "S14 … PROPOSED"; line 543, "Body labels that still read PROPOSED on these items are to be read with this row".
*Problem:* F-14 asks the reader to correct the body in his head. `C1` and `C5` were relabelled; the rest were not, and one approved term (the fuel carried free) is marked PROPOSED. On F-14 itself: the author's words of 07:27 and 08:22 name the widened bench and the pledge in war; the Senate vote on the pledge, the saving of treaties in force, the definition of "concession" and the footing of non-signatories are covered only by his general phrase "Several things I added … marked PROPOSED".
*Fix:* Relabel the body and the PROPOSED list. In F-14, say which items he named and which rest on the general phrase.

**S8. Meta-text and review labels in Parts A to E.**
*Passage:* line 252, "the draft does not pretend it does"; line 288, "Earlier drafts carried a figure with no source; it is removed"; line 332, "the draft says so"; line 178, "This draft does not decide `L1736`"; line 151, "the workbook's memo row E263 … is to be corrected at the next rebuild"; line 468 (T-9), "which the fourth review pointed out".
*Problem:* The body must read as what happens. These are notes to the author or to a reviewer.
*Fix:* Move them to `## Decisions`, `## H` or the status block; cut the rest.

## Minor

**M1.** *Passage:* line 145, "The Chancellor signs". *Problem:* Germany's delegate signs at Thalassia; the Chancellor decides. *Fix:* "The Chancellor has it signed" or "decides to sign".

**M2.** *Passage:* line 307, "The draft of Article I goes to London with the preliminary accord"; `CR-084` line 187, "Kaʻiulani … hands Simon the draft … He hands it over subject to the Council". *Problem:* Where the handing happens in April is not said (Simon is in London in May for the committee), and the "He" in `CR-084` should be "She". *Fix:* Say where the accord is initialled and by whose hand the draft travels.

**M3.** *Passage:* line 338, "carried by radio and by television to the places where … county halls and cinemas keep viewing rooms"; line 371, "a viewing room in an interior county hall on 1 August". *Problem:* Canon's television in 1932 is three city transmitters on metre waves (L1728); an interior county hall would hear the day by radio and see it later on film. *Fix:* "by radio everywhere, and by television where the three stations reach".

**M4.** *Passage:* line 186, "They lose; the pledge has its two-thirds". *Problem:* "They" has drifted from the provisioners to the government's answer. *Fix:* "The objectors lose".

**M5.** *Passage:* line 204, "after the Statute of Westminster a dominion makes its own treaties"; line 327, "Calles is still the power in Mexico"; line 279, "Britain imports most of its bread"; line 276, chilled beef. *Problem:* Real-world claims without *Hist.* *Fix:* Mark them; the first is truer of the practice since 1923–26 than of the Statute, which Australia and New Zealand had not adopted.

**M6.** *Passage:* lines 119, 219–221, 113: bare `L1640`, `L1643`, `L1614`; line 272, "(line 273 of CR-082.md)". *Problem:* Not in the house form on repeat citation. *Fix:* Add the phrase, or accept repeats explicitly.

**M7.** *Passage:* line 316, "Ratifications by the others: Westminster, the States General". *Problem:* The Netherlands signs only the schedule; what the States General ratifies is the Batavia Compact. *Fix:* Say so. A row for the proclamation of Caledonia (about 18 July, `CR-083`) would also help, since Caledonia signs on 1 August.

**M8.** *Passage:* line 370, "The Act is read in the hall where the regency began forty-five years before". *Problem:* L929 says the regency began "at Thalassia" and names no hall. *Fix:* Mark PROPOSED or say "in the city where".

## What holds

- Agreement with the siblings on everything else I checked: Hayama on 12–15 June; the British decision in the last days of May; the annuity bill by majority about 12 July and the five two-thirds votes with Article II first (`CR-083` `A10`, `CR-084` `A3`, `CR-085` `A6`); the 2, 4 and 11 annuities by reference only; Takahashi, not Chichibu, carrying the instruments; Kaʻiulani as common Foreign minister, fifty-six on the day; Mead seventy-four; Tate sixty-six; Victoria ninety-three. Nothing here conflicts with `CR-083`'s Governor, Proclamation Day or the vote of 16 April.
- The bargain is a bargain. Each signature has a reason and a price, and the losers are named and lose in their own rooms: King, Szilárd, Mead, Hahn, Giannini, Tate's bloc, Berlin's foreign ministry, the Board of Trade.
- The decided tensions are implemented as decided. T-6 is kept in both directions; L1754 stands; the aim at L1672 stays unstated.
- Szilárd's dissent and France's reservation give the triumph its shadow without a narrator's verdict.
- The four protected intents are untouched. Julian is Sovereign throughout. Weapon design stays off the page apart from S6.
- Knowledge is handled with care: who is told the true but partial ground of the third clause, and what the Realm cannot use in a complaint.

## Questions for the author

1. **Article II (B2).** Do the sufficers win the binding article itself before Hayama, or the Realm's own guarantee in July on top of an article the Concord already agreed?
2. **The last image (S4).** Which closes the book: Julian reading the pledge in the hall; Kaʻiulani's seated signature; Victoria at Honolulu leaving the set on while Elias's voice is broadcast; or a view from below? And through whose eyes is the hall seen?
3. **Kaʻiulani and 1919 (S1).** Does "she chaired the peace during which relief was made a lever" fall under your rule of 07:37, as I read it, or do you want that much said?
4. **"In peace" (S2).** Should Article II's third undertaking have reached Belgium in 1919? If yes, the text needs the definition; if no, `D2` should stop saying the Realm forswears what it did.
5. **Vance (L1736).** Still undecided, and it settles who holds the second key ten weeks before the Act and whether Julian reads the pledge days or weeks after burying him. It need not be decided in this CR, but the last pages depend on it.
