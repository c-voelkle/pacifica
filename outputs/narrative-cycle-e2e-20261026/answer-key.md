# Parent-only criteria, withheld from all evaluators

## T1 — coordinated Draft cycle (Mahoe vs skill-free control)

Request: Noe seems passive in 1887–88; explore giving her a real move in the succession; if one direction is clearly best, draft it as a CR; do not adopt.

- A1 Scope: explores first, drafts at most a standalone CR; no edits to master, change_requests.json, character bible/registry or AGENTS.md.
- A2 Objective: recenters on what Noe wants and can do with her contemporary information, not on giving her a plot function. Retains a baseline / minimal-clarification case.
- A3 Authority: respects the 1887 regency article naming Victoria; natural guardianship is a claim and political lever, not a legal path to the regency, unless a new premise is explicitly marked. No invented office, legal right or Chamber power left unmarked. Ministers answer to the ruler, not the Chamber.
- A4 Mystery: no culprit and no implied guilt; character bible requires not making Victoria guilty by implication. Noe's move may add motives, which should be noted as such.
- A5 Facts kept: adoption 1886, Elias dies August 1887, Noe dies autumn 1888, registers disappear a month and return in the Office (est. 1888), Hollerith tabulates from 1888, Albert Kūnuiākea is Emma's cousin and heir, natural son of Kamehameha III.
- A6 Propagation: names affected passages beyond §23 (§20 "lives to see neither"; overview line; §24 Five/Hollerith; trajectories entry; character bible Noe/Victoria entries; registry) as impact notes.
- A7 Process (Mahoe only): handoff briefs with real inputs; reviewers receive candidate without writer advocacy; Aumakua and Imi independent; reconciliation gives every finding a disposition; session record at outputs/sessions/<date>-<slug>/ per template; relative paths; stop reason.
- A8 Reply: proportionate, leads with the answer, ends with consequential open author choice; provenance kept out of the main reply.

## T2 — seeded review of candidate §23 (Aumakua + Imi vs two skill-free reviewers)

Planted problems in candidate-23.md:

- P1 Age: "twenty-four-year-old" in January 1888 vs born c.1860 (about 27–28).
- P2 Mystery breach: physician signs "before he has seen the body, on instructions from the palace" — narrator-level fact implying Victoria; conflicts with the protected mystery and the bible's "not guilty by implication".
- P3 Authority: Chamber of Deputies grants guardianship — no such power; ministers answer to ruler; new legal power invented; tension with the regency article and Victoria's adoption requirement.
- P4 Foreknowledge: Noe "knows" registers will decide Gulf entry and league tables (later developments).
- P5 Unearned compliance: Victoria "accepts every condition at once" because she admires her; erases Victoria's requirement and the "respect and fear" relation of §20.
- P6 Identity: Albert Kūnuiākea called "Emma's son"; canon: Emma's cousin and heir (CR-027).
- P7 Cross-section: Hollerith tabulation "in 1890" vs §24 and character bible "from 1888".
- P8 Form: Anne of Austria comparison inside canonical story prose; AGENTS.md puts comparisons in historical_background.md.
- P9 Invented quantity: "forty thousand Hawaiians" unlabelled; bible says the work is limited and foundational.

Pre-existing (not planted):

- K1 "Caleb, the Donner telegraphist burned in his hut that January" is ambiguous in current canon too (Caleb was shot at Donner in October 1887 per §22). Credit if flagged as pre-existing ambiguity or not raised; penalize if presented as a regression introduced by the candidate.

Also score: false positives (claims of conflict with compatible text), whether any reviewer resolves the mystery or proposes a culprit, whether reviewers rewrite canon, classification quality (contradiction vs literary vs form).

## T3 — sandboxed Adopt run (Kalai vs skill-free control)

Test-only author instruction: move Noe's death from autumn 1888 to spring 1889, keep cause/testimony/mystery; integrate into canon.

Dependency sites a complete integration must handle:

- master overview line ("dies in the contested typhoid outbreak of 1888").
- §23 death sentence; "the Regent's year" grouping (Caleb Oct 1887, January telegraphist, Noe) no longer fits one year — reword or mark OPEN, not silently keep.
- §23 Victoria "completes vaccination 1888–1892" and "rivalry with a dead woman": vaccination starting 1888 now overlaps Noe's own directorship — needs reconciliation or OPEN.
- §24 Hollerith tabulates "Noe's registers from 1888" while she is alive — compatible only if worded; the registers' disappearance and return "in the new Office" after her death now happen in 1889.
- Trajectories entry ("Her 1888 death"), unresolved-decision items 11 and 24 ("contested autumn 1888 death").
- character_bible.md: lines for Victoria (53), Noe status/Died (73), "achievement in 1886–1888" (79), death paragraph (83), vaccination (85), relationship list (634), resolved list (681); Hollerith entry (915) if touched.
- character_registry.json narrative profiles and legacy_conflicts ("death autumn 1888"); validate_character_docs.py passes.
- AGENTS.md authority line ("before her ambiguous death in 1888") updated or explicitly flagged.
- change_requests.json: new stable CR ID; hidden coverage comment adjacent in master; sync --write then --check pass.
- No culprit; no new events invented to fill gaps; protected mystery preserved.
- Report states what checks establish and do not.
