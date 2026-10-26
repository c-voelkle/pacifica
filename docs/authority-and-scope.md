# Shared authority and scope rules

The Pacifica skills (Kalai, Clio, Chryseis) and any agent working in this repository apply these rules. Each SKILL.md states only how its own role applies them. When a rule changes, change it here.

## R1. Authority of sources

- Follow the repository's `AGENTS.md`, its canonical read order and its dated "current authorial authority" section.
- Current master storyline, CR register and direct author corrections govern. Later explicit author decisions override earlier proposals, source snapshots, legacy profiles and assistant suggestions.
- Use the current character bible and stable-ID registry for identity, motivation and voice. `book-agent/character_bible.json` and other first-draft sources never override approved kinship or chronology.
- Keep APPROVED, PROPOSED, OPEN and MODEL labels attached to the detail they qualify. An overview or an approved direction does not approve every detail beneath it.
- If approved instructions and current prose disagree, report the integration mismatch; do not silently pick one.

## R2. Working modes and authorization

The author's current request sets the mode. A session can move between modes.

| Mode | Permits | Does not permit |
| --- | --- | --- |
| Explore | Substantive analysis, challenge, alternatives | CR, canon, approval or identity edits. "Still brainstorming" stays binding until the author changes it. |
| Compare | Pinned cases, mechanisms, costs, outcomes; retaining the baseline is always a case | Treating the favored case as selected |
| Draft | A complete standalone proposal or candidate prose with impact notes | Altering the master, approvals or identities |
| Adopt | Revising master prose and affected records, synchronization, validation, within the stated scope | Expanding beyond that scope |

- A direct correction or integration instruction authorizes its stated scope. Do not ask again for permission already given, and do not turn routine specialist handoffs into permission questions.
- Publishing an alternative, adopting it, integrating it and merging a PR are separate scopes.
- Approval is never inferred from favorable verdicts, an attractive draft, another assistant's praise, a passing validator or elapsed time.
- Ask only for a genuinely consequential author choice that cannot be carried as labelled conditional cases. Continue independent work while it is pending.

## R3. No invention to close gaps

- Do not invent quantities, probabilities, scores, replacement events, off-page amendments, institutions, motives, culprits or genealogical links to make a draft, calculation or audit close.
- Unknown is never zero. Keep missing evidence, missing calculations and unresolved bridges visible, marked OPEN at the appropriate level, with concrete alternatives in notes.
- Protected mysteries stay protected: no murderer for Noe Kaʻanoe Ward, no resolution of open genealogy. A character's suspicion is not evidence.
- An explanation that makes an existing mechanism clearer is not an increase in power in the world. A new right, bargain, institution or resource is a new premise with its own consequences.

## R4. Contemporary actors

Actors pursue their own purposes with the information available at the time. The author's 1932 evaluation endpoint is not knowledge any earlier actor has. Partners, opponents and local communities keep their purposes and their ways to refuse. Do not assume the authored outcome of a contingency, such as a war, is inevitable.

## R5. Review independence

- For an initial independent assessment, give the reviewer the actual text and governing context, and withhold the writer's advocacy and other reviewers' conclusions. Reconcile known issues afterwards.
- State coverage and prior exposure honestly. If one agent performs several roles, say that independence was unavailable.
- Another model's opinion is not independent historical corroboration, and it does not supply a missing calculation.

## R6. Sources, outputs and versions

- Pin the baseline (commit and file hashes) before a substantial comparison, draft, audit or automated round.
- Supplied attachments, synced sources, the financial workbook, original manuscripts and legacy profiles are immutable unless a task explicitly authorizes changing them.
- Write working outputs to a task-owned directory, never into canonical prose, synced sources or installed skill folders. Session records follow [session-record-template.md](session-record-template.md).
- Record paths relative to the repository root. Do not record absolute local paths or usernames.
- Never update a hash alone to hide a changed premise. Changed premises make dependent conclusions stale until they are reassessed.

## R7. Limits of tools

- A passing validator establishes only the condition it checks. Synchronization of the generated index is not literary integration, and a clean `lint_canon.py` checks only the facts in `canon_facts.toml`.
- Skills are procedures. They do not install a scheduler, call another service, or message user-owned chats; those need their own implementation and the user's request. Supplied external critiques keep their provenance.
