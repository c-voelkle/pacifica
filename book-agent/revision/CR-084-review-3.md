Fresh-context review of CR-084, revision 6, 23 November 2026. The reviewer read the draft, AGENTS.md and current canon, and not the writer's notes or earlier reviews.

Tools run first: `lint_canon.py --only` reports 19 findings, all of them the nine new character IDs not yet in the registry; `preflight.py --draft` exits with 0 errors and 9 warnings (the same nine IDs); `cr_facts.py preview --tensions` reports that no canon tension carries fact changes. Nothing below repeats those. Line numbers of the draft are written "draft L…"; storyline lines are written "L…".

## Verdict

One more revision. The new sections are the best material in the draft: the oil trust heard and overruled (`A2a`), Brooke's refusal, and a British committee in which the man who was wrong in 1924 makes the right argument and loses. But `B5` does not yet say where the British ministers are when they decide, the "one schedule, voted once" cannot be squared with the three dates on which Westminster acts, the 10° S line sits in a treaty to which Japan is not a party, and the Decisions table marks as APPROVED a good deal that the author's quoted words do not cover. None of this needs a redesign; it needs the four drafts to be made to agree and the labels to be made honest.

## Blockers

**B1. The cabinet decides "in London" in the week the conference is sitting on Oʻahu.**
*Passage:* `B5`, draft L136 ("In the last week of June 1932, before the moratorium runs out on the 30th, the cabinet decides to sign"); calendar, draft L182–183.
*Problem:* Canon puts the conference "At the Thalassia Conference in June–July 1932" (L1746) and Thalassia "on Kāneʻohe Bay on windward Oʻahu" (L1324). London to Oʻahu is about two weeks in 1932. The draft never says who leads Britain's delegation, whether MacDonald, Chamberlain and Simon (three of the committee of six, and the men who "extract" the reverter in `B1`) are in London or at the table, or how the decision and the "three things" reach Thalassia. If they are sent by cable they cross the Pacific, and canon says "the cipher room reads British official traffic in China and the Pacific" (L1534); CR-086 `C5` says the cabinet's minute relies on exactly that. Thalassia would then know Britain's reserve price before it answers "one and a half" of three requests, and the scene changes. Separately, the 30 June deadline is only a deadline if an instalment falls due after it; the draft gives no due date for the annuity, and the ledger entry says of the moratorium "Duration, debtors covered and restructured terms not stated."
*Fix:* Decide and state: (a) who goes to Thalassia and who stays; (b) whether the decision is taken before the delegation sails (late May, which fits "MacDonald's committee hears Tizard and Lindemann" in May) with the three requests carried as instructions, or cabled; (c) if cabled, whether Thalassia reads it, and who in Julian's cabinet knows; (d) the due date of the first annuity after the moratorium, so that 30 June bites.

**B2. "One schedule, voted once" contradicts the draft's own dates and the sibling drafts.**
*Passage:* `B1`, draft L90 ("one tranche of one schedule, voted once in each of the Realm's chambers and once at Westminster"); `A2` gain 4, draft L62; `B5` draft L131 and L139; `A3`.
*Problem:* Three inconsistencies. First, Westminster acts three times: CR-083 has the "Recognition / Severance Act (May–June 1932)" "paired with this CR's share"; this draft has a May debate on the retrenchment; and `B5` has Britain's share "cancelled on ratification at Westminster", which cannot precede the Final Act of 1 August (CR-086). That is not one vote. Second, the Realm's vote: `A3` dates it "July 1932, following signing", before the article that a third of the tranche pays for is signed. Third, the draft does not say which annuities are cancelled. `A2` calls them "the least collectable tail of the debt" (the 1970s and 1980s, since the ledger runs `C-1923-UK-FUNDING` to 1985), while Chamberlain in `B5` calls the tranche "money Britain receives now". Both cannot be true, and the believability of the British decision turns on which is. The sufficers' position on this one bill also differs in three drafts (see "The four drafts together").
*Fix:* Keep one schedule in the ledger, but give it three dated tranches, each with its own trigger (Severance Act; ratification of `C-1932-UK-RETRENCHMENT`; ratification of the Final Act), and say whether the cancelled annuities are the nearest or the last. If they are the last, Chamberlain needs a different argument (the suspended instalment written off, and a smaller book against which sterling can be stabilised). If the nearest, strike "least collectable tail".

