# Session record template

Copy this file to `outputs/sessions/<YYYYMMDD>-<slug>/session.md` at the start of a substantial or resumable cycle. `<slug>` is a few lowercase words naming the question, such as `20261026-okhotsk-fortification`. Put specialist outputs, drafts, diffs and manifests in the same folder.

Fill only the sections the session uses. Delete a section rather than writing "n/a". Keep IDs stable once assigned: later rounds add new IDs and update status; they never renumber. Paths are relative to the repository root (R6).

ID prefixes: `D` author decision, `Q` open author choice, `C` case, `H` handoff, `F` review finding, `X` check executed.

```markdown
---
session: 20261026-okhotsk-fortification
started: 2026-10-26
updated: 2026-10-26
mode: draft              # explore | compare | draft | adopt (current; history below)
status: active           # active | paused-for-author | stopped
baseline:
  commit: 1f7be67
  files:
    book-agent/revision/master_storyline.md: sha256:<hash>
    book-agent/revision/change_requests.json: sha256:<hash>
independence: separate-agents   # separate-agents | same-agent (say which roles were combined)
---

# <The author's question, in one sentence>

## Brief

- **Desired outcome:** what the author wants this session to produce.
- **Objective:** the end sought, such as Julian's effective power by 1932 under the success contract, or a literary or consistency aim.
- **Authorization:** what the author has actually permitted, quoted or closely paraphrased, with date. What remains out of scope.
- **Sources of history:** which prior chats, CRs or critiques informed this, with provenance. Say what is unavailable.

## Mode history

| Date | Mode | Trigger |
| --- | --- | --- |
| 2026-10-26 | explore | Author: "still brainstorming, no CR revisions" |
| 2026-10-26 | draft | Author: "write C1 up as a CR" |

## Author decisions and open choices

| ID | Type | Statement | Source | Status |
| --- | --- | --- | --- | --- |
| D1 | decision | ... | author message 2026-10-26 | current |
| Q1 | open choice | ... | raised in session | open |

Decisions record what the author said. Discussion of an option is not a decision. Mark superseded decisions `superseded by Dn`; do not delete them.

## Cases

| ID | Case | Earliest divergence | World change or exposition only | Status |
| --- | --- | --- | --- | --- |
| C0 | Retain baseline | none | n/a | live |
| C1 | ... | 1874-03 | world change | live |

For each material case: concrete additions, removals and date changes; affected actors, institutions and passages; unresolved premises (link to `Q` IDs); consequences followed to the endpoint.

## Handoffs

| ID | To | Task | Inputs (paths and IDs) | Withheld for independence | Output | Status |
| --- | --- | --- | --- | --- | --- | --- |
| H1 | Kalai | Draft C1 as standalone CR prose | master §12–14; D1, Q1 | — | `draft-C1.md` | done |
| H2 | Fresh reviewer | Consistency and literary review of draft | `draft-C1.md`, master §12–14 | Kalai notes | `review-C1.md` | done |

## Review judgments

Keep the three judgments separate; never combine them into one score.

- **Contract:** per power dimension, improvement, weakening, trade-off or unresolved. Label explanation-only gains separately.
- **Consistency:** new supported conflicts; earlier findings retained, resolved or not reproduced; coverage actually read.
- **Literary:** concrete effects on agency, motivation, conflict, viewpoint, voice, structure and clarity.

| ID | Judgment | Finding | Location | Disposition |
| --- | --- | --- | --- | --- |
| F1 | consistency | ... | master §13 | repaired in draft v2 |

## Checks executed

| ID | Check | Result |
| --- | --- | --- |
| X1 | `python3 book-agent/revision/sync_master_storyline.py --check` | pass |

## Round log and stop reason

| Round | Date | What changed | Stop reason |
| --- | --- | --- | --- |
| 1 | 2026-10-26 | Draft C1 v1, reviews H2–H3 | Usable proposal; Q1 needs the author |

Stop reasons: usable proposal; requested comparison complete; blocked on named author choice (`Q` ID); blocked on unavailable evidence; iteration limit reached.

## Resume here

Two to four lines for the next session: current state, the next action, and which conclusions are stale because a premise changed.
```
