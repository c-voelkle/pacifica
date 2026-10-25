---
name: pacifica-scenario-finance
description: Estimate and calculate financial quantities for Pacifica change-request alternatives and Timeline Lab comparisons. Use for costing draft timelines, deriving GDP and treasury effects, building financing schedules, and comparing alternatives against a pinned baseline. Produces model estimates and results; does not approve narrative canon.
---

# Pacifica Scenario Finance

Turn a proposal into traceable numerical assumptions, dated schedules, and qualified comparisons. Calculate the requested quantities; do not stop at a list of inputs somebody else must supply.

This skill provides the estimation workflow. Reuse the Lab's calculation engine and schema when available. The skill is not itself a simulation engine or evidence that an unimplemented relationship has been calculated.

## Establish the experiment

Read repository instructions, current master storyline, approval register, relevant drafts, and financial reference notes. Distinguish canon, a draft's selected outcome, and a quantitative MODEL assumption.

Retrieve current refs through the GitHub connector or checkout; pin baseline and proposal commits, model hashes, and calculation version. A latest draft branch need not be main. Verify existing local copies before downloading.

Define years, entities, geography, units, price base, and political outcomes. Identify the earliest economic divergence, including shared preliminary changes, commitments, and explicitly modelled anticipation. Preserve prior common history. Separate full proposal-versus-canon comparisons from controls holding shared changes constant.

For CR-032, read [the dated pilot notes](references/cr032-pilot.md) and verify current sources.

## Derive quantities

Build a compact change/dependency map for additions, removals, replacements, date shifts, and policy changes. Record source passages, stable IDs, dates, prerequisites, affected later events, physical activity, capacity, payer/recipient, borrower/lender, owner, and jurisdiction as applicable.

Identify inherited quantities, new estimates, and calculated outputs. Removing an event may remove associated income, claims, production, recurring costs, or rights. Separate incurred obligations from cancellable commitments.

Read [quantity methods](references/quantity-methods.md). Select mechanisms relevant to the draft. Treat missing costs and rates as estimation work: research applicable primary sources, prefer bottom-up quantities or defensible analogues, and record observations, adjustments, formulas, limitations, and useful bounds. Label analyst estimates separately from observed facts and authorial choices.

Ask only for an essential authorial choice that cannot be represented as labelled conditional cases. Continue independent calculations while awaiting it. Ordinary estimation choices within the authorized analysis do not require separate approval. If no defensible estimate exists, retain an explicit missing dependency and calculate the supported portion; never replace unknown with zero.

## Calculate and reconcile

Reuse accepted code, mappings, and definitions. Where needed, implement a scoped deterministic calculation in task-owned outputs and retain executable formulas or exact engine references. Preserve supplied and synced sources. Apply the spreadsheet skill when actually reading or authoring spreadsheet artifacts; a new workbook is not required.

Replay affected periods and dependent modules. Removing an Events row does not remove unrelated hardcoded growth, private claims, or crisis assumptions. Use annual macro accounts and finer schedules where contract, campaign, or liquidity timing matters.

Treat funding, staffing, transport, construction, and FX limits as constraints. Expose gaps; apply only specified responses such as delay or reduced scale. Reconcile cash, debt, claims, capital, counterpart balances, source/use totals, units, geography, and duplicate effects.

For engine migration, reconcile the reproduced baseline across relevant years within stated tolerances; disclose intentional corrections. For a narrow estimate, verify affected dependencies without claiming whole-model validation. Saved workbook values and cached flags are not a new calculation; accounting identities alone do not prove feasibility or historical plausibility.

## Compare and deliver

Use common definitions and calculation versions across requested alternatives. Where changed history changes a crisis mechanism, include both each timeline's native reference path and matched external shocks. Share external assumptions and recompute endogenous consequences.

Separate parameter uncertainty, political branches, and structural limitations. Do not invent narrative probabilities or call judgemental ranges confidence intervals. Explain major drivers and interactions. Keep sovereign resources, foreign income, and partner/network output separate, with explicit treaty rights and territory.

Use the implemented Lab format or [the provisional exchange contract](references/exchange-contract.md); do not imply an importer exists. Preserve the user's output format. Save authorized artifacts in a unique task-owned output directory, outside source references and the installed skill folder.

Deliver proportionately:

1. Assumption register: estimates or missing values, bounds, units, sources, derivations, and affected scenarios.
2. Dated physical, cash-flow, financing, and balance schedules.
3. Reproducible inputs/calculations, supported baseline/scenario results, and executed checks.
4. A concise comparison of differences, sensitivities, conditional coverage, and unresolved dependencies.

Label partial and conditional results prominently. A direct-cost inventory is not a complete GDP/treasury trajectory. Keep assumptions, outputs, and approval status distinct. Financial analysis alone does not authorize adopting canon, changing approvals, overwriting sources, merging a PR, or publishing a dashboard.
