# CR-049 — verification and fresh-context review

**Status:** Review of a PROPOSED CR, 2 November 2026. This record does not adopt the fictional changes or certify the accelerated scientific dates.

**Baseline:** `main` at `a267b87103d9f7f11000225b12480c783bf6d821`, including PR #57's canon-revisability policy. The working proposals originated at `7ab6434`; the storyline, character and approval-register bytes are unchanged between those bases. CR-049 contains its own Canon tensions section under the new policy.

## Fresh-context review

One reviewer received only the actual CR, affected author/canon context, current repository AGENTS and shared scope rules. No writer advocacy, prior drafts or prior review findings were supplied. The retired Pacifica specialist skills were not used.

The review covered chronology, identities, authority, approval status, agency, causal development and usefulness as a formal decision record. It found two material payload issues:

- Regex backslashes in seven common fact additions had invalid JSON escaping. Corrected; all payloads now parse.
- A guard fixed neutron confirmation in 1890 although the chronology says “by 1890”. The exact-year guard was removed; the deadline remains.

The reviewer found no further material issues for publication as a proposed CR. Expedition episodes remain outline-level development work. Historical, financial and engineering feasibility were not independently verified by that review.

## Checks

- Current canon lint: clean, four files checked.
- Approved register/facts agreement: passes, 34 approved fact changes.
- Storyline/index synchronization: passes.
- Canonical character validation: passes, including 250 legacy profiles.
- Commitments ledger: 188 commitments checked, zero problems.
- Whitespace check: passes.
- Standard `cr_facts.py preview --tensions` executed with temporary data inside the working directory. Common payload: 14 additions; T2 adds seven scientific point dates. T1 and T3 have empty machine-readable amendments and explicit prose impacts/open decisions.

The **default draft lint reports seven unregistered IDs**, exactly the seven proposed characters. Those IDs remain absent from the canonical registry because the CR is unapproved. This is not reported as a clean default draft lint.

A separate read-only proposal-overlay check used the same linter, the declared proposed facts and **only those seven declared IDs** in addition to the current registry. It checked current canon and the CR for the common case and each tension independently: zero findings in all four cases. No canonical file was changed by either preview. Range-valued proposals remain explicitly subject to human comparison; the exact-year linter does not certify them.

## Publication boundary

The proposed PR adds only `book-agent/revision/CR-049.md` and this review record. It does not amend the approval register, master storyline, canonical facts, character documents, commitments ledger, supplied attachments or financial model. Earlier local working drafts are not included. Adoption and subsequent integration require an explicit author decision on the selected groups and tensions.
