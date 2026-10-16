# Pacifica repository — instructions for AI collaborators

This repository contains an author-directed historical novel and generation tools. The author controls canon.

## Canon authority and reading order
1. `book-agent/revision/master_storyline.md` — **single human-readable, chronological working synopsis**, including approved changes, retained first-draft events, editorial proposals and unresolved decisions.
2. `book-agent/revision/change_requests.json` — **structured authority for approved authorial changes**, approval status and outstanding decisions.
3. `book-agent/manuscript_chaptered.md` — primary first-draft text, currently **not yet revised**. It can contradict approved canon.
4. `book-agent/beats.json`, `bible.md`, `character_bible.json`, `concept.txt` — historical first-pass sources, **not automatically authoritative where superseded**.

## Mandatory behavior when the author approves a new storyline change
- Record a new, stable `CR-###` in `change_requests.json`, or amend the approved request explicitly.
- Edit the affected **authored narrative** sections of `master_storyline.md` in the same change, including cascading effects across later eras and characters. Mark any unresolved decisions `[OPEN]` instead of inventing them.
- Run `python3 book-agent/revision/sync_master_storyline.py --write` and then `--check` to refresh the generated approved-change ledger and verify coverage.
- Changes that add/modify approvals must not be presented as fully integrated if the synopsis remains contradictory. GitHub Actions may sync the *ledger* automatically; it cannot write coherent new prose on its own.
- Preserve `main` and the old manuscript until the author specifically authorizes a rewrite. Make plans and canon updates on a dedicated revision branch and submit for review.
- Protect the narrator's hybrid chronicler/multiple-POV design and the author's chronology preference. Do not settle genealogical or historical ambiguities without authorization.
- When responding with the storyline, link to `master_storyline.md`, never merely the register or README.

## Approval vs proposal
Statements by the author expressly approving content become approved direction. Editorial suggestions, inferred motivations, historical connective material and unresolved dates are proposals until accepted. The manuscript is evidence of the **old draft**, not proof of new canon.
