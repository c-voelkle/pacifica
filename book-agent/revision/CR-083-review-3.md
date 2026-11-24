Fresh-context review of CR-083, revision 8, 23 November 2026. The reviewer read the draft, AGENTS.md and current canon, and not the writer's notes or earlier reviews.

Tools run first: `lint_canon.py --only` gives 10 findings, all the five unregistered character IDs (expected until the registry commit). `preflight.py --draft` gives 0 errors and 5 warnings, the same five IDs. `cr_facts.py preview --tensions` reports that no canon tension carries fact changes. Line references below are `L<n>` for `master_storyline.md` and "draft line n" for `CR-083.md`.

## Verdict

One more revision. The architecture (the fork of 1870–71, a republic outside the crowns, the Senate's refusal, the compacts, Canada's quay) is sound and most of its history checks out. It is not ready to integrate because the draft contradicts itself on the A6 sequence it says it fixed, marks several things APPROVED that no quoted author's words cover, disagrees with CR-084 on when and by whom the annuity tranche is voted, and leaves the wheat contract and the Trilateral Treaty less cleanly separated than it claims. None of this needs a redesign; it needs one careful pass and three or four author decisions.

## Blockers

**B1. A6's sequence is stated two ways inside the draft.**
- *Passage:* A6 (draft lines 95–96) against the Calendar (draft line 106), the A6 heading (line 89), Set piece 2 (line 211), impact note for L1100 (line 188) and A9 (line 137).
- *Problem:* A6 now says Pattullo's coalition asks for union in "late January – February 1932" and "Julian asks for leave ... (February 1932)", and adds "Julian did not bid before he was asked". The Calendar still reads "Dec 1931 – Jan 1932 | **Julian's leave refused:** Before Victoria petitions, Julian asks Pacifica's Senate in closed session for leave to offer a fourth crown if Victoria turns south". The heading still ends the section in "January 1932", Set piece 2 has "Winter 1931–32", and the impact note has "winter 1931–32". The calendar row is the old order the Decisions section says was changed. A9 also has the Provisional Commission negotiating compacts "from January", before Tolmie has resigned ("late January") and before the February refusal produces the republic offer whose conditions the compacts are. Tolmie resigns in "Dec 1931 – Jan 1932" in the Calendar and "late January 1932" in A6.
- *Fix:* one order, everywhere: Tolmie resigns; Pattullo's coalition asks for union; Julian asks for leave; the Senate refuses; Thalassia offers the Gulf path; the Provisional Commission and the compact talks start. Redate the Calendar row, the heading, D2, the L1100 note and A9's "January".

**B2. The Decisions table marks APPROVED what the quoted words do not cover.**
- *Passage:* `## Decisions`, N-3, N-5, N-6, N-7, N-8; A4's "(`T7`, approved)"; A8's "Upfront constitutional terms (approved)".
- *Problem:* AGENTS.md: "Do not mistake an editorial proposal, assistant suggestion or historical illustration for author-approved canon." Case by case:
  - **N-7** ("Two strictly separated Prairie wheat instruments ... APPROVED (22–23 Nov 2026)"): no quoted sentence mentions two instruments, the machinery quota, the Great Bear renewal, the Burrard quay or the Peace–Mackenzie board. The only relevant approval is CR-082's R-1, which approved something else (see B5). The draft itself says of the quota "Not yet reviewed" and lists Camsell's board as PROPOSED item 5.
  - **N-8** (private syndicates refund the bonds): no quoted words at all.
  - **N-3**: the quote is "Maybe we could take a moment here to explicate why Britain leaves gold ... Yes this version works for me." The ellipsis hides which version. The Bamfield lease and "Island protections" are in N-3 as APPROVED and in PROPOSED item 3 as awaiting sign-off; the British cabinet is PROPOSED in A6 and A7. The annuity band's own approval ("Acceptable pending modeling", 20:11) is quoted in CR-084 and not here.
  - **N-5**: the bracketed gloss lists "First Nations compacts, repeal of the 1927 ban, labour article, and ending racial disabilities". The examined civil service, the Office of Measures, balanced-budget limits and the Fraser salmon clause are not in it. The 16:57 quote is "I approve 1 3 and 4 **pending the check**"; the draft never says what the check was or that it passed, and that approval was given on 22 November for the fourth-crown design, a day before the pivot.
  - **N-6**: the author's words are conditional: "**If** the water diversion is rejected, it doesn't need to appear on-page at all." The draft reports "dropped completely (author, 23 November 2026)". The sentence that rejects it is not quoted.
  - **N-4**: "I confirm those 2 points [... Pattullo vs. Tolmie in CR-083]" covers the pairing. "Tolmie resigns rather than break with the King" is marked PROPOSED in A6 and APPROVED in N-4.
  - **T7** is "approved" in A2 and A4, but the 15:43 quote covers "1 [T3], 3 [T5], 4 [T8], 5 [N-8, Yukon at the fork], and 6 [N-10/N-11]". T6 and T7 are "Amended by T4" by the drafter's inference. That is reasonable, and it is still an inference.
  - The "Architectural pivot (author, 23 November 2026)" bullets state as the author's that Pacifica "gains hydroelectricity exported south, an Alaska transit corridor"; the quoted words are a question ("What do you think about a middle path ...").
