# CR-083 review 5

Fresh-context review of `book-agent/revision/CR-083.md`, revision 10. The reviewer read the draft, `AGENTS.md`, the cited lines of `master_storyline.md`, the party and commitment IDs in `commitments/data/ledger.toml`, the Tate, Giannini and Camsell entries of the character documents, `canon_facts.toml` (searched only), `population/provisioning.py` (searched only), and the sibling drafts `CR-084.md`, `CR-085.md` and `CR-086.md` for cross-references only. No earlier review, nothing under `planning/` or `outputs/sessions/`, and no writer's notes were read. `CR-082.md` was not on the permitted list, so the draft's quotation of its line 281 and its six line numbers are unchecked.

Scripts. `preflight.py --draft` reports 0 errors and 5 warnings, all the same kind: the five `add_person` entries (Pattullo, Tolmie, Bennett, Kelly, Paull) are not yet in `character_registry.json` and must land in the same commit; it declares the draft ready for a fresh-context review. `cr_facts.py preview --tensions` reports that no canon tension carries fact changes.

## Verdict

One more revision. The structure holds, every fight has a loser, and the citations sampled quote their lines correctly. Three things stand between this draft and integration: a count of Senate refusals that contradicts canon and hides the question of why Julian obeys this time, a British motive that the sibling's annuity schedule has removed, and an admission count that is called a match for the Gulf's and is softer than it.

## Blockers

**B1. The Senate's "second" refusal is its third, and 1927 is not answered.**
- *Passage:* line 126, "the Senate refuses him a second time"; line 137, "his second check after the Gulf count"; line 248; line 271, "his second Senate check after the Gulf count"; line 88, "Under Julian the rule holds because the Senate holds it".
- *Problem:* canon `L1593` has the Senate refuse the Concord treaty in 1927, and Julian answer by "provisional application under the treaty prerogative", cured only in 1928 (`L1604`). The Gulf count of 1931 (`L1100`) is therefore his second refusal and Caledonia his third. More than the number is at stake. A reader who remembers 1927 will ask why the man who overrode the Senate for Japan submits to it for a coast he wants. The draft gives no reason, and line 88 makes the Senate's hold the whole of the no-flag rule.
- *Fix:* count the refusals correctly in all five places, and give Julian one sentence of reason in `A6`: the indemnity of 1928 and its conditions, Ka Lōkahi's two votes against, and a renewal three months off that he cannot risk. No tension is needed; the reason only has to be on the page.

**B2. Westminster's motive for the Severance Act rests on relief the schedule does not give.**
- *Passage:* line 149, "Baldwin and Chamberlain carry the **Recognition / Severance Act (June 1932)** only because the Admiralty admits the coast is indefensible against an atomic Concord and the Exchequer needs relief on the war debt"; line 261, "London's price is principal cancellation".
- *Problem:* `CR-084` `B1` and `T-A2` (decided at 23:52) take the first tranche, this CR's, "from the end of the schedule, which runs to 1985". `CR-084` itself states the cost of far-end cancellation: "Britain's yearly payment does not fall at all". The near-end relief was given only to the third tranche. So in June 1932 Britain releases a loyal dominion and a No-voting Island for annuities due in the 1980s, and the draft says the Exchequer did it for relief. One of the two reasons a main actor acts is void, and the two drafts disagree on what the tranche is worth to London.
- *Fix:* either state honestly in `A7` that the first tranche shortens the book and relieves nothing now, and let Chamberlain carry the Act on the Admiralty's admission, the dominion's own request under the Statute, and the wider April accord of which Caledonia is one clause; or ask the author whether part of the first tranche also comes from the near end, which is a change to `CR-084` `T-A2` and his to decide. The Beaverbrook attack becomes stronger under the first course and should use it.

**B3. The admission count is softer than the Gulf's, months after the Senate refused to soften the Gulf's.**
- *Passage:* line 158, "The Gulf-Style Admission Clause (PROPOSED, matching `C-1900-GULF-COMPACT`, `L1091–1093`)"; line 160, "A year in which a test fails is not counted and does not reset the count; three failed years running reset it".
- *Problem:* `L1093` reads "Every measure must hold for twenty-five consecutive years", and `L1100` shows what that means: "The 1931 oil glut breaks the general-measures streak". In 1931 the Senate refused Julian a shorter count because "a shorter count would lower that bar". The draft then has the same Senate consent, by two-thirds, to a count for a white settler republic in which a failed year costs nothing. That is a departure from the model it claims to match, it is not listed under `## Canon tensions`, and nobody in the draft objects. The Gulf's Black leaders and the senators who held the line in 1931 are the obvious objectors.
- *Fix:* either make the count consecutive as the Gulf's is, or list the difference as a tension with both cases, drop the word "matching", and name who objects and what they get. The sheet's phrase "one slump year does not reset the count" supported the budget trim of 83-4; it did not approve the rule.

