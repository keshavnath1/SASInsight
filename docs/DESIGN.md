# SASInsight: why this design exists

## The problem we are solving

A SAS codebase often contains the most complete record of how a workload currently behaves, while business documentation and architecture diagrams are incomplete or outdated. Translating that code line by line can preserve not only its behavior, but also unnecessary sequential steps, repeated preparation and other legacy design choices.

Before building Python or a distributed implementation, the team needs to answer three questions:

1. **What does this SAS workload actually do, and what evidence supports that understanding?**
2. **Which behavior must stay the same, and which execution choices could be redesigned?**
3. **What should we implement next, and how would we prove correctness and efficiency?**

SASInsight turns authorized source evidence into a readable draft architecture package that helps people answer those questions. It is the **understanding and design step before migration**, not the migration engine itself.

## The outcome we want

The team should be able to open `START_HERE.md` and understand the workload, follow each important finding back to source, compare candidate architectures, and see the decisions and tests still required. This should take one starting request, not a sequence of unfamiliar verification commands.

Potential benefits are clearer requirements, better-informed modernization decisions and earlier discovery of unsafe optimization assumptions. These are design goals, not measured savings or guaranteed speedups.

## Understand behavior; do not copy execution structure blindly

Consider three SAS scenarios that appear to run sequentially. A modern design might share preparation and run independent branches concurrently. But three scenario names—or counts such as 1,000, 2,000 and 3,000 records—do not establish independence or justify distributed computing.

The agent first checks inputs, outputs, producer-consumer dependencies, grouping/order, mutable state and side effects. It then proposes a design with explicit safety conditions. If one scenario consumes another's output, that dependency stays in the target design. Missing includes or unresolved macro effects remain unknown, not evidence of independence.

The design separates **behavioral invariants** from **implementation choices**:

| Preserve unless a human explicitly changes scope | May redesign with supporting evidence and proof obligations |
|---|---|
| Business formulas, filters and model event definitions | Shared scans and preparation |
| Missing-value, duplicate and key behavior | Algorithms and intermediate materialization |
| Required grouping, order, state and output contracts | Partitioning, scheduling and runtime |

Native Python may be the best option. Spark, Ray or Dask are candidates when workload and platform constraints justify them—not mandatory destinations.

## How the repository works

```text
Human supplies authorized intake and a request
    ↓
AI agent reads AGENTS.md and orchestrate/SKILL.md
    ↓
understand → specify → design → review → package
    ↓
Readable draft output + open decisions + validation plan
    ↓
Human review and downstream migration workflow
```

The [operating contract](../AGENTS.md) defines scope and roles. The [orchestrate skill](../.agents/skills/orchestrate/SKILL.md) coordinates the next drafting step. The [specialist skills](../README.md#what-each-skill-does) explain how each step works.

## Why agents, skills and deterministic scripts are separate

| Component | Responsibility | Why it exists |
|---|---|---|
| AI agent: Codex or Copilot | Read files, reason and use authorized tools | The task needs interpretation of varied SAS workloads |
| Skills | Reusable instructions for understanding, specification, design, review and packaging | The team can inspect and improve the method without editing a runtime engine |
| Deterministic helper | Calculate/check input file hashes | Exact arithmetic and byte comparison should not be guessed by an LLM |
| Human | Confirm intent and approve downstream decisions | Source behavior and AI recommendations cannot grant business authority |

A skill can ask the agent to call a script for a mechanical operation. **That does not make the script the workflow controller.** The current repo has one helper, [input_snapshot.py](../scripts/input_snapshot.py); it does not parse SAS, draft requirements, select architecture or verify semantic equivalence. The team does not need to run it manually when the agent has permission to do so.

Scripts do not make AI reasoning deterministic. Skills guide behavior; they are not a tamper-proof enforcement system.

## Why these five drafting steps

| Step | Question answered | Main output |
|---|---|---|
| Understand | What does the supplied SAS declare or show it executed? | SOURCE_EVIDENCE.md |
| Specify | What capabilities and behavioral contracts can we draft from that evidence? | PRD.md and MODULES.md |
| Design | How might we preserve those contracts with a better execution structure? | ARCHITECTURE.md, candidate ADRs and VALIDATION_PLAN.md |
| Review | Are the important claims supported by original evidence? | REVIEW.md |
| Package | What should the team read and decide next? | START_HERE.md and HANDOFF.md |

`SOURCE_EVIDENCE.md` is the single factual record. Requirements and designs cite it instead of creating competing factual graphs. Source-derived requirements remain drafts: existing code reveals current behavior, not necessarily intended business policy. Humans must reconcile intent and requested changes.

A fresh reviewer challenges the author's claims without repairing the drafts during review. That review can improve document quality, but is not an independent SAS behavioral oracle. If a fresh context is unavailable, the limitation remains visible.

## Where SASInsight ends

Routine drafting continues automatically within tool permissions and scope. Critical gaps block affected conclusions; useful partial findings remain possible. Runtime choice and final approval are not silently delegated to the agent.

SASInsight delivers **proposals and a validation plan**, not proven optimized code. Downstream work must implement the approved design and satisfy two separate proof obligations:

- **Correctness:** compare implemented outputs against a trustworthy SAS reference using human-approved keys, population, coverage and tolerances.
- **Efficiency:** benchmark the implementation against a named baseline on representative workloads and comparable resources, after correctness passes.

A tie-out PASS does not prove speedup. A faster execution does not prove preserved semantics. Both require scoped evidence; neither is established by generating these documents.

## What we deliberately left out

No custom orchestration service, parser package, platform bootstrap framework, copied approval history or mandatory cluster is needed to draft the package. A short PROGRESS.md supports resuming the exact run. Input and generated output remain private by default; Git versions the reusable method, not business intake.

See [the walkthrough](WALKTHROUGH.md) for a small example, [validation](VALIDATION.md) for actual checks and limits, and [provenance](PROVENANCE.md) for the relationship to the original Codex work.
