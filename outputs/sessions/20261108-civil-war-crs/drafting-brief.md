# Drafting brief — the Civil War CRs (CR-060 to CR-065), 8 November 2026

This brief is shared by the six drafting agents. Each writes ONE new file `book-agent/revision/CR-06x.md` on branch `revision/cr059-oregon` in `/home/claude/pacifica`. Nothing else in the repository is edited by a drafting agent: no canon files, no `CR-059.md`, no register, no ledger, no `canon_facts.toml`, no other agent's CR. Do not commit or push; the coordinating session commits.

## Authorization

The author, 8 November 2026 (after reading the sources review):

> Can you run a number of subagents (preferably opus 5.5 high) and create drafts for the crs b through g and add them to pr 69 as well as adding the requisite edits to cr a (numbered as cr-059)?

Earlier, the same morning: "Before we move forward with the four planned change requests for the civil war chapters, can you cross reference canon and its planned changes against these historical sources and let me know any hard blockers you might find or additional change requests you think we should plan." The three sources were Boatner's *Civil War Dictionary*, Hattaway and Jones's *How the North Won* and Hess's *Civil War Logistics*.

Everything in these drafts is **PROPOSED** (or **MODEL** for figures, **Hist.** for the historical record, **OPEN** for choices the author must make). Nothing is APPROVED. Write "Status: DRAFT for the author's review, 8 November 2026. Not approved; nothing is integrated."

## Numbering and scope

| Plan name | File | Title |
|---|---|---|
| CR-A | CR-059 (exists; not yours) | Oregon and the Northwest |
| CR-B | CR-060 | The interior: Deseret, Washoe, Idaho, Montana and the divide, 1861–1867 |
| CR-C | CR-061 | The Southwest: the Rio Grande, Santa Fe and Fort Union, 1862–1867 |
| CR-D | CR-062 | The peace, Alaska and the Senate, 1864–1867 |
| CR-E | CR-063 | The Gulf without New Orleans, 1862–1865 |
| CR-F | CR-064 | The Union's war without Sherman, 1862–1864 |
| CR-G | CR-065 | The election of 1864 and the lame-duck winter |

## What to read first (in this order)

1. `AGENTS.md` (the house rules; especially "Mandatory on author approval", which defines the `## Fact changes` and `## Canon tensions` sections every draft must carry) and `docs/authority-and-scope.md`.
2. `book-agent/revision/CR-059.md` — the draft CR this set belongs to, and **the format to imitate**: header block (Status, Authorization, Read with), "What this CR does", a "Decisions" section of tables with lettered-and-numbered IDs, Parts that argue each decision with Hist. anchors, "Storyline text (draft, for integration)" with `**[PROPOSED — CR-06x]**` labels, "Canon tensions" (CT1…), "Commitments ledger (proposed)", "Character registry (at integration)", "Fact changes", "Open decisions" (numbered), "Research tasks", sources. Read it whole; it is the standard.
3. `outputs/sessions/20261107-cr059-oregon/plan-v2-four-crs.md` — the plan for CR-A to CR-D (your section, and the Spine and Working principles).
4. `outputs/sessions/20261108-civil-war-crs/sources-review.md` — the cross-reference that found the blockers and proposed CR-E to CR-G, with the three findings files beside it (`findings-boatner.md`, `findings-hnw.md`, `findings-hess.md`). Cite the sources as the review does (Boatner by headword; H&J by printed page; Hess by chapter). Quote only what those files quote; do not invent page numbers.
5. Canon: `book-agent/revision/master_storyline.md` Part II (§§9–12) and §13; `book-agent/revision/CR-015.md` sections A, F and H; `book-agent/revision/war_base_assumptions.md` (MIL-01); `book-agent/revision/historical_background.md` (search for your topics); `commitments/data/ledger.toml` (entries C-1861-PROTECTOR, C-1865-ARMISTICE, C-1865-CSA-AMITY, C-1867-WESTERN-LINE, C-1867-VENDOR-CREDIT and others you touch); `book-agent/revision/character_bible.md` and `character_registry.json` for any person you name (Elias Thorne, Victoria, Marcus Vance I, Logan Turner, Sherman, Halleck is not registered, etc.). Check registry IDs before using one.
6. `book-agent/revision/CR-059.md` sections W and I again for the interfaces: the Walla Walla convention of July 1862, Idaho inside Pacifica's supply system, the Lewiston lease, Bear River as "the price of the Snake road", W10 on Lee's hanging and Deseret.

## Interface decisions (fixed for this drafting round, so the six drafts agree)

