---
name: sas-architect
description: Compare candidate component and runtime choices using the public running-balance evidence.
---

# Compare candidate component and runtime choices

## Trigger

Use this skill for its assigned review step in the [worked example](../../walkthrough/04-how-to-write-the-skills.md).

## Inputs

Read the [evidence graph](../../tests/fixtures/running-balance-workload/evidence/EVIDENCE.json),
[manifest](../../tests/fixtures/running-balance-workload/evidence/MANIFEST.json)
and [source program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).

## Workflow

Use the recovered state and branch constraints. Separate native Python from conditional distributed alternatives and explain the evidence needed to choose.

## Output

An HLD, LLD and draft ADRs with tradeoffs and decision owners.

## Checks and stop conditions

Cite the evidence pointer and original source location for each source fact.
Keep inferred relationships, profile assumptions and proposed decisions separate.
If an essential citation or prerequisite is missing, mark the affected claim
unresolved. Leave human decisions pending and preserve the SAS acceptance boundary.
