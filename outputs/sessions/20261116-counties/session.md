---
session: 20261116-counties
started: 2026-11-16
updated: 2026-11-16
mode: drafting
status: paused-for-author
baseline:
  commit: 28b7263
independence: self-review only (the consistency check of 16 November was done in the drafting session); no fresh-context review yet
---

# CR-071 (counties), CR-072 (the Prosperity Party), CR-073 (Ralston): drafting

## Brief

- **Author, 16 November 2026:** implement the consistency check's fixes; then "From now on let's only work in the repo please". The drafts were moved from the claude.ai project to this repo; the project copies are superseded and no longer updated.
- **Branch:** `drafts/cr071-073-counties`, from `main` at 28b7263. Nothing is integrated; `main` is untouched.

## What was done

- **Files** (all in `book-agent/revision/`): `CR-071-outline.md`, `CR-071-D-meiji.md`, `CR-071-E-preparation.md`, `CR-071-FG-triggers-act.md`, `CR-071-H-resistance.md`, `CR-071-consistency-check.md`, `CR-072-party.md` (draft 8), `CR-073-ralston.md` (draft 3, as approved on 15 November).
- **Consistency check** (`CR-071-consistency-check.md`, section E): every point fixed or decided; decisions K-1 to K-15 approved, with D-8, E-17, R-1 and R-2.
- **Checked against `main`:** the member list (nine members from 1867, eight legislatures; Arizona is New Mexico's Arizona county); the entrenched charters of 1866 (K-15: an article of supersession, F–G section T); the Act of Settlement in 1907, the regency 1887–1907 and the Senate dispute of 1910–1911 (CR-040). The earlier drafts had drawn these from stale project snapshots of CR-021, CR-022, CR-027 and the storyline of 28 October.
- **Part H** (draft 2): H-1 to H-12 approved, including the Honolulu rising of 30 July 1889 (H4) and the comparison with Meiji (H5).

## Checks at the end

`lint_canon.py --only` clean on every draft except one false positive in `CR-072-party.md` line 45 ("Taylor resists until he dies on 25 July 1887" read as Elias's death). Canon checks clean (no canon files changed).

## Resume here

- **Next: Part I, the map of the 124 counties.** Settle the drawing rules (I1, with the historic lands' outer boundaries kept), the allocation that replaces the strawman behind G3's counts (K-7: 123 county senators, Thalassia none), Alaska (I5; CR-070 open decision 9; CT3), the Native homelands (I4; CT5; the Diné homeland as the test), and the named list with seats and county languages. Research first: historical county counts about 1887 per region; the census of 1880 and the population model's figures for 1887.
- Then Parts A, B, C and J; storyline text, fact changes, ledger (Japan's loan of 1873; the seven charter entries, F–G section T5), registry lines, model rows; a fresh-context review; integration in the K-1 order (CR-073 and CR-072 in one pass, then CR-071).
- Still open in CR-071: D decision 9 ("ready for approval"), the Guard's commander and Wilcox's later life (H4), CT3, CT5, CT4's Columbia and Washoe rows in the outline.
- On `main`, for a later CR or review branch: the leftover "until 1914" in §25's languages paragraph (should follow CR-040's 1907); AGENTS.md's "A Crown-affiliated party is on hold" (CR-038), which CR-072 supersedes at integration.
