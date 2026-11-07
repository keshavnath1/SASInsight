---
name: package
description: Assemble SASInsight drafts into a reading guide and candidate handoff after review. Use for final human presentation, not downstream import approval, release or publication.
---

# Package

Read AGENTS.md, actual outputs, REVIEW and PROGRESS. Keep every file in the run folder. Packaging means a readable guide/handoff, not another archive, graph or runtime.

## Work

1. Reconcile actual files and retain reviewer findings. Never invent missing review/ADRs/approvals to make a package look complete. Mark missing artifacts PARTIAL/BLOCKED.
2. Check the source manifest if available. Changed source prevents ready status and requires a fresh linked run. NOT_CHECKED integrity or unavailable independent review remains visible and PARTIAL.
3. Write START_HERE.md: plain-language workload story, coverage, SAS behavior, proposed module/design choices, relative reading links, open decisions and actual readiness.
4. Write HANDOFF.md: DRAFT authority, snapshot hash when available, evidence/requirements/ADR/review links, recommendation, unresolved decisions and limits. Downstream canonical trace/map/IR/evidence paths are receiving targets, not artifacts SASInsight has produced.
5. Explain downstream requirements: source verification, human intent/PRD/SPEC/ADR approval, implementation, governed fixtures/oracle, exact approved tie-out contract, correctness checks and representative benchmarks. No receiver is implemented here.
6. Finish PROGRESS with readiness, actual integrity/review status, executed/not-run actions and a copy-ready human-review request. Approvals remain NOT_APPROVED; runtime tie-out/benchmarks remain NOT_RUN unless genuine scoped supplied evidence is separately attributed.

Return the run folder and START_HERE path, brief proposed choices/open decisions and next action. Stop for human review; do not push private outputs, select architecture or invoke downstream migration.
