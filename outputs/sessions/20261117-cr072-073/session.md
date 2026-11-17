---
session: 20261117-cr072-073
started: 2026-11-17
updated: 2026-11-17
mode: integration
status: done
baseline:
  commit: 7b2cb15
independence: one fresh-context reviewer for the integrated storyline text (only the diff, the surrounding storyline, AGENTS.md and the two CRs' canon tensions); the integration itself is by the drafter
---

# Integration of CR-072 and CR-073 on main

## Brief

- **Authorization (author, 17 November 2026):** decisions 4 and 16 of CR-072 approved at 20:57 ("I approve both": P25, P26); "Yes please" at 21:07 to re-checking CR-073 against `main`, applying CR-071's S amendments and integrating CR-072 and CR-073 in one pass (CR-071 K-1).
- **Branch:** `integrate/cr072-073`, made from `main` at 7b2cb15 with only the two CR documents brought over from `drafts/cr071-073-counties`. Merging into `main` waits for the author's sign-off on the pull request.

## What was done

- **CR-073 re-checked** against `main` after CR-057's integration (CR-073 Part I2): CR-057 settled; the Reserve Bank's collateral rule stays PROPOSED; the canal purchase worded so the Patrimony arranges a syndicate and does not spend.
- **CR-071 S1–S6 and S8** applied to CR-073's document. S7 (CR-071 E-15) and Japan's loan of 1873 wait for CR-071.
- **Storyline:** CR-072 in §§12, 14, 19, 21, 22, 25, 26, 27; CR-073 in §§8, 14, 19, 25, 27 (tables in each CR's "Storyline text (as integrated)"). Header notes for both.
- **Register and facts:** CR-072 and CR-073 entries; `cr_facts.py apply` for both (eleven and seven fact changes).
- **Characters:** six new short profiles (Broderick, Judah, Taylor, Cannon, Alvord, Sharon); CT-RALSTON's "later fate" lines replaced (CR-073 CT1); Huntington and Hallidie extended. 308 identities.
- **Ledger:** the Spanish loan's agent, the Patrimony's chairman and recharter, the 1895 syndicate.
- **Other canon:** `historical_background.md` section; AGENTS.md "Current canon" paragraph and identity count.
- **Fresh-context review:** two blockers (women's vote; the houses' money in 1866) and the should-fix items applied; recorded in each CR's "Fresh-context review of the integration".

## Checks at the end

- `lint_canon.py` clean; `cr_facts.py check` agrees; `sync_master_storyline.py --check` synchronized; `validate_character_docs.py` valid; `ledger.py check` 272, 0 problems.

## Resume here

- **Author, 17 November 2026, 21:46:** approved both suggestions (CR-072 P27, Julian's lever on the 1911 ballot; CR-073 R26, the canal money) and the merge into `main` with the rest of the integration. Applied and merged.
- **Next:** rebase `drafts/cr071-073-counties` on the new `main`; CR-071's integration then adds S7, Japan's loan of 1873 with the Bank of California's part, and the Deseret charter's carrying-over (T3).
