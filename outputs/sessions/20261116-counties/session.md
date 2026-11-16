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

## Part I, steps 1 and 2 (16 November, afternoon)

- **Author:** "Please merge main in ... Then go ahead and start with steps 1 and 2." `main` (7b2cb15, CR-057 with the Deseret sheet) merged into the branch; canon checks clean.
- **Step 1, the historical baseline:** `population/counties_1887.py` builds `population/outputs/counties_1887.csv` and `counties_1887.md` from `population/data/counties/` (the Newberry atlas's counties of 1 August 1887, CC0; county census totals from the counties' Wikipedia articles, checked against the state totals in `census.toml`). 233 mainland counties lie wholly or partly on Pacifica's side; about 2.29 million people in 1887 in our timeline, 1.10 million of them in California.
- **Step 2, the regional split (MODEL, not decided):** four variants in section 2 of `counties_1887.md`. The population model has no regions; California's share of the 5.84 million of 1887 runs from 77% (interior as in history) to 47% (every region in proportion).
- **Found on the way:** Baja California (purchase of 1867, PROPOSED in §16) is in neither the strawman nor the model; the line in Montana, Wyoming and Colorado needed county assignments (`overrides.toml`, `[pacifica_share]`, guesses for the split counties).
- **Not done:** county seats; maps (the atlas's geometry is available as topology in `localgeohistoryproject/county-boundaries-topology`, CC0, and can be rebuilt); 1880 sums for Colorado, Montana and Oregon do not close (444, 170, 100); three 1890 figures unverified.

## Resume here

- **Decided (author, 16 November 2026, 14:08):** Baja counts among the 124; Bozeman is Pacifican. Baja's population about 1887 is still to be sourced (Mexican census of 1895) and added to `counties_1887.py`.
- **Approved (author, 16 November 2026, 14:37):** a settlement programme for the interior is part of the hollowing of 1865-87, with multiples of history differentiated by unit ("I approve"); Asian settlers go where their presence does not cause too much disruption, and the interior may have counties with an Asian majority or a large Asian minority. Built as `population/regions_1887.py` with `data/counties/regions_1887.toml` -> `outputs/regions_1887.md`: the acceded mainland at 1.96 times history, California 56%. The multiples, the Asian shares by unit and Baja's 70,000 are the assistant's proposals (MODEL), not yet confirmed number by number.
- **Approved (author, 16 November 2026, 14:43):** the drawing rules (I1) "make sense to me": a population band with a travel or watershed cap for the empty interior, one railway town as seat, no county that rebuilds an old member, California's outer line kept. The author asks whether Alaska should become counties and whether the homelands should be counties or something else (answered in chat with a recommendation: Alaska stays under the Northern Commission outside the 124; homelands are compact lands, not counties; no decision yet).
- **Waiting for the author:** the allocation of the 124 (`regions_1887.md`, section 2; rule C, the square root of people times area, comes out close to the strawman); I1 (drawing rules), I4 (homelands), I5 (Alaska). The programme itself (railways early, irrigation districts, Land Fund terms, diverted plains settlers, industrial anchors) is to be written into Part C and costed in the workbook.
- **Then:** G3 recounted on the chosen allocation; the map region by region, Deseret first (step 5); `CR-071-I-map.md` (step 6).
- Then Parts A, B, C and J; storyline text, fact changes, ledger (Japan's loan of 1873; the seven charter entries, F–G section T5), registry lines, model rows; a fresh-context review; integration in the K-1 order. K-1 named "the CR-057 project document as approved on 6 November" as the base; CR-057 is now integrated on `main` (PR #73), so CR-073 and CR-072 integrate on `main` as it stands.
- Still open in CR-071: D decision 9 ("ready for approval"), the Guard's commander and Wilcox's later life (H4), CT3, CT5, CT4's Columbia and Washoe rows in the outline.
- On `main`, for a later CR or review branch: the leftover "until 1914" in §25's languages paragraph (should follow CR-040's 1907); AGENTS.md's "A Crown-affiliated party is on hold" (CR-038), which CR-072 supersedes at integration.
