# Fresh-context review 3-A: CR-068 (revision 29) and CR-065 (revised 12 November 2026)

Reviewer: independent, fresh context. Read: AGENTS.md; the canon extract (§§8–13); CR-068.md in full; CR-065.md in full; from the neighbours only the cited rows (CR-059 E2, H7, W4, W12, W15, V1–V17, S3, CT8; CR-060 C2, C4–C6, D4, D4a, D5, D9, CT6; CR-062 A1–A6, T1–T15, O6, M3 and its §12 text; CR-067 A1). Not read: anything under outputs/sessions/, the companion files of CR-068 (lincoln-career, samples, two-houses, sources, record), so rows K1–K27 and A1–A13 are unchecked. `lint_canon.py --only` is clean for both candidates. No file was edited.

Classes: BLOCKER (fix before integration), SHOULD-FIX, NOTE. Each finding says whether it needs the author or is mechanical.

## Verdict

- **CR-068: not ready for integration.** Round G9a and the §12 text for 1865 contain one sequence that cannot happen as written, one motive that contradicts the position its holders take, and four drafter suggestions that are still "to confirm" but are written under an APPROVED label. Everything before 1865 is consistent enough to integrate after mechanical fixes.
- **CR-065: ready after mechanical fixes**, subject to the author approving the CR as a whole (its header still says every decision is PROPOSED).

## 1. Blockers

**B1. Unconfirmed drafter suggestions sit inside APPROVED text (labels; author decision, then mechanical).**
Four items are marked "PROPOSED: drafter's suggestion of 13 November 2026 … to confirm": the Council's adoption of the Terms in September 1863 (CR-068 G6, line 264; CR-060 C5; CR-067 A1), the cut wire of April 1864 (G8, line 322; CR-060 D4a), why Hawaii agrees (G9a, line 355) and the order of autumn 1865 (G9a, line 356). Against that:
- The label legend (line 7) says of suggestions "none is left"; "Open decisions" (line 911) says "Everything else in this CR is decided"; "Before adoption" (line 947) says "Nothing in this CR is blocking". None of the four is listed as waiting.
- The §12 storyline text (line 643) is labelled APPROVED and states "In September Elias brings the Enabling Law himself", which belongs to the unconfirmed order. The next paragraph (line 645) carries two labels at once, "[APPROVED — CR-068] [PROPOSED — CR-068]", with no indication which sentence is which.
- The score table (line 400) still says G9a's weight "waits on the author's answers to the second review", while the status header says revision 29 resolved it.
- Two of the four facts (Council adoption, cut wire) appear in no storyline block in CR-068, CR-060 or CR-067, so they would be lost or orphaned at integration.
AGENTS.md: "Do not mistake an editorial proposal, assistant suggestion or historical illustration for author-approved canon." Fix: the author confirms or rejects each; then one label per sentence, the list in Open decisions, and a storyline sentence for each confirmed fact.

**B2. The bargain of 1865 cannot be conducted on the calendar given (chronology; author decision).**
G9a (lines 353–357) and the §12 text: Elias brings the law in September; both confederal chambers pass it by two-thirds in September and October; California ratifies; Sherman loses the argument on the term and sails in October; Lot and Victoria "bargain for the revenues and for the list of provisions the cabinet may not legislate around, and win both; they side with Sherman … and lose"; Hawaii ratifies in December.
- A ratifying legislature can accept or reject a text; it cannot amend it. The revenues and the list must therefore be in the bill the chambers pass by October. Honolulu is about twelve days from Monterey each way (CT24). A bargain with Lot and Victoria between a September introduction and an October passage allows one exchange at most. Either the bargain was made before September, which contradicts the picture of a law he "brings himself" after six months of drift, or it was made by the resident delegation on instructions, which is not what the text says.
- "Sherman argues for a term there and loses" (line 356): "there" has no referent. Sherman is Inspector-General and sits in no chamber. By the time Lot and Victoria "side with" him he is at sea or in Washington.
- "Washington signs in December knowing that only Hawaii's ratification is outstanding" (line 356) and "Victoria carries it in December": the order of the two December events is not given, and news of a December vote at Honolulu cannot reach Washington in December. CR-062 T1 and its §12 text say nothing of the Enabling Law. The six months' pressure is that Washington "asks who is bound"; if Washington then signs before the answer is law, the pressure is shown to be weak.

