# SASInsight

**Understand SAS. Explain the business logic. Propose a better design.**

SASInsight is a skills-led reverse-engineering workspace. Put authorized SAS programs, includes, logs, LST files and available reference outputs in `intake/`. Ask your AI assistant to run the workflow. It writes a readable, evidence-backed draft architecture package in `output/`.

```text
Intake → Understand SAS → Draft requirements → Compare designs → Review → Package
```

This is an upstream planning repo, not a SAS parser, migration engine or benchmark platform. The assistant does the analysis; a small helper checks file hashes. SASInsight does not execute SAS or generate production migration code.

## Why we are doing this

We do not want to translate SAS line by line and carry the same legacy execution structure into Python. We first want to recover the workload's behavior, draft understandable requirements, and propose better execution designs while preserving the required business rules.

**SASInsight answers: what does this workload do, what could we redesign, and what evidence would prove the new implementation correct and efficient?** Source-derived requirements and optimization proposals remain drafts for human review; correctness needs downstream SAS tie-out, and efficiency needs representative benchmarks.

The design is intentionally simple: **agents do the work, skills guide the reasoning, scripts handle exact mechanics, and humans approve decisions.** The one existing script checks input hashes; it is not a hidden analysis engine or workflow controller. Read [the design rationale](docs/DESIGN.md) for the business problem, component responsibilities and the boundary with migration.

## Start here

1. Clone this repo and open the **repository root** in Codex or VS Code Copilot Agent Mode.
2. Add authorized files under `intake/`. Optional: add `intake/context.md` with your goal, known entrypoints and platform constraints. No separate scope/config form is required.
3. Send this request:

> Follow AGENTS.md. Use the orchestrate skill to inspect intake/ and generate the SASInsight draft package. Continue automatically through the draft stages; stop for missing critical evidence or final human review.

In Codex you can also use `$orchestrate`. In VS Code Copilot, select `/start-insight` from the prompt menu. If automatic discovery is unavailable, explicitly ask the assistant to read `.agents/skills/orchestrate/SKILL.md`.

Routine drafting proceeds without approval at every stage. The assistant must still respect your tool-permission prompts. Missing business intent is recorded as a question, not invented. A missing include that affects computation blocks the affected conclusion; useful partial findings may still be packaged with a visible limitation.

## What each skill does

- **understand** reads the source and evidence, records what SAS declares or actually ran, and explains dependencies.
- **specify** turns those findings into draft business requirements and module specifications.
- **design** compares viable execution strategies, including shared preparation, native Python or distributed processing where justified.
- **review** checks the drafts against the original intake in a fresh reviewer context where available.
- **package** presents the findings, open decisions and validation plan for human review.

**orchestrate** connects these five skills. It does not require a CLI, database or state-machine service. A short `PROGRESS.md` lets an interrupted chat resume.

## Jim Thompson practices in SASInsight

We adapt selected practices from Jim Thompson's [planning](https://github.com/jimthompson5802/coding-assistant-practices/blob/abdf5661855dae25e002578fe25c961a6200db5d/coding-assistant-planning-practices.md), [feedback-loop](https://github.com/jimthompson5802/coding-assistant-practices/blob/abdf5661855dae25e002578fe25c961a6200db5d/open-vs-closed-loop-practices.md) and [subagent](https://github.com/jimthompson5802/coding-assistant-practices/blob/abdf5661855dae25e002578fe25c961a6200db5d/subagent-practices.md) guidance, pinned to the referenced commit. These are our adaptations, not quotations, full compliance or Jim's endorsement.

