# CR-084, revision 10: fresh-context review 6 (24 November 2026)

Reviewed: `book-agent/revision/CR-084.md` (revision 10 with the changes of 24 November). Read: the draft in full; `AGENTS.md`; about fifty cited lines of `master_storyline.md`; the cited entries of `commitments/data/ledger.toml`; the registry and character bible for Kaʻiulani, Hoare and the listed IDs; `finance/CR-083-086-workbook.md`; and `CR-083.md`, `CR-085.md`, `CR-086.md` and `CR-087.md` for cross-references only. No earlier review, planning file or session note was read. Line numbers below are raw line numbers of `CR-084.md` unless they carry an L, which is the storyline.

Scripts: `preflight.py --draft` exits with 0 errors and 13 warnings. Nine are the new persons not yet in the registry, which is expected before the registry commit. Four are "line 299", "line 48", "line 191" and "line 126" inside the quoted answer sheet (lines 58–59), which the script reads as unchecked citations; they are quotation and can be answered in one sentence in the draft. `cr_facts.py preview --tensions` reports "no canon tension carries fact changes".

## Verdict

One more revision. The story of `B1` and `B5` now holds, and the canon citations I sampled are sound, but the approval labels cannot be integrated as they stand, the first tranche's remedy contradicts `CR-083`'s calendar, and the passages rewritten in revisions 9 and 10 have left about a dozen stale or contradicting sentences behind them. None of it needs new decisions from the author except B1 and S9.

## Blockers

**B1. The bulk approval row is in the wrong table and contradicts three other statements.**
*Passage.* Line 92, row `R-10`, sits in `A1`'s table of instruments ("Instrument | Lawful Maker & Ratification | Basis in Canon"), not in `## Decisions`. It approves "The drafter's PROPOSED additions of revision 10, as listed under 'The should-fix items … one by one' below".
*Problem.* (a) The list it points to (lines 575–588) is a list of review findings and what was done with them, not a list of proposals; several entries are revision 9's ("S3, S4: annuity years are defined (revision 9)", "S5: … rewritten in revision 9"), which the row itself excludes ("Proposals made before that revision are not covered"). A reader cannot tell which sentences are approved. (b) Line 13 still says "`A2a` and `B5` are the drafter's … nothing in them is approved", while S6, S7 and S8 are additions to `B5`. (c) Line 558 says "Everything approved has been taken off this list", yet item 11 (line 569) still lists as PROPOSED "Hawaii as Tonga's guarantor" (marked "approved, author, 24 November 2026, 07:27" at line 174) and "the coup in the committee, Hankey's minute, Lindemann's breach and Simon's messenger", which are exactly S6, S8 and S14(d). (d) "The labels in the body still read PROPOSED … and are to be read with this row" leaves two labels on the same sentence. The same misplaced row is in `CR-085` (line 104, `R-7`) and `CR-086` (lines 181–182, inside the table of signatories).
*Fix.* Move the row into `## Decisions`. Replace the pointer with an explicit list of the items it covers, each with its section, and limit it to what the author's words can carry (see "Approvals" below). Take those items off the PROPOSED list, change their labels in the body, and correct line 13.

**B2. The first tranche's remedy cannot work on `CR-083`'s calendar, and the draft still says elsewhere that there is none.**
*Passage.* Line 140: "The accord of April gives it one remedy: if the bill fails, the Severance Act's commencement order is not made."
*Problem.* `CR-083` (line 154 and `A7`) has the Act pass in the last week of June and the Republic "proclaimed in the first days of July", with the floors in effect on Proclamation Day, and has the chambers vote the bill later in July; it states the month's risk with no remedy ("for a month Britain has released a dominion on the strength of an initialled accord"). A republic already proclaimed cannot be un-commenced. Inside this draft, line 592 still lists the same finding as not addressed ("without giving London a remedy"), against S2 at line 577.
*Fix.* Either the Realm's chambers vote the bill before Proclamation Day and both calendars say so, or the remedy is dropped and Britain's month of risk is told as a risk it knowingly takes (with who in London objects). Put the same sentence in `CR-083` `A7`, and delete line 592.