**B3. Hawaii's reason for agreeing contradicts Hawaii's own position, and rests on a premise CR-059 removes (causal logic; author decision).**
- Line 355: "For Hawaii the guarantor has to outlast the new states' first generation; a guarantee of ten years would protect it only until they have learned to count." Line 357 and the §12 text: Lot and Victoria argue for a term of years and lose. Both cannot be Hawaii's view. As written, Hawaii's stated motive is an argument for the thing Hawaii opposes.
- The motive is that "Hawaii's half of the Council is about to end". CR-059 CT8 (decided 12 November) says "Constitutional ratification stays with the founding states". Hawaii therefore keeps a permanent veto on every amendment, including each accession charter (CR-059 V10 is "ratified by California and Hawaii"). What it loses is parity in ordinary Council votes, and the Enabling Law itself moves legislation from the Council to the cabinet. The reader is not told why a founding state with a standing veto needs a personal guarantor, or why it ratifies after losing on the one point it contested.
- "They could keep parity by refusing to ratify the accessions, and that would wreck the peace": the treaty cedes territories; nothing in CR-062 makes their admission as member states a term of the peace.
The fact that the guarantor later breaches (canon §17) is intended irony and is fine. The gap is the motive in 1865.

## 2. The year 1865, place by place

| Event | CR-068 | CR-062 | CR-059 | CR-067 A1 | CR-065 | Canon |
|---|---|---|---|---|---|---|
| Richmond's armistice | "March to June" (G6b) | April (A1) | n/a | n/a | "in a month" from 3 Feb (L6), then March–June | March–June |
| Pacifica's armistice | May (G9a); "two weeks" before 31 May (B16a) | mid-May, signed by Elias as Protector (A1) | "armistice of May 1865" (V2) | May | March–June | March–June |
| Treaty of Amity | last week of May, last act as Protector (G9a) | last week of May (A6) | n/a | n/a | n/a | spring 1865 |
| Protectorship ends | last day of May | same | "laid down in May 1865" (V11) | same | n/a | not stated |
| Chancellor | June–December | same | n/a | same | n/a | chancellorship lapses with the Enabling Law |
| Enabling Law | chambers Sept–Oct; California; Hawaii December | "of December" | "life office of 1865" | "in December" | n/a | 1865 |
| Western treaty | Washington, December | Washington, December (T1) | protocol "signed with the treaty in December 1865" | n/a | n/a | 1865 peace |

The dates agree across the five drafts and with canon. Remaining findings:

