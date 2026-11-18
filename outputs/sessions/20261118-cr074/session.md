---
session: 20261118-cr074
started: 2026-11-18
updated: 2026-11-18
mode: drafting, review and integration
status: done
baseline:
  commit: 2ad4016
independence: one fresh-context reviewer for draft 5 (the CR, the affected canon passages, AGENTS.md and the CR's canon tensions; `CR-074-review.md`); the integration itself is by the drafter, without a second review
---

# CR-074 drafted, reviewed and integrated

## Brief

- **Author, 18 November 2026, 07:16–12:02:** draft CR-074 (the Pacific Companies) from CR-071's approved dates and shape; decisions D-1 to D-37 in rounds at 09:04, 09:54, 10:16, 11:05, 11:14 and 11:51; the review's blockers and nine items approved at 11:37; "You can proceed with the integration and then add the model rows" (12:02).
- **Sources supplied by the author:** Carr, *The Devil Soldier*; Smith, *Mercenaries and Mandarins* (used for the fact check and set pieces; not committed).
- **Branches:** `drafts/cr074-companies` (drafts 1–7 and the review); `integrate/cr074` from `main` (2ad4016).

## What was done

- **CR:** `CR-074.md` (draft 7, approved and integrated) and `CR-074-review.md`.
- **Storyline:** the integration summary; §4 (Olompali, Camilo Ynitia), §6 (Ward in 1854; the first licences and Crabb), §8 (the note of 1856), §19 (l. 817: "the first company abroad"; Ward, the will, Suzhou, Hakodate, 1878, Keelung), §25 (the Companies Act; raised and Philippine companies and the roll; Korea and China; 1894; Formosa; Borneo and the Palatan peace), §26 (the crowns' companies, 1907), §28 (the letters of 1914), §30 (accession, 1919).
- **Register and facts:** CR-074's entry; `cr_facts.py apply CR-074` applied 4 (Ward, the Companies Act, the accession of 1919, Korea's treaty).
- **Ledger:** the venture licence and the Companies Act updated; new: the Paris note (1856), the letters of 1878 and 1914, Korea's and China's treaties (1888), the Formosan guard (1895), the Palatan peace (1898), the accession (1919); party NBINTERIOR.
- **Characters:** CT-FREDERICK-WARD (321 identities); notes on Li Hongzhang, Fong, Logan Turner, Caleb and Silas.
- **Other canon:** `historical_background.md` (the Pacific Companies entry rewritten with the sources); AGENTS.md (CR-071's companies line, CR-074's paragraph, the identity count, the workbook line); the "canton" note at the head of `legacy_secondary_cast.md`.
- **Model:** `finance/build/cr074_companies.py` (Events E247–E250, master lever `cp_on`), added to `cr057_rebuild_pair.py`; `finance/CR-074-workbook.md`. `cp_on` 0 reproduces the input (114,440 values). Story 0 / Stress 50 failed checks, unchanged; residents and GDP unchanged; domestic taxes +$12.0m over 1846–1932. MODEL.

## Checks at the end

- `lint_canon.py` clean; `cr_facts.py check` agrees (204); `sync_master_storyline.py --check` synchronized; `ledger.py check` 300, 0 problems; `validate_character_docs.py` valid.

## Resume here

- The pull request `integrate/cr074` into `main` waits for the author's sign-off. A fresh-context review of the integrated storyline text (as for CR-071) has not been run; offer it before merging.
- Still OPEN in CR-074: Siberia's line guard (D-14, deferred); the company's part in Queen Min's survival in 1895 (OPEN-1, for a Korea CR); the Shanghai and Hakodate captains; the Companies Office's first director and the school's first commandant; the Borneo captain of 1894; the Nationalist customs after 1928–29; Pacifica's naturalization rule (T9, PROPOSED).
- CR-071's own OPEN items stand (see `20261118-cr071-integration`).