- **Oregon**: as CR-059 has it. Oregon is never a state; the Enabling Act of 2 March 1861; the compact; the Walla Walla convention (July 1862) sends the interior regulars east over the Mullan Road; the October 1866 vote; the conditional Oregon article in the treaty (CT14, adopted by the author).
- **Deseret**: association in December 1862, accession on exchange of the treaty in 1867 (plan CR-B); CR-059 CT11 and W10 allow this. Lee is surrendered, tried and hanged in 1863 (APPROVED canon).
- **Nevada**: the first constitution fails in January 1864 under the Union; Pacifica retakes Washoe in spring 1864; no October 1864 admission (plan CR-B; CR-059 CT9).
- **Southwest**: Carleton-type column from Fort Yuma, Rio Grande in summer 1862, the Mesilla clash (Pruett dies; CR-022, kept — but the Texans there are Sibley's rear guard, not Baylor's: Boatner has Baylor removed by Davis in 1862), Albuquerque and Santa Fe in autumn 1862, Fort Union held by the Union, the front frozen at Glorieta, Connelly at Las Vegas; **the column is garrison-sized** (the review's blocker B4: on the order of 1,500–2,000 men, few animals, gold for Rio Grande grain, a staged Tucson road for ammunition and specie). CR-061 sets the number; the others refer to "the Rio Grande garrison".
- **The Gulf**: New Orleans Confederate from 24 April 1862; Pensacola Union from 9 May 1862; **no Union Department of the Gulf field army**; Sabine Pass and the Brownsville expedition are not Hist. here (review blocker B1); Port Hudson is never besieged from the south; Mobile untaken on 8 November 1864; the lame-duck Mobile attack and Farragut's death remain the canon default (CR-015 F2/F4, APPROVED) and **CR-063 decides** whether that attack stays in February 1865, its size, Farragut's presence, and what the Union forgoes to mount it (Fort Fisher or not). CR-062 and CR-065 refer to "the February 1865 attack at Mobile (CR-063)" and do not re-decide it.
- **The West under the Union**: Halleck is in Union service (general in chief from 11 July 1862; he was in California with Sherman in 1861, so CR-064 must say in one line why he goes east and Sherman does not). Sherman is Pacifican (canon §8). The Atlanta campaign stalls: Johnston is not removed and Atlanta does not fall before the election, by the mechanism CR-064 chooses (default: a methodical Thomas tied to the single-track railroad; Johnston's Alabama flank position; no raid). CR-065 and CR-062 refer to "the stalled Atlanta campaign (CR-064)".
- **The election**: McClellan wins in November 1864 (APPROVED CR-015 A1); CR-065 decides the Valley campaign, the September movement to shelve Lincoln, the October states and the soldier vote. CR-062 begins after the election.
- **The Pacific sealift** (§10's Iowa regiments through Panama): CR-059 will take a sentence (the Pacific Mail ships caught at Panama are Union property; or British charters from Victoria). Do not decide it in your CR; refer to CR-059.
- **No field army east**: Pacifica's part in the Confederacy's war is credit, specialists, specie, arms and mines through Matamoros (not bulk; Hess), Logan's mission, and the second front in the West. Keep it so.

## House rules that bite

- Historical persons over invented ones; if you must invent, say so and mark the name OPEN. No invented scientists. Use the registry's IDs for registered people and propose `CT-…` IDs for new ones under "Character registry (at integration)".
- Every date, number and name you present as history must be in one of the three findings files, in `historical_background.md`, or in canon; if you add a historical fact from your own knowledge, mark it **"(Hist.; to verify)"**. Figures you compute are **MODEL**.
- `## Fact changes`: a ```json list in the `cr_facts.py` format (read the docstring at the top of `book-agent/revision/cr_facts.py`), or the word `none`. Run `python3 book-agent/revision/cr_facts.py preview book-agent/revision/CR-06x.md` and put its output under "Impact (preview)".
- `## Canon tensions`: for every conflict with existing canon, both cases (draft adapted to canon; canon amended, with its json block) and a recommendation. The sources review's §5 table lists several that belong in your CR.
- Run `python3 book-agent/revision/lint_canon.py --only book-agent/revision/CR-06x.md` and make it clean (the linter checks dates and protected facts; a draft that states an old value in a non-tension passage will fail).
- Storyline text: prose that reads as what happens, not an edit memo; no model-documentation style; label every sentence `**[PROPOSED — CR-06x]**` (or `**[OPEN]**`, `**[MODEL]**`). Say where it goes (§ and the sentence it follows).
- The author's standing preferences: each step must be logical and materially motivated; the lens is Pacifica's power and wealth; the Union is a rational antagonist, not a fanatic; the Civil War is also an intellectual agon between Elias and Lincoln; "Promises are made to be tested" (plan principle 5); the Union's grievance stays pointed at Richmond (principle 4); no state is ever ceded (principle 1); consent before title (principle 2); emergency power does not annex (principle 3).
- Keep the draft to a length a reader can review in a sitting — CR-059 is at the upper limit. Aim for 250–500 lines. Decisions tables first, argument after, storyline text after that.
- Finish with a "## Self-review" section: what you could not verify, where you departed from the plan or the review and why, and the questions you would put to a fresh reviewer.

## Deliverable

The file `book-agent/revision/CR-06x.md`, lint-clean, with the preview output pasted in. Your final message to the coordinator: under 300 words — the CR's five most consequential proposals, its canon tensions by number, and any interface conflict you noticed with the other CRs' fixed decisions above.
