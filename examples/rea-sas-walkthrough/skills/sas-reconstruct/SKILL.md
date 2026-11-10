---
name: sas-reconstruct
description: Recover the public SAS source behavior using the public running-balance evidence.
---

# Recover the public SAS source behavior

## Trigger

Use this skill for its assigned review step in the [worked example](../../walkthrough/04-how-to-write-the-skills.md).

## Inputs

Read the [evidence graph](../../tests/fixtures/running-balance-workload/evidence/EVIDENCE.json),
[manifest](../../tests/fixtures/running-balance-workload/evidence/MANIFEST.json)
and [source program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).

## Workflow

Match original source spans to operations, and report unsupported scope or unresolved prerequisites.

## Output

A cited TRACE/MAP summary distinguishing declarations and inferred edges.

## Checks and stop conditions

Cite the evidence pointer and original source location for each source fact.
Keep inferred relationships, profile assumptions and proposed decisions separate.
If an essential citation or prerequisite is missing, mark the affected claim
unresolved. Leave human decisions pending and preserve the SAS acceptance boundary.