- **SHOULD-FIX (author). The laying down is both pledged and "unasked".** G8 item 6 (line 328): Hawaii's price is "no renewal of the Protectorship after the war", accepted in the chamber and written into a Council resolution. G10 and CR-059 V11: he laid the office down "as he had promised". But MD4 (line 164) says he "lays the yearly power down unasked"; G9a (line 346) says "Everyone expects him to ask for one more year … and Hawaii would grant it"; the score table has Lincoln's reading expecting him to keep the power. If the resolution binds, there is no surprise and no risk, and Hawaii would not grant what it forbade six months earlier (CT29's adapted case says a renewal "breaks the price of 1864 in its first test"). The round's drama depends on the pledge being weak; its legitimacy depends on the pledge being strong.
- **SHOULD-FIX (author). Victoria's reason for giving up the yearly vote is contradicted by the record.** G8 item 6: three renewals "have shown her that Hawaii's yearly vote on the man cannot be used". TL6 and its table show her using it every time: the relief boat in 1862 (CR-059 W4), the delay of 1863 that nearly ended the office, three conditions in 1864.
- **SHOULD-FIX (author). The case for life is weaker than the page admits.** (a) The Washington argument: the vendor credit is paid "through 1872" (canon §12; CR-062 T4). A ten-year term outlasts it, so Washington's question does not support a life office. (b) The votes are missing. Two-thirds of both confederal chambers and California's legislature pass a life office in about six weeks, in a subordinate clause. In November 1864 California's delegation split five to four, with two "constitutional men" who would not confirm even a yearly office (line 329). No vote, opponent or count is given for 1865, and California's president is not mentioned. (c) Canon §12 gives Marcus the opposite view to Sherman ("can accept lawfully established durable executive authority"); G9a has no advocate for the office except its holder. (d) Sherman's objection is left unanswered by design; that works as irony only if the reader has first seen why sensible men voted yes.
- **SHOULD-FIX (author). What six months as Chancellor show.** "The interior has no lawful government" (line 349) assumes that occupation authority came from Article XIV alone. Under an armistice the lines are held by the ordinary law of occupation, and defence is a common power of the Confederation (canon §8). The spent decrees and the unpaid garrisons are plausible; the commander "who asks under what law he holds his court" is not obviously so. Also "Nobody obstructs him" removes any antagonist from the half-year that is meant to carry the argument.
- **SHOULD-FIX (mechanical). Washington's commissioners.** G9a and B16a place "Washington's commissioners" among "the callers at Monterey"; CR-062's place table rejects a Union delegation at Monterey because it "reads as surrender", and the treaty is negotiated by Vallejo and Sherman in Washington from November. Say where the armistice commissioners sit in the summer.
- **NOTE.** G9a's "dropped his promise within three months: the amendment failed" attributes to the Union's change of President a vote lost in Lincoln's own lame-duck House (CR-065 L3). Loose, not wrong.
- **NOTE.** G10 heads Lincoln's reading "MD4, confirmed by 1865"; MD4's row says it was "wrong again in G9a". Pick one.

## 3. 1863–64

Consistent across CR-068, CR-060 and CR-067: Terms printed in the last days of August 1863; Council adoption in September (PROPOSED in all three); Nevada Enabling Act 21 March 1864; Washoe retaken in April under the first reservation, Vance commanding, about 1,500 men, garrison out armed and unparoled; Victoria's conditions attached afterwards at the May renewal, four asked and three granted (no annexation, Carson's guarantees, entry and quarantine), Washoe's self-determination refused; blind vote on Saturday 12 November 1864, twelve to six; Hawaii's price as in CT17. The weekdays are right (8 November 1864 was a Tuesday).

- **SHOULD-FIX (mechanical, research 38). The telegraph makes some of the "mails" too slow.** CR-060 D4a has the Union's wire running through Salt Lake to Union Washoe until April 1864. Carson is a few days from San Francisco. Before April 1864, anything printed in Washington is therefore known at Monterey within about a week. CR-068 G4 has the State Department's printed circular of June 1862 reach Monterey "in August", and TL5 treats a lag of weeks as general. The blind vote and the inaugural of 1865 fall after the cut and are consistent.
- **NOTE (research).** "The Union's wire to Denver" (G8; D4a): the historical trunk ran by Fort Laramie and South Pass, with Denver on a branch. South Pass and Fort Bridger become Pacifican (canon §12), so "ends east of the divide" is safer than naming Denver.
- **SHOULD-FIX (author). Standing instructions.** At the two decisive moments Victoria is at Honolulu and Hawaii's delegation acts on "her standing instructions" (G8 item 6; G12; W1: "instructed by his wife"). A vote announced on Wednesday for Saturday could not be referred, so the instructions must already have contained a constitutional price for a contingency nobody foresaw. Lot, king since November 1863 and jealous of royal authority (canon §12), is not mentioned. Canon §8: "no confederal article assigns the Kuhina Nui an exclusive personal countersignature"; AGENTS.md: "do not restore the superseded personal-veto … explanations". The draft should attribute the instructions to Hawaii's government. This is not declared in any canon tension.
- **NOTE.** CR-067 A1 and CR-060 C5 say Hawaii's delegation voted for the September resolution "because the Terms bind him". That resolution also pre-authorizes the occupation of Washoe, the ground of Victoria's victory of 1860. One sentence on why her delegation accepted the reservation would help.
- **NOTE.** CR-059 is not clear whether the Oregon protocol is signed with the armistice (V1, V2) or with the treaty in December (line 422). CR-068 CT9 follows the first.

