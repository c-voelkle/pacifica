# CR-085 review 7 (fresh context, final, 24 November 2026)

I read `CR-085.md` (revision 11) in full, `AGENTS.md`, `CR-083-086-calendar.md`, the storyline lines the draft cites for Part A and the stations (L1589 to L1604, L1634, L1646, L1651 to L1655, L1695, L1720 to L1736, L1780, L1782, L790, L863), the ledger entry `C-1932-CONCORD-RENEWAL`, the registry entries for Kiyoshi, his son, Chiyo, Takahashi, King and Silas, and the sibling drafts `CR-083`, `CR-084`, `CR-086` and `CR-087` by search only, for dates and cross-references. I read no earlier review, proposal, prose check or planning note. `preflight.py --draft` exits 0 with ten warnings, all of them the persons added under `## Fact changes` who are not yet in the registry. `cr_facts.py preview` reports canon lint clean and no canon passage still stating an old value; its 17 findings are the same unregistered IDs inside the draft. The historical claims were checked against my own knowledge only, not fetched.

## Verdict

**Ready once the items under Blockers are fixed.** The spine holds: the calendar, the three siblings and the draft agree on the coup, the two cabinets, Hayama, the July votes, the Emperor's signature, Takahashi's voyage and the exchange on 1 August, and the approvals quoted cover what is labelled approved, with the exceptions listed. The two blockers are both in the quota and share terms added today: each states one term two ways, and each needs a sentence or two and, for B1, one word from the author.

## Blockers

**B1. The yards' and the pool's 35 per cent: two review dates and two labels.**
- *Passage:* line 587, row R-10: "the yards' and pool's shares fixed at 35 per cent to the first review"; line 588, row R-11: "fixed to the second review, in 1942"; line 211: "a share of the common fleet's orders of 35 per cent, fixed to the second review, in 1942"; line 207: "the share formula and where the ventures refine are OPEN"; line 598, P-2: "The share formula ... remain PROPOSED"; line 646: "the pool's share formula (`B2`)"; line 372, the ledger line: "fleet/grid procurement shares".
- *Problem:* Two APPROVED rows give the same shares different end dates. R-10's wording cannot be right for the pool in any case, since pool entry happens on the day of the first review. The pool's share is a fixed 35 per cent in `A6` and `B2` and an open formula in `B2`'s heading, P-2 and the OPEN list, and its ledger line carries no figure, though `A6` says it is fixed "in its own instrument". The author's words of 11:21, as the draft summarises them, name only the yards' share ("4, fix the yards' share to the second review"), so R-11's APPROVED on the pool's share claims more than is quoted.
- *Fix:* Correct R-10 to refer to R-11 for the date. Decide (author, Q1) whether the pool's share is 35 per cent fixed to 1942 or an open formula; then make `B2`'s heading, line 211, P-2, the OPEN list and the ledger line of `C-1932-HAYAMA-GRADUATION` say the same thing, and label the pool's share PROPOSED unless he says otherwise.

**B2. The quota's default says two things, and Tokyo's knowledge of Tate's cap is not stated.**
- *Passage:* line 146: "failing agreement, the quota moves to the share the audit of output gives ... its cabinet's second condition is met in full only for the quota"; line 177: "It may not raise what the Realm pays above 65 per cent without a vote of the Realm's chambers; unless the chambers vote the increase, the common budget scales down to the capped shares ... it is not in the treaty ... the Diet has nothing to reopen"; line 134: "a review that fails changes nothing but the quota".
- *Problem:* The form is approved and I do not reargue it. As written, though, three things are left contradictory or open. (a) The treaty text of 15 June moves the quota to the audited shares, which sum to 100, so the Realm's share rises; the Realm's law forbids that. The draft does not say whether Tokyo is told of the Senate's condition (voted about 9 to 11 July) before the Privy Council advises "on the quota's default" and the Emperor signs about 16 July. If it is not told, Japan ratifies a default the Realm has already resolved not to honour in full. (b) "Scales down to the capped shares" has two readings with different money: the Realm keeps paying its old amount and Japan pays its audited share of the old budget (Japan then pays more than its audited share of the smaller budget), or the budget shrinks until the Realm's audited share equals its old amount (Japan pays less still). (c) With the cap, a failed review also cuts the common budget, which is mostly the fleet. Line 146's "met in full" and Saitō's "nothing but the quota" are then no longer true, and either partner's negotiators would see that failing a review shrinks the fleet. If the weights follow output, the audited share could fall far below 35 per cent and the cut would be large.
- *Fix:* Add to `A6`: the condition is cabled with the votes, the Privy Council's committee has it before it advises, and Takahashi accepts it as the Realm's internal matter (or objects and is answered). State which reading of "scales down" is meant, in one sentence with a worked example marked MODEL. Amend line 146 ("met for the quota, subject to the Senate's cap") and line 134 or add that the cabinet argued before the cap existed. Note the consequence for the fleet in the cabinet's two figures or in `A6`, and add the cap and the default to the impact note for L1595, L1597 and L1604.

