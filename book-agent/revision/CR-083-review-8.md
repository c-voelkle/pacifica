# CR-083 review 8 (fresh context, final, 24 November 2026)

I reviewed `CR-083.md`, revision 15, in full, as a fresh-context reviewer with no earlier review, proposal, planning note or session record before me. I read `AGENTS.md`; `CR-083-086-calendar.md` (approved decisions A to K, with the changes of 10:45 and 11:21); the storyline lines the draft cites (L705, L708, L892, L927, L1020, L1091, L1093, L1100, L1137, L1139, L1142, L1234, L1265, L1385, L1554, L1593, L1597, L1604, L1614, L1617, L1651, L1672, L1687 to L1695, L1734, L1738, L1746 to L1754, L1881) and a search of the storyline for other passages on Canada and British Columbia; the ledger entries the draft amends; the registry for the IDs it names; and the passages of `CR-084`, `CR-085`, `CR-086` and `CR-087` that touch Caledonia, the annuities, the Senate's votes, the guarantee, Great Bear, Tate and the Waterton line. `preflight.py --draft` exits with 0 errors and 7 warnings, all of them the seven new people not yet in `character_registry.json` (to land in the same commit). `cr_facts.py preview` lists 11 passages in canon that would still state an old value (AGENTS.md line 116; storyline lines 91, 708, 1137, 1142, 1554); every one is in the draft's impact notes. Its findings inside the draft are the draft's own quotations of the old wording and the unregistered IDs.

## Verdict

**Ready once the items under Blockers are fixed.** There is one blocker, and it is a matter of two sentences: what Japan's clause contains and what Pattullo says about it contradict each other, and `A8` and `A10a` give the clause two different scopes. Everything else agrees with the calendar and the sibling drafts on dates, figures and votes; the should-fix items are small and none needs a new decision except the two questions marked "before approval" below.

## Blockers

**B1. Japan's clause is stated two ways, and Pattullo's answer is false on the draft's own text.**
- *Passage:* line 264, "Japanese subjects resident on Proclamation Day become Caledonian citizens with every other resident unless they decline within two years (`A8`), and those who decline keep the floors and a right of entry and residence reciprocal with Caledonians' in Japan … Pattullo answers that it covers residence and not the vote, which goes with citizenship"; line 217, "Realm citizens have entry and residence by the Association Treaty, and Japanese subjects by the Concord's guarantee".
- *Problem:* (a) As written, the condition Japan gets makes resident Japanese subjects citizens, and citizens vote; so the clause does cover the vote, and Pattullo's hustings answer is untrue. The author approved the citizenship rule at 10:45 because it "makes Pattullo's hustings answer accurate"; the wording here undoes that. (b) Line 264 gives entry and residence to the residents who decline citizenship. Line 217 gives it to Japanese subjects as such, which is an open door for future entry and a much larger thing for Vancouver to split over. The dominion votes on this text on 16 April; canon cannot carry both.
- *Fix:* Put citizenship where line 217 already has it, in the founding articles, as Caledonia's own rule for every resident. Let Japan's clause in the guarantee say only what Japan asked for: that its subjects who stay Japanese keep the floors and their residence, and a stated right of entry. Then Pattullo's answer is true. Choose one scope for entry (residents of Proclamation Day and their families, or all Japanese subjects under Caledonia's ordinary law, as `A10` has it for Realm citizens) and state it identically at lines 217 and 264. The scope is the author's (Q1).

## Should fix

**S1. Julian's reason for obeying in February uses knowledge he does not yet have.**
- *Passage:* line 184, "in July he will need two-thirds of this Senate five times (`CR-086` `E1`). A sovereign who took the coast against its vote in February would not get them."
- *Problem:* Of the five votes, Article II's binding form is won in late May (calendar, D), the striking of the term follows Japan's offer of 26 May, and the Association Treaty exists only because of this refusal. In February Julian can foresee the renewal of 1932 and the conference's treaties, not five votes. As written the motive is the narrator's hindsight.
- *Fix:* Give him what he knows in February: the Concord's renewal falls due this year on the Senate's conditions of 1928 (L1604), and the conference's treaties will need the Senate. Keep "five times" as the narrator's later count, in a separate sentence.