- *Fix:* quote the missing sentences with their times, or move N-7, N-8, the unquoted parts of N-3 and N-5, and N-6 to PROPOSED. Every bracketed gloss should be marked as the drafter's. Four of the 23 November quotes have no time; the earlier ones do.

**B3. The annuity tranche: CR-083 and CR-084 disagree on date, order and who objects.**
- *Passage:* A7 (draft line 117), Calendar "May – June 1932", A10 (line 149); CR-084 `B1`, `A` (its lines 75–77), its Calendar ("July – Aug 1932") and `B5`.
- *Problem:* both drafts say there is "one debate at Westminster and one vote in each of the Realm's chambers for the whole tranche". CR-083 has the Recognition / Severance Act pass in "May–June 1932", "paired with" the cancellation, with the Republic proclaimed at once. CR-084 has the British cabinet decide the third purpose (Article I) "in the last week of June", cancellation "on ratification at Westminster", and the Realm's chambers voting in "July – Aug 1932 ... after signature". So Britain releases Caledonia one to three months before the tranche that pays for it is agreed or voted, and the "one debate" happens twice. Who objects also differs: CR-083 A10 has "the **sufficers object on-page**" to the cancellation; CR-084 has Giannini, the Industrial Board, Tate's bloc, the oil trust and the Navy's provisioners opposing, while "The **sufficers** ... support writing down a loan for sea room", and CR-086 `D5` has the sufficers make Article II their condition for "the British annuities". The words CR-083 gives the sufficers ("in the same winter Pacifica's own foreclosed farmers receive no mortgage relief") are Giannini's in canon: L1695, "Giannini answers in the Senate that the money should go to the mortgages". Churchill differs too: CR-083 has him with Beaverbrook denouncing a "Pacific Liquidation"; CR-084 has "Churchill's restrained opposition", "he does not raise a revolt".
- *Fix:* decide once, in CR-084 since it owns the debt. Either the Severance Act passes in May–June on a signed preliminary agreement with the cancellation conditional on the later vote (say so, and say what Britain risks), or the Act and Proclamation move to July. Give A10's objection to Giannini and Tate, and give the sufficers their own (a guarantee for a state the Senate would not admit). Reconcile Churchill.

**B4. Foreign affairs and the navy are the Concord's, and Japan is absent from every instrument.**
- *Passage:* A10 ("Pacifican defense guarantee"; "joint naval repair contract at Esquimalt"), A8 test 4 ("open common-navy dockyard access"), A11 Instrument 2 ("Signed by the Concord Foreign Minister (for Pacifica)"), Part F parties.
- *Problem:* L1597: "Foreign Affairs, the common Navy and their Finance belong to the Concord ... At least one must be Japanese by law; convention gives Japan the Navy". A guarantee of Caledonia is kept by a navy whose minister is Japanese, and Japanese subjects were among the victims of 1907 and the disabilities of 1895. Japan neither consents, objects nor signs. CR-084 handles the same question explicitly (Concord treaties "agreed at Hayama ... ratified by both crowns and the Concord's delegations", with `JP` a party; Realm money acts voted by both chambers). CR-083 does not: the Trilateral is the common minister's and carries party `CROWN`, the Association Treaty carries `PAC` and "the Senate ratifies" it alone, and the defence guarantee is called Pacifican. CR-085 does not mention Caledonia at all.
- *Fix:* say for each instrument which body makes it and which ratifies, in CR-084's table form. Give Japan a position on the guarantee and on the floors for Japanese residents; it is a party with an interest and a grievance, and at present it is not in the room.

