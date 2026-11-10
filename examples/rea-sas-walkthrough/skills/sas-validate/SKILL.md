---
name: sas-validate
description: Draft engineering and independent reference checks using the public running-balance evidence.
---

# Draft engineering and independent reference checks

## Trigger

Use this skill for its assigned review step in the [worked example](../../walkthrough/04-how-to-write-the-skills.md).

## Inputs

Read the [evidence graph](../../tests/fixtures/running-balance-workload/evidence/EVIDENCE.json),
[manifest](../../tests/fixtures/running-balance-workload/evidence/MANIFEST.json)
and [source program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).

## Workflow

Separate synthetic engineering expectations from SAS reference evidence. Identify the keys, row multiplicity, missing values and order checks.

## Output

A verification plan that leaves unperformed SAS and benchmark checks NOT_RUN.

## Checks and stop conditions

Cite the evidence pointer and original source location for each source fact.
Keep inferred relationships, profile assumptions and proposed decisions separate.
If an essential citation or prerequisite is missing, mark the affected claim
unresolved. Leave human decisions pending and preserve the SAS acceptance boundary.