**S2. The countersigned full powers cannot be where the draft puts them, and cannot recite a vote not yet taken.**
- *Passage:* line 263, "those full powers carry Tokyo's mandate in so many words: the Diet's sixty delegates voted the guarantee with the Realm's sixty about 9 to 11 July, and Saitō's cabinet countersigned the full powers before the deputy sailed"; line 202, "the envoy sailed before the Senate's vote and signs on cabled authority".
- *Problem:* Thalassia to Victoria is about six days and Tokyo to Thalassia about ten (calendar). A paper countersigned in Tokyo must leave by about 1 July to sail from Thalassia by 12 July, so it predates the delegations' vote and cannot name it. The draft does not say where or when the cabinet signs, or whether the deputy and the Realm's envoy are one person. `CR-084` line 118 also says there is "no prime-ministerial countersignature on treaties"; a reader will ask how this differs.
- *Fix:* One sentence: the full powers are drawn at Hayama in mid-June, when the Council confirms the guarantee, and countersigned there for the cabinet by its envoy Takahashi (or by cable from Tokyo to Chichibu at Thalassia); the deputy sails about 10 July; the delegations' vote reaches him by cable, as the Senate's reaches the envoy. Say that the countersignature is on the full powers and not on the treaty.

**S3. The Island's nationality option and automatic citizenship are not reconciled.**
- *Passage:* line 208, "protected Crown pensions plus a two-year British nationality opt-in"; line 217, "Every such resident becomes a citizen of the Republic on that day unless he declines within two years … The vote goes with citizenship."
- *Problem:* The draft does not say whether a resident who opts to keep British nationality thereby declines Caledonian citizenship. If he does, the loyalist Island gives up its vote in the Republic's first elections, which changes what the Island's bargain is worth and what the petty officer of set piece 5 is doing. If he does not, the Republic begins with dual nationals, and Britain's side of that belongs in the April accord.
- *Fix:* One sentence in `A7` or `A8` either way (Q2).

**S4. One item, two labels.**
- *Passage:* line 156, "(PROPOSED addition to an approved compact:) … the Columbia compact is also signed with the nations of the upper river", against row R-12, line 577, which lists "the upper-river signature" as APPROVED. Line 196, "Tolmie's caucus splits and he resigns rather than break with the King (PROPOSED)", against line 173 and row N-4, where the resignation is approved. Line 643, "Giannini losing on the wheat contract" under PROPOSED, against line 274, "(APPROVED, `R-12`)".
- *Fix:* Line 156 to APPROVED (`R-12`). Line 196: move the label to the caucus split and the date. Line 643: drop Giannini from the PROPOSED list or say what of him is still proposed.

**S5. What the sufficers win in March takes the guarantee out of the Senate's reach, and the draft does not notice.**
- *Passage:* line 250, "The guarantee is taken out of the treaty and written as the Concord's, external only … They do not raise it again in July"; line 276, where Tate says of the Trilateral Treaty that it "was moved out of the Senate's reach on purpose".
- *Problem:* Under `CR-084` `T-S1` a guarantee of the Realm takes two-thirds of the Senate. The sufficers' objection ends with a defence guarantee that the Senate never votes, kept by a navy the Realm pays 65 per cent of. That is the same move Tate denounces four paragraphs later, and here the Senate's own bloc asks for it and is content. As it stands the objection has no cost and no loser.
- *Fix:* A sentence of motive and price: the sufficers accept the Concord's form because the Realm's sixty delegates are chosen half by each chamber (L1604) and because "external only" is in the text; and someone (Tate is at hand) says in March what he says in July. Or let the sufficers demand, and get, that the Senate be told the guarantee's text before the delegations vote.

**S6. Process notes in body sections A to E.**
- *Passage:* line 250, "(moved from May; author, 24 November 2026, 08:58)"; line 247, "This settles for this draft the question `L1881` lists as open"; line 159, "(PROPOSED; the Nisga'a petition of 1913 came from the Nass, and its signers would not sign an Nlaka'pamux compact)", which answers a reviewer and not the reader.
- *Fix:* Line 250: "The sufficers in March (author, 24 November 2026, 08:58)". Line 247: "This settles the question `L1881` lists as open". Line 159: keep "PROPOSED" and move the reason to `## Decisions`.