**B5. The wheat contract departs from approved R-1 without a listed tension, and the two instruments are not cleanly separate.**
- *Passage:* A11; draft Part B; N-7.
- *Problem:* approved CR-082 line 281: "Contract and credit come in 1931 by CR-083's **treaty with Canada** (A9), which also carries the price." The draft has no treaty in 1931: a board contract in December 1931 and a treaty in June–July 1932, with the price in the board's contract. That may be the better design, but it amends R-1 and is not under `## Canon tensions`; Part B's six line edits speak only of the water. On separation, L892 says the Patrimony invests "never in a government in default or in treaty negotiation with Pacifica". The draft answers only for December 1931. From about February 1932 Canada is in treaty negotiation with Pacifica while the Patrimony carries a ten-harvest credit to an agency "under federal guarantee"; Instrument 2 then "Records the Prairie Wheat Contract" and "Links the Patrimony's Dec 1931 contract to the bonded quay", and the Final Act schedules the board's contract to a sovereign article. A contract recorded in one treaty and scheduled to another is no longer only the board's. CR-086 `D4` applies the same rule strictly to keep the granary off the Pampas ("the Patrimony behind it lends to no government in negotiation"), so the suite reads L892 two ways. There is also a cost to the plot: if the contract is unconditional and six months old, Bennett has already been paid when he concedes the machinery quota and fifty years of Great Bear, and the treaty gives him only the quay he already used.
- *Fix:* list the R-1 change as a tension with both cases. Then choose: (a) the board's contract is unconditional and the treaty does not record or link it (Article II's schedule names it as a contract "the Realm will not interrupt", CR-086's wording for the Pampas), and Bennett's concessions are paid for by something else that is stated; or (b) the buyer is not the Patrimony. State whether "earmarked gold-dollar credit" is a balance Canada owns or a loan to it, and whether L892's bar runs during a contract's life or only at signing.

## Should fix

**S1. The four admission tests are not all measurable outcomes.**
- Test 1's "at least **90% of unceded territory**" under compact collides with A9's own rule that a nation may refuse: every refusing nation (the Sekani, the Tahltan) becomes a veto on admission, and Caledonia gains a motive to press it. The Gulf's tests (L1091) measure what happens to people, never signatures. Keep the parity half ("95% / 1.05×"), which does match L1091.
- Test 2's "**zero statistical disparity**" is not a threshold; no sample gives zero. Use a ratio as L1091 does. It also requires counting residents by origin under a constitution "naming no race"; say that this is accepted.
- Test 3 cites L1091 for "Pacifica's weakest **county** benchmark". L1091 says "the bar set by Pacifica's weakest **former-territory state**". "Balanced gold-dollar accounts" for twenty-five consecutive years is an input, and one slump year resets the count; L1093 asks for "revenue sufficient for the common navy and debt quota; and a limit on debt held by Union creditors".
- Test 4 is a list of standards met on Proclamation Day. Canon also lists them apart from the measures ("must accompany").
- "verified annually by the **Caledonian** Office of Measures": the tested party measures itself. Missing from the Gulf model: "Pacifica may demand a second generation", the common foreign policy, and "without adding risk or a veto".
- Admission "as counties" changes the 124 and the Senate (one senator a county, L927). The dilution the nations' senators feared returns in another form and nobody in the draft notices.

**S2. February to June 1932 holds too much, and the nations have too little choice in it.** After B1 is fixed, a draft constitution, a referendum (April), compacts with the Nlaka'pamux, Secwépemc, Dakelh, Sekani, Dane-zaa, Kaska, Fort Nelson Dene and Yukon nations (initialled by May), Westminster's act and Proclamation fall in about four months. Nations that petitioned in 1909 and 1913 and were refused for sixty years hold their strongest hand in exactly these weeks; the draft has them sign on schedule with one "candidate" refusal. The referendum is held before any compact is executed, on a roll that excludes the nations as well as Asian residents (the draft mentions only the latter), and the draft does not say whether First Nations people are among "every resident" who gains the vote on Proclamation Day.

