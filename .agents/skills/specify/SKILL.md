---
name: specify
description: Draft PRD and module specifications from the SASInsight factual record and business context. Use after understand; legacy code is not approved business intent.
---

# Specify

Read AGENTS.md, SOURCE_EVIDENCE.md, supplied business context and PROGRESS. Cite O/D/U IDs rather than reconstructing a second factual record.

## Work

1. Separate supplied intent from inferred capabilities. If intent is absent, write a candidate goal labeled INFERRED and a human question; do not invent final requirements or stop all useful documentation.
2. Write PRD.md: DRAFT status, candidate outcome, capabilities, scope/non-goals, success criteria, dependencies, assumptions and open human decisions. Evidence-link source-derived capabilities.
3. Write MODULES.md: proposed boundaries, inputs/outputs, keys/known types, rules/invariants, state/order, cross-module contracts and unknowns. Group by capability/dependency, not automatically by program file.
4. Distinguish observed behavior from requested changes. Optimization may change execution structure, not silently change formulas, filters, multiplicity or model event definition.
5. List downstream decisions: business scope, runtime constraints, oracle/keys/tolerance and population. Present sample 50, full population, phased 50 then full, or custom governed sample as choices; mark OPEN unless explicitly chosen by the user. Recommendation is not selection.

Output PRD.md and MODULES.md only. Keep approval NOT_APPROVED and pass draft constraints to design. Do not edit facts, fit models, execute data or materialize approved migration config.
