# H5 — Aumakua: consistency audit of the CR-033 candidate against current canon

**Session:** `outputs/sessions/20261026-noe-succession-move/`
**Skill:** `.agents/skills/aumakua/SKILL.md` (with `.agents/skills/mahoe/references/authority-and-scope.md` and `.agents/skills/aumakua/references/review-records.md`)
**Deliverable:** `outputs/sessions/20261026-noe-succession-move/aumakua-H5.md` (readable issue ledger with coverage)
**Permitted side effects:** write the deliverable only. No canon edits; no sync script with `--write`. You may run read-only checks (`python3 book-agent/revision/sync_master_storyline.py --check`, `python3 book-agent/revision/validate_character_docs.py`) against the unchanged baseline if useful, and must report what they establish and what they do not. No web research.

**Ontology note:** the compact ontology runtime (rdflib/pyshacl) is not installed in this sandbox and must not be installed. Do a prose-first audit and state that graph integration and RDF validation were unavailable; do not claim them.

## Files to give the specialist

- `AGENTS.md`
- `.agents/skills/aumakua/SKILL.md`, `.agents/skills/aumakua/references/review-records.md`
- `.agents/skills/mahoe/references/authority-and-scope.md`
- `book-agent/revision/master_storyline.md` (full; baseline sha256 prefix 8b5df6f2b8bc9e32)
- `book-agent/revision/change_requests.json` (CR-016, CR-021 incl. R9-09, CR-022, CR-026, CR-027, CR-029 entries)
- `book-agent/revision/character_bible.md`
- `book-agent/revision/character_registry.json`
- `book-agent/revision/CR-016.md`, `CR-021.md`, `CR-022.md`, `CR-026.md`, `CR-027.md`, `CR-029.md`
- `book-agent/revision/historical_background.md` (Hawaiian rows only)
- `outputs/sessions/20261026-noe-succession-move/candidate-sections.md` (primary text under audit)
- `outputs/sessions/20261026-noe-succession-move/CR-033-draft.md`

## Withhold

`session.md`, `kalai-H3-notes.md` (writer's self-review and known-issue list), `imi-H2.md`, `clio-H1.md`, and any H4/H6 output. You will be shown prior findings only after your independent sweep.

## Task

Audit whether the candidate passages, read as if merged into the master, can all hold together with current canon and governing approvals. In particular, align and check:

- **Institutions and authority in 1887–1914:** does any candidate sentence imply a Hawaiian legislature, House of Nobles or ʻAha Aliʻi lawfully sitting before the 1914 Act; is the 1913 ʻAha Aliʻi stance (line 632) consistent with the candidate §26 sentence that no lawful chiefly body can act while the Territorial Council stands; does the Hawaiian Supreme Court plausibly exist and sit in 1887–88 per canon; does anything conflict with the 1887 regency article naming Julian Heir of the Realm or with the 1914 Act/plebiscite/Ka Lōkahi mechanics.
- **Chronology and knowledge:** winter 1887–88 timing vs Donner (Oct 1887), the January telegraphist death, the 1888 restriction, the Office of Public Measures founding (1888), Hollerith tabulation from 1888; Julian's and Victoria's ages; who knows of the undertaking when (unpublished default) and whether later clauses assume wider knowledge than the default permits.
- **Identity and kinship:** Noe's Maui line "traces its descent to Kahekili" — no new genealogical link beyond canon; Albert's description; no invented named chiefs.
- **Protected mystery and labels:** no culprit established or implied; APPROVED/PROPOSED/OPEN labels kept attached; no approved sentence altered.
- **Integration mismatches** between the CR draft's decision table (A1–A12), its section C text and candidate-sections.md.
- Any **pre-existing** canon tension the candidate surfaces (report as such, with its own classification).

Use the issue-ledger fields from `review-records.md`. Record coverage: directly read, searched-only, unread.
