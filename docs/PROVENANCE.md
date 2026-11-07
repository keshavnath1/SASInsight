# What SASInsight keeps and leaves behind

SASInsight is newly authored as a skills-led upstream planning workspace. It draws on domain lessons from [sas-reverse-engineering](https://github.com/keshavnath1/sas-reverse-engineering/tree/400138a74d7bc2fb76c294efc3d8a919411457b1), inspected at commit `400138a74d7bc2fb76c294efc3d8a919411457b1` on 2026-11-07. No runtime source code, fixed-fixture outputs or approval history was copied.

**Kept:** source-linked SAS reading discipline; state/order/missing-value/modeling pitfalls; separation of source facts, intended business requirements and target proposals; conservative dependency reasoning; independent source-aware review; honest unmeasured/unapproved status.

**Left behind:** the 28-script dispatcher surface, packaged parser/runtime, platform filesystem/bootstrap qualification, frozen artifact identities, historical regression totals, legacy scope forms, approval ledgers and fixed-fixture limitations. They remain unchanged in the original repository and do not qualify SASInsight.

The new repository uses six small instruction skills, Markdown outputs/progress and one optional standard-library file-hash helper. The helper proves only that currently read file bytes match the recorded snapshot. It does not prove complete SAS semantics, hostile-writer safety, source authenticity or human approval.

Skill discovery follows current [Codex documentation](https://learn.chatgpt.com/docs/build-skills) and [GitHub Copilot documentation](https://docs.github.com/en/copilot/concepts/customizations/agent-skills), which support `.agents/skills/`. Host/version/policy differences still require a fresh-chat discovery check; no local Codex or Copilot execution is implied by these documentation checks.

The code and synthetic examples here are new. Real intake and generated outputs remain private by default. Publishing source files or reports requires explicit authorization, not merely a successful local review.
