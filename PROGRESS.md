# SASInsight progress

Updated 2026-11-07. This is the public project/rehearsal summary, not a live run-state controller or approval record. Each actual run keeps its own private `output/<run-id>/PROGRESS.md`; do not copy this summary into a new run as evidence.

## Author and reviewer were separate

In the synthetic Manus rehearsal, an author used the understand/specify/design skills on the two repository examples and wrote source-linked draft requirements and candidate ADRs. The author stopped before review. A different, fresh-context Manus reviewer then reread the original synthetic sources and the drafts, checked the existing input snapshot and wrote REVIEW.md only. A separate packaging context subsequently wrote the short reading guide and handoff.

The reviewer found no material factual/design contradiction. It reported nonblocking excessive detail. Packaging led with a shorter guide; the core design drafts were not repaired, and no fresh re-review occurred. Packaging is not a substitute for a repair/re-review cycle.

**Observed:** author/reviewer context separation, source-aware document review and package completion. **Not established:** live Codex/Copilot execution, protected evaluator isolation, an independent SAS oracle or human architecture approval. The public [validation record](docs/VALIDATION.md) describes the checks; the private detailed draft/review logs are deliberately excluded from Git.

## Bounded correction: specified, not yet exercised

The existing [operating contract](AGENTS.md#simple-records), [orchestrate](.agents/skills/orchestrate/SKILL.md) and [review](.agents/skills/review/SKILL.md) define:

```text
Author draft → fresh reviewer findings
    ├─ No material correction: package → human review
    └─ Draft correction needed: author revision 1 → fresh re-review
         ├─ Resolved: package → human review
         └─ Unresolved: PARTIAL/BLOCKED; no second revision loop
```

Factual errors or changed source start a fresh linked run rather than editing the factual record to make a design pass. Missing fresh review stays NOT_AVAILABLE and partial. These are instruction-level rules, not script-enforced identity, access or retry controls.

Actual rehearsal correction count: **0**. A completed repair/re-review cycle is **NOT_RUN**. A deliberately false ADR submitted for reviewer rejection is **NOT_RUN**. The reviewer identified unsafe interpretations as counterexamples, but did not reject a material false claim in an actual author ADR. The [walkthrough](docs/WALKTHROUGH.md#illustrative-false-adr-not-an-executed-result) labels the proposed demonstration explicitly.

## Current project checkpoints

The skills-led framework was published at `bac1f49`. The business purpose and design rationale were published at `3f1f6b6`. The current documentation update adds the [Jim-practices mapping](README.md#jim-thompson-practices-in-sasinsight), visible review/correction handoffs and truthful observed-versus-unrun status. Jim's guidance is attributed at its pinned source commit; historical results from the Codex repository are not inherited by SASInsight.

No new source analysis, false-ADR experiment, repair cycle or runtime test was executed for this documentation update. Final publication identity is the Git commit containing this file.

## Next evidence still needed

A separately requested synthetic demonstration could challenge the false independence claim in `examples/dependent.sas.txt`, retain the actual reviewer finding, let an author correct the draft once, and obtain a fresh re-review. Record all actual contexts, paths and outcomes; never prefill a rejection or pass. Keep original inputs and the source record unchanged.

Real assistant-host qualification, business intent/runtime selection, downstream migration, SAS tie-out and representative benchmarks remain outstanding. Runtime is **NOT_SELECTED**, approvals are **NOT_APPROVED**, and parity/performance are **NOT_RUN**.
