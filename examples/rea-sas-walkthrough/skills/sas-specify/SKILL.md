---
name: sas-specify
description: Draft the running-balance requirements using the public running-balance evidence.
---

# Draft the running-balance requirements

## Trigger

Use this skill for its assigned review step in the [worked example](../../walkthrough/04-how-to-write-the-skills.md).

## Inputs

Read the [evidence graph](../../tests/fixtures/running-balance-workload/evidence/EVIDENCE.json),
[manifest](../../tests/fixtures/running-balance-workload/evidence/MANIFEST.json)
and [source program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).

## Workflow

Use the DATA and SQL declarations to propose requirements for balance state, ordering and join multiplicity. Mark open policy choices explicitly.

## Output

A short PRD and module contracts with acceptance criteria and evidence references.

## Checks and stop conditions

Cite the evidence pointer and original source location for each source fact.
Keep inferred relationships, profile assumptions and proposed decisions separate.
If an essential citation or prerequisite is missing, mark the affected claim
unresolved. Leave human decisions pending and preserve the SAS acceptance boundary.