**B3. The ore argument in `B5` contradicts CR-086 Part A and the author's decision on Australia and New Zealand.**
*Passage:* `B5`, draft L127 ("The ore is under contract elsewhere"), L129 ("ore he does not have"), L141 ("this closes the last imperial source of ore").
*Problem:* CR-086 `A2` says "Cornwall alone holds some tens of tonnes, which in time would feed a first British device", that "London is behind" the British buyers of Urgeiriça in 1929, and that at Radium Hill "The Commonwealth closes the door" to the Works. So Britain has ore in Cornwall, a mine in Portugal and a dominion source in South Australia. Great Bear is not the last imperial source. CR-086 `C3` and its Decisions table (F-4b, "APPROVED (author, 20:11)") have Australia and New Zealand sign Article I on Canada's footing; this draft's "The dominions" paragraph names only Canada and its request section omits the 20:11 answer.
*Fix:* Let Tizard say what CR-086 says: enough ore for one late, small device and no more; that is a better line than "none". Rewrite the dominions paragraph for Canada, Australia and New Zealand, and say what South Africa does or mark it OPEN.

**B4. The 10° S line is placed in a treaty that does not bind Japan or the common Navy.**
*Passage:* `C3`, draft L166–171; `C2.3`, draft L163 ("Japan is bound in the south only by … the 10° S non-basing line"); M-4.
*Problem:* The draft keeps `C-1932-ANZ-DEFENSE` "bilateral (`ANZ`, `PAC`)", as the ledger has it (`parties = ["ANZ", "PAC"]`). Canon gives "Foreign Affairs, the common Navy and their Finance" to the Concord (L1597). A treaty of the Realm cannot bind Japan or a navy that is not the Realm's. Only the non-fortification clause is said to be "mirrored in `C-1932-BATAVIA-COMPACT`"; the line itself is mirrored nowhere, yet CR-085 `A4` lists "any base south of 10° S (`CR-084`)" among what Japan is refused.
*Fix:* Put the line in a Concord instrument (a protocol to the retrenchment treaty or to the Compact, signed by `JP`), or make Japan accede to that article of the ANZ treaty, and say how that sits with Australia and New Zealand "refusing the racial equality clause" (L1752). While doing so, test the geography (S9).

