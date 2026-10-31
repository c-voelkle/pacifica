---
session: 20261031-cr045-047-omsk
started: 2026-10-30
updated: 2026-10-31
mode: adopt
status: stopped
baseline:
  commit: 9aa40f7
  files:
    book-agent/revision/master_storyline.md: sha256:aaaed6a8adf3e07e0d76cacdd952fa03dc598530edf3f1a44dab05174ca73ed0
    book-agent/revision/change_requests.json: sha256:e6839983ccbdfd209c04757ec210382b2bf3255968624fb13749f2094df66e76
independence: same-agent drafting and integration; one fresh-context review of the storyline diff before merge (findings and fixes in the PR description)
---

# Who was Mikhailov, what did Britain fear in 1927, and where does the Turkish frontier run?

## Brief

- **Desired outcome:** historical depth and texture for the Omsk section, with Mikhailov featured as a man who joins Pacifica on the surface, a Pacifican counterpart who sees his game, a Julian–Mikhailov scene and Maria Grishina-Almazova on the page; then what makes the 1927 showdown with London matter; then Kars, Ardahan and Batum.
- **Authorization:** author, 30–31 October 2026 (the dossier request; "For the next CR I would like to add some historical depth and texture to the Omsk section"; "Volkov, Maria as hostess and Japanese informant"; "I like it, including Kiyoshi's son as Maria's handler"; the 1927 decisions 1, 2, 4–7; "it goes all the way"; "I think the death in 1921 is a good way to end it"; Batum as a Georgian port with both presences; "Yes you can put the three districts in their own short cr"; "Want to go ahead and merge the open crs and update the character docs, ledgers and the financial workbook?").
- **Sources of history:** the diaries of Vologodsky, Ilyin and Budberg; Serebrennikov (*Velikii otkhod* and memoirs ch. III); Krol; Gins; Petin 2019 on Maria Grishina-Almazova; the project's `Mikhailov-dossier.md`; Wikipedia (Oswald Rayner; Kars oblast and okrugs); King's College London (Steveni); UK treaty record (Copenhagen, 1920).

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-30 | research | Author: "Let's create a dossier on Ivan Mikhailov" |
| 2026-10-31 | draft | Author: "For the next CR I would like to add some historical depth and texture to the Omsk section" |
| 2026-10-31 | draft | Author: "Let's get into how Volkov's motive depends on the showdown with London over Baku" |
| 2026-10-31 | draft | Author: "Yes you can put the three districts in their own short cr" |
| 2026-10-31 | adopt | Author: "Want to go ahead and merge the open crs" |

## Author decisions and open choices

- CR-045: shape approved; Kiyoshi's son as Maria's handler; corrections accepted.
- CR-046: the Petrograd account goes "all the way"; the 1920 payment is ransom and cover-up, not aimed at Japan; the Chronicler holds the file; Victoria knows the ledger; Stalin killed in 1921 after approaching Pacifica; no British protection of Georgia; the British find out about Kamo on their own.
- CR-047: district vote on the 1914 rolls; Batum a Georgian free port.
- Q1: Kashevarov's and Kashiwagi's names.
- Q2: whether Julian answers Victoria in 1921 with the ledger she kept shut.
- Q3: the rest of the Turkey decisions (T1–T6, T8), Nakhichevan and Kemal's file.
- Q4: the remaining money-trail strands (German, French, Swiss, Union) and the trial ruling (B4).

## Checks executed

- X1: `cr_facts.py apply` for CR-045, CR-046 and CR-047, then `check`; `lint_canon.py` clean; `sync_master_storyline.py --write` and `--check`; `validate_character_docs.py`; `commitments/ledger.py check` (183 commitments, 0 problems) and `report`; population unit tests.
- X2: the Kazan gold escrow stays at Chelyabinsk (CR-041); the CR-045 sentence was corrected during integration so that it answers to the paymaster at Omsk.
- X3: CT-STALIN's stale `killed_by CT-KIYOSHI` link (original K1, superseded by CR-044 B6) removed.
- X4: the workbook recalculated in LibreOffice: the unchanged workbook reproduced all 66,092 numeric cells; after the change no check fails.
- X5: fresh-context review of the storyline diff.

## Round log and stop reason

Integrated on branch `integrate/cr045-047` after PR #54.

## Resume here

- The Turkey CR (T1–T6, T8; Kemal's file; Nakhichevan); the remaining money-trail strands (German, French via the Legion, Swiss, Union) and the trial ruling (B4); Kiyoshi's sword and death poem.
- Housekeeping: narrow CR-044's forbidden pattern `kills Stalin` to the Kronstadt case (CR-046 note), which needs a supported way to amend an approved fact.
