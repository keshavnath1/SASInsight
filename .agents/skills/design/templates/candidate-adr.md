# ADR-<id>: <candidate execution strategy>

**Status:** DRAFT / NOT_SELECTED / NOT_APPROVED

## What changes and why

Explain the source-linked opportunity, operation/dependency IDs and scope. Separate a suspected bottleneck from measured evidence.

## HLD: components and data flow

Show a readable Mermaid diagram with source-linked operations and shared preparation/scheduling only where justified. List constraints and unresolved dependencies.

## LLD: how the work would run

Describe proposed operation changes, algorithm, partition/group/key/order handling, joins, state, memory/materialization, model fitting versus scoring, and output reconciliation. Do not generate production code.

## What must stay the same

State formulas, filters, missing values, row/key multiplicity, grouping/order and business/model invariants. Cite SOURCE_EVIDENCE IDs.

## Why the transformation may be safe

Record supporting evidence and exact proof obligations. Missing evidence remains UNKNOWN; a diagram is not proof.

## Tradeoffs and alternatives

Compare native baseline and other viable designs, coordination/data-transfer costs, failure recovery, operational constraints and scalability hypotheses.

## Validation and rollback

Reference the common correctness plan. Describe runtime-specific tests and a representative benchmark. Measurements: NOT_RUN. Explain reversal triggers and rollback approach without claiming an implemented rollback.

## Human decisions

List unresolved scope, architecture, oracle, keys, population, tolerance and platform choices. Candidate recommendation is not selection.
