# Pacifica

Read the current [master storyline](book-agent/revision/master_storyline.md), supplied on 23 October 2026 and updated through CR-031.

The [character bible](book-agent/revision/character_bible.md), identity registry, [historical background](book-agent/revision/historical_background.md) and approval register are reconciled to that version. The [integration record](book-agent/revision/CR-031-integration.md) describes changes, source limits and validation. Original manuscripts, 250 original character profiles, stable mappings and older source CRs remain preserved.

Current financial planning uses the supplied [CR-031 workbook](finance/Pacifica_financial_model_1846-1932.xlsx). The [financial review](finance/CR-031-review.md) records saved MODEL results and source discrepancies; the older [Ledger](finance/Pacifica-Ledger.md) remains a dated snapshot. PROPOSED, OPEN and MODEL qualifications remain explicit.

Before and after a session, run `python3 tools/session.py start` and `end`. `book-agent/revision/lint_canon.py` checks prose against [canon_facts.toml](book-agent/revision/canon_facts.toml); `cr_facts.py` carries each approved CR's fact changes into it.
