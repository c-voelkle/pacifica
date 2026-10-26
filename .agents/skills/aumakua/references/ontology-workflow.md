# Ontology-assisted consistency audits

Use this workflow for substantial Aumakua audits when the repository has `docs/power-review/ontology/consistency/`. Read that profile's README, ontology, shapes and queries, plus the compact profile's source/claim definitions. Reuse them; no database or new dependency stack is required. A narrow passage question need not produce a graph.

## Preserve the independent pass

Complete the requested continuous prose reading and save its findings/coverage as a frozen `prose-first.md` before inspecting existing graph suggestions or prior issue lists. Pin the narrative, approvals, identities, skill/profile versions and this snapshot. If earlier records were already visible, describe that exposure; do not label the pass independent. An existing saved review can be linked retrospectively, but that is a conversion of earlier findings, not a fresh blind test.

Select an existing graph only if its revision, cases and source scope are relevant. Never silently load the old gold pilot. Pin the chosen graph as a SourceDocument and name it in the Audit. Reconcile each input graph's local SourceDocuments into the new manifest. Preserve its original historical-retrieval status; graph reuse is not new research. If no graph is relevant, author the source/finding/coverage records without inventing missing power Claims.

## Run suggestions, then review the prose

The query file supplies overlapping-period relational disagreements and quantity differences, plus finding links, coverage and unmapped read passages. Candidate comparisons require exact shared entity, relationship, case, jurisdiction and authorial status; quantity candidates also share unit, accounting basis and quantity kind. These are conservative suggestions, not a complete contradiction detector. Coarse year overlap, unstructured conditions, different narrator stances, amendments and different metrics can still explain a row. Exact-string units/bases can miss equivalent formulations; no conversion or identity merging is inferred.

Run the final validator/query command below after building an initial audit shell and selecting data; query rows can then guide additional source inspection. Candidate queries may also be executed directly with RDFLib on the explicitly selected graph before final assembly. Save the executed rows, including an empty result. Check the raw passages and governing approvals before accepting any candidate. Add accepted findings with `GraphSuggested`; rejected candidates can be recorded as compatible readings. Do not rewrite the frozen prose-first record. Consult prior issue lists afterward and record their dispositions with `PriorReconciliation` when adding them.

## Write the linked record

Use stable review-specific IRIs. The additive profile has three record types: Audit, Finding and CoverageRecord. Reuse core SourceDocument, SourcePassage and existing Claim IDs. Do not represent a contradiction as an unqualified world triple or force it into Aegis's restricted power predicates.

- Audit: source revision, actual coverage, exposure/order note and pinned prose snapshot; pin any inspected existing graph.
- Finding: paired quote-bearing passages, classification and separate lifecycle, detection basis, normalized scope, reasoning and compatible readings. Link relevant existing Claims with a note stating their bounded relevance. If none represents the issue, supply `claimGap`; partial/contextual links may also retain a gap. Preserve missing extraction explicitly rather than inventing a Claim to hide it. Mark repair options as proposals. Resolution requires evidence.
- SourcePassage: source document revision, precise locator and short exact quotation. Separate fragments in one paragraph may use different passage IDs. Prefer inclusive line windows for local text. The runner checks the quoted string against pinned UTF-8 source text and, when supplied, those lines. This checks text identity, not interpretation or source authority.
- CoverageRecord: passage, directly-read/searched-only/unread mode, actual mapped Claims and an extraction note. A contextual related Claim is not automatically a complete extraction mapping. Findings need directly-read coverage for each cited passage in the same audit. Coverage is declared, not mechanically certified; record the whole requested scope in the coverage note, not just passages that yielded findings.

Preserve local PROPOSED, OPEN and MODEL qualifications in the normalized scope and linked Claims. Classification, lifecycle, authorial status and detection basis are different schemes. A compatible reading can have a Finding record without becoming a contradiction. Prior finding IRIs remain stable and may refer to an earlier review without merging its whole graph.

## Execute and reconcile

Save `audit.ttl`, `input-manifest.json`, `prose-first.md`, the readable final review and executed JSON output in a unique review directory. The manifest's `files` maps each local source path to `sha256` and `hash_basis` (`ExactBytes` or `LFNormalizedText`); follow the core profile's existing conventions. Record skill/profile hashes separately as execution provenance. Use Python with RDFLib/pySHACL from the core requirements and UTF-8 stdout:

```sh
python -X utf8 docs/power-review/ontology/consistency/validate_consistency.py \
  --data outputs/REVIEW/audit.ttl \
  --data outputs/EXPLICITLY-SELECTED/review.ttl \
  --manifest outputs/REVIEW/input-manifest.json --repository .
```

Omit the second `--data` when there is no selected existing graph. No data or manifest defaults to a pilot. The runner validates core and consistency records, checks source hashes and quotations, and executes all five views. Save stderr/failures too. Resolve structural mistakes, inspect candidate rows, and reconcile finding IDs and dispositions with the final prose. Preserve unresolved editorial issues; validation is not a consistency score, a coverage guarantee or author approval.
