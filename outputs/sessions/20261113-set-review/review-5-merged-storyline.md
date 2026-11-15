# Fresh-context review 5: the nine storyline texts applied together (13 November 2026)

Reviewer: a separate agent context given only AGENTS.md, a verbatim extract of canon §§8–13 and the nine drafts' "Storyline text" sections, with greps in the drafts allowed for single questions. It did not see the session records or CR-068-record.md. Points marked "(my knowledge)" are the reviewer's own. State reviewed: commit 91739ce.

## Verdict

No, the nine texts cannot be merged as they stand. The biggest obstacle is canon §10's paragraph "A Pacifican California column…": four drafts and an unlisted tenth text (CR-066 Part E) all target it, two anchors disappear once the others are applied, and the result runs 1862–63, back to October 1861, then forward to 1864. Section 12 has the same problem on a smaller scale, and five events are told twice in different words.

## Merge map

| § | Anchor (first words) | Drafts and action | Verbatim? | Resolution |
|---|---|---|---|---|
| 8 | "Throughout the 1850s, California's sovereignty changes" | 068 inserts before [OPEN] | yes | apply |
| 8 | "the 1858 paragraph" | 059 inserts after | ambiguous: three paragraphs qualify | place after "The external crises…" (ends with British Columbia) |
| 8 | "Washington threatens retaliation" | 068 cuts the bondholder clause | yes | apply |
| 8 | "At the **Carson Convention**" | 068 inserts after | yes | apply; see contradiction 12 |
| 9 | "Fort Sumter's bombardment" | 068 appends | yes | apply; put 064's Halleck paragraph after it |
| 9 | "Demands and attempted… / Sherman organizes readiness" | 068 appends; 064 and 067 insert after the same last sentence | yes | 068 before the Sherman sentence, then 067; move 064 up |
| 10 | "John Whiteaker negotiates" | 059 wraps the sentence | yes | state that the paragraph's other sentences stay |
| 10 | "Southwestern and interior expansion follows" | 060 replaces | yes | apply |
| 10 | "A Pacifican California column" | 061 replaces the first half; 059 inserts after a half-sentence; 060 inserts and replaces; 068 inserts after the paragraph; CR-066 Part E | yes today; 068's anchor opening is removed by 061 | split into three paragraphs (collision 1) |
| 10 | "Bear River becomes a Pacifican atrocity" | 060 replaces the sentence; 061 replaces the rest of the paragraph | yes | 060 first, then 061 |
| 10 | "…come down the Snake under its protection." | 060 inserts after (Owyhee) | no, in neither canon nor 059's text | collision 2 |
| 11 | "Federal wooden ships withdraw" | 064 replaces sentence and [OPEN] | yes | also delete the two leftover Virginia sentences |
| 11 | "The difficulty lies in delivering" | 063 inserts after | yes | apply |
| 11 | "Confederate commanders attack Grant at Shiloh" | 064 replaces | yes | apply |
| 11 | "Farragut attempts New Orleans" | 063 two inserts, one replacement | yes | apply; split the paragraph |
| 11 | "Sherman refuses an assignment" | 067 inserts mid-paragraph; 068 after | yes | apply |
| 11 | "Grant and Porter bypass" | 063 replaces sentence 2 to [OPEN]; 064 after "…before adding an escape."; 068 after | 064's anchor is removed by 063 | 063, then 068 (August 1863), then 064 |
| 11 | "The consequences of the altered armored fleet" | 064 replaces "first sentence" | that sentence is not the Drewry's Bluff one | collision 8 |
| 11 | "At Mobile, Eads's river monitors" | 064 paragraph before; 063 replaces the Logan sentence; 064 replaces the last sentence; 065 paragraph after | yes | compatible |
| 11 | "In December 1864–January 1865" | 063 replaces and inserts twice | yes | apply |
| 11 | "The paired failures at Mobile and Petersburg" | 064 replaces two sentences | yes | contradiction 5 |
| 12 | "In the 1864–1865 consolidation struggle" | 065 inserts mid-paragraph; 068 appends | yes | collision 4 |
| 12 | "McClellan wins a civilian swing" | 065 replaces; 062 after the kept last sentence; 068 after the paragraph | 068's anchor opening is removed by 065 | 065, then 062; move 068 to the end of §12 |
| 12 | "The Western line is agreed" | 061 inserts mid-paragraph after "103°W."; 062 and 059 after the paragraph; 060 after 059 | yes | 062, 059, 060; move 061 to the ratification paragraph |
| 12 | "The surviving Puget Sound enclave" | 062 inserts after | yes | apply |
| 13 | "…go south through Paso del Norte from New Mexico." | 061 inserts after | yes | apply |
| 13 | "Travel-paper controls" / "Victoria objects" | 068 replaces | yes | apply |
| 13 | Grant's-war treaty; "1872" | 068, "at integration" | no anchor given | name the sentences |