**S3. Giannini "wins", against L1695, and through a board the Crown "cannot direct".** L1695: Giannini wants "the mortgages", loses, and "Farmers who sell to it at the slump's price still lose their farms". A11 has him "win an enlarged home-crop purchase", which is not what he asked for, and has a Senate speech move a board whose independence is the reason for Instrument 1. L1695's granary also takes contracts abroad only "for beans and rice, which the Realm's fields do not grow"; a wheat contract abroad needs that sentence revised. The board's own reason to buy ten harvests of a crop the Realm exports in a glut is missing (it "publishes the return it aims to beat", L892). "Replacing Canada's distressed direct sales rather than the Realm's" is asserted with no figure.

**S4. "Renewed for fifty years" presupposes a term canon does not have.** L1265 gives "an exclusive contract" with no term, and the ledger's `C-1912-GREATBEAR-OFFTAKE` has `until` empty and its year PROPOSED. Say what the old term was or call it an extension to a fixed date. Fifty has no stated reason. CR-084 `B5` has the British cabinet weigh the renewal in "the last week of June"; the draft does not say the Trilateral is signed by then.

**S5. The cabinet's two figures are missing.** L1020: "every treaty, loan, lease and holding abroad goes to the cabinet with two figures beside its price". CR-084 and CR-086 give them for each instrument. CR-083 gives none for the Association Treaty, the Trilateral Treaty or the wheat contract, though A6 says Julian acts "for the provisioner's reason". What that reason is for Caledonia (CR-082 line 312 leaves "Caledonia's own land and people" uncounted) is not stated.

**S6. Citations that do not carry the claim.** L927 ("twelve Polytechnic seats and eight aliʻi seats") is cited for Victoria Kamāmalu having "no vote"; the line says nothing about her. L1381's racial equality clause is **[PROPOSED]** in canon; A5 builds "a formal treaty ground" on it without the label. L1752's "Canada remains British" is **[PROPOSED — OPEN-019-06]**; the impact note says it "stands" without saying the label stays.

**S7. Figures with no model behind them.** "roughly two-thirds to three-quarters of the dominion's trade (**MODEL**)": no script or workbook sheet produces it. "roughly a sixth" for Vancouver Island is the historical share (about 121,000 of 694,263 in 1931, from memory), yet Part E says the mainland interior is modelled larger, which would make the Island's share smaller. The debt that drives the whole crisis has no size ("sums to be sized"); the crisis cannot be judged plausible until it has one, and Part E puts the sizing after review.

**S8. "No flag" and Julian.** A2: Pacifica "asks for no flag and no sovereignty ... the Regent's and Julian's after them." A6: Julian "wants to say yes". The retired tension `T12` (*"no flag"*) "no longer arise[s]" only because the Senate stops him. Say in A2 that the rule holds because of the Senate, or restore T12 as a nuance; T8's "foreclosure by currency" is stronger if the sovereign did want the coast.

**S9. Statute of Westminster and the form of the exit.** The draft makes British Columbia a Dominion from 1907 and cites section 4 (no British act for a Dominion "without request and consent"). Then the Severance Act needs a request from the legislature at Victoria, and the draft never has it make one; it is a scene (the Island members voting on it). Caledonia is also not among the signatories of CR-086's `C-1932-FINAL-ACT` or of Article I, though its treaties are annexed and the Yukon is mineral country.

**S10. Chamberlain is not Chancellor in September 1931.** The Calendar's "21 September 1931 ... Whitehall's Treasury declines gold guarantees" falls under Snowden; Chamberlain takes the Exchequer on 5 November (CR-084 has this right). Date Tolmie's request after 5 November or name Snowden.

**S11. "Victoria" means three things.** The draft defines "the dominion at Victoria" and then writes "Victoria asks first", "Victoria's opposition to a fourth crown from Honolulu" and "Victoria Kamāmalu" within a page. In the storyline bare "Victoria" is the Queen. Integration prose built from this will mislead and may trip lint patterns.

## Minor

