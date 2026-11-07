---
name: design
description: Propose evidence-backed modernization designs and candidate ADRs from SASInsight requirements and dependencies. Use after specify, not implementation, runtime selection or claimed speedup.
---

# Design

Read AGENTS.md, SOURCE_EVIDENCE, PRD/MODULES and supplied constraints. Use [the ADR template](templates/candidate-adr.md). Never alter facts to fit a runtime.

## Work

1. Inspect repeated scans/preparation, independent branches, group/state operations, joins, fitting/scoring and exports. Separate source-supported opportunities, suspected bottlenecks and unmeasured hypotheses.
2. Include a sensible native Python baseline when feasible and viable alternatives or explained exclusions. Compare Spark/Ray/Dask/hybrids only when warranted; no mandatory distributed runtime or invented cluster benefit.
3. Write ARCHITECTURE.md with readable Mermaid as-is/to-be diagrams. Link O/D/U IDs in nodes or accompanying text. Retain required dependencies and blocking unknowns. Separate branches in a diagram are not independence proof.
4. Write each viable `adrs/ADR-<id>.md`: DRAFT HLD components/flow; LLD operation/algorithm/partition/key/order/state/materialization/scheduling changes; preserved invariants; proof obligations; alternatives/tradeoffs; missing evidence and rollback ideas. These are candidates, not approved decisions.
5. If supplied, incorporate approved Kubernetes podTemplateFile, Spark executor image and resource constraints. Do not invent files/images, contact a cluster, generate deployment scripts or select Spark. Unknown platform details stay OPEN.
6. Write VALIDATION_PLAN.md with common comparison obligations: independent SAS oracle, keys, population choices, coverage, duplicate/missing/order/numeric semantics and proposed tolerance rationale. Keep choices OPEN and runtime producer/environment bindings deferred to downstream implementation.
7. Define a representative benchmark plan: baseline, workload/scale, resources, end-to-end metrics, repeats, warm/cold/cache treatment, correctness prerequisite and limits. Measurements are NOT_RUN unless genuine attributable supplied evidence is explicitly distinguished; never invent speedup.

Output ARCHITECTURE, candidate ADRs and VALIDATION_PLAN. Keep NOT_SELECTED runtime and NOT_APPROVED architecture unless a human choice is explicitly recorded; downstream approval still remains separate. Send to review. Do not write scorers/Spark jobs, fixture oracles or approved config/tieout.yaml.