## Collisions

1. **§10 "A Pacifican California column" (059, 060, 061, 068, CR-066 E).**
   - 061 turns the first half into nine paragraphs and says the Idaho, Washoe and Nevada sentences "stay, as amended by CR-059 and CR-060".
   - 059 inserts after "Idaho's mining districts turn toward the Northwest in 1863", which is half a canon sentence; 060 inserts after the whole sentence. No order is given.
   - 068 anchors on a paragraph opening that 061 deletes.
   - 061 carries a placeholder for CR-066's Taos paragraph, which is not in canon ("Taos article" does not occur in master_storyline.md). 061 later relies on it: "the Taos article has settled its account with 1847".
   - Fix: three paragraphs. (a) Rio Grande: 061 with CR-066 E. (b) Columbia and Idaho: 059's text moved up beside the Whiteaker and enclave material, then 068's Port Townsend convention. (c) Montana and Washoe: 060.

2. **060's Owyhee paragraph.** Its anchor is a sentence of 059 decision row I7 that 059's storyline text never uses; that text has only "Boise grows beside a Pacifican post." "The doctrine" and "the mounted police" are therefore never introduced. Fix: 059 adds the Camp Boise sentence and 060 names both.

3. **060 against canon and itself.** Canon's "Washoe is retaken in 1863–1864." sits between 060's anchor and the sentence it replaces, and 060's text repeats it. 060 also says "Pacifica retakes Washoe in the spring of 1864" and "in March Congress passes Nevada's Enabling Act", then "In March Congress passes an enabling act". Canon's closing [OPEN] sentence is rewritten but not listed as replaced. Fix: replace from "Washoe is retaken" to the end of the paragraph, with one date and one Enabling Act.

4. **§12 dissolution (065, 068).** 065: "its voters give him the Assembly he asked for. He dissolves the Assembly once the news…" puts the result before the cause. It cites "(CR-068)" in prose and refers to the blind vote before 068's text, later in the same paragraph, introduces it. Fix: drop 065's last sentence; keep its first two after 068's block.

5. **Lincoln's *Oregonian* letter, June 1866 (059, 068).** 059: "who dismisses a Providentor for life?" 068: "in which country they would rather be able to lose an election". Elias's answer also differs. Fix: one telling, in 059's paragraph.

6. **Lincoln's 1867 letter and the vote (062, 068).** 062 has the *Chicago Tribune* and "The Senate consents"; 068 has "a public letter" and "the Senate ratifies". Fix: keep 062.

7. **Evacuations.** Fort Union's march over Raton Pass is told in 061 §12 and twice in 062. Port Townsend is in canon ("is evacuated under the treaty") and twice in 062. Fix: once, in 062's ratification paragraph.

8. **Drewry's Bluff (064).** The paragraph's first sentence is "The consequences of the altered armored fleet continue…". Replacing the second sentence loses Charleston 1863. Either way the paragraph's [OPEN] "Whether these operations occur" now contradicts a dated battle. Fix: name the sentence and rewrite the [OPEN].

