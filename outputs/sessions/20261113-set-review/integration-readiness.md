# Integration readiness, CR-059 to CR-065, CR-067, CR-068 (13 November 2026)

Nothing is integrated. `master_storyline.md`, `change_requests.json`, `canon_facts.toml`, the ledger and the character files are unchanged. This note says what a dry run showed and what integration will take.

## Text of record

`merged-storyline-8-13.md` in this directory is the text of record for §§8–13. Where a draft's own "Storyline text" block differs from it, the candidate governs; the drafts' blocks were its sources and have not all been re-synchronised.

Four sentences fall outside §§8–13 and are taken from the drafts at integration: CR-068's sentence for §4 (Lincoln's vote of 1848); CR-062's for §14 (Sitka, October 1867); CR-060's for §19 (the Uncompahgre lease) and §25 (the Union's critics).

## Dry run (the candidate placed in `master_storyline.md`, checks run, file restored)

| Check | Result |
|---|---|
| `lint_canon.py` (all canon files) | clean |
| `sync_master_storyline.py --check` | synchronized |
| `validate_character_docs.py` | valid |
| `cr_facts.py check` | register and facts agree (no new facts applied yet) |
| `commitments/ledger.py check` | 10 problems, all expected (below) |

## Ledger changes integration must make

| Entry | Problem in the dry run | Change | Decided in |
|---|---|---|---|
| C-1847-LONDON-DEBT | quote gone (the bondholders' warning of 1860) | re-quote; the debt is repaid in 1859 | CR-068 CT26 |
| C-1862-DESERET | two quotes gone | re-quote from the candidate: articles of December 1862, Compact of 24 July 1863, accession in 1867 | CR-060 CT1 |
| C-1863-MATAMOROS | quote gone | re-quote from the candidate | CR-063 CT5 |
| C-1863-NAVAJO | quote gone | re-quote: "In Navajo country the government chooses a different course." and "In 1865 a treaty recognizes the Navajo homeland." | CR-061 CT3 |
| C-1865-APACHE | quote now in §12 | section 10 → 12 | author, 13 November 2026 (§10 kept to 1861–64) |
| C-1865-MX-SCALP | quote now in §12 | section 10 → 12 | the same |
| C-1865-HI-GUARANTEES | quote gone | re-quote from the bargain paragraph; note the resolution of November 1864 | CR-068 CT29 |
| C-1871-FUGITIVE | two quotes gone | re-date to 1863 and re-quote; drop the override sentence | CR-061 CT9; CR-068 CT18 |
| C-1861-PROTECTOR | (no failure) | add the dates 1 June 1861 to 31 May 1865; ends by expiry | CR-068 CT29, CT30 |

New entries listed in each draft's "Commitments ledger" section are added at the same time (for example the Compact's travellers' article, the Box Elder compact, the Spanish Fork agreement, the Rio Grande compact, the Western treaty's articles, the Oregon protocol, the Alaska treaty).

## Per CR, at integration

| CR | Fact changes declared | Also needed |
|---|---|---|
| CR-059 | 6 | register entry; `cr_facts.py apply`; ledger entries; registry IDs for new historical persons |
| CR-060 | 7 (plus 3 in CT1, decided) | the same; §19 and §25 sentences |
| CR-061 | 8 | the same; CT9 (fugitives) is decided |
| CR-062 | 4 | the same; §14 sentence |
| CR-063 | 3 | the same |
| CR-064 | none | register entry; registry rows |
| CR-065 | none | register entry |
| CR-067 | none | register entry; registry rows for the officers |
| CR-068 | none (Lincoln's `add_person` was deferred and is due now) | register entry; §4 sentence; character bible additions; the Chronicler's frame stays out of the storyline |

Then, as `AGENTS.md` requires: `sync_master_storyline.py --write` and `--check`; `ledger.py check`; `validate_character_docs.py`; `lint_canon.py`; the historical reasons go to `historical_background.md`; AGENTS.md's "Current canon" gains a paragraph for the set.

## What only the author can give

1. **Approval of each CR for adoption.** Every draft's status line still reads "DRAFT… not approved". `cr_facts.py apply` refuses an unapproved CR, and the labels **[APPROVED — CR-061]** and **[APPROVED — CR-068]** in the candidate become true only then.
2. **The gap-fillers still marked PROPOSED (drafter).** They can be adopted with their PROPOSED labels, as earlier CRs were ("local labels retained"), or confirmed first: who signs the Oregon protocol; how Lincoln knows the maxim of 1848; McClellan's own reason for ceding the West; the Radicals' constitutional charge; Young signing despite Lincoln's assurance; Marcus's evidence and Victoria's seat in the Council of 1865; the XIII Corps after October 1863; the Maine pair's motive; the Black Hawk agreement's terms.
3. **Two things to re-read in CR-068** after the writ was withdrawn: the heavy beats (now three) with TL7's winners, and Sherman's part after 1865.
4. **Deferred by the author and still deferred:** the Legion's pay (CR-060 CT7); CR-059 open decision 17; the amounts of the private lending of 1867 (CR-062 M3).

## Known weaknesses adopted as they stand unless fixed first

- About half of the doubled events tabled in `review5b-merged-candidate.md` remain; none is a contradiction.
- A charter for Washington Territory is listed among the Senate's papers and never told.
- The passes made after the seventh reading (the writ withdrawn; §12 reordered; labels) have not had a fresh-context reading.