## Should fix

**S1. Kiyoshi's son as Navy minister: kinship, age, timing, countersignature, ID.**
- *Passage:* line 139: "In July, under the new protocol, Julian names his successor: Kiyoshi's son".
- *Problem:* (a) The registry has him as `CT-KURODA-SON`, Elias's grandson; he is Julian's half-nephew, of a line that renounced the Pacifican crown in 1907 "for himself and his descendants". The draft never says so, though it sharpens King's objection and is what Tokyo's army and Tate would say first. (b) If he is a child of Kiyoshi's marriage of 1886 he is at most forty-five, a captain or junior flag officer set over the admirals; the registry leaves his age open, and the draft should say the choice is pointed. (c) "Under the new protocol" in July is before the protocol is in force: the draft's own ledger line has Julian ratify it on 1 August. (d) L1597 requires the Japanese prime minister's countersignature for a common minister; the draft cites the rule at line 122 and does not apply it here. (e) The ID is not used, he is missing from the registry list (line 378) and from the character bible entries to update (line 318), and the impact note for L1732 does not mention the appointment.
- *Fix:* Two sentences in line 139: he is Elias's grandson and the Emperor of Pacifica's nephew, barred from the crown by his father's renunciation, young for the post; Julian names him with Saitō's countersignature under L1597, to take the seat on 1 August when the protocol is in force. Add `CT-KURODA-SON` to the lists.

**S2. The court for the naval officers is stated in one place and left unstated in another.**
- *Passage:* line 147: "the naval officers of 15 May are under arrest and will be tried by their own service"; line 139: "Which court tries the naval officers of 15 May is not stated in this CR"; rows R-10 and OPEN.
- *Problem:* The author approved leaving the venue unstated. "Their own service" states it, and under the draft's own reading (no Japanese navy after 1927) it means the common Navy's courts.
- *Fix:* In line 147 write "are under arrest and will be tried", as canon's "court-martialled with the others" already allows.

**S3. Simon arrives on two dates.**
- *Passage:* line 137: "Simon arrives about 14 June".
- *Problem:* The calendar and `CR-084` (lines 225 and 273) have about 12 June, which fits a sailing about 29 May and fourteen days. The 14th leaves one day for four requests to be cabled, considered and answered before the Council rises. The author's note of 10:45 says "~14 June", so the calendar and the draft follow different words of his.
- *Fix:* Use about 12 June here, or change the calendar and `CR-084`; one date in all three.

**S4. The yen: what authorises the reset, and whether the renewal "carries" it.**
- *Passage:* line 131: "an instrument of the two finance ministries and takes effect on signature"; line 175: "Giannini's allies the yen reset ... in the choice and instruction of the Senate's thirty delegates"; line 363: the renewal "Carries ... `C-1932-ADJUSTABLE-PARITY`"; line 130: the July advice "covers nothing else".
- *Problem:* Gold parity is one of the Concord's "agreed matters" (L1597). The draft does not say what vote lets two finance ministers change it. If the reset in principle is in the text of 15 June, the delegations vote it on 9 to 11 July and Giannini's fight has a vote to lose; if it is not, an executive instrument alters an agreed matter and his fight has no object. The ledger line says the ratified renewal carries the parity agreement, while `A3` says the agreement is outside the July ratification. The same lines call the Navy protocol, the pool protocol and the Board's charter "ratified by the Emperor about 16 July", which the calendar's "nothing else" allows only if they are parts of the renewal.
- *Fix:* One sentence in `A3` or `A7`: the renewal's text of 15 June contains the reset in principle and the three protocols, so the July votes and the July advice cover them; the agreement of 28 or 29 July carries it out and needs no further ratification. Reword the ledger's "Carries". The ledger parties for the agreement should include the Concord, since the common Finance minister signs.

**S5. "The pledge" is used for two different undertakings in `A5`.**
- *Passage:* line 169: "The pledge binds Japan as well as the Realm. Japan may embargo no signatory in peace".
- *Problem:* In line 167, the calendar and `CR-086`, the pledge is the Realm's undertaking in Article I not to use the weapon, which Japan countersigns. Line 169 uses the word for Article II's rule of never denying. Read literally it says the weapon pledge binds Japan, against line 166 ("Japan is therefore not asked to renounce").
- *Fix:* "The rule of never denying binds Japan as it binds the Realm."

