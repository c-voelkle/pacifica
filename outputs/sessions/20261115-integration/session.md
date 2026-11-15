---
session: 20261115-integration
started: 2026-11-15
updated: 2026-11-15
mode: integration
status: paused-for-author
baseline:
  commit: 1b0d4d8
independence: one fresh-context reviewer for the candidate storyline (brief in review-brief.md); the integration itself is by the drafter
---

# Integration of CR-059 to CR-065 and CR-067 to CR-070 with the model

## Brief

- **Authorization (author, 15 November 2026):** "Yes please go ahead" to recomposing the storyline with all eleven CRs and the current model figures, a fresh-context review, integration on one branch with the model, and a pull request for the author's sign-off; then "I approve the crs"; on review finding B1, "Young acts; paid after".
- **Branch:** `adopt/cr059-070`, made from `revision/cr069-gold` with `models/cr059-068-civil-war` merged (1b0d4d8). Merging into `main` waits for the author's sign-off on the pull request.

## What was done

- **Storyline.** `build_candidate.py` splices the master storyline's §§1–7, the 13 November candidate for §§8–13 and §14 onward, inserts the CR-068 to CR-070 blocks and the population figures, and applies the review's fixes. `candidate-full.md` is now `book-agent/revision/master_storyline.md`; `new-passages.diff` is the change against `base-13nov.md`.
- **Fresh-context review.** One reviewer had only the candidate, the affected canon, AGENTS.md and the four tensions files (`review-brief.md`, `tensions-CR-0*.md`). Its report was not saved verbatim; its findings and what was done: B1 (the Bannack deployment contradicted "Elias orders no operation" and "sends no money … before the vote") went to the author, who chose "Young acts; paid after", and the text, CR-060 M11 and the workbook's E216 (now 1865) follow. S1–S11 and the nits were fixed in the build script's review stage (the Senate-loan repetition, Ralston's agency, the wire clause, the labels, the Front Range wording, the White Pass compact and others). The Robben Island nit was reverted: it would break the `seal-convention-signed` fact pattern.
- **Register and facts.** `register.py` added the eleven register entries (approved 15 November 2026, local labels retained); `cr_facts.py apply` was run for each CR.
- **Ledger.** `ledger_integration.py` amends twenty entries in place (stable IDs: C-1847-LONDON-DEBT ends 1859; C-1862-DESERET becomes the association of 1862–1867; C-1863-NAVAJO is the treaty of 1865; C-1871-FUGITIVE runs from 1863; C-1911-FUR-SEAL from 1886 with Russia's Commander Islands share; C-1861-PROTECTOR ends 31 May 1865; the Western treaty, the armistice, the vendor credit, Alaska, Arizona and the Sunset articles, Juárez's credit, Carson, the Hawaiian guarantees, Matamoros, the Apache peace, the scalp convention, amity, the peace of 1871 and the guarantee) and adds Part 4: 25 parties and 43 commitments. Only what the storyline states is entered; each CR's ledger items that the storyline does not state (CR-059's Klamath compact, Paiute peace and Coeur d'Alene passage; CR-061's Pima compact, Hopi agreement, Conejos agreement and the Fort Garland convention; CR-060's Soda Springs agreement; CR-070's station and placer compacts and the franchise's terms) are named in the entries' `open` notes or left out.
- **Characters.** `characters_integration.py` adds 69 persons (Lincoln as a dossier, 68 short profiles: those on the page plus CR-067's approved officers) and appends the CRs' additions to 19 existing entries; Kit Carson's pending CR-061 markers are now approved text. The registry's profiles are refreshed from the bible. Persons named only in the CRs stay without entries.
- **Other canon.** `historical_background.md` has a section for the set (history, divergence, a pointer to each CR's sources; CR-068's prepared background); AGENTS.md has a "Current canon" paragraph and the registry count (299); each CR file's status says approved and integrated; CR-066's Part E is noted as integrated with CR-061.
- **Model.** The workbook is the fifth-addendum build (SHA-256 `a061a7ba…`; Story 0 failed checks, Stress 15, garrisons 25% dearer 15); `finance/CR-059-068-workbook.md` has the fifth addendum. The population outputs were regenerated and the tests pass.

## Checks at the end

`lint_canon.py` clean; `cr_facts.py check` agrees (151 facts); `validate_character_docs.py` valid; `commitments/ledger.py check` 0 problems (262 entries); `sync_master_storyline.py --check` synchronized; population tests pass.

## Resume here

- The pull request from `adopt/cr059-070` to `main` waits for the author's sign-off; do not merge before it.
- CR-059 open decision 17 is decided (author, 15 November 2026: Washington Territory accedes as Columbia, Part IX); it was wrongly listed as deferred.
- Still open after integration: Sherman's fate after 1865, the CRs' listed open decisions, and the ledger and registry items left out above.
- After the merge, retire `models/cr059-068-civil-war` and `revision/cr069-gold`, which this branch contains.