## Should fix

**S1. The accord of April is told two ways across the drafts.** Line 139: "a **preliminary accord** is initialled in London by Britain, Pattullo's government and the Realm". `CR-084`'s calendar has a "Preliminary Anglo–Concord Accord initialled" in April whose listed contents are Labuan, Brunei, Fanning and Tonga, handed over by the Concord's Foreign Minister, with no mention of Caledonia or Bamfield. `CR-084` `B1` then leans on "the accord of April" for the suspended instalments. Say whether there is one accord or two, who initials for the Pacific side, and put Caledonia and Bamfield in `CR-084`'s list. Line 149 calls it "a signed accord"; it is initialled.

**S2. Japan's entry right is added after the vote.** The April ballot is taken "on the published draft constitution and Association terms" (line 146), and Vancouver "splits" over the labour article. In June Japan obtains, inside the guarantee, citizenship for resident Japanese subjects and "a right of entry and residence reciprocal with Caledonians' in Japan" (line 200). Asian entry is the most dangerous question in the dominion's politics, and it changes after the people have voted. Nobody reacts. Either publish it before April or name who protests in June and why Pattullo survives it.

**S3. Entry and residence for Realm citizens is in `A8` and missing from `A10`.** Line 157 says "Realm citizens have entry and residence by the Association Treaty". The list of Association terms at line 186, the table at line 195 and the ledger entry at line 315 do not carry it. It is unlabelled; it is the drafter's and should read PROPOSED.

**S4. T14 is decided in one place and PROPOSED in two.** Line 333: "**Decided: Case B** (author, 23 November 2026, 23:52: \"5 yes\")". Line 206: "(`T14`, PROPOSED)". Line 540 lists "**the reading of `L892`** (`T14`)" among items for sign-off. The same holds for the pace of the compacts: line 169 says "the pace [is] PROPOSED", line 173 "(`T15`, decided)".

**S5. The Island's bargain is APPROVED in the table and PROPOSED in the list.** N-3 (line 508) approves "Island protections" on item 83-2, whose words name "the Island's capital/autonomy/pensions/opt-in bargain". Line 538 lists the same bargain as PROPOSED. Likewise the higher Great Bear royalty: approved by 83-7 and N-7, marked "(PROPOSED)" at line 215.

**S6. `A8` promises a speech that `A10` does not contain.** Line 166: the nations' senators "say so in the debate of `A10`". Neither the May paragraph (line 187) nor the July paragraph (line 188) has them speak.

**S7. The two-thirds for the Association Treaty is told differently in `CR-086`.** Line 188 has the treaty get its two-thirds "from the majority that refused the fourth crown in February, since it is the alternative that majority asked for". `CR-086` `D5` and `E1` make it one of three votes the government "cannot do without", for which the aliʻi seats make Article II their condition, "and the Senate takes Article II first". `CR-084` `A3` says its own two-thirds is reached "with the eight aliʻi seats and not without them". Add the condition and the order of votes here. A refusal in February by majority is also no proof of two-thirds in July.

**S8. The refunding has no dates, no bridge and no objector.** The bonds are "maturing 1932" (line 122) and the syndicates refund them in July "once the Republic is proclaimed" (lines 142, 185). Nothing says when in 1932 they fall due or who carries the dominion from September 1931 to July 1932 without a default, which matters because `L892` turns on default. The syndicate lends abroad in the winter when canon has "county banks fail" and Giannini asking credit for farmers (`L1695`), and he objects to the wheat and the annuities and not to this. Give the maturity, a bondholders' standstill or an extension, and a voice against.

**S9. The Columbia half is treated as money while canon leaves it open.** `L1554`: "Whether the half is paid in power or in gold is undecided." Lines 122 and 185 count it as gold-dollar income and as collateral. The draft admits this at line 517. Decide it here, since `L1881` lists it as open and the refunding rests on it, and label the decision.

**S10. Unlabelled additions to approved canon.** Line 110: "At Pacifica's insistence the Columbia compact is also signed with the nations of the upper river" changes an approved compact with no label. Lines 301, 302 and 304 convert the western-waters treaty into "a Pacifica–Caledonia water board" and pass the seal and halibut treaties to `CLD`; the body never says so. State treaty succession once in `A8` or `A10` and mark it PROPOSED.

