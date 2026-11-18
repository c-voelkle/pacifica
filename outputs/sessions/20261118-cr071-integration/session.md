---
session: 20261118-cr071-integration
started: 2026-11-18
updated: 2026-11-18
mode: integration
status: done
baseline:
  commit: 586ca26
independence: one fresh-context reviewer for the integrated storyline text (the diff, the integrated sections, AGENTS.md and the CR's canon tensions); the integration itself is by the drafter
---

# CR-071 integrated

## Brief

- **Author, 18 November 2026, 05:01–06:36:**
  - the realism review of 1887;
  - H-15 to H-20 approved: the settler majority, the Feather River case, the agon, the honest avenue abroad and the proposals of H7 with three caveats;
  - "I approve the revisions with the company's dates, but leaving the details as proposed pending the next cr. Let's finish up 071 now."
- **Branch:** `integrate/cr071`, from `drafts/cr071-073-counties`, which holds `main` (586ca26) plus CR-071's documents and model work. Merging into `main` waits for the author's sign-off on the pull request.

## What was done

- **Part H:**
  - H6 (the settler majority) and H7 (proposals for the open items, approved with the caveats);
  - H7.3 corrected at drafting: the water decision of October 1886 goes against the districts, so the Feather River case's turn is that the Court which protected the families cannot protect the settlers' rivers;
  - Silas's oath at Sacramento moved to a week after the handover, since he takes his commission at Thalassia on 1 August.
- **Part E:** E-2a, "the slack years after 1873", checked against the model.
- **Storyline (draft 3, written in):**
  - §§5, 6, 12, 13, 14, 15, 19, 20, 21, 22, 23, 24 and 25;
  - fourteen rewordings and two moved canon paragraphs (§19's l. 775 after CR-072's l. 777; §14's Iwakura sentence);
  - the header note.
- **Register and facts:** CR-071's entry. `cr_facts.py apply CR-071` applied 31 fact changes: the outline's 15, three new ones (the venture licence, the Feather River, Rock Springs and Hells Canyon forbidden) and 13 `add_person`.
- **Ledger:**
  - twenty new entries, Guaymas split from the Baja purchase among them;
  - the charters of 1866 ended by the article of supersession;
  - the Constitution's conditions (Deseret's carry-over T3, the labour article);
  - the quotes that R1 changes.
- **Characters:** twelve new identities (del Valle, Fair, Wilcox, Nowlein, Powell, Mattson, Ouray, Dall, Henry Miller, Victorio, Roney, Kearney) and sixteen amended; 320 identities.
- **Other canon:**
  - `historical_background.md` section;
  - CR-021.md's amendment note (the record of revision 9 is not rewritten);
  - AGENTS.md (CR-071's "Current canon" paragraph, Sherman's line, the identity count).

## Checks at the end

- `lint_canon.py` clean.
- `cr_facts.py check` agrees.
- `sync_master_storyline.py --check` synchronized.
- `ledger.py check`: 292, 0 problems.
- `validate_character_docs.py` valid.

## Resume here

- PR #75 (`integrate/cr071` into `main`) waits for the author's sign-off. The fresh-context review of the integration found one blocker and fifteen should-fix items, all applied (`CR-071-review-on-main.md`).
- Next CR: CR-074, the Pacific Companies. The companies' dates are approved; their details, the Companies Act's terms, the name, the Declaration of Paris, the partners and the warrant's size are open.
- Still OPEN in CR-071 (outline and Parts H and I):
  - the first Commissioners, the Baja commissioners and the first Chancellor;
  - when Powell enters service, and Sand Creek;
  - Oraibi's year and the Hopi leaders, and the Cochimí;
  - Victorio's death;
  - the ladder's year.