- **M1.** Calendar rows are out of order: "1 Aug 1932" stands above "June – July 1932".
- **M2.** Draft line 179: "on branch `drafts/cr083-caledonia`"; the branch is `drafts/cr083-086-endgame`.
- **M3.** A7, draft line 117: "The annuities are (`C-1923-UK-FUNDING`, `L1385`—cancelling principal ...) and guarantees a long-term commercial lease" is a broken sentence. It also says "cancelling principal rather than a moratorium-suspended instalment", while CR-084 folds "the suspended instalment of 1931–32" into the tranche.
- **M4.** Part F: "the four shares 'to `CA`'" in `C-1911-FUR-SEAL`. The ledger has four `owes` rows but three shares in canon (15, 15 and 10 per cent; one changes payer in 1921).
- **M5.** `IIC` is called "the same party as in `CR-084`'s Fanning lease", but CR-084's new-parties list has no `IIC`; only this draft declares it.
- **M6.** "President/Premier **Duff Pattullo**": choose the office. A strong executive on Pacifica's model is one or the other.
- **M7.** People who act on the page and are not registered or noted: Churchill (`CT-WINSTON-CHURCHILL` exists and gains a note), Chamberlain (registered only in CR-084), MacDonald, Baldwin, Norman, Beaverbrook. AGENTS.md leaves "whether Giannini is CT-GIANNINI" OPEN; the draft assumes it.
- **M8.** New IDs do not collide: `BC`, `CLD`, `CALEDONIA-NATIONS`, `CA-CSA`, `IIC` and the six new `C-` IDs are absent from `ledger.toml` and from CR-084 to CR-086. `ESTATES` for the Patrimony follows `C-1932-GRANARY-CONTRACTS`.
- **M9.** The `add_event` patterns match one exact sentence each ("In December ... the Patrimony's board votes a ten-harvest"). They guard nothing unless the integrator writes those words.
- **M10.** "no nitrogen fertilizer, which 1931 prairie farms barely used" is a historical claim without *Hist.* or a source.

## The PROPOSED items

1. **Victoria asks first; Julian is refused; the 25-year clause; admission as counties.** Keep the sequence and the refusal: it is the best thing in the draft, a sovereign who wants something and is told no by his own Senate and his mother. Change the tests (S1). Keep "counties, never a fourth crown", but drop "permanently": one Senate cannot bind the next, and the Gulf compact keeps Pacifica's discretion.
2. **The National Government, Churchill, Bennett's wound, the sufficers' objection, "foreclosure by currency".** Keep the cabinet (historical, and CR-084 uses it). Change Churchill to agree with CR-084. Keep Bennett's wound, but it needs the bargain of B5 to be real. Change the sufficers' objection (B3). Keep "foreclosure by currency"; it is true enough to hurt and T8 is better for it.
3. **Vancouver Island's bargain.** Keep. It gives the losers terms and a grievance. "Victoria remains the capital" for a No-voting town is a good irony. Add what the mainland members say about paying for it.
4. **Fork and railway debt; Pattullo's route north.** Keep the mountain section on San Francisco bonds and the removal of the 1873 scandal (it follows from T4). Keep the PGE. Pattullo as "a young journalist" who comes to Victoria in the mid-1890s is invented to replace Walsh's secretaryship and is harmless; label it invented, not *Hist.*-grounded.
5. **Allied Tribes surviving; one refusal; Giannini's buy; Camsell and Alberta; desalination.** Keep the Allied Tribes and Kelly and Paull. Keep the refusal and name the nation; "at least one ... (candidate)" is a placeholder where the scene should be. Change Giannini's buy (S3). Keep Camsell (the character bible calls him "Canada's partner, never Pacifica's agent", which fits a commissioner). Drop the desalination note or leave it to a later CR: it puts a post-1932 programme into canon to fill a gap in a table.

## Literary effect

