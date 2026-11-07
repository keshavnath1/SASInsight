# One request, one understandable package

A team has SAS programs but no clear explanation of their behavior or options for modernization. Instead of asking AI to translate every line, they ask SASInsight to explain the computation and propose designs.

## Follow the files

1. **README.md:** the human sees the purpose, inputs, outputs and starting request.
2. **AGENTS.md:** the assistant learns its scope, author/reviewer roles and stop rules.
3. **orchestrate/SKILL.md:** it routes the request through five focused skills.
4. **intake/:** the actual source and supplied context become the evidence.
5. **output/<run-id>/START_HERE.md:** the team reads the result before looking at detailed evidence or ADRs.

The skills live once under `.agents/skills/`; no symbolic-link setup, script dispatcher or installed Python package is required.

## A small scenario

`examples/two-branches.sas.txt` is newly authored synthetic source text. It declares one preparation step and two branches that read the prepared data. One selects current records; another selects past-due records. That is an opportunity to consider shared preparation and possibly parallel branches—not proof that parallelism is safe or faster.

To rehearse only this example without analyzing the counterexample too, copy that one text file into a fresh authorized `intake/` (keep it as text), or explicitly scope the assistant to it. Say:

> Follow AGENTS.md. Analyze only the authorized synthetic two-branches.sas.txt example with the orchestrate skill and create a new draft output package. Do not execute SAS.

**understand** records source-linked operations: prepare, current, past_due. There are producer-consumer dependencies from prepare to both branches. Unknown input size, keys, other macro effects and actual execution stay visible.

**specify** drafts two capabilities and module rules. A business purpose inferred from those names remains a candidate interpretation until a human confirms it.

**design** compares a simple native baseline with a conditional distributed design. It explains partitioning, missing values, row multiplicity and output reconciliation. Runtime, oracle, tolerance and population choices remain OPEN. No speedup is fabricated.

**review** rereads the original text, checks citations and challenges whether the claimed dependencies and optimizations are supported. A separate reviewer context is useful but not a behavioral SAS oracle.

**package** writes START_HERE and HANDOFF. The team can see what is known, what is proposed, what remains unknown and what decisions come next.

## The unsafe counterexample

`examples/dependent.sas.txt` declares scenario_b reading scenario_a's output. A proposed design that starts both together without their producer-consumer dependency is wrong. The reviewer should identify the source-backed contradiction, not remove the edge to make the design pass.

Both files are source-only examples. They include no real customer data, SAS LOG/LST, generated predictions or runtime results. A source-only package can be useful and reviewable while behavioral tie-out and benchmarks remain NOT_RUN.

## Author, reviewer and one correction cycle

The author writes the factual record and draft PRD/ADRs. A fresh reviewer reads original intake and those drafts, then writes REVIEW.md only. The reviewer does not repair the author's work or rewrite expected behavior. Orchestrate reconciles the findings and routes any draft correction back to the author.

```text
Author draft → fresh review → author correction 1 → fresh re-review
                                                    ↓
                             Resolved: package for human review
                             Unresolved: PARTIAL/BLOCKED and stop
```

If no material correction is needed, go from review to packaging without inventing a repair. If a factual error or changed source is discovered, preserve the run and start a fresh linked run. Do not rewrite source evidence to rescue a failed ADR. If fresh review is unavailable, record the limitation rather than claiming independence. These are workflow instructions, not a new enforcement engine.

### Illustrative false ADR, not an executed result

For `examples/dependent.sas.txt`, a draft that says “scenario_a and scenario_b can start independently from the raw input” conflicts with line 8: `set work.scenario_a;`. The correct finding would cite that producer-consumer dependency. An author could revise the design to keep the dependency and obtain a fresh re-review; resolving this contradiction would still not prove runtime speedup or parity.

This is an **illustration** of the intended challenge, not an observed ADR rejection. The existing rehearsal used correct conditional designs, received a fresh Manus document review, and needed no material draft correction. False-ADR rejection and completed correction/re-review remain **NOT_RUN**. See [public progress](../PROGRESS.md) and [actual validation](VALIDATION.md#author-reviewer-separation-and-correction-status).

### What a private run records

Append to `output/<run-id>/PROGRESS.md` after each handoff: the role and actual context, skill, input/output paths, finding reference, stage status, correction count and next action. For example, an actual correction entry should cite the initial REVIEW finding and revised ADR; a re-review entry should name the new context and record its real outcome. Do not prefill results. Keep earlier entries and all unresolved findings.

The published root [PROGRESS.md](../PROGRESS.md) is only a sanitized project summary. It does not replace a run's detailed evidence or authorize another run. [Jim's practices](../README.md#jim-thompson-practices-in-sasinsight) explain why these responsibilities are separate.

## If the chat stops

Name the exact run and ask:

> Resume output/<run-id> using PROGRESS.md. Recheck the input snapshot and invoke only the next unfinished skill. Stop if inputs changed.

If there is no fresh reviewer capability, the package remains PARTIAL and says so. Open a new chat with the reviewer skill and exact input/run paths for an independent draft review. This does not require another state engine or hidden verification scripts.