9. **Texas, February 1863.** 061 has the San Antonio convention, with no Pacifican signatory named. 068 has the credit terms printed. Canon (CR-022) has the trip itself, which stands four paragraphs after 068 has already used it. Fix: move the CR-022 paragraph ahead of 068's block and cross-refer.

## Contradictions

1. **Sherman at Vicksburg.** 063: "Sherman bridging the river at Bridgeport" and "Sherman's leading division comes onto it". Canon makes Sherman Pacifican, and 064 has "Steele… leads the XV Corps through Vicksburg". Fix: Steele.

2. **Jackson, July 1863.** 063: "Grant drives Johnston out of Jackson". 064: "McPherson drives Johnston's relief army… out of Jackson". Fix: Grant sends McPherson.

3. **Oregon's convention.** 059: "The convention never meets" and "meet at last at Salem". 068: delegates "sit at Port Townsend as a convention and adopt a state constitution". Fix: 059 says it never meets in Oregon and mentions the rump.

4. **Enabling Act and exclusion.** 059: the Act offers statehood "without slavery or exclusion". 062 (Sumner): "the Union's own Enabling Act never removed it". Fix: reword 062 as "never got it removed".

5. **The East.** 064: "the war runs its historical course". Against that:
   - 065's Early is "beaten and not destroyed";
   - 063 sends Terry's eight thousand to Mobile, so there is no Fort Fisher (my knowledge);
   - canon's "paired failures at Mobile and Petersburg" has no Petersburg failure narrated by any draft.
   Fix: replace 064's sentence with the actual divergences and one sentence on Petersburg.

6. **Peonage.** 068 (early 1863): Pacifica's account cites "the ending of peonage in New Mexico". In 061 the compact, signed that spring, only promises it "when the peace comes"; the ordinance is December 1865. Fix: "its undertaking to end".

7. **No operation in 1864.** 068: "After Lincoln's refusal in February he… orders no operation during the Union's campaign." 060: Washoe is retaken that spring: "He moves in the first weeks the roads allow." Fix: "after Washoe".

8. **First armoured ship.** 068: "the first armoured ship completed is stationed at Honolulu". Canon §10: "The first operational Ericsson turret ship helps secure the lower Columbia". Canon §8 already has "some armored warships" by April 1861. Fix: say which hull.

9. **Port Townsend.** 065: Pacifica "makes no move against Port Townsend". 068: "A force staged on the Sound to take Port Townsend". Fix: 065 says "until the vote".

10. **Victoria in 1864.** 060 gives three conditions: "no annexation, Carson's guarantees kept, and Washoe to choose for itself". 068 gives "among them Hawaii's control of entry". These are compatible but never stated together. Fix: list all four in §12 and cross-refer from §10.

11. **Victoria in 1866.** 059: "Victoria, in San Francisco that summer" follows sentences about the 1865 peace. Row X2 means 1866, matching canon's voyage. 059 then puts the Salem convention (July–August 1866, row V5) before "In June 1866". Fix: date and reorder.

12. **Credit.** 068 (1862): "its war advances end when both governments accept an armistice". 062 (1865): Washington asks for a ban on credit "and Elias refuses". These are reconcilable only through a gloss in 068's decision notes. Fix: add "beyond war advances" to 062.

13. **First instalment.** 062: "Before the vote the first instalment is counted into the New York Subtreasury", then ratifications "exchanged… against the first payment". Fix: say it is deposited, then released.

14. **Vicksburg figures.** 063's text gives "about fifteen thousand" surrendered. The 12,500 escapees appear only in decision rows, and the 12 November sheet defers "which set of Vicksburg numbers stands". Keep [MODEL].