**B5. APPROVED and "Decided" labels reach further than the author's quoted words.**
*Passage:* Decisions table M-1 to M-4; `T-NF1`; `T-U1`; draft L8.
*Problem:* `docs/authority-and-scope.md` R1: "An overview or an approved direction does not approve every detail beneath it." Cases:
- M-3 is marked APPROVED with the 50-year term, "Japanese company/consular guards inside the fences", the KPM and New Guinea lines, the sugar clause and the bond. The quoted words are "I think B makes sense" and "I recommend sticking to the leased ports approach unless this torpedoes the whole new design." The bracketed gloss on the first is the drafter's. Guards, term and bond are not in the author's words. (I cannot see the text of "rung B" he was answering; if it named guards and a term, quote it.)
- M-4 marks the 10° S to 165° W line and the non-fortification clause APPROVED; no quoted sentence mentions either, and the drafter's own list (item 5) calls the non-fortification outcome PROPOSED. The same item is labelled twice.
- M-1 marks APPROVED the reverter, the cap east of Ceylon, the Nanjing reservation, the Labuan roll and the Fanning buyout; the drafter's list (item 2) calls the roll and the buyout PROPOSED.
- M-2 marks APPROVED a Cortes vote to enlarge the Mariveles dry dock; the author confirmed "voluntary commercial yard work at Mariveles" (in the drafter's bracket). Palau as a naval anchor is approved in the table and appears nowhere in Parts A to C.
- `T-NF1` is "Decided: Case B (author, 22–23 November 2026)". The author's list of tensions reads "T-K1 … T-L1 … T-O1 … T-U1 … T-B1"; `T-NF1` is not in it. It is an inference from "B makes sense".
- `T-U1`: the author wrote "Case B, but split it." Nothing in the draft says what was split or shows the split.
- Two approvals are conditional: quick question 1 "insofar as nothing of importance (according to the strategic plan shape above) is lost to Pacifica", and the leased ports "unless this torpedoes the whole new design". The draft does not report back on either condition.
*Fix:* Reduce each APPROVED row to what the words cover, move the rest to the PROPOSED list, mark `T-NF1` "Recommended", answer "but split it", and add two sentences answering the two conditions.

## Should fix

**S1. `A2`'s year for the margin departs from canon and is not listed as a tension.** Draft L57: "from about 1941–43 when the Realm's home margin closes". L1672: "the margin closes about 1940–42"; the table of 1930 puts the crossing at 1938.

**S2. The straits are justified by bread that mostly does not pass through them.** `A2` and `A2a.1` rest the four straits on "the Mekong, Burmese, and Australian grain sellers". Mekong rice reaches the Realm by the South China Sea and the Philippines, through none of the four; eastern Australia's wheat crosses the open Pacific. CR-082 calls India and Burma "Sellers of the century, not of 1932" and defers them, and L1672 has the Mekong "last". What does pass Malacca on its way to the Realm is the oil of L1620 ("the sheikhdoms and Kirkuk are the 1930s' oil bought at 1920s prices"), rubber and tin. The minute should say oil first and bread later. The figure promised "from `population/provisioning.py`" cannot come from it: the script has no routes or straits.

**S3. `A1` cites L927 for a rule it does not state.** L927 describes the Senate's composition. Canon's only treaty votes are Senate votes: "The Senate votes the rescue loan but refuses the treaty" (L1593) and "two-thirds Senate consent" (L1604). The draft gives the Chamber of Deputies a vote on a guarantee and lets the bills "pass both chambers narrowly". If consent to a treaty of the Realm needs two-thirds, "narrowly" is not available; if it does not, the draft is making constitutional law and should say so as a tension. CR-086 `D5` makes the same assumption, so one decision serves both.

**S4. The sufficers' "Chile precedent" is not a precedent.** `A3` and set piece 1 cite L1560, which says "The sufficers would write the loan down as the price of the Strait; the provisioners convert it". The write-down was their losing proposal. That makes a better speech: in 1932 they win the argument they lost in the 1920s.

**S5. The third clause tells London something, and the draft says it tells nothing.** `B5`, draft L126: "The paper discloses nothing about what the Works has made or can make." The same paper asks for "all fuel that has been through a pile". Canon: "By 1932 the element such piles breed is an idea in Europe, with no production pile, no chemistry and no weapon route" (L1614), and that chemistry is in the part of the record sealed to 1947 (L1612). The author accepted the tip-off in CR-086 (19:32: "even if the article's specifications tipped them off"). So strike the sentence, and let Tizard, the "reader of other people's tables" (character bible), be the one who reads the clause aloud and says what it confirms. Lindemann's argument already depends on it.

**S6. Britain's "pile work".** Draft L127: "its pile work waits on heavy water". Canon speaks of "A European heavy-water pile, aimed at power" (L1614) and "Europe's first pile" (L1643), and says of Britain only that it "begins to copy the halls after 1927" (L1640); "Germany comes later, starting from power reactors". A British pile programme, and Tizard "asked to turn the pile work to power", is new and unlisted. Either list it or give Britain only the separating plant. "Fully committed from 1928" is the Works' MODEL assumption in L1614, not a stated fact about Britain; the draft and CR-086 both treat it as one, and both date the reckoning to 1928, which canon does not.

**S7. Nobody in the committee proposes to stop paying.** A cabinet off gold, owing gold dollars, would hear the word default before it heard anything else; in our history Britain made token payments in 1933 and none after 1934 (from memory). The draft's Britain pays 33 to 38 more annuities and gives up Sembawang, Fanning, Labuan and the weapon for a third of the book. That can be believed in this world (the gold credit of L1566 that "can be withdrawn", the sterling the champions hold, the sheet, the column of water), but someone has to say it and be answered. Eyres-Monsell or Lindemann is the natural voice; Hoare's "the offer will not improve" is the natural answer.

**S8. Baldwin briefing Churchill.** Draft L135 has Baldwin tell Churchill "on Privy Council terms". Lindemann is "Churchill's friend from 1921" (character bible), and in 1926 Churchill's Treasury declined the factory "on Lindemann's advice" (L1578). Churchill would have the whole of it from Lindemann the same evening, and he is the minister whose refusal cost Britain six years. That is the scene: the two men who were wrong together in 1926. `B1`'s Westminster debate, `B5` and CR-083's "Pacific Liquidation" speech give Churchill three moments in one season, each restrained by the same remembered sheet. One is enough. Hoare's line should also be narrowed: canon says Churchill "cannot know what else Thalassia holds" (L1609); Hoare knows what the account contained, not what Thalassia holds. Note that L1609's Hoare sentence is itself PROPOSED (CR-046) and his bible entry reads "Character use: Off the page".

**S9. The 10° S line does less than `C3` says.** (a) Portuguese Timor and Dili lie north of 10° S, so the nearest foreign harbour to Darwin is outside the line. (b) Canon does not say who holds the former German New Guinea, Rabaul, Nauru or Western Samoa: L1316 (PROPOSED) says Pacifica and Japan take the islands "with their partners, including Australia and New Zealand" and L1381 says "Pacifica and Japan retain Germany's Pacific islands". If the Concord holds Rabaul at 4° S, a line at 10° S is worth little to Canberra, and the impact note "Former German Pacific territories unaffected" hides the question. (c) The line stops at 165° W, which leaves New Zealand's Cook Islands (about 160° W) outside it. (d) Swains, Pacifican in canon (L700), lies at about 11° S inside the zone and is not grandfathered with Tutuila. (e) Tutuila as "a pre-1932 light station" is new; L1175 gives it a long-wave arc station. Coordinates are from memory.

**S10. `C1`: what The Hague gets, and the guards.** The draft says de Jonge "limits the damage by holding four lines the Netherlands already possessed". Then why does The Hague sign? The stated motive is "no European navy left east of Ceylon" and a fear of "uncontrolled confrontation", but canon gives Japan's overseas commands to common control in this same renewal (L1734), so the threat is the Concord's own, and nobody utters it. The carrots (sugar in bond, rubber and tin contracts, a bond with no guarantee) are real in a slump and should be put first, with a figure when the workbook has one. The armed foreign guards are the hardest thing to believe for a colonial government that in our history distrusted every Japanese fishing boat. I would make the guards the point de Jonge wins or half wins: company watchmen without arms inside the wire and Dutch field police at the gate. For Japan the draft names one refused demand (the shipping lines); the navy's wish for a fortified pier should be named as refused here too, since CR-085 says it is.

**S11. Bintan's bauxite has no destination.** Draft L154 has it "strictly as *additional* tonnage on top of Arkansas bauxite"; the ledger note at draft L257 says it "feeds Pacifica's pool"; `C2.1` has it held by "Japanese consortia". Japan "builds no aluminium … industry against Pacifica's before 1937" (L1600) and the Gulf "gets the alumina refinery and the royalty" (L1560). Who refines Bintan's ore, and where? CR-085 `B2` allows Japanese firms "up to 49% of joint smelting and refining ventures outside Japan" in 1932–37 and pool entry in mid-1937; this draft says the annex is "Preserved through 1936". A 50-year Japanese bauxite port is the aluminium champion's loss after 1937, and `A2a` counts only the oil trust's.

**S12. Seria's oil leaves through Sarawak.** In our history Seria's crude went by pipeline to the refinery at Lutong, in Brooke's Sarawak. So the trust's "posted-price Seria commercial offtake" depends on the one ruler who has just refused the Concord. Either this is Brooke's leverage and part of the "slow fuse", which would strengthen `B3.3`, or the draft needs a loading point in Brunei. Seria was also small in 1932; "genuinely displaces part of the trust's Texas/Gulf shipments" is a claim about the later 1930s.

**S13. The Fanning estate's owner is wrong.** See "History checked". `FANNING-ESTATE` names "Rougier's syndicate" as a treaty party in 1932; Rougier sold both islands in 1911.

**S14. The Fanning cable gain is misdescribed and its cost to the dominions is missing.** Draft L59 ties the station to traffic "Pacifica's cipher room has read since 1925 (`L1534`)". L1534 is about "the legation at Peking, the consulates, Hong Kong's government and the China Station". The Pacific Cable runs Canada–Fanning–Fiji–Australia and New Zealand and carries none of that. What Fanning adds is the dominions' and London's traffic with each other, which is a new intelligence gain and, under CR-077 D-6 as amended, a question (the dominions become treaty partners in 1932). With CR-083's Bamfield lease, both ends of the first span pass out of British hands in one season. Neither Canberra nor Wellington objects in `C3`.

**S15. `C-1919-NAVAL-LIMITS` is PROPOSED in the ledger and is amended here.** `T-F1` rightly approves `C-1923-UK-FUNDING` before amending it. The same reasoning applies to the naval limits (and to the conference itself, which the draft notes is "PROPOSED in canon").

**S16. The standalone merge check understates the dependencies.** Draft L7 claims "one marked exception". `B1` needs CR-083 for the schedule; `B2.3` and `C1.3` schedule clauses to an article of CR-086; `B1`'s reverter and `T-L1` are written against a renewal that CR-085 amends.

**S17. Set piece 3 puts Julian at Nukuʻalofa in July 1932.** The conference sits at Thalassia in June and July and the Final Act is signed there on 1 August (CR-086). Tonga is several days' steaming each way.

**S18. The New Zealand rebate rests on a figure that is not New Zealand's.** £2,113,000 is the combined total "to the end of the present financial year" in November 1929 for three contributors. New Zealand's share is not in the source and the total had grown by 1932.

## Minor

- M1. Draft L130 cites L1572 for "called the separation factory impossible"; that is L1575, and the Treasury's refusal is L1578.
- M2. "~28–38% of remaining principal" is 15/53 to 20/53 of the count of annuities. The share of principal depends on which annuities go (B2).
- M3. "Hague Arbitration Court" (draft L87): canon has "a permanent arbitration court" (L1381) and "the arbitration court's new charter" (L1746) and gives it no seat.
- M4. "mirroring the historical Dindings-to-Perak retrocession" (draft L102) is the drafter's analogy; the retrocession came after 1932 and no character can cite it.
- M5. Harlan Tate is "Silas's old adjutant" (L1593). An adjutant of the 1880s is past the retirement "at 68 for senators" (CR-038) by 1932. Canon already seats him in 1927–28, so this may be an older inconsistency; I could not find his birth year.
- M6. "The Navy's provisioners" opposing in the Senate: the Navy has no seats (L927). Say which senators.
- M7. `IIC` is a party in CR-083 and is missing from this draft's new parties. `SHELL` and `LABUAN` as parties to a harbour lease, and `JP` as a party to a Philippine appropriation, look like tagging rather than signature.
- M8. Draft L85 lists Simon, Chamberlain and Cunliffe-Lister as opening the talks; the calendar adds Eyres-Monsell and Hoare.
- M9. The forbidden pattern "guarantees? (?:of )?(?:British )?Hong Kong" will fire on a natural integration sentence such as "the Concord gives no guarantee of Hong Kong".
- M10. "the cancelled annuity count would have been reduced accordingly" (No-branch) has no number behind it.
- M11. "BPM" is Bataafsche in the period's spelling.
- M12. A committee of six with no secretary: Hankey would be in the room, and J. H. Thomas's absence leaves the dominions unrepresented in the one meeting that notes what Canada's signature does.
- M13. Under CR-085 `T-R3` the Concord no longer lapses in 1937; `B1`'s "Against the risk that the Concord lapses (`L1734 ("Japan may refuse in 1937")`" should read "is dissolved".

## The PROPOSED items

1. **M-0, approve the 1923 funding.** Keep. Add the instalment dates and extend the approval to the naval limits (S15).
2. **Brooke refuses Limbang; the Labuan ballot; the Fanning instruments.** Keep Brooke; it is the draft's one clean refusal with a cost, and S12 would sharpen it. Keep the ballot and its No-branch. Change the Fanning estate's party (S13).
3. **The Gulf's five-year lifting share; the Senate floor.** Keep the undertaking; it gives the Gulf agency and the trust a real grievance. Change the floor: fix the voting rule (S3), the Chile speech (S4) and the sufficers' position across the suite.
4. **The British cabinet, Churchill, the New Zealand rebate, the moratorium dates.** Keep the cabinet and the moratorium dates. Change Churchill (S8) and the rebate (S18).
5. **Tonga; Canberra; NKPM; the band.** Keep Tonga, but nobody loses there: the consul, or the Free Wesleyan and chiefly factions who preferred the British tie, could. Change Canberra's settlement (B4, S9). Keep NKPM. Keep the band as MODEL once B2 is settled.
6. **The cabinet's minute and the oil trust.** Keep. It answers the question a reader would ask (why the Realm alone pays). Change statement 1 (S2) and add the aluminium champion (S11). The trust president's two asks are well chosen; Julian's two refusals are the first time in the draft he acts.
7. **Britain's decision to renounce.** Keep, with B1, B3, S5 to S8. The three requests and "one and a half" are right. The dismantled laboratory plant is the right loss.
8. **One combined schedule.** Change to one schedule with three dated tranches (B2).
9. **Four straits scheduled to Article II.** Change. Say what scheduling adds to clauses already in two treaties (the court's jurisdiction, presumably), and resolve the Netherlands' signature (below). In 1932 a promise to keep straits "open to peaceful commerce" in peace restates the law of the sea; if the Realm is buying more, such as notice before closure in war, say what.

On the listed tensions: `T-F1` Case B is right. `T-B1` Case B gives the book the vote and Brooke. `T-O1` Case A is the honest one and `A2a` now carries it. `T-NF1` Case B is defensible only as a recommendation: read narrowly as the trust's rule it survives, but a fenced port with foreign guards is what "no flag" was written against, and the author should decide it knowingly (B5). `T-L1` Case A should be re-read against CR-085, which makes the Navy ministry Japanese by treaty law.

## Literary effect

The draft is still largely a term sheet: bold-headed clauses, tables and a calendar. Three passages are scenes in waiting. In `A2a` a man with a balance sheet asks for two specific things and is refused both for reasons he cannot answer. In `B3.3` a Rajah says no, London will not press him, and a young Sultan signs for half of what he wanted. In `B5` Tizard's "the figure that matters" is the one he does not have, and Lindemann is right at last and loses.

What `B5` lacks is MacDonald. He chairs and has no line. In our history he was the cabinet's disarmer in the year the Geneva conference opened (from memory); a Prime Minister who wants to sign for reasons his Chancellor finds sentimental would divide the room on a second axis. The speeches are positions laid end to end; none answers another. The best turn would be Hoare's private word to MacDonald, which needs a viewpoint. The draft names none for any scene.

Motive and cost are uneven. Britain, Brooke, the oil trust, Canberra and Lindemann want something and lose something. Sālote wants one thing and gets it. Fanning's workers are offered a choice and nobody refuses. The Dutch "fight hard" and keep what they had. Japan wins without asking. Carey is, by the draft's own dates, a Resident of twenty-eight advising a Sultan of eighteen or nineteen who "is bound to follow" the advice; the draft does not use it. Labuan votes in the month of the coup in Tokyo, on a lease half-held by Japan; the draft puts both in one calendar row and connects neither.

Victoria "declines to enter the debate" for the second sibling draft running. One refusal is characterisation; in four drafts it risks becoming a way of parking her.

## History checked

**Confirmed**
- Commons, 13 November 1929: work "shall be slowed down as much as possible", "all work that can be suspended shall be suspended", contributions "£2,113,000", a floating dock provided. The figure is a combined total with no split by contributor. https://api.parliament.uk/historic-hansard/commons/1929/nov/13/singapore-base
- The cabinet of 5 November 1931: MacDonald, Baldwin, Chamberlain, Simon, Cunliffe-Lister, Thomas, Eyres-Monsell, Hoare. https://wikiwand.com/en/articles/National_Government_(1931%E2%80%931935)
- T. F. Carey, 1903–1966, Resident 1931–1934. https://en.wikipedia.org/wiki/Thomas_Carey_(cricketer)
- Seria well S-1, 5 April 1929, British Malayan Petroleum. https://en.wikipedia.org/wiki/Seria_oil_field
- Seria's oil piped to Lutong in Sarawak for refining (not in the draft; see S12). https://borneohistory.net/a-history-of-brunei-oil-1906-1932/
- De Jonge: born 22 January 1875, died 24 June 1958; Minister of War 1917–18; BPM board under Colijn's government; Governor-General 12 September 1931 to 16 September 1936; kept Boven-Digoel in use. https://en.wikipedia.org/wiki/Bonifacius_Cornelis_de_Jonge
- Riau bauxite found 1924, mined in the 1930s, mostly for Japan. The page gives no start year; "post-1935" is not confirmed by it. https://en.wikipedia.org/wiki/Bauxite_mining_in_Indonesia
- Tonga: Treaty of Friendship of 18 May 1900; the consul's hold on foreign policy and finance. The 1905 agreement is not on the page (the draft lists it as unverified). https://www.wikiwand.com/en/articles/Kingdom_of_Tonga_(1900%E2%80%931970)
- Hoover's moratorium: proposed 20 June 1931, one year. The page does not give 1 July to 30 June; those dates are right from memory. https://en.wikipedia.org/wiki/Hoover_Moratorium

**Wrong or doubtful**
- "in 1930–32, Fanning and Washington's copra plantations were owned by Father Emmanuel Rougier's syndicate (*Fanning Island Limited*)". Rougier bought the islands in November 1907 and sold them in October 1911 to a Canadian syndicate; he died on 16 December 1932. The draft's own source says so. The Burns Philp purchase of 1935–36 is supported by an archive title only; the "mortgage" and "managing agents" are not verified (the draft says as much). https://wiki.krisyotam.com/content/wikipedia_en_all_nopic_2026-03/Emmanuel_Rougier and https://archives.library.auckland.ac.nz/archival_objects/fanning_and_washington_islands-_purchase_of_by_mes
- A Japanese-linked "Borneo Olie Maatschappij" founded in 1930 exists in the Dutch company register with a Japanese director in 1940; I could not confirm its concession. It would anchor "unallocated East Borneo blocks" if verified. Doubtful, not wrong. https://www.colonialbusinessindonesia.nl/en/database-en/catalog/item/borneo-olie-maatschappij

**From memory, not checked on the web**
- Churchill's New York accident (13 December 1931) and return in spring 1932; his estrangement from Baldwin and his quarrel with Hoare over India in these years, which bears on S8.
- Tizard was Rector of Imperial College from 1929; the bible has him at the DSIR "from 1920" and the draft gives him no post in 1932.
- Limbang annexed 1890; Miri's peak in 1929; Tokelau to New Zealand 1926; Fanning and Washington added to the colony 1916; Sālote's dates; Ahmad Tajuddin's dates and voyage; the Chadbourne agreement of 1931; Ruijs de Beerenbrouck's third cabinet; the Lausanne Conference of June–July 1932.

**Not checked**
- Labuan's census figures; the Imperial and International Communications interest date; NKPM; KPM's legal position; Sulawesi nickel; the Indies' deficits; every item the draft itself lists as "Not yet independently verified".

## The four drafts together

1. **The sufficers on the annuity bill.** CR-083 `A10`: "the sufficers object on-page" to "cancelling a tranche of British war-debt principal". CR-084 `A3`: the sufficers "support writing down a loan for sea room". CR-086 `D5`: they "make the article their condition for … the British annuities". CR-085 `A1`: they warn the cabinet that the Batavia Compact spends the lever. If it is one bill voted once, they need one position. CR-086's is the strongest and can contain the other three.
2. **The ore** (B3): CR-084 against CR-086 Part A.
3. **Australia and New Zealand under Article I** (B3): in CR-086, absent here.
4. **The schedule's dates** (B2): CR-083's May–June act, this draft's July vote, CR-086's 1 August.
5. **The Netherlands.** CR-086 `C3` lists it among "States not at the conference" and in the next sentence has it sign "the Final Act for its straits". This draft has the Compact only "initialled in June" and ratified by the States General in "autumn 1932". So on 1 August the Netherlands signs a Final Act scheduling a clause of a compact it has not ratified, at a conference it does not attend. Sign the Compact in July, or let the Netherlands accede to the schedule in the autumn.
6. **Labuan's command is nobody's.** `C2.2` says command at Labuan "is `CR-085`'s"; CR-085 does not mention Labuan. Palau as a naval anchor (M-2) appears in neither draft's text.
7. **The Navy seat and the perpetual Concord arrive after Britain and Australia have settled.** The preliminary accord is April; CR-085's Hayama Council is "late May". Simon bargained for a reverter against a Concord that might lapse in 1937 and for a harbour under a navy Japanese "by convention"; by June it is Japanese "by treaty law" and the Concord has no term. Neither London nor Canberra reacts. One paragraph in `C3` would do, and it gives Canberra a second grievance.
8. **The Hayama annex**: "through 1936" here, "through mid-1937" in CR-085 (S11).
9. **Churchill** speaks in CR-083 `A7` and twice here (S8).
10. **CR-083 `A11`** still renews Great Bear "ahead of Britain's 1933–35 atomic programme"; under CR-086 `T-1` there is none.
11. **The cabinet's minute.** CR-086 `C5` says the minute mentions the cipher room's reading of British traffic. `A2a` gives the minute four statements and none is that. Say whether it is the same minute.
12. No double decision found on the renewal, the Council or the Navy seat: `C2` now keeps to what its two instruments say. The remaining leak is in the tensions (`T-L1`'s "Japan's by convention") and in `A1`'s row for Concord treaties, "agreed at Hayama", which gives the May Council business the calendar does not show it doing.

## Impact notes missing

- **L1578** ("the Treasury under Churchill declines the factory, on Lindemann's advice"): used by `B5`, not listed.
- **L1617** ("Ottawa keeps the contract") and **L1265**: the dominions paragraph.
- **L1752**: three clauses change or are tested ("the guarantee that no hostile base stands on the dominions' soil"; "refusing the racial equality clause", if Japan is to be bound by the line; "Canada remains British" beside Canada's own signature). The draft lists L1752 only for the line.
- **L1316 and L1381** ("Pacifica and Japan retain Germany's Pacific islands"): must be settled, not noted as "unaffected" (S9).
- **L1385**, second half: "Britain retains fleet and empire while becoming the senior junior partner" needs a sentence after the retrenchment.
- **L1534 and CR-077 D-6**: whether dominion traffic through Fanning is read (S14).
- **L1597** ("convention gives Japan the Navy") and **L1734**: with CR-085, as they bear on Labuan.
- **L1740** ("two independent routes on Pacifican or allied ground"): Fanning and Bamfield add a third.
- **The overview paragraphs** at the head of the storyline (L67, L79, L91 among them) summarise the Petrograd sheet, "no weapon route exists before 1932" and Great Bear; I did not check each for a sentence on 1932, and the draft lists none of them.
- **`character_bible.md`**: Hoare ("Character use: Off the page"), Giannini, Victoria and Keawe are used and not listed; the draft lists Julian, Churchill, Tizard and Lindemann.
- **AGENTS.md**: the registry count (362) and the sentence "the renewal runs to 1937" (CR-085's, but the reverter here depends on it).
- **`commitments/data/ledger.toml`**: `IIC` as a party; `C-1932-NZ-CROP-GUARANTEE`'s no-hostile-base clause beside the line; the `open` note on `C-1931-HOOVER-MORATORIUM` ("Duration, debtors covered and restructured terms not stated") is answered here and should be closed.
- **`population/provisioning.py`**: the draft says it is "untouched" and also promises a strait-transit figure from it (S2). One of the two is wrong.
