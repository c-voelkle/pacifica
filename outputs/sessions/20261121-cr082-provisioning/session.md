---
session: 20261121-cr082-provisioning
started: 2026-11-21
updated: 2026-11-21
mode: draft
status: paused-for-author
baseline:
  commit: 501791d
independence: same-agent (writer only; no review yet)
---

# How does Pacifica mean to feed half a billion people, and how does that guide its policy abroad?

## Brief

- **Desired outcome:** an outline for a provisioning doctrine CR, written before work on CR-081 (China) continues.
- **Authorization:** author, 21 November 2026, 17:24 ("Yes please- I don't think it makes sense to continue on the China CR without it"), after a review of CR-081 the same afternoon. Outline only; no prose, no canon change.
- **Sources of history:** the CR-081 review in chat (21 November 2026); `drafts/cr081-china` at fe076f7, read but not merged.

## What was done

- `book-agent/revision/CR-082-outline.md`: the author's request, method, reference works, Part A (the account, with the population model's figures), Part B (the doctrine), Part C (the instruments), Part D (effects on other CRs), Part E (candidate scenes), three canon tensions, fourteen decisions F-1 to F-14.
- `population/provisioning.py`, `population/data/provisioning.toml`, `population/tests/test_provisioning.py`, `population/outputs/provisioning.md` and `provisioning_by_year.csv`: the provisioning account (F-1). A3 of the outline carries its first results and corrects the skeleton's hand estimate.

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | The leadership plans for half a billion Pacificans a century ahead, and this guides China policy explicitly | author message 2026-11-21 17:09 | current |
| D2 | decision | Build the script; the Office assumes the same diet but not the early years' growth rate; the Philippine crown is counted after Julian's accession | author message 2026-11-21 17:59 | current |
| D3 | decision | Yield research on land and at sea is part of the central case, with Santa Fe as the nexus for dry areas; the central case comes first, then the slowing, then the stance toward food producers | author message 2026-11-21 18:16 | current |
| Q1 | open choice | The form of Pacifica's claim on foreign surplus land (trade, hold or settle) | author message 2026-11-21 17:09 ("I'm not sure yet") | open (F-13) |

## Resume here

The central case is built on six dated yield innovations (MODEL; author's request of 18:30): mechanised fallow, breeding before short straw, cheap nitrogen, the hormone weedkiller, short-straw wheats and the deep-furrow drill, each with history's dates and canon's earliest and central dates in `population/data/provisioning.toml`. Central yields are 1.12 times history's in 1910, 1.49 in 1920, 1.93 in 1930 (a lead of 27 to 34 years). Without research the Realm outgrows its soil in 1918; in the central case it feeds itself in 1932 with about three-tenths to spare and outgrows soil and sea about 1941–43; the century's need is about nine times the home ceiling. Nitrogen is the critical path: 480 thousand tonnes a year by 1930 against CR-054's 90. Next, in the author's order (18:16): confirm the central case (F-1a the dates, F-1c the 22 million irrigated acres, F-1d nitrogen against CR-054, F-1e the sea), then the slowing (F-1b), then the stance toward the food producers (Part C), where Chile's nitrate now belongs too. Still to do in the script: a verified irrigated yield series, the dry-land series from the Census of Agriculture, part-state shares from the 1887 county map, Alaska's landings, the Japan series. CR-081 (PR #83) stays unmerged; CR-080 stays parked.
