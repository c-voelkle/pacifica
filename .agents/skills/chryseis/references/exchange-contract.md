# Provisional Timeline Lab exchange contract

Prefer an implemented schema. This is a fallback for reproducible financial-analysis packages, not a claim that a Lab importer exists. Preserve requested formats; describe any adapter needed.

Use one JSON bundle or linked JSON/CSV files for the manifest, assumptions, event changes, schedules, results, and checks. Include calculation code or an exact engine invocation. Omit irrelevant empty sections.

## Manifest

Record contract/run/experiment IDs; repository; baseline and proposal commits; source paths/hashes; scenario labels and parents; political assumptions; earliest divergence; years and resolution; engine revision; execution time; input hash; units, currency, price base, entities, geography, metric definitions; unresolved dependencies; seeds only when used.

Run states:
- specified: definitions exist, calculation not executed;
- partial: some quantities calculated, affected outputs unavailable;
- conditional: executed under explicit unresolved branch assumptions;
- calculated: declared scope executed with required inputs.

These states are separate from validation, estimate quality, narrative approval, and feasibility. Mark saved workbook results as imported-cache origin. Retain earlier runs; changed inputs, sources, code or shocks create a new run identity. Associate UI caches with input and engine hashes.

## Assumptions

Each material input needs a stable ID, description, role, applicable scenarios/entities/periods, numeric value or null, units/scale/currency/price base, bounds and rationale, dependencies/correlation, and source kind.

Source kinds: supplied_model, historical_observation, analyst_estimate, author_scenario_assumption, derived.

Retain exact source passages/cells or external URLs and locators; raw observations; conversions; derivation formulas/code and input IDs. Keep narrative and quantitative approval separate. For missing values record the reason and affected outputs. Unknown is not zero; a derived value must not become an unexplained input. Avoid arbitrary confidence scores.

## Event changes

Use stable semantic IDs plus source row/cell mappings. Operations include add, remove, replace, shift, change_scale, change_funding, change_policy.

Record target, source, dates, preconditions, entities, quantities, funding, accounting, and dependent events/claims. Make replacement relationships explicit. Resolve conflicting changes to the same field/period; do not silently apply the last one. Unpriced additions are not free.

## Schedules and results

Records carry run_id, scenario_id, entity_id, metric_id, period, value or null, units/scale/currency/price base/geography, provenance/dependency IDs, and coverage/status/reason.

Metric kinds: flow, opening_stock, closing_stock, rate, capacity, diagnostic. Transactions additionally identify relevant counterparties, ownership/instrument, cash/noncash treatment, and commitment versus drawing. Declare signs.

Annualization sums flows, takes stock endpoints, and recomputes ratios from matching components. Do not sum debt stocks. Compare requested cases with the pinned baseline and labelled controls/shocks; percent change from a zero baseline is undefined.

Supported metrics may include nominal/real GDP, population/per-person output, Treasury revenue/spending/balance, cash, gross/net public debt, reserves, monetary gold, public/private foreign claims, debt service, cumulative costs, and funding gaps. Deliver relevant supported measures; mark required unavailable outputs explicitly.

## Checks and explanation

Each check records ID, scope, expected identity/limit, observed value or residual, tolerance, status, and evidence. Separate arithmetic errors, missing evidence, infeasible resources, and assumed political outcomes.

Explain influential assumptions, reconciliation differences, conditional branches, and unresolved mechanisms. A direct-cost calculation is not a macro simulation; schema validation is not independent financial validation.