- **Who wants what.** Julian, Tolmie, Pattullo, the Island and London each want something and each loses something. Tolmie's resignation rather than break his oath is the cleanest scene in the draft.
- **Who is missing.** Japan (B4). The mainland voter: the referendum "carries narrowly" and no one on the Yes side is a person. The First Nations appear as places and one unnamed "petitioner of 1913"; Kelly and Paull are "prominent at the tables" and say nothing. What does Kelly ask for that he does not get?
- **Canada.** Bennett is the one party whose loss is asserted and not shown. He "declines", "has accepted", "does not go home triumphant". He never refuses anything at Thalassia. Give him one thing he asks for and is denied, or one thing he denies.
- **Scene or term sheet.** A6 and A7 are scenes. A8, A10 and A11 are term sheets: numbered clauses, each side's gains tidy. The Trilateral's four heads have no negotiation in them.
- **Cost.** The Realm's cost is a share of annuities whose size is OPEN and a guarantee nobody tests. The refunding is private, so the Realm risks nothing. That is a deliberate choice to honour L892 and L1695, and it also means Pacifica gains a coast, a corridor and a dockyard for free, which is the critics' charge. Let someone in Thalassia say it too.
- **Viewpoint.** D5's cannery worker and petty officer are the right instincts. The worker "could not vote in April's referendum and gains full legal floors"; the scene is in what he thinks of a republic made without him.

## History checked

**Confirmed**
- Stickeen Territories from 19 July 1862, north to the 62nd parallel, under Douglas; in July 1863 the part north of 60° returned to the North-Western Territory: https://en.wikipedia.org/wiki/Stickeen_Territories (the page gives the month, not "28 July").
- Vancouver riots 7–9 September 1907; $26,000 to the Chinese and $9,000 to the Japanese community: https://en.wikipedia.org/wiki/1907_Vancouver_anti-Asian_riots
- Franchise removed from Chinese (1872), Japanese (1895) and South Asian (1907) residents: https://thecanadianencyclopedia.ca/en/article/anti-asian-racism-in-canada
- Royal Navy vacated Esquimalt on 1 March 1905: https://en.wikipedia.org/wiki/Esquimalt_Royal_Navy_Dockyard
- Prohibition 1 October 1917 to 15 June 1921, government stores from that day: https://en.wikipedia.org/wiki/BC_Liquor_Stores
- Pacific Great Eastern incorporated 27 February 1912 on provincially guaranteed bonds; taken over early in 1918: https://en.wikipedia.org/wiki/BC_Rail
- Tolmie born at Victoria 25 January 1867; premier 21 August 1928 to 15 November 1933; died 1937: https://en.wikipedia.org/wiki/Simon_Fraser_Tolmie (he was a federal MP and minister from 1917 to 1928, which the draft's "local dominion career in this timeline" replaces).
- Pattullo born 1873 at Woodstock; Yukon from 1897 as Walsh's secretary; Prince Rupert 1908; elected and Minister of Lands 1916; Liberal leader 1928; premier 1933–41; died 1956: https://en.wikipedia.org/wiki/Duff_Pattullo (the page does not give the mayoral year; "1913" is not checked).
- Allied Tribes formed 1916; the 1927 amendment; Paull a leader: https://en.wikipedia.org/wiki/Allied_Tribes_of_British_Columbia

**Wrong or doubtful**
- "the federal government has guaranteed and **taken over** the prairie pools' Central Selling Agency": the draft's own source says the government gave guarantees and "took over the sale of their inventories", not the agency: https://plainshumanities.unl.edu/encyclopedia/doc/egp.ag.057.html . Whether `CA-CSA` is a government for L892 turns on this.
- "Imperial and International Communications Ltd. (*Hist.:* owner from March 1930)": the cited Bamfield page does not mention the company: https://en.wikipedia.org/wiki/Bamfield . Hansard of 18 February 1930 says the remaining conveyances were expected "in the course of next month", an expectation and not a completion: https://api.parliament.uk/historic-hansard/commons/1930/feb/18/imperial-and-international . Doubtful as dated.
- "One petitioner of 1913 lives to sign at Spences Bridge": the petition of 1913 is the Nisga'a's, from the Nass. Interior nations meeting at Spences Bridge backed it in 1915 (same Allied Tribes page), but a signer of 1913 would be Nisga'a and would not sign an Nlaka'pamux compact. Doubtful; use the Spences Bridge declaration of 1911 or move the petitioner.
- The Allied Tribes page does not name Kelly as chairman; the draft's FNESC source was not opened.

