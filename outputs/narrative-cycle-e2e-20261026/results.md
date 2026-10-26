# Second narrative-cycle evaluation: results

26 October 2026. Three tests on real Pacifica canon (§§20–24, Noe Ward and the 1887–89 succession), each run once with the updated skills and once by a skill-free agent that had only the repository and its AGENTS.md. Every run used a disposable sandbox copy; nothing here changed canon. The parent's [answer key](answer-key.md) was withheld from all agents. One run per condition: these are observations, not a benchmark.

## T2 — seeded review (candidate §23 with nine unlabelled planted problems)

| Reviewer | Planted problems found | Pre-existing "telegraphist" ambiguity | Length |
| --- | --- | --- | --- |
| Aumakua (skill) | 9 / 9 | said "no conflict" | ~3,250 words |
| Imi (skill) | 9 / 9 | correctly flagged as pre-existing | ~2,600 words |
| Consistency (no skill) | 9 / 9 | not raised | ~1,850 words |
| Literary (no skill) | 9 / 9 | not raised | ~2,200 words |

**No detection difference.** The skill-free reviewers caught everything the skilled ones did, in shorter reports. The skills added citation of approval IDs and coverage statements, not findings.

## T3 — sandboxed Adopt (move Noe's death to spring 1889)

Both runs integrated the change across master, CR register, character bible and registry and AGENTS.md; added CR-033 with coverage comments; passed `sync --check` and `validate_character_docs.py` (re-verified by the parent); kept the mystery; and marked the new 1888 overlap (Office, vaccination, Hollerith while Noe lives) OPEN rather than inventing a fix. Kalai put the OPEN marker in story prose and also updated the power timeline; the control kept it in the unresolved list. **Roughly equal.**

**Real workflow gap found by both runs independently:** any authorized canon change breaks the ontology CI check, because its manifests pin hashes of `master_storyline.md`, `change_requests.json` and `character_registry.json`. The skills say "never update a hash alone", but the repository has no documented refresh step for Adopt. This needs fixing before the next real adoption.

## T1 — coordinated Draft cycle ("give Noe a real move in the succession")

| | Mahoe (skill, coordinated) | No skill (single agent) |
| --- | --- | --- |
| Time | ~2.5 hours, not finished (last re-check pending when stopped) | ~23 minutes |
| Handoffs | 9 (Clio, Imi ×3, Kalai ×2, Aumakua ×2, Aegis) | none |
| Text produced | ~35,000 words of working files | ~2,700-word CR draft + reply |
| Direction chosen | Guardian's petition to the Hawaiian Supreme Court traded for a Hawaiian-succession undertaking | Essentially the same |
| Scope kept (no canon edits) | yes | yes |
| Session record | followed the new template | n/a |

Both converged on the same idea independently. Mahoe's process did work as designed: briefs listed real inputs and withheld advocacy, and the independent reviews caught real problems in its own first draft (sentences tilting suspicion toward Victoria; a conflict with the eight aliʻi Senate seats from 1887) that were then repaired. The control's draft was never independently reviewed, so it is unknown whether it has the same problems.

## What this means

- On this evidence, the specialist skills do not outperform a strong model with the repository's AGENTS.md on detection or adoption. AGENTS.md already carries most of the value.
- Mahoe's full cycle costs roughly six times the time of a single pass for the same direction. Its only demonstrated advantage is independent review of its own draft, which a single review pass could supply far more cheaply.
- Recommended next changes: make Mahoe's default a single drafting pass plus one independent review, with full multi-specialist rounds only on request; cap a cycle at one revise-and-review loop; add a documented ontology-manifest refresh step to Adopt.

## Limits

One run per condition; the parent wrote the seeded candidate and judged the outputs; the T1 Mahoe run was stopped before its final reply. The relay of handoffs went through the parent, which added waiting time a native subagent setup would not. Two agents wrote temporary files just outside their sandboxes (disclosed by them); no answer-key file was read by any agent.
