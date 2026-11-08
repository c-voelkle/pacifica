---
session: 20261108-civil-war-crs
started: 2026-11-08
updated: 2026-11-08
mode: draft
status: paused-for-author
baseline:
  commit: 73d81dd
  files:
    book-agent/revision/master_storyline.md: sha256:78bebc52d9183853…
    book-agent/revision/change_requests.json: sha256:b3b1f32ce5b5f4f1…
independence: separate-agents   # one source-check agent per book; one drafting agent per CR; one fresh-context reviewer over the set
---

# Cross-reference the Civil War canon against Boatner, Hattaway–Jones and Hess, then draft CR-060 to CR-065 beside CR-059

## Brief

- **Desired outcome:** the four planned continental-settlement CRs (A–D) checked against three military histories before drafting; the blockers found; the set enlarged with the CRs the check showed were missing; drafts of B–G on PR #69 beside CR-059, with CR-059 amended where the set requires.
- **Objective:** a Civil War Part II whose every Union and Confederate move survives a reader who knows the war's logistics; Pacifica's gains through consent, compacts and a paid cession; the Elias–Lincoln agon intact.
- **Authorization:** author, 8 November 2026: "Before we move forward with the four planned change requests for the civil war chapters, can you cross reference canon and its planned changes against these historical sources and let me know any hard blockers you might find or additional change requests you think we should plan"; then "Can you run a number of subagents (preferably opus 5.5 high) and create drafts for the crs b through g and add them to pr 69 as well as adding the requisite edits to cr a (numbered as cr-059)?" Nothing is approved; no canon file is changed.
- **Sources of history:** Boatner, *The Civil War Dictionary*; Hattaway and Jones, *How the North Won*; Hess, *Civil War Logistics* (author's copies, read in full by one agent each; findings in this folder). Earlier: `outputs/sessions/20261107-cr059-oregon/plan-v2-four-crs.md`, CR-015 A/F/H, canon §§9–13.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-08 | explore | Author: cross-reference canon and the plan against the three books |
| 2026-11-08 | draft | Author: draft CR-B to CR-G as subagents, add to PR 69, edit CR-059 |

## Findings of the cross-reference (`sources-review.md`)

Hard blockers: (B1) the Union's 1863 Texas expeditions sailed from New Orleans and cannot be Hist. with New Orleans Confederate; (B2) Butler's 15,000 at Ship Island unaccounted for and Mobile undefended in 1862; (B3) Farragut home ill in December 1864 and the Union's ocean fleet fully committed to Fort Fisher in the same winter as canon's Mobile attack; (B4) the Southwest column's winter supply beyond wagon radius unless garrison-sized. Constraints C1–C7 (Shiloh's day, Port Hudson, the corridor's value, Atlanta's mechanism, the Valley campaign and the election, the Pacific sealift, Hampton Roads). Three CRs added (E, F, G).

## Drafts written (all DRAFT, nothing approved)

| CR | File | Writer's five proposals (summary) |
| --- | --- | --- |
| CR-059 (A) | amended | The seven-CR set; W13 the Union's ships to the Sound; W14 Casey stays and the Boatner command datings; CT9/CT11/CT14 cross-references |
| CR-060 (B) | CR-060.md | Connor commands the Salt Lake road garrison; Compact of Association Dec 1862 with a travellers' court (Lee's trial); Nevada's Enabling Act as Lincoln's "admit to bind" answered by retaking Washoe in spring 1864; Hess-based supply argument; the Ute agreement of 1866 under the later Uncompahgre lease |
| CR-061 (C) | CR-061.md | Rio Grande garrison about 1,800 men on the sources' wagon arithmetic; Glorieta freezes for a counted reason; Caleb Vance commands; Mesilla a fight over grain; peonage ends with the 1865 Navajo treaty's captive clause |
| CR-062 (D) | CR-062.md | Armistice term only what a consul can see; the Oregon condition in the treaty with armistice protocols; Washington, Dec 1865, Vallejo and Sherman signing; Russia sells to Pacifica Dec 1866; the Senate built question by question, no count asserted |
| CR-063 (E) | CR-063.md | Mobile option M-a: no Fort Fisher, the winter expedition goes to Mobile; Farragut returns from New York to lead it; Butler's 15,000 recalled east after the Seven Days, a brigade at Pensacola; Sabine Pass and Brownsville struck; Pemberton's council votes to march out on 18 May, rear garrison to summer; the corridor carries coin, rifles, tools and men |
| CR-064 (F) | CR-064.md | Halleck sails east May 1861, Sherman a citizen since 1857–58; Shiloh on 5 April gains hours, McArthur at Shiloh Church; McPherson keeps Grant in June 1862; Thomas takes the western command March 1864; Atlanta stalls on the Chattahoochee with Polk's army on the Blue Mountain–Selma railroad |
| CR-065 (G) | CR-065.md | Atlanta, not Mobile, decides the election; Valley option (c) one victory without the XIX Corps; the September movement fizzles and Lincoln loses on his own ticket; McClellan 120–103 (MODEL); Lincoln's winter fails four ways, no talks with Monterey |

## Interface conflicts reported by the writers (for the reviewer and the author)

- CR-060 CT1 (Deseret an associate 1862, member 1867) requires three CR-059 edits if adopted: Part V route table, Part VI offers table ("Deseret a fellow member"), W10.
- CR-062 reconciles CR-059's two homes for the Oregon condition (V1 treaty; CT14 armistice) with the treaty article plus armistice protocols.
- The XIX Corps does not exist without a Union New Orleans (CR-063): CR-064 and CR-065 take it out of Early's July 1864 defence and Sheridan's Valley army.
- Vicksburg escapees: CR-064 assumes about 15,000 (MODEL); CR-063 sets the number and frees Grant from late May, not July.
- CR-062's Senate packet should add New Mexico's charter (CR-061), western Montana's consent step (CR-060), the Fort Union evacuation article and the Santa Fe Trail as a named route.
- Registry: Halleck proposed as `HALLECK` (CR-064; CR-063 to share), Lincoln and Greeley as `LINCOLN`, `GREELEY` (CR-065); the linter rejects unregistered CT- IDs in drafts.
- Juárez credit: ledger year 1867 vs CR-058's 1865 (CR-061 CT4, CR-062 CT5). Navajo treaty: ledger 1863 vs CR-061's 1865 (CT3).
- CR-064's weakest point: Thomas historically proposed the Snake Creek Gap march; the stall must survive that.

## Checks executed

- X1 `lint_canon.py --only` on each of CR-059 to CR-065: clean.
- X2 `cr_facts.py preview` (and `--tensions` where tensions carry blocks): pasted in each draft; no canon passage conflicts outside the declared tensions.
- X3 Fresh-context review over the set: commissioned 8 November (result in `review-set.md` when returned).

## Resume here

- CR-059 to CR-065 are drafts on `revision/cr059-oregon` (PR #69, draft). Canon, the register, the facts file and the ledger are unchanged.
- Next: the author reads `sources-review.md` and the drafts' decisions tables; decides the interface questions above (Mobile M-a; Deseret associate-first; the Valley option; Lincoln on the ballot); then each CR's open decisions; then approval and integration in plan order (A, then B and C, then D; E–G alongside, since D's Senate and G's winter depend on E).
- Research still open: the "to verify" items each draft lists; Thomas and Snake Creek Gap (CR-064); the Valley campaign without the XIX Corps (CR-065); the Pacific Mail's ships at Panama in May 1861 (CR-059 W13); the Rio Grande road distances (CR-061).