**S6. Julian's mandate is silent on what the offer asks, and three objectors lose in days that do not mention their subjects.**
- *Passage:* line 136: "It instructs him to accept no term only with five-year reviews, to concede the Navy seat by law only if he still names the minister, to refuse the alternating executive, and to ask for the home army"; line 142: "the chief constructor, Giannini and Ryan in the cabinet's five days".
- *Problem:* Tokyo's offer names its price (line 134: the yen's reset, the quota's default, the yards' share). The mandate covers none of the three, nor pool entry, so the reader cannot tell who conceded the yards' share, the one new thing Japan gets, or what is left for Julian and Takahashi to settle in the evenings. The draft's own list records this as not done. It is also the draft's main literary weakness: the solution arrives from Tokyo and Julian's choices at Hayama are mostly made before he sails.
- *Fix:* Add the three to the mandate with a limit each (a range for the reset, the default conceded for the quota only, the yards' share conceded below capital ships), and leave one of them for Julian to decide at Hayama against his instructions or at their edge.

**S7. The sufficers' price is dated differently from the calendar.**
- *Passage:* line 173: "they made the two-thirds on a condition met at the conference"; line 136 (the mandate before the Senate's committee).
- *Problem:* Calendar D and `CR-086` `D5` have the price named in the committee in late May, carried to Hayama and adopted there. `A3` describes the committee sitting without the price, and `A6` places its satisfaction at the conference.
- *Fix:* Add the clause to line 136 and write "met at Hayama" in line 173.

**S8. The newest decisions are missing from the impact notes and the draft's own calendar.**
- *Passage:* lines 306, 307, 311; line 287.
- *Problem:* No impact note carries the yards' 35 per cent to 1942 (L1600), the quota's default and the Senate's cap (L1595, L1597, L1604), the Emperor's signature in July and the exchange on 1 August (L1734), Kaʻiulani by cable and Takahashi beside the sittings (L1651), Kiyoshi's son's appointment (L1732), or Wigner's year (L1634). L1593, cited four times in Part A, has no note. The Hayama row of the draft's calendar omits the default, the yards' fixed date and the Navy minister's order.
- *Fix:* Add them; the integrator works from these lists.

**S9. Labels that reach past the quoted words.**
- *Passage:* line 597, P-1: "keeps the 65/35 quota to the first review with an audited-output review (no automatic executive link) | APPROVED"; line 176 (the quota paragraph, unlabelled); line 594, P-0a against row R-10 and the calendar.
- *Problem:* The words of 20:11 and item 85-1 name the Navy seat and the Materials Board, not the quota kept to 1937, the joint audit or the refusal of a link. `A6`'s quota paragraph carries no label. Araki's objection and Chichibu's errand are PROPOSED in P-0a, while the cabinet-room set piece is APPROVED in R-10 and Chichibu's errand "Stands" in the approved calendar. The author's "Yes to all four rows" names R-12 and R-10, which in this draft are now different rows (R-12 is not a decision; R-10 was created by the same message).
- *Fix:* Mark the quota paragraph and that part of P-1 PROPOSED; move Araki's objection and Chichibu's errand out of P-0a; add a note saying which draft's rows the words of 10:45 confirmed.

## Minor

**M1.** *Passage:* lines 299, 301, 603: "Wusong shore-end"; line 265: "(the place is OPEN)". *Problem:* the landing is named in three places and open in two. *Fix:* "near the Yangtze's mouth" throughout.

**M2.** *Passage:* line 431: "The eight `add_person` entries"; line 379; line 378: "Inukai carry no registry IDs". *Problem:* there are ten; the "New" list has seven and omits Inukai, Saitō and Araki; the parenthesis contradicts `CT-INUKAI-TSUYOSHI`. Tate has no ID. *Fix:* correct the count and lists; add Tate on integration.

**M3.** *Passage:* line 288: "(`C-1932-ADJUSTABLE-PARITY`, 20–25% reset, MODEL)". *Problem:* the body and P-3 call the range PROPOSED, an estimate not yet modelled. *Fix:* PROPOSED.

**M4.** *Passage:* line 173: "it is his last fight"; line 177: "his one gain in his last fight". *Problem:* `CR-083` line 251 calls the annuity bill of 12 July his last fight, and `CR-083` `A11` and `CR-084` line 276 have him opposing again in late July. *Fix:* "his last summer in the Senate" in all three.

**M5.** *Passage:* line 169: "loses to the court, the navy and Takahashi". *Problem:* on the draft's own reading there is no Japanese navy or navy minister in the cabinet, and `A3` takes care that the court does not overrule a cabinet. *Fix:* "loses to Saitō and Takahashi, with the Emperor's wish known".

**M6.** *Passage:* line 127: "In June it votes its quota ... and chooses its sixty delegates". *Problem:* the delegates must vote at Thalassia about 9 to 11 July, ten days' sailing away, and Mori's speech presupposes Hayama's result. *Fix:* "in the second half of June; the delegates sail before the month ends".

**M7.** *Passage:* line 147: "In the General Staff's paper"; line 136: "King, for the General Staff". *Problem:* canon has King as the Works' naval ordnance officer with his later career open; the draft gives him a second post without saying so. *Fix:* a clause, PROPOSED.

**M8.** House rules in body sections. Line 210: "as `CR-084` now also says" and line 213 (the Case A alternative) are notes on the drafting; line 123 "a week later than first planned" reads as one. Bare citations without a phrase remain (`L1607` at line 185, `L75` at line 219, `L1869` at line 230, and repeated bare `L1597`, `L1600`, `L1734`). Rows 1893 to 1931 of the calendar, Parts E and G and set pieces 5 to 7 keep the telegraphic style ("+5%", "60+60", "±5%", dashes, "A Hokkaido settler"). No exclamation marks; no weapon design on the page.

**M9.** History still from memory or unsourced. Listed by the draft as from memory: the May 15 incident, Saitō's cabinet of 26 May, Araki as army minister in both cabinets, Hiranuma as vice-president of the Privy Council and his birth year, the Privy Council and the London Naval Treaty in 1930. Listed as unverified: the landing concessions of 1899 and 1900, the yen's fall of about 60 per cent, the Nagoya and Ōta works, Tokyo Dentō, Hokkaido's acreage and *Fukoku*. Marked *Hist.* or stated as history with no source at all: Saionji recommending the premier, the birth years of Inukai, Saitō and Araki, Hayami and Ruttan, Capron's opposition to rice (unmarked), the Honolulu Volcano Observatory. In the calendar: the ministers' sailing for Ottawa on 13 July and the agent-general's office of 1872. None of these looked wrong to me. One looseness: Hokkaido's "development agency" was abolished in 1882; the station of 1893 was the Hokkaido government's.

**M10.** *Passage:* lines 3 and 14. *Problem:* the status lines stop at 10:59 and 10:45 and omit the decisions of 11:21 and row R-11; the 07:31 words on Kaʻiulani are quoted only in the OPEN list. *Fix:* update.

## What holds

- The sequence from 15 May to 1 August agrees with the calendar, `CR-084` and `CR-086` on every date except S3, and the sailing times work: offer on about 28 May, five days in cabinet, ten days to Yokohama, Hayama on 12 to 15 June, home about 25 June; Emperor's signature about 16 July, Takahashi at Thalassia about 27 July.
- Meiji practice is handled correctly: the offer is a cabinet's and not the court's, the cabinet does not vote, Araki can resign and does not, the genrō recommends and persuades, the Privy Council advises after the fact with a recorded dissent, and the Emperor ratifies. Takahashi signing for Japan is consistent with a Japan that has no foreign ministry of its own.
- The named Japanese figures hold their real offices of May to July 1932.
- Who is where in June is consistent in the body, the table and the set pieces: Finance and Navy at Hayama, Kaʻiulani at Thalassia by cable, Chichibu at Thalassia, Hirohito host and silent.
- Hirohito's reason, Chiyo's silence, Araki winning the home army in his absence, King's third point, and the naval party saving the Concord that ends its squadron are the draft's best material. Losers are named on both sides.
- The four protected intents are untouched. `T-R3`'s costs are stated fairly, including that the "new bakufu" charge becomes true in law.
- The arithmetic of `A7` and `D1` is right.

## Questions for the author

Needed before approval:
1. **The pool's share (B1).** Is it 35 per cent fixed to 1942, like the yards', or an open formula? Your words of 11:21 as quoted name only the yards.
2. **Tate's cap (B2).** Is Tokyo told of the Senate's condition before the Emperor signs, and does it accept it? And when the cap bites, does the Realm keep paying its old amount, or does the budget fall further until the Realm's new share equals its old amount?
3. **Simon's arrival (S3).** About 12 June, as the calendar has it, or about 14 June, as your note of 10:45 has it?

Can wait for integration:
4. Whether the draft should say outright that the new Navy minister is Julian's nephew and Elias's grandson, and how old he is (S1).
5. What Julian's mandate allows on the yen, the default and the yards, and which one he decides himself at Hayama (S6).
6. Whether King holds a General Staff post as well as his post at the Works (M7).