## Should fix

**S1. Two statements of when Britain next pays.** Line 138: "Britain therefore pays nothing from the moratorium until the instalment of 15 December 1938". Line 143: "Between those dates Britain owes nothing; its next instalment falls on 15 December 1932." The second is the older text and is true only if the July bill fails. Revision 9's stated aim was "what Britain pays and when is one statement". Cut the clause or add the condition.

**S2. A sentence contradicted by its own figures.** Line 141: "Eleven annuities of the 1970s and 1980s are worth less in 1932 than two of the 1930s", after giving $114m for the eleven and $93m for the two. The workbook says "worth about as much as". Use its wording.

**S3. Two years or six.** Line 190: the refusal of 1926 "cost Britain two years, from 1926 to 1928". Set piece 6, line 286: "the refusal cost Britain six years".

**S4. Hoare speaks twice and in opposite directions.** Line 185: "Hoare adds that the offer will not improve" (sign now). Line 189: "Hoare's side: … wait and see whether the Concord survives June" (do not sign yet). Line 188 says he "says little", `T-B5b` Case B says "he speaks once, as written", and set piece 5 says he "says almost nothing". Give the argument for waiting to Eyres-Monsell, who is already the opposition, or choose which line is Hoare's.

**S5. Stale counts of annuities.** Line 275: "33–38 remaining annuities" (it is 36). Lines 263 and 325: "15–20 annuities cancelled" (line 308 says 17). Line 134's heading says in one sentence that "the split among the tranches is OPEN" and that it "was decided on 24 November at 00:12", and labels the near-end arrangement APPROVED by item 84-8, which approved the far end.

