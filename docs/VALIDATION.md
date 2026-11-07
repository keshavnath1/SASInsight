# What has actually been checked

Local checks on 2026-11-07 in the Manus Linux sandbox:

- Six skill packages passed the skill-package validator.
- Ten synthetic tests passed for the optional input hash helper: reproducibility, unchanged check, modified/added/removed input, tampered/duplicate-key manifest, no overwrite, input/output separation, symlink rejection and nested files.
- Framework Markdown links and Git exclusions for private intake/output were checked.
- A Manus author-agent rehearsal used the actual understand/specify/design skills on the two newly authored synthetic source text examples. A fresh Manus reviewer reread the original evidence and checked source citations, dependencies, proposed changes, unknowns and authority language. No material source/design contradiction was found; overly detailed drafts were a nonblocking presentation finding.

The reviewer outcome concerns source-linked draft quality. It is not an independent SAS oracle, runtime tie-out or performance result. All generated rehearsal documents remain private under ignored `output/`; they are not accepted business evidence or seeded requirements for another run.

## Author-reviewer separation and correction status

**Observed in the synthetic rehearsal:** the author stopped after design; a different fresh-context Manus reviewer read original sources and actual drafts and wrote REVIEW.md only. It checked the unchanged source snapshot and found no material factual/design contradiction. A later package stage wrote a shorter reading guide without repairing the core draft designs. This demonstrates context-separated draft review in this bounded Manus exercise, not protected role isolation or live Codex/Copilot behavior.

**Specified but not exercised:** one author draft revision followed by fresh re-review, then stop PARTIAL/BLOCKED if unresolved. The actual rehearsal used **0 correction cycles**. A deliberately false ADR submitted for rejection and a completed repair/re-review cycle are **NOT_RUN**. Discussing unsafe interpretations in the review is not evidence that a false candidate ADR was rejected.

The [public progress summary](../PROGRESS.md) and [walkthrough](WALKTHROUGH.md#author-reviewer-and-one-correction-cycle) show the intended handoffs. They preserve the distinction between planned controls and observed results. No new agent experiment or runtime test was run for this documentation update.

## Limits and continuation

The input helper verifies recorded file bytes without parsing SAS. Frozen factual records and author/reviewer separation are instruction-level workflow rules, not a tamper-proof storage or access-control system. Open the exact run and recheck evidence before reuse.

Live Codex/Copilot discovery and execution have **not** been tested here: neither CLI is installed in this sandbox. Mac/Windows host qualification, real SAS workloads, downstream import, numerical parity, cluster execution, benchmarks and production readiness are **NOT_RUN**. Documentation describes the intended local skills workflow, not guaranteed offline AI or enforcement by the model host.

Maintainer checks (not the team's execution interface):

```bash
python3 -m unittest discover -s tests -v
```

For a real team trial, open the repository root in the approved assistant, verify that orchestrate is discovered or load its SKILL.md explicitly, and run authorized intake to a fresh output folder. Review the resulting guide and original evidence before downstream decisions. Do not inherit the synthetic rehearsal's interpretations as requirements.