## 4. Internal consistency of CR-068 (mechanical unless marked)

Revision 29 added G9a and B16a without carrying them through the apparatus:
- Line 48: "twenty-two beats"; there are twenty-three. Part G heading (line 147) omits G9a; Part H heading (line 441) omits B16a.
- Line 51: "It changes no date and no approved decision of its own" is stale; the list of new facts omits the lapse, the eighteen-member Council, the sugar contract and the September resolution.
- B16 (line 546) and the scale table (lines 590, 593): "three years in three sentences" covers November 1864 to December 1865. Act IV is given as "Eight months" and "Under 1" year but now runs to December 1865.
- G9a/B16a are absent from the weights table, the stratagems table, "Where Elias could have lost", the chain X1–X16 (TL2 claims every beat is in it), O1–O2, TL10, the map to Parts A and C, and the CT-ELIAS and CT-SHERMAN additions. Whether G9a is a heavy beat is an author decision (TL1 says four).
- §12 text for 1864 (line 639) states as APPROVED fact that "the peace must be ratified by both chambers and both founding states"; CR-062 O6 has "Exact procedure OPEN", and G8 admits the rule is new to canon. No canon tension declares it.
- "Review" (line 960) lists checks at revision 23; revisions 24–29 are self-reviewed.
- "Fact changes: none", with Lincoln's `add_person` deferred. AGENTS.md asks for identities in the draft's fact list.
- CT24's table is headed "When (1863)", begins in November 1862 and has its April row out of order.
No leftover of the Port Townsend incident or Marcus's offer was found outside the revision history.

## 5. CR-065

- **SHOULD-FIX (mechanical).** "Self-review" (line 418) says no fresh-context review has been run; line 369 lists fixes after one. The impact preview is dated 8 November, before the revision.
- **SHOULD-FIX (mechanical).** M4 and Part VI describe the mirror as dissolution against election ("The other calls one he will win"). CR-068 G8 now makes the mirror the blind memorandum against the blind vote. CR-065 mentions the blind vote only in open decision 14.
- **NOTE (labels).** The header says every decision is PROPOSED; nineteen open decisions read "Decided (author)". The file explains the difference once (line 367). CR-068's storyline blocks are labelled APPROVED while resting on CR-065 rows that are PROPOSED (M1, P2, E6, L2).
- **NOTE.** L6: Stephens expects an armistice "in a month"; CR-062 A1 dates Richmond's to April.
- The arithmetic holds: 120 to 103 of 223; 107 to 64 is seven short of two-thirds.
- Still open by its own account: Butler, the western armies' winter, what the captured letters reveal, Richmond's motive at Hampton Roads.

## 6. Canon and protected intent

No breach of the four protected intents. The account of the nations depends on Bear River not being a Pacifican massacre (CT15 says so). Departures not declared as tensions: the standing instructions (section 3); the ratification rule for treaties (section 4); free navigation as the guarantor's condition in 1871 and the fugitive agreement as Richmond's price for the association treaties (both marked "new" inline in G12, with a storyline sentence, but no tension). All other departures found are declared (CT3–CT29).

## 7. Literary judgement: the three weakest points

1. **The life office is won offstage.** The book's largest transfer of power is carried by a contractor, a commander and "callers", told "quickly, with no shot fired", with no opponent who has a face and no count. The one objection is left unanswered, and the Chronicler declines to choose between readings, as he also does in W1 and B16. Used a third time, the reserve reads as evasion.
2. **Lincoln has no voice yet, and loses by formula.** Ten of his papers are "argument only; text OPEN". He is "right and loses" in G5, G9, G10 and G11, and his wins are sentences. Elias's one outright loss (G4) is repaired inside the same beat by his own act. Because O1 has him announce every decisive move beforehand, the reader is rarely behind him.
3. **The judge is absent from her own verdicts.** TL6 makes Victoria the judge, but in November 1864 and in 1871–72 she is an ocean away and acts through instructions; the twelve-to-six count with California at five to four is arithmetic arranged for effect. The people neither man asked are "left to the reader" three times (CH7, G4, G6b), which the reader will notice as a pattern.
