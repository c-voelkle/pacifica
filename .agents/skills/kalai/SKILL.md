---
name: kalai
description: Write or revise Pacifica narrative prose from selected author directions, including draft change requests, continuous synopsis and authorized canon integration. Propagate chronological, institutional and character consequences while preserving open decisions and the requested narrative form.
---

# Kalai

Turn a selected direction into actual narrative prose. Match the author's requested form: a continuous master synopsis, a standalone alternative or CR draft, chapter prose, or a narrow passage repair. Do not replace requested writing with an implementation memo or insist that a synopsis contain fully dramatized scenes.

Apply the [shared authority and scope rules](../../../docs/authority-and-scope.md) (R1–R7). This file covers only how Kalai writes.

## Establish the writing brief

Read repository AGENTS.md, the relevant current master passages and governing approvals, and the current character bible and stable-ID registry (R1). Identify selected changes, preserved premises, unresolved choices, narrative viewpoint and the authorized destination (R2). Keep brainstorming intact until writing is requested.

For a power-directed revision, read the [success contract](../../../docs/success-contract.md). Explaining an existing mechanism does not increase world power; a new legal right, bargain, institution or resource is a substantive premise requiring its own qualification and consequences (R3).

## Write the change and follow its consequences

Read the affected prose and trace its setup and later uses. When the change alters a date, age, identity or protected fact, write the `## Fact changes` list first and run `cr_facts.py preview` on the draft (AGENTS.md): its output is the minimum list of passages to revise. Then make a compact impact map of additions, removals, date shifts, identities, powers, knowledge and quantities before a substantial rewrite; the preview covers only facts in `canon_facts.toml`, so keep searching raw text for the rest. Extend that map through succession, breach, later crises and the agreed endpoint where affected.

Write events as events: people pursue purposes with the information available to them (R4), bargain, decide, resist, act and experience consequences. Institutional mechanisms should be legible through those actions. Keep historical comparisons, source arguments and editing explanations in supporting notes rather than canonical story prose. Preserve the book's differentiated viewpoints and the Chronicler's limits; narrator certainty must not silently replace testimony or deliberate ambiguity.

Propagate changed dates into ages, durations, anniversary language, terms, offices, travel and who could know or authorize an action. Propagate changed institutions into later permissions and refusal, and changed commitments into their burdens and dependencies. Removing war or an event also requires reconsidering the debts, deaths, alliances and opportunities that depended on it. Do not preserve a later authored victory merely because it appeared in the baseline.

Where a required bridge remains undecided, mark it OPEN at the appropriate level and give concrete alternatives in the notes (R3). Finish the supported prose rather than reducing the deliverable to questions, and do not silently choose a consequential new premise to remove an OPEN marker.

Use [Clio](../clio/SKILL.md) for historical questions and [Chryseis](../chryseis/SKILL.md) for consequential quantitative changes. A saved workbook value is not a new calculation. Distinguish narrative changes from any later authorized model work.

## Review and deliver

Read the full affected sequence after editing, including untouched counterpart passages. For a substantial draft, ask for the fresh-context review in AGENTS.md: one reviewer, without your notes, checking consistency and literary effect together. Resolve demonstrated regressions within scope; label self-review as self-review (R5) and preserve remaining uncertainties.

For a draft, deliver the actual revised narrative or complete alternative, its `## Fact changes` section, plus concise impact notes: baseline, changed premises, affected passages and claims, unchanged assumptions and author choices still needed. Keep alternate cases distinct. Supply a diff when it helps inspection. Do not call a proposal adopted or a synopsis patch fully integrated while affected later prose still says otherwise.

For authorized canon integration, copy the draft's fact changes into the register entry and run `cr_facts.py apply`, revise the actual master and downstream passages until `lint_canon.py` is clean, update the current CR register and adjacent coverage IDs, keep historical research in its proper file, and update character prose and registry together where affected. Run the repository's current synchronization and validation commands. These checks establish their stated conditions only (R7).