**S7. Historical claims marked *Hist.* without a source, or still from memory.**
- *From memory, as the draft says:* the Governor as channel to London in New Zealand and Newfoundland (line 155); the Imperial Conference of 1930 on who advises the King on a Governor's appointment (line 174); British Columbia's agent-general in London from 1872 (line 199); the pools' growers giving up their five-year delivery contracts in 1931 (line 269); the Bamfield cable's owner in 1930 (line 209); the Squamish, Musqueam and Tsleil-Waututh at Burrard Inlet and the Tsimshian at Prince Rupert (line 236); Dane-zaa, Fort Nelson Dene and Secwépemc signing places (line 242).
- *Marked* Hist. *or stated as history with nothing under `## Sources`:* the conference of 1926 on the Governor's position (line 174); Lang's dismissal on 13 May 1932 (line 180); Chamberlain at the Exchequer from 5 November 1931 and the National Government of 24 August 1931 (lines 171, 194); the Abnormal Importations Act and the Import Duties Act (line 167); the Ottawa conference opening on 21 July 1932 (line 202); the railway to Prince Rupert chartered in 1903 and failing in 1919 (line 169); Treaty 8 in 1899–1900, the petition of 1909 and the Spences Bridge meeting of 1911 (line 159); the Kitsilano and Capilano reserve lands (line 234); Canada's wheat exports of 1931–32, on which "about 18%" rests (line 272); Australia's trade (line 172).
- *Fix:* Add a "from memory, to source before integration" list under `## Sources` naming these, so the label is honest in one place. None of them looked wrong to me; the dates of Lang, Chamberlain, the Statute and the Ottawa conference are as I know them.

## Minor