**S6. The annex and `T-P1` are not carried through.** The body has three stations (line 227: "so the annex has three entries"). The `M-4` row (line 556) and the impact note for L1127 (line 257) still say "Tutuila and Swains"; the impact note for L1316 (line 259) says the former German territories are "unaffected by the 10° S line", though Apia is on its annex. `T-P1` (line 354) says canon "does not say who holds Samoa, New Guinea and Nauru after the peace"; L1381 says "Pacifica and Japan retain Germany's Pacific islands". That supports Case B, but it should be cited, and it raises a question the draft does not list: what Japan retains (canon's L794 leaves Germany the Marshalls). "Pacifican since 1919" needs that sentence before it is integrated.

**S7. The old voting rule survives in two places.** Line 253: "both Senate and Chamber vote the Realm money/guarantee acts"; under `T-S1` the guarantees go to the Senate alone. Set piece 1 (line 281) is titled "The Senate & Chamber" and puts the two-thirds there. In `A3` (line 120) the third group "who opposes" is "the provisioners on the Realm's General Staff", who are officers and have no vote; `CR-086` `C2a` has them "make King's argument in the chamber", so say through which senators.

**S8. The naval limits are amended in the body and not amended in the ledger list.** Line 148: the cap east of Ceylon is "amending `L1381`". Line 310: "`C-1919-NAVAL-LIMITS` — not amended"; line 552: "no longer amended here".

**S9. The four requests.** They are numbered 1, 2, 4, 3 (lines 193–196). The PROPOSED list says "the three requests" (line 560) and lists the fourth separately (line 566). The committee also "makes Japan's countersignature a condition of Britain's own" (line 189), which is a fifth term, is not among the requests, and is not recorded in `CR-085` `A5` or `CR-086` as something Britain asked for. With the signature's tranche now four annuities of 1934–38, request 3 ("cancelled on signature" against "on ratification", line 196) no longer costs or gains Britain anything in 1932; say what Britain wanted from it or drop it.

**S10. The retrenchment tranche no longer holds Westminster to anything, and no one in London notices what it is paid in.** Item 84-8's stated purpose was "preventing London from pocketing debt relief before Westminster ratifies each instrument". Since the split of 2, 4 and 11, the trigger for ratifying `C-1932-UK-RETRENCHMENT` is eleven annuities of 1974–85, which the draft itself calls "the ones least likely ever to have been collected" (line 106). A House that ratified the Final Act and voted down the retrenchment treaty would lose nothing before 1974. And Britain gives Sembawang, the cap, Labuan, Fanning and Tonga for the least valuable paper in the schedule; Eyres-Monsell would say so. Either make the tranches conditional on one another, or give the sentence to someone and name who answers it.

**S11. Believability of the decision.** Britain's decision is believable on Tizard's figures (one device, late, against a rival with some fifteen), on the Exchequer's and on a six-year holiday from payment; it is the strongest part of the draft. Three things are too easy. (a) Lindemann's case, that the third clause makes the signature irreversible, is called "the best one made against signing" (line 184) and nobody answers it; he "loses" without a reply. One sentence from Tizard or Chamberlain would do it. (b) "no soldier or airman is in the room" (line 189): Hankey is also secretary of the Committee of Imperial Defence, and the Chiefs of Staff would expect to be heard; give the reason for keeping them out. J. H. Thomas, Dominions Secretary, is absent from a committee whose decision the dominions must sign beside. (c) Churchill and Hoare are both silenced by the same Petrograd sheet, and the cabinet "had foreseen the answer" on France. Each is defensible; together they remove every obstacle. The ratification at Westminster in the autumn, on which two tranches hang, has no named fight and no named loser.

**S12. Distance and travel.** Thalassia is on Oʻahu in canon (L1543, L1740). "By King's Messenger, eleven days each way by liner and rail" (line 131) leaves out the Pacific crossing; on timetables of 1932 London to Honolulu is about fourteen days. The dates still work at fourteen (Hayama ends 15 June, London about 1 July, cabinet 8 July, answer at Thalassia about 22 July). The draft does not say where the April accord is initialled; `CR-083` (line 152) says London, by "the Concord's Foreign minister". That puts Kaʻiulani, with the heart canon gives her, in London in April and at Hayama on 12 June. It can be done; say it, or let a deputy initial. Simon is away from the Foreign Office from late May to August, which wants a sentence.

**S13. France's ore.** Line 195: Thalassia answers "that France has no ore, no separating plant and no pledge". `CR-086` has France keep Madagascar's ores (its `A`, lines 100 and 209) and calls France "One holdout, with a school, gold and a reason to look". Drop "no ore".

**S14. Stale header.** Line 15: "Next: the third fresh-context review" (this is the sixth). Line 227: "the third review corrected it" is a revision note in the body. Line 3 dates the revision to "the author's decisions of 00:12" though the draft carries those of 07:27 and 07:31.

**S15. Kaʻiulani is named and then forgotten.** Line 179: "Kaʻiulani, the Concord's Foreign minister, hands Simon the draft … He hands it over subject to the Council". The calendar (line 235) still has "Concord Foreign Minister". The files to revise (line 277) list the character bible for "Julian, Churchill, Tizard, Lindemann" and not for Kaʻiulani or Hoare. No set piece uses her.

## Minor

- Line 111, last sentence: "…when the fleet and not a treaty keeps a strait open; which would make the Realm the policeman of Malaya and the enemy of Nanjing at Hong Kong." The "which" has lost its noun (the base at Singapore).
- Line 212: "none but those four is bound by it"; the sentence before names "the powers on the shores and the Concord", which is two powers and the Concord or four signatures. Say which.
- Line 155 has the Dindings "under study as its own precedent"; S14(c) at line 588 says "the Dindings is no precedent".
- Line 184 cites L1572 for Lindemann calling the factory impossible; L1572 is his misreading of 1922, and "impossible" is L1575 and L1578. Tizard's citation (L1575) is right, so the open item at line 599 can be closed.
- Line 183: "On the money voted since 1931" does not fit a programme begun in 1928.
- Line 227: "the meridian has no margin and may be moved to 156° W" leaves a treaty term undecided while the ledger entry (line 325) says 155° W.
- Line 174: the Hawaiian privy council's advice "in June" is not in the calendar. Line 156 and the calendar: the Sultan signs the lease in July and sails for England in July; say where he signs.
- Line 129: talks open "through Simon, Chamberlain, and Cunliffe-Lister"; the calendar (line 235) adds Eyres-Monsell and Hoare.
- `A2`'s "five concrete gains" and `A2a`'s four statements cover the same ground, with a note (line 102) on which governs. One of them can go.

## Leftovers from earlier revisions

The draft is hard to read for its apparatus. Lines 5–9 are five "What changed" paragraphs; lines 575–608 are four lists of findings from three reviews, and parts of them are now false: line 592 (B2 above), line 603 ("whether the Concord holds Rabaul", decided by `T-P1`), line 599 (Tizard's line). Process notes stand in the body: "(restores author's 22 Nov Rung B decision)" in `C1`'s heading; "The author accepted that the clause tips its readers off (19:32); Tizard is the reader" (line 183); "Canon's sentence on Hoare is itself PROPOSED … so his lines here are a proposal to bring him on" (line 188, which repeats `T-B5b`); "(the drafter's fuller list…)" (line 102). Cut to one "What changed" paragraph for the current revision and one list of open findings; move the rest to the commit message.

