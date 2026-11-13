---
session: 20261109-cr063-064-self-directed
started: 2026-11-09
updated: 2026-11-09
mode: draft
status: paused-for-author
baseline:
  commit: faa62b4
independence: separate-agents   # one research agent per CR; one fresh-context reviewer per CR
---

# CR-063 and CR-064: the CR-061 cycle, run self-directed

## Brief

- **Desired outcome:** CR-063 (the Gulf without New Orleans) and CR-064 (the Union's war without Sherman) brought to the state CR-061 reached on 9 November 2026 before the author's decisions: every research task and "to verify" item previewed against the record; the load-bearing mechanisms written step by step; every open decision brought up to date with a recommendation; a fresh-context review of each draft and its fixes; lint and fact previews clean; pushed to PR #69.
- **Authorization:** author, 9 November 2026 (chat): "I'm wondering if you could do what we did for CR-061 for the CRs 063 and 064 self-directedly."
- **Reading of the request:** "self-directedly" means without stopping for the author at each step. It does not mean deciding for the author: nothing is approved, no canon tension is decided, no canon file, register entry, facts file or ledger is changed. Where CR-061's author made a choice on Claude's recommendation, these drafts carry the recommendation, labelled for the author.
- **Out of scope:** integration; CR-059 to CR-062 and CR-065, except as interfaces noted for the author.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-11-09 | draft | Author: "do what we did for CR-061 for the CRs 063 and 064 self-directedly" |

## Agents

| ID | To | Task | Inputs | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | research agent | previews for CR-063's research tasks and "to verify" items | CR-063 | — | `research-cr063.md` | done; applied |
| R2 | research agent | previews for CR-064's research tasks and "to verify" items | CR-064 | — | `research-cr064.md` | done; applied |
| H1 | fresh-context reviewer | consistency, history, literary effect | CR-063 (after R1), AGENTS.md, storyline §§9–12, CR-015 A and F, bible entries | this record, the research files | `review-cr063.md`: 5 blockers, 13 should-fix, 9 consider | applied (CR-063, last section) |
| H2 | fresh-context reviewer | consistency, history, literary effect | CR-064 (after R2), AGENTS.md, storyline §§8–13, CR-015 A and F, bible entries | this record, the research files | `review-cr064.md`: 4 blockers, 12 should-fix, 6 consider | applied (CR-064, last section) |

## What changed most

- **CR-063, Vicksburg:** the record puts Sherman's XV Corps on the Benton road at 9:30 a.m. on 18 May and that day's council voting to hold, so the escape moves to a council on 17 May (the record has none) with Davis's authority from about 10 May. After the review the fresh divisions (Forney, Smith) march and the beaten ones (Stevenson, Bowen) hold the works; about 12,500 reach Johnston and about 15,000 surrender at the turn of June and July (MODEL).
- **CR-063, Mobile:** the February attack step by step; after the review the mines kill Farragut, as approved F4 requires (*Hartford* strikes the new row leading the column across at his order), and he is not made vice admiral.
- **CR-064, Atlanta:** Polk's divisions held Resaca historically, so Polk comes east in May; after the review the Snake Creek hinge is Thomas at the gap's mouth on the afternoon of 10 May, the Alabama flank is Richmond's order which Johnston makes his plan, and Polk strikes Kingston in August so that Thomas's caution is learned; Grant chooses McPherson for the West and is overruled for Thomas.
- **CR-064, Halleck:** his May 1861 sailing is now a labelled divergence (historically appointed in August while in California).

## Checks

- X1 `lint_canon.py --only` on CR-063 and CR-064: clean after every change.
- X2 `cr_facts.py preview`: CR-063's three fact changes unchanged and clean; CR-064 none.
- X3 Interfaces: CR-064 takes CR-063's 12,500 escapees; CR-065's needs (Thomas's army engaged in September–October; S-a; Mobile in February) still met. Not edited: CR-059 to CR-062, CR-065, CR-061 (another session was working on CR-061 the same evening).

## Resume here

- CR-063 and CR-064 are drafts on `revision/cr059-oregon` (PR #69), each with a "Self-directed cycle, 9 November 2026" section at the end. Canon, the register, the facts file and the ledger are unchanged.
- Next: the author reads the two cycle sections and decides the open decisions (CR-063: 1–13; CR-064: 1–18) and the canon tensions (CR-063 CT1–CT14; CR-064 CT1–CT5). The judgement calls most worth the author's eye: CR-063 open decision 8 (the 17 May gamble), CR-063 Part VI steps 5–7 (how Farragut dies), CR-064 open decisions 3, 5 and 7 (Thomas's appointment, the June order, the gap's mouth).
- Research still open: CR-063 tasks 1–3, 5, 11–12; CR-064 tasks 8, 9, 14 (Castel on Resaca's defenders; the Fort Gaines supply and the torpedo field; Granger's numbers; the River Line). Unfinished items stand as story assumptions until checked.