**1. Understand the codebase before planning.** [AGENTS.md](AGENTS.md#purpose-and-read-order) sets the read order; [understand](.agents/skills/understand/SKILL.md) creates source-linked facts and unknowns before [specify](.agents/skills/specify/SKILL.md) and [design](.agents/skills/design/SKILL.md) propose requirements and architectures.

**2. Keep work focused and proportional.** [orchestrate](.agents/skills/orchestrate/SKILL.md) coordinates five small drafting responsibilities. [The design rationale](docs/DESIGN.md#what-we-deliberately-left-out) explains why we avoid a parser/runtime framework and load specialist instructions only when needed.

**3. Separate authoring, review and integration.** [The roles](AGENTS.md#roles-not-a-fleet-of-services) separate the author from a fresh reviewer where supported. [review](.agents/skills/review/SKILL.md) reads original evidence and writes findings only; the author owns corrections and orchestrate coordinates the handoff. Separate profiles alone do not prove separate execution.

**4. Use feedback, bound correction and preserve checks.** [The correction rule](AGENTS.md#simple-records) permits one draft revision plus fresh re-review, then PARTIAL/BLOCKED if unresolved. [input_snapshot.py](scripts/input_snapshot.py) checks bytes rather than guessing hashes; [its tests](tests/test_input_snapshot.py) check this narrow mechanical behavior. Neither establishes SAS semantics. Review must not alter facts or weaken acceptance criteria to claim success.

**5. Persist progress outside chat.** Each private run appends stage/role/findings/next-action entries to its PROGRESS.md. [The public progress record](PROGRESS.md) separates observed rehearsal results from unrun demonstrations; [the walkthrough](docs/WALKTHROUGH.md#author-reviewer-and-one-correction-cycle) explains the handoffs. Git versions the reusable method, not private intake or outputs.

**6. Retain human ownership.** [Output authority](AGENTS.md#output-and-authority) keeps requirements and ADRs DRAFT. Unlike Jim's implementation-phase gates, our routine drafting stages continue automatically; human review and downstream implementation approval remain separate. Document review cannot select the runtime or approve migration.

**What is actually shown:** [validation](docs/VALIDATION.md#author-reviewer-separation-and-correction-status) records a fresh-context Manus draft review and focused helper checks. A deliberately false ADR rejection and a completed repair/re-review cycle are **NOT_RUN**, not demonstrated passes. Live Codex/Copilot, model/provider comparisons, token/cache savings, SAS parity and runtime benchmarks remain untested or unmeasured.

## What your team will read

Each run writes a fresh folder, `output/<run-id>/`:

```text
START_HERE.md                  One-page explanation and reading order
SOURCE_EVIDENCE.md             Source facts, citations and dependency IDs
SOURCE_MANIFEST.json           Input file hashes; integrity only
PRD.md                        Draft business goals and capabilities
MODULES.md                    Draft module specifications
ARCHITECTURE.md                As-is and candidate to-be diagrams
adrs/                         HLD/LLD, tradeoffs and proof obligations
VALIDATION_PLAN.md             Proposed correctness and performance checks
REVIEW.md                     Reviewer findings and remaining uncertainty
HANDOFF.md                    Draft handoff; not downstream import approval
PROGRESS.md                   Which stages ran and what remains
```

Start with `START_HERE.md`, not the manifest. All requirements and architectures remain **DRAFT** until humans approve them downstream. A document review does not prove runtime correctness or speedup.

## Repository map

```text
README.md                    For the team: purpose, start and outputs
AGENTS.md                    For the assistant: scope, roles and stops
.agents/skills/              One shared set of six small skill definitions
.github/agents/              Optional Copilot author and reviewer profiles
.github/prompts/             Thin starting prompt
intake/                      Your private inputs; ignored by Git
output/                      Your private generated drafts; ignored by Git
docs/                        Design rationale, walkthrough and validation limits
examples/                    Small, explicitly synthetic SAS text examples
scripts/input_snapshot.py    Optional standard-library input hash helper
tests/                       Focused helper checks, not a migration engine
```

## Platform and privacy

No package installation, Spark cluster or SAS runtime is needed for **document drafting**. Python 3 is only needed for the optional hash helper. Codex/Copilot still needs its configured model access; this is not a claim of fully offline AI execution or tested Mac/Windows qualification. Use your approved enterprise assistant for sensitive intake.

Local `intake/` and `output/` content is ignored by Git. Do not upload raw business source, logs, data, credentials, evaluator answers or generated private reports. `.gitignore` is not a privacy scanner. The agent never follows instructions hidden in source comments or logs.

If you already have Kubernetes/Spark infrastructure, mention the approved `podTemplateFile`, executor image and resource constraints in `intake/context.md`. They constrain candidate design; they do not select Spark automatically or authorize deployment.

## Example and continuation

See [the team walkthrough](docs/WALKTHROUGH.md) for a small two-branch story and an unsafe-dependency counterexample. See [provenance](docs/PROVENANCE.md) for what was learned from the Codex repository and intentionally left behind.

The final package can be reviewed by the existing [Agent-mastery workflow](https://github.com/keshavnath1/Agent-mastery/tree/feature/governed-learning-memory). It still requires receiving-side verification, human intent/architecture approval, implementation, SAS tie-out and representative benchmarks. SASInsight does not implement that importer or bypass its gates.