House style. No exclamation marks and no "(Fixes …)" labels were found. `A2a`, `B1`'s sub-items and `B5` are in plain prose. `B2` to `B4`, `C1` and Part D are not, and it matters for two reasons: they are the text an integrator will lift into the storyline, and their bold type and intensifiers ("strictly", "explicitly", "exact", "concrete", "honestly", "real") hide which words are terms of a treaty. The three worst passages:
1. Line 164 (`B3.5`): one paragraph carrying Zamboanga, Sulu, Mariveles, the Cortes, the separatists, sugar and the Sultan of Sulu, with seven codes and four parentheses.
2. Line 211 (`C1`, concessions): "development from 1932, post-1935 deliveries strictly as *additional* tonnage on top of Arkansas bauxite, preserving the Gulf's alumina refinery royalty at … and respecting the 1937 Hayama Annex bar at …".
3. Line 120 (`A3`, who opposes): a single sentence of about 170 words with three numbered groups, two dashes and six citations.
Rewriting these three and stripping the bold from `B2`–`B4` and `C1` would be enough for integration; Part D can stay a list.

## The five drafts together

- Votes and ratification agree with `CR-086` `E1`: the delegations vote the Concord's treaties in July, the crowns ratify on 1 August, the annuity bill passes both chambers by majority, and the two counter-signatures with `C-1932-ANZ-DEFENSE` are one of the Senate's five two-thirds votes. `CR-084` does not say the three are taken in one vote; `CR-086` does.
- Article I as `CR-086` `C1` gives it (no separating plant, no test, all irradiated fuel to the Works; the Realm's pledge to a signatory "that keeps the article") matches line 180. `CR-086` adds that the pledge holds in war; `B5` does not need it.
- Japan: `CR-085` `A5` and `CR-086` have Japan's crown countersign the pledge, which fits line 189, but neither records it as Britain's condition (S9). Hayama on 12–15 June, the coup of 15 May and Saitō's cabinet of 26 May agree across the four.
- Caledonia: `CR-083` has the same two near-end annuities, $93m and the Severance Act of late June. It lacks the commencement-order remedy and proclaims the Republic before the bill (B2).
- The workbook's figures agree with lines 133–141 (17 of 53; $48.8m a year; $93m, $169m, $114m; 30.9%; nothing paid in 1932–33 to 1937–38), except S2.
- France's ore (S13). The misplaced bulk-approval rows in `CR-085` and `CR-086` (B1).
- `CR-087` shares nothing with this draft.

## Approvals against the quoted words

- **`R-10` (line 92).** Not clear enough. The author's words, "I approve the other proposals as well", answered one sentence that named three things: "the widened court bench for Article I complaints, the pledge holding in war, and Hawaii as Tonga's guarantor", "among them". Only the third is this CR's. The words fairly cover the proposals of that report; the draft does not say which of its sentences were in that report, and it points to a list that includes revision 9's work. As written the row could be read to approve the coup in the committee, Lindemann's breach, the messenger, the cabinet of 8 July and the commencement-order remedy, none of which the quoted sentence names. List them and let the author see the list, or keep the label to Hawaii as Tonga's guarantor.
- **`T-B5a` (lines 177 and 358) and line 183** rest on "the author … at 19:32". No words of 19:32 are quoted in `## The author's request`; the draft's own list (line 591) records that an earlier reviewer read them as a question. The label "decided" reaches beyond the file. Quote them or mark the tension PROPOSED here.
- **`M-0`, `T-F1`, `T-S1`** cite "author, 23 November 2026, 23:11" and quote the sheet. By the draft's own account (line 63) those words are the sheet's and are his by adoption at 23:14. Cite 23:14, as `M-1` to `M-4` do.
- **`M-4`** is approved for "the 10° S line as a Concord protocol and the bar on fortifying the piers". The 155° W limit and the annex are correctly kept PROPOSED (line 566); the row's "(Tutuila and Swains excepted)" should not sit inside the approved text.
- **`M-2`** approves "Palau and Labuan"; Palau has no section, as the draft says three times.
- **Line 134** labels the near-end tranches APPROVED by item 84-8, which said the far end; the approval is the words of 23:52 and 00:12, which the line cites last.
- Sound as labelled: Kaʻiulani (07:31); `T-A2` (23:52 and 00:12, item 4); `T-P1` ("6 Pacifica") for who holds the islands, with the form of the holding rightly left open; `T-K1`, `T-L1`, `T-O1`, `T-U1`, `T-B1`, `T-R1`, `T-NF1`; the dominions (19:55, 20:11). `T-B5b` and `T-B5c` are correctly PROPOSED.

## History checked

On the web today:
- Thomas Falkland Carey, born 1903, died 1966, Resident in Brunei 1931–34: confirmed (Wikipedia, "Thomas Carey (cricketer)"). He was twenty-eight, which a scene may want to use.
- Ottawa: Baldwin led the delegation with Chamberlain, Runciman and J. H. Thomas, crossing on the *Empress of Britain* in mid-July (*Time*, 25 July 1932); the conference opened on 21 July (Wikipedia, "British Empire Economic Conference"). Baldwin and Chamberlain are confirmed. Cunliffe-Lister was not named in what I could fetch; from my own knowledge he went, with Hailsham and Gilmour. Thomas's presence at Ottawa should be added to line 191.
- The Dindings: in the Commons on 1 November 1934 Cunliffe-Lister said every Colonial Secretary since Joseph Chamberlain had agreed it "ought to be done", so "under study" in 1932 is fair (Hansard, Dindings Agreement (Approval) Bill).

From my own knowledge, not fetched: Hankey was Cabinet Secretary from 1916 to 1938 and secretary of the Committee of Imperial Defence, so he keeps the minute. The cabinet list of 5 November 1931 is right (Hoare had the India Office from August). The election was on 27 October 1931 and sterling left gold on 21 September. Churchill left the Treasury in June 1929 and had known Lindemann since 1921. Labuan (1846, 1848, 1907), Limbang (1890), Seria (1929), the Tongan treaty of 18 May 1900, Sālote's dates, de Jonge's term, Ruijs de Beerenbrouck's third cabinet, Tokelau (1926), Fanning and Washington in the colony from 1916 and Inukai's death on 15 May are right as stated. In history Simon spent June and July 1932 at Lausanne and Geneva, which the conference at Thalassia displaces. Boven-Digoel dates from 1927, under de Graeff; "de Jonge's internment camp" (line 208) should be "the internment camp". Geography: Penrhyn at 9° S, the Cook Islands west of 157° W, Rabaul at about 4° S, Nauru just south of the equator, Apia and Tutuila south of 10° S and Kupang just south of it are right; the western Society Islands begin near 154°40′ W, so 155° W does exclude French Oceania with no margin.

Not checked: the £2,113,000 of 1929, the Lutong pipeline's date, Fanning Island Limited, the instalment dates, NKPM's holdings and the KPM's legal position.
