---
name: sas-analyze
description: Check whether enrichment depends on SORT using the public running-balance evidence.
---

# Check whether enrichment depends on SORT

## Trigger

Use this skill for its assigned review step in the [worked example](../../walkthrough/04-how-to-write-the-skills.md).

## Inputs

Read the [evidence graph](../../tests/fixtures/running-balance-workload/evidence/EVIDENCE.json),
[manifest](../../tests/fixtures/running-balance-workload/evidence/MANIFEST.json)
and [source program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).

## Workflow

Check the inputs declared by operations 2, 3 and 5 and compare edges 2 and 3. Separate dependencies from scheduling assumptions.

## Output

An as-is Mermaid graph, a proposed target graph and the proof still needed.

## Checks and stop conditions

Cite the evidence pointer and original source location for each source fact.
Keep inferred relationships, profile assumptions and proposed decisions separate.
If an essential citation or prerequisite is missing, mark the affected claim
unresolved. Leave human decisions pending and preserve the SAS acceptance boundary.