Checked and consistent:
- Electoral count: 120 to 103 is 223, which matches no Nevada, California or Oregon (my knowledge of the 1864 apportionment).
- Mobile force: three ironclads plus *New Ironsides*, eight thousand men.
- Farragut: killed February 1865; nothing later has him alive.
- Western command: Thomas, in 064 and 065.
- Deseret: an associate from December 1862, a member in 1867, once 060 replaces canon's "accedes".
- Oregon 1866: Lane and Nesmith speak; Lincoln and Elias appear only in print.

## Order and form problems

1. **§12 order.** The merged section reaches 1867 and 1869 before canon's "In 1865 Elias secures the Enabling Law", so "Providentor for life" (059) is used before it exists. Reorder: 1864 home front; Union election; armistices and lines; Enabling Law; treaty of December 1865; consent in 1866; Alaska and ratification; Lincoln coda.
2. **Forward references.**
   - 060 §10: "the October recall" (introduced later by 059) and "Pacifica had printed, the summer before" (the Terms of Monterey, §11).
   - 060: "Connor's camp".
   - 061: "Sunset articles", "Sunset road".
   - 059 §12: "the Chinese floor", "the Native article", Nesmith, and an Idaho charter never narrated.
   - 062 lists a Washington Territory charter that no draft narrates.
3. **061 Navajo paragraph** runs January 1863, spring, December 1862, May 1863, 1865.
4. **064 Hampton Roads** leaves "Virginia gains a period of local advantage… can eventually make her position untenable" after her destruction on 11 May.
5. **Memo language in prose.**
   - 064: "runs its historical course".
   - 063: "(open decisions 8 and 9)".
   - 065: "(CR-068)".
   - 061: the italic CR-066 placeholder.
   - 068: "at integration" used as an anchor.
   - 059: "the cause that lost in 1859 because Lane carried it survives because…".
   - 060: "where the doctrine fails before it holds".
6. **Labels.**
   - 068's text is all [APPROVED], yet its header says DRAFT and several sentences rest on PROPOSED facts in 059, 060 and 065.
   - 061 raises canon's [PROPOSED] on Barboncito and on abolition to [APPROVED — CR-015]; check the register.
   - 065 doubles a label.
7. **Coverage comments.** All nine drafts have at least one. Missing on 063's last three blocks, 067's second, and 060's §25 sentence.
8. **067's rule.** "An operation beyond it needs a new resolution": no draft gives the Rio Grande, Salt Lake or Washoe operations one.

## Literary effect of the merged text

1. **Victoria's assents.** The same move occurs in 1861, 1862, 1864 (twice), 1865, 1866 and 1867. Stage two, the relief steamer and the blind vote, and report the rest in a clause.
2. **Lincoln and Elias.** The correspondence is spread over §§9, 11 and 12 as "answers in a public letter" eight or more times and becomes a list. Group the 1863–64 exchange in one paragraph and summarise the minor letters.
3. **Washoe.** Elias's motive is split: the reservation is in 068 and the seizure in 060. Put the reservation sentence beside the act, or the seizure reads as a breach of "asks no state".
4. **Halleck and Baker.** Both are un-naturalised San Francisco lawyers leaving in 1861. Set them in adjacent sentences as a deliberate pair, or cut one description.
5. **Lincoln's last winter.** 063 says he "wants the bay in Union hands before a successor"; 065 says he "keeps the pledge" to McClellan. Neither mentions the other, so add one linking sentence in §12.
6. **§10 compacts.** There are seven or more (Oregon, Puget Sound, Deseret, Box Elder, Montana, Washoe, Rio Grande). Define the Oregon model once and say "on Oregon's terms" after that; move 061's Fort Union sentence out of the boundary description.

## What I did not check

- CR-068 §4, CR-062 §14 and CR-060 §25 targets, which lie outside the extract.
- CR-066 Part E's wording.
- The register (change_requests.json), the ledger quotes and the linter.
- Historical accuracy beyond the items marked.
- The decision rows of 063, 064, 065 and 067 beyond the greps cited.
- `outputs/` and CR-068-record.md, as instructed.