**M1.** *Passage:* line 138, "The Yukon is settled here (N-8, approved)". *Problem:* N-8 in `## Decisions` is now the bond refunding; the Yukon was N-8 in an older numbering (the author's words of 15:43, "5 [N-8, Yukon at the fork]"). *Fix:* cite the author's date in place of the number, or N-1, which covers it.

**M2.** *Passage:* line 234, "They do not sign in fourteen weeks what they have asked for since 1909"; line 401, "between March and the end of June". *Problem:* Proclamation moved to about 18 July; March to mid-July is about eighteen weeks. Line 206's "seven weeks" for late January to 25 March is nearer eight. *Fix:* "in one spring", or recount.

**M3.** *Passage:* line 319, "the second line through the Fraser canyon is built under the dominion's charter (see `A3`), not on running rights". *Problem:* `A3` says nothing of a second line. L1554 has the Canadian Northern's blasting at Hells Gate in 1913–14, so the impact note is needed, but its pointer leads nowhere. *Fix:* add a clause to `A3`, or drop "(see `A3`)" and mark the point PROPOSED.

**M4.** *Passage:* line 259, the guarantee's row, "both crowns and the Concord's delegations". *Problem:* Caledonia is a party (ledger line 382 has `CLD`) and the clause on residents binds it, but the row names no Caledonian signer or ratifier, and line 263 names only the Concord's deputy. *Fix:* add "Pattullo; Caledonia's legislature".

**M5.** *Passage:* line 249, "The treaty is signed for the Realm by the minister Julian names (office OPEN)"; line 202, "Pattullo and the Realm's envoy sign". *Fix:* say the envoy signs under that minister's full powers.

**M6.** *Passage:* line 388, the list of new people. *Problem:* `CT-HARLAN-TATE` is under `## Fact changes` (line 422) and not in this list; the registry has no Tate under any ID. The registry count in `AGENTS.md` (362) will change by seven and is not in the impact notes. *Fix:* add both.

**M7.** *Passage:* line 298, "Lines 36, 281, 302, 316, 358, and 369 of `CR-082.md`". *Problem:* lines 18, 314, 320, 370, 496 and 500 of that file also name the northern water or the Liard (77 and 81 are the author's quoted words and stay). The quotation of line 281 in `T9` is exact. *Fix:* extend the list or say "every mention outside the author's quoted words".

**M8.** *Passage:* line 142, "in the year of the *Chicora* crisis and the Treaty of Washington". *Problem:* the *Chicora* is May 1870 (L705) and the treaty May 1871 (L708). *Fix:* "between the *Chicora* and the Treaty of Washington".

**M9.** *Passage:* line 23, "Next: the third fresh-context review"; lines 595 to 600, where the list for revision 12 still calls PROPOSED and places in `A6` what row R-12 and `A10` now carry as APPROVED. *Fix:* correct line 23; add "since APPROVED, `R-12`" to the old list or cut it.

**M10.** *Passage:* line 161, "The colony strips the vote from … South Asian residents in 1907". *Problem:* from 1907 it is the dominion. Also "Victoria" still stands for the dominion's government in `A4`, `A5` and `A6` (the draft's own open item S11); in a book whose Regent is Victoria this must not reach the storyline. *Fix:* on integration.

**M11.** *Passage:* line 207 and line 199, "the Association terms as initialled, Japan's clause among them". *Problem:* Japan's clause is in the guarantee (line 264), not in the Association Treaty. *Fix:* "the Association terms and the guarantee as initialled".

**M12.** *Passage:* row N-4, line 586. *Problem:* the quoted words (item 83-3) give Tolmie's resignation; "Pattullo leads the Convention and the Republic" rests on "I confirm those 2 points [… Pattullo vs. Tolmie in CR-083]", which the row does not quote. The draft lists this itself as unaddressed (line 615). *Fix:* quote those words in the row.

## What holds

- **Dates and sequence.** The draft's calendar, `A6` to `A10a`, the ledger lines and the set pieces agree with one another and with `CR-083-086-calendar.md`: terms published about 25 March, vote on 16 April, accord in the last days of April with the High Commissioner initialling, request and consent in May, Hayama on 12 to 15 June, the Act in the last week of June, the Senate's consent about 9 to 11 July, the bill about 12 July, the commencement order about 15 July, Proclamation about 18 July, Pattullo at Thalassia about 25 July, the Trilateral Treaty in the last days of July, the Final Act on 1 August, the Emperor's ratification of the guarantee in the autumn. Sailing times fit, with the margins the calendar admits.
- **The siblings.** `CR-084` gives the same two annuities (1932–33 and 1933–34), the same $49m and $93m, the same split of 2, 11 and 4, the same commencement-order device and the `IIC` ID; `CR-085` and `CR-086` give the same votes on the same days, five two-thirds votes with the Association Treaty among the first four, Tate at sixty-six, Pattullo signing on 1 August; `CR-087` gives the Waterton line the map paragraph relies on.
- **Authority.** The Governor after 1926 and 1930 is handled correctly: he acts on his ministers' advice, sets conditions only at the commission, refuses the dissolution because the ministry has the House, declines to reserve, forwards the petition, and the comparison with Lang is the right one. The Island's three formal requests and the press's call are counted as the author worded them at 10:45. Request and consent precede the Act. Parliament approves and the Crown ratifies. The Senate consents before the other party exists, on an initialled text, and the draft says why.
- **Canon.** L892 and L1695 are kept to the letter (private syndicates; the board's second investment; "beans and rice" untouched). The third refusal is rightly counted from L1593 and L1100. The four protected intents are untouched. Ages are right: Victoria ninety-three, Kaʻiulani fifty-six, Tate sixty-six, Buchan fifty-six.
- **Approvals.** Every APPROVED label I checked has dated words quoted under `## The author's request`, apart from M12; R-17 and R-19 say plainly which part is the drafter's choice between two forms the author allowed.
- **Literary effect.** Julian is asked, wants to say yes and is stopped by a body with its own reasons; Tolmie, the Island, Bennett and Buchan each lose something specific and none is a fool; the nations hold a real card and one of them refuses; the foreclosure charge is left standing against Pacifica. Buchan is the draft's best addition. The weak places are the sufficers' costless win (S5) and Giannini and Tate losing every time, which the draft lists as open.
- **House rules.** No exclamation marks. Figures carry MODEL. Citations are in the required form and preflight confirms each phrase.

## Questions for the author

**Needed before approval**

- **Q1 (for B1).** How far does entry for Japanese subjects go: only those resident on Proclamation Day (and their families), or any Japanese subject under Caledonia's ordinary law, as Realm citizens have it? The second is what line 217 says now, and it is the larger concession for a dominion voting in April 1932.
- **Q2 (for S3).** Does a resident who keeps British nationality under the Island's option stay a citizen of the Republic and keep his vote, or does opting for Britain mean declining?

**Can wait for integration**

- **Q3.** Whether the sufficers' win in March should cost them or anyone something (S5).
- **Q4.** Whether February to July is a believable pace for a constitution, a vote, two compacts, an Act and a Proclamation; the dates are now consistent, and the draft leaves the judgment to you.
- **Q5.** The office that signs the Association Treaty for the Realm; the vote percentages; the Great Bear royalty's rate; the band's width.
