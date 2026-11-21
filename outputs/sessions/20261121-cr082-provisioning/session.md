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
| Q1 | open choice | The form of Pacifica's claim on foreign surplus land (trade, hold or settle) | author message 2026-11-21 17:09 ("I'm not sure yet") | open (F-13) |

## Resume here

F-1 to F-3 are decided and the script is built (MODEL): canon's farmers feed the Realm with a surplus from about 1871 to 1921; from about 1922 it outgrows its own soil even with every irrigable acre watered; in 1932 about a fifth of residents eat from other people's land; the table of 1930 puts about half a billion people a century on, needing fifteen times the home ceiling. Next: the author decides F-1a (whether canon's farmers, about 22 million irrigated acres by 1910, is canon), F-1b (the slowing rate) and F-1c (where the missing fifth comes from in 1932), then Part B. Still to do in the script: the Japan series, the dry-land series from the Census of Agriculture, part-state shares from the 1887 county map, and reconciliation of the yield path with CR-056's farm channel. The historical anchors in the outline's Sources are still to verify. CR-081 (PR #83) stays unmerged; CR-080 stays parked.
