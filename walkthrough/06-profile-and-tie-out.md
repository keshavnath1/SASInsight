# Configure and check the running-balance example

The **migration profile** describes what to run and what it produces. The
**tie-out** describes what to compare and how to decide whether it matches.

Agent Mastery separates the migration profile from the tie-out contract.
Its tie-out identifies the comparison population, expected result source,
producer, comparisons, and output. The examples below apply that structure
to running balance and enrichment. They are design drafts for the team.
The candidate uses the original INTAKE files and the evidence generated
from them.

## Migration profile draft

The input is three SAS files plus `scope.json` and `profile.json`.
The [typed profile](../example/source/profile.json)
supplies both input tables as synthetic rows.

~~~yaml
module_id: running_balance
status: DRAFT
business_outcome: Produce ordered running balances and an enriched lookup view.
source:
  entrypoint: main.sas.txt
  includes: [settings.sas.txt, enrich.sas.txt]
  scope: scope.json
  input_profile: profile.json
inputs:
  work.raw:
    columns: [group, subkey, amount]
    rows: 3
    declared_input_order: [group, subkey]
  work.lookup:
    columns: [group, weight]
    rows: 2
candidate:
  runtime: Python 3.12
  reads: [original_intake, generated_evidence]
  output: candidate.json
outputs:
  work.running:
    columns: [group, subkey, amount, balance, previous, marker]
  work.export_order:
    source: work.running
    columns: [group, subkey, amount, balance, previous, marker]
    ascending_by: [group, subkey]
    equal_key_order: stable_input_order
  work.enriched:
    sources: [work.running, work.lookup]
    columns: [group, balance, weight]
    join_key: group
    post_join_filter: "weight > 0"
    preserve_repeated_rows: true
~~~

Stable SORT ties describe the current Python candidate. The team still
needs to decide whether that is the intended business policy. Enrichment
uses the prepared rows directly, so the sorted output is a separate branch.

## Tie-out draft

The comparison covers all three input rows and both lookup rows. Expected
values come from the public fixture’s engineering expectations.
`null` represents a missing numeric value in the candidate JSON.

~~~yaml
module_id: running_balance
status: DRAFT
population: full_public_fixture
actual: candidate.json
expected_source: public_fixture_engineering_expectations
comparisons:
  work.running:
    method: exact_ordered_rows
    expected:
      - [1, 1, 2, 2, null, null]
      - [1, 1, null, 2, null, 1]
      - [2, 1, 4, 4, 2, 1]
  work.export_order:
    method: exact_ordered_rows
    ascending_by: [group, subkey]
    expected:
      - [1, 1, 2, 2, null, null]
      - [1, 1, null, 2, null, 1]
      - [2, 1, 4, 4, 2, 1]
  work.enriched:
    method: exact_row_multiset
    expected:
      - [1, 2, 3]
      - [1, 2, 3]
      - [2, 4, 5]
~~~

A multiset counts both copies of `[1, 2, 3]`. A set would hide a missing
duplicate. The existing test checks the exact emitted lists for this
fixture. The proposed multiset comparison expresses the design requirement
for enrichment separately from that stricter fixture check.

## How the design fits together

| Step | Give it | Get back |
| --- | --- | --- |
| Reconstruct | Three SAS files, declared scope, and typed synthetic inputs | Source-linked evidence and both YAML drafts |
| Run the Python candidate | The evidence package and the same INTAKE files | `candidate.json` with running balances, the sorted output, and enrichment |
| Check the result | Candidate rows and the public engineering expectations | A comparison of order, values, and repeated rows |

The evidence directory contains the separate generated
[migration profile](../example/evidence/migration-profile.yaml)
and [tie-out draft](../example/evidence/tie-out.yaml)
with their source and evidence bindings. Read the design examples above to
understand the workload. Use the generated files to trace the review back
to the exact inputs.

[Next: apply the method to your own INTAKE](07-apply-to-your-intake.md)