**From memory, not checked on the web**
- About 30,000 miners on the Fraser in 1858; the transfer of 15 July 1870; Raymond at Fort Yukon in 1869; the *Chicora*; Treaty 8 (1899–1900); New Zealand and Newfoundland as Dominions in 1907; National Government 24 August 1931; gold left 21 September 1931; Abnormal Importations Act (November 1931), Import Duties Act (February 1932), Ottawa (July–August 1932); Statute of Westminster 11 December 1931; Bennett 1930–35; Camsell born at Fort Liard, deputy minister from 1920; Alberta's resources transferred in 1930; BC's 694,263 and the Yukon's about 4,200 in 1931; New Zealand's roughly 80% export share to Britain; Kelly 1885–1966 and Paull 1892–1959. I believe all of these are right.

**Not checked**
- The imperial mail subsidy for the Vancouver–Hong Kong liners; Teit as first secretary; the signing places the draft itself marks "to verify" (Dane-zaa at Fort St John, Fort Nelson Dene, Secwépemc of the North Thompson).

## The four drafts together

- **CR-084, annuities:** the total is stated once there (15 to 20 of about 53) and CR-083 only refers to it; that part agrees. The date of the vote, the order of release and payment, the objectors and Churchill do not agree (B3).
- **CR-084, instalment:** CR-083 says principal "rather than" the suspended instalment; CR-084 writes the suspended instalment off inside the tranche (M3).
- **CR-086, Article II:** agrees. CR-086 `D3` schedules `C-1931-PRAIRIE-WHEAT` and names CR-083 as owner; CR-083 A11 says the schedule "adds nothing to the Patrimony board's contract". The two drafts read L892 differently, strict for the Pampas and loose for the prairies (B5).
- **CR-086, Article I:** agrees on Canada signing for itself, on the 19:55 quote and on the reason (London cannot ask Ottawa again). CR-086's table says Canada is paid by "The prairie wheat contract scheduled to Article II", which makes a board's commercial contract the price of a sovereign signature and sharpens B5.
- **CR-086, Final Act:** agrees that Caledonia's treaties are annexed on 1 August. Caledonia itself signs neither the Act nor either article (S9). The Trilateral's party is `CROWN` here and the Final Act's is `CROWN`; the Association Treaty's is `PAC`.
- **CR-084 and CR-086, Great Bear:** both leave the renewal to CR-083 and decide nothing twice. CR-086 adds a company name and tonnage to the same ledger entry; the two amendments must be merged in one edit.
- **CR-085:** no mention of Caledonia, Esquimalt or the guarantee, though it settles the Navy seat by treaty law in May 1932 (B4).
- **Double decisions:** none found. Chamberlain is registered in CR-084 and used here; Bennett is registered only here, as the draft says.

## Impact notes missing

- **L1020:** the two figures for each of this CR's instruments (S5).
- **L1597 and L1604:** which body makes and ratifies each treaty; Japan (B4).
- **L1695:** the sentence "ten-year contracts abroad for beans and rice" must change if a wheat contract abroad is added; the note mentions only adding the contract.
- **L1746 and L1748:** the conference's list of who attends and enters has no Canada and no Caledonia; the note covers "1746–1754" in general terms only.
- **L1754:** "Britain is managed through debt" after a cancelled tranche (CR-084 notes it; this draft's share is silent).
- **L1381:** the racial equality clause is PROPOSED and A5 leans on it.
- **L1100:** "Admission is outside the novel" needs a parallel sentence for Caledonia (earliest 1957).
- **CR-082.md line 281:** "treaty with Canada ... which also carries the price" is a change of substance, not only of the water (B5).
- **`commitments/data/ledger.toml`:** `C-1932-THALASSIA` (parties, the annexed treaties), `C-1880-DEV-FUND` (if L892's reading is fixed), and the `CA` party's name are touched; only the last is mentioned.
- **`character_bible.md`:** entries for the five new people, and notes for Julian, Victoria and Giannini; only Camsell's lines are listed.
- **`historical_background.md`:** only line 195 is listed; AGENTS.md wants every source and reason for divergence there, and `## Sources` here is long.
- **`population/outputs/` and `population/data/provisioning.toml`:** the northern-water rows and the generated provisioning document, beside `provisioning.py`.
- **`energy/` workbook:** hydroelectricity exported south and the Columbia compact turned into a bilateral power compact are energy changes; Part E lists only finance and population.
- **`change_requests.json`:** no entry for CR-083 yet; the fact changes go into it on approval.