**S11. A citation that does not say what it is cited for.** Line 210: "He loses because the Senate cannot instruct the board (`L892`)". `L892` says nothing of the Senate. `L1695` has "the board, which the Crown cannot direct". The Senate's want of power is the drafter's inference and should be labelled or cited to the charter differently.

**S12. Who can sell ten future harvests.** Line 205 makes the seller the pools' Central Selling Agency "under that guarantee". From memory, the pools' five-year delivery contracts were given up in 1931 and the Agency became a holder of unsold stock under a federal manager. An agency in that state has stock to sell and no claim on the crops of 1932–41, yet the contract "takes new harvests" and leaves the stock alone (line 209). Say how the Agency binds growers for ten years in this timeline, or have it buy to deliver.

**S13. The Trilateral Treaty's maker and its "settled boundary".** It is "A treaty of the Concord" (line 212) with ledger parties `CROWN`, `JP`, `CLD`, `CA`, so four parties under the name Trilateral, and Japan's delegation ratifies a Canadian quay and a quota for Pacifican machines. The Association Treaty, by contrast, is the Realm's. The draft does not say why one is the Concord's and the other not, and the effect is that the quota and Great Bear never face the Senate where Giannini and Tate sit. Item 4 pays Canada with a boundary "declared settled" (lines 214, 216), but `A2` fixed that line in 1870 and no dispute is told after Macdonald's protest. Either Canada kept a claim to the Peace country or the Yukon until 1932, which should be said, or the boundary is no payment.

**S14. The two ratified compacts are the two the treaties need.** Line 173: the nations "do not sign in fourteen weeks what they have asked for since 1909", yet the compact on the most valuable and most contested ground in the country, with three nations, is among the two finished. Line 175 still says the quay and district "wait on a compact there". Give Burrard a reason to close fast (what Paull's side wins that it could not win later, and what the syndicates and the Canadian Pacific pay), or let Burrard run on too and make the quay paper in July, which `T15` Case B already allows.

**S15. Harlan Tate's year is "stated here" and carried nowhere.** Line 8 says this CR states it for the suite. It appears once, at line 188, with no fact change, no registry line (line 321 lists Camsell, Julian, Victoria and Giannini), and no registry record exists for Tate. `CR-085` says he "needs a registry entry on integration". Add it here, since this CR merges first.

**S16. T6's "prairie border".** Line 343 lists "the prairie border" among Canada's remaining dealings with Pacifica. With British Columbia out, check where Canada touches the Realm at all: canon puts western Montana, "the Missouri-headwaters gold camps" (`L629`), on Pacifica's side and Fort Benton on the Union's. If the two meet only on a short stretch of the forty-ninth parallel, say so; if nowhere, strike the phrase. The answer also bears on `L1142`'s western-waters list.

**S17. Prince Rupert and the second railway.** The draft uses Prince Rupert as a port, a chartered district and the site of "Canada's transit shed", and sends Pattullo there in 1908, but never says who built a railway to it in a dominion Canada does not own. Line 255 has the Canadian Northern "blasting at Hells Gate on running rights", which is construction and not running rights. One sentence on the northern line's charter and owner is needed.

## Minor

- M1. The calendar's "March – May 1932" row stands before "April 1932". The referendum votes on a "published draft constitution" in April while the Convention sits March to May; the draft never says when or how the Convention is elected.
- M2. Line 96: "in the year of the *Chicora* crisis and the Treaty of Washington". The *Chicora* and the transfer are 1870; the treaty is 8 May 1871 (`L708`).
- M3. Line 109: the dockyard "is already the dominion's own from then", meaning 1905, two years before dominion status.
- M4. Line 148 labels the Island's sixth MODEL; line 525 calls it "the historical sixth". One label.
- M5. Set piece 4 is "San Francisco, December 1931" while line 210 has Giannini object "in the Senate". Set piece 2's title names February and July and its text adds May.
- M6. Line 542 leaves "which northern nation exercises the 1932 standstill refusal" OPEN; line 182 and set piece 3 name McLeod Lake.
- M7. "Great Bear's fifty-year renewal" (lines 7, 252, 512) against line 215, "canon's exclusive contract has no stated term. The treaty gives it one". It is a term, not a renewal. `CR-086` line 9 repeats "renewal".
- M8. The ledger entry `C-1932-CALEDONIA-SEVERANCE` has parties `UK`, `CLD`, `IIC`, though the Realm initials the accord, cancels the annuities and "guarantees" the lease.
- M9. Line 148 gives the Island "provincial autonomy"; `A8` describes no provinces.
- M10. `A8` does not say what franchise the Republic has. The Gulf's compact asks for "examinations for office and franchise" (`L1093`); the draft gives "the vote" to every resident and is silent on examinations.
- M11. Line 126 puts "With Victoria's request on the table" one sentence before "Victoria Kamāmalu". The draft lists this as open (line 526); this is the worst instance.
- M12. The *Hist.* claims of `A6` have no entry in `## Sources`: the Abnormal Importations and Import Duties Acts, the Ottawa Conference's dates, Chamberlain's appointment, the National Government's date, Norman, Beaverbrook, and Australia's trade. Dominion status for New Zealand and Newfoundland in 1907 has none either.
- M13. Line 401's linter message reads "CR-083 (rev 7)"; a revision number should not enter `canon_facts.toml`.
- M14. Line 215: "Ottawa has told London since May that it will sign" does not say what.
- M15. The Statute of Westminster names its Dominions; the draft should say British Columbia is among them.
- M16. Line 121 does not say whether San Francisco offered London credit in August and September 1931. Canon has the Bank "lend gold rather than hoarding it" (`L1693`) and a credit that "can be withdrawn" (`L1566`); one clause would close the question.

## Leftovers from earlier revisions

- Line 16: "**Next:** the third fresh-context review". Four reviews are named in the status lines and this is the fifth.
- Line 92: "(N-8, approved)" for the Yukon. In the present table N-8 is the San Francisco syndicates; the label is from the numbering of 22 November.
- Line 4: `T15` "is put to the author". It is decided (line 337). Line 524 likewise leaves the pace as "the author's call".
- Line 328: "(Revision 9 said here that the sentence gained an exception; that was the drafter's error and no part of what was approved.)" and line 235: "Revision 8 proposed a desalination programme". Both are drafting history inside text that will be read as the proposal.
- Lines 446 and 455: the event patterns accept "May" and "spring" for the proclamation and "June" for the Trilateral Treaty. The text now has late June and early July.
- Line 550 still cites the cable sale as "completed March 1930"; line 528 says the date "is no longer asserted".
- Line 175, "wait on a compact there", against line 173's ratified Burrard compact (see S14).

## The four drafts together

- **Who votes what.** Agreed. `CR-084` `T-S1` Case A, `CR-086` `E1` (five two-thirds votes, the Association Treaty among them; the annuity bill by majority in both chambers) and this draft's `A10a` say the same. The guarantee as the Concord's, ratified by "both crowns and the Concord's delegations", agrees with `CR-085` `A4`. The gap is S7.
- **Dates.** 15 May, Hayama on 5–8 June, the July votes and 1 August agree in all four. The April accord does not (S1). The older change notes of `CR-084` and `CR-085` still say "the May Hayama Council"; their calendars say June.
- **Annuities.** One schedule of 15 to 20, three tranches, the first triggered by the Severance Act, one bill in July: agreed. The worth of the first tranche to London is not (B2).
- **Wheat and Article II.** `CR-086` `D3` schedules `C-1931-PRAIRIE-WHEAT` and its table says Canada's signature "is not bought with the Patrimony board's wheat contract"; agreed. `T14`'s note that `CR-086` `D4` does not use the day-of-investment reading is correct.
- **Harlan Tate.** About 1866 in `CR-083` and `CR-084`. `CR-085` points to "`CR-083` `A10`", correctly. `CR-086` line 252 points to "`CR-085` `A6`", which is wrong. His following is an "interior bloc" here, a "county bloc" in `CR-084` and "what remains of his bloc" in `CR-085`; canon has it split in 1928 (`L1604`).
- **Caledonia and Canada as signatories.** Agreed: Caledonia signs the Act and both articles (PROPOSED here and in `CR-086` item 12b); Canada signs by plenipotentiary while Bennett is at Ottawa. `IIC` is used by `CR-084` as this draft asks. Bennett is registered only here, as stated.
- **Giannini** loses in December, in July here, and again in `CR-084` and `CR-086`. `CR-085` notes it. Four defeats in one season make him a device; give him one thing he wins.

## Approvals against the quoted words

- **Rest on the quoted words:** N-1 (19:45); `T14` and `T15` (23:52, with the questions restated); N-6, N-7, N-8, `T6`, `T7`, `T9` and the Tolmie half of N-4 (23:14, adopting sheet items quoted in full); the wording trim of 83-4; Canada's signature (19:55).
- **Rest on the drafter's bracketed glosses.** N-2 and the first half of N-5 quote "I agree with both recommendations for the two quick choices"; what the two choices were is supplied in brackets. N-9 and Pattullo rest on "I confirm those 2 points" in the same way, and `T5`, `T8` and the Yukon on "Approved 1 [T3], 3 [T5], 4 [T8], 5 [N-8, Yukon at the fork]". The 23:52 entry shows the better form: restate each question as put. The hour of "two quick choices" is, as the table says, not recorded.
- **N-4 reaches further than its quote.** It is labelled APPROVED on item 83-3, which covers only "Tolmie resigns rather than break with the King". That Pattullo "leads the Constituent Convention and Republic", and is "President" (line 152), rests on "Pattullo vs. Tolmie" inside a gloss. Split the row.
- **N-3 reaches further than its quote.** Item 83-2 covers "gold exit, London's refusal, Bamfield lease, Island protections". It does not mention annuities; the words on the band (20:11) are quoted only in `CR-084`. Quote them here or take "this CR's share of the one annuity schedule" out of the row.
- **`T8` and `T4`.** `T8` is marked approved on 22 November, 15:43, before the republic existed in the plan; "foreclosure by currency" is in the PROPOSED list (line 537) and is mentioned in sheet item 83-8. Cite 83-8. `T4` carries the Republic of 1932 under the approval of 21 November, which covered only staying out of Confederation.
- **16:57.** Given "pending the check"; line 146 says the roll rule is "honouring the author's 16:57 decision". Item 83-5 at 23:14 covers it without condition and should be the one cited.
- **Tate's year** is labelled PROPOSED, correctly, but the request it cites (item 85-4) is quoted only in `CR-085`.
- **The sheet** is described accurately as the author's "by adoption and not by authorship". No assistant opinion is used as an approval.

## History checked

On the web, two pages were fetched and both confirm less than the draft says. The Great Plains encyclopedia page the draft cites states that in 1931 the Canadian government gave financial guarantees "for the pools" and took over the sale of their inventories; it does not name the Central Selling Agency and says nothing of pooling contracts after 1931 (see S12). The Grace's Guide page on Imperial and International Communications confirms the company's formation from the merger decided in 1928 and its renaming as Cable and Wireless in 1934; it does not mention the Pacific Cable Board or Bamfield, so the draft's caution on that point is right and line 550 should lose its date.

From memory, and agreeing with the draft: Britain off gold on 21 September 1931; the National Government of 24 August and Chamberlain at the Exchequer from 5 November 1931; the Abnormal Importations Act (November 1931) and Import Duties Act (February 1932); the Ottawa Conference opening 21 July 1932; the Statute of Westminster of 11 December 1931 and its request-and-consent rule; Creditanstalt in May 1931; the Stickeen Territories of 1862 and the Act of 1863; the transfer of 15 July 1870; Raymond at Fort Yukon in 1869; the boundary on the divide and the 120th meridian; Tolmie's, Pattullo's, Bennett's, Kelly's and Paull's dates and offices; the Pacific Great Eastern in 1912 and 1918; prohibition from 1 October 1917 to 15 June 1921; the franchise acts of 1872, 1895 and 1907 and the riot of September 1907; the Allied Tribes of 1916 with Teit, Kelly and Paull; the Royal Navy leaving Esquimalt in 1905; dominion status for New Zealand and Newfoundland in 1907; the 1931 census figure; Alberta's resources transferred in 1930.

From memory, with reservations: the Mackenzie King awards were a little above the round sums given; Paull was the Squamish council's secretary and not a chief, so "signs for the Squamish" needs chiefs beside him; the memorial of 1910 was at Kamloops and the declaration of 1911 at Spences Bridge, which supports the draft; the riot of 1907 drew on agitators from the American coast and a surge of arrivals by way of Hawaii, both of which this timeline changes, so the riot needs a cause of its own; the Finlay and Parsnip valley is the country of the northern Sekani bands as much as of McLeod Lake. Not checked: the nations named at Burrard Inlet, Prince Rupert, Kamloops, Fort St John and Fort Nelson; New Zealand's export share; Vancouver Island's share of population.

House style: no exclamation marks; no review labels in the body beyond the two revision notes listed under leftovers; no weapon design on the page.
