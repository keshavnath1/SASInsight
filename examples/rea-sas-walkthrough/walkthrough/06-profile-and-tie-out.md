# Configure and check the running-balance example

The **migration profile** describes what to run and what it produces. The
**tie-out** describes what to compare and how to decide whether it matches.

Agent Mastery separates the migration profile from the tie-out contract.
Its tie-out identifies the comparison population, expected result source,
producer, comparisons, and output. The examples below apply that structure
to running balance and enrichment. They are design drafts for the team.
Run the shell commands on this page. The candidate reads the evidence
package and INTAKE directory through its CLI.

## Migration profile draft

The input is three SAS files plus `scope.json` and `profile.json`.
The [typed profile](../tests/fixtures/running-balance-workload/source/profile.json)
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
  script: scripts/run_running_balance.py
  arguments: [--package, "$evidence", --intake, "$scratch/INTAKE"]
  output: "$scratch/candidate.json"
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
values come from the [public engineering test](../tests/workflow/test_running_balance.py).
`null` represents a missing numeric value in the candidate JSON.

~~~yaml
module_id: running_balance
status: DRAFT
population: full_public_fixture
actual: "$scratch/candidate.json"
expected_source: tests/workflow/test_running_balance.py
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

## Run the example

From the walkthrough folder, use the Python 3.12 environment in
[chapter 7](07-apply-to-your-intake.md#replay-the-teaching-example).

~~~sh
scratch=$(mktemp -d /tmp/sas-rea-example-XXXXXX)
scratch=$(cd "$scratch" && pwd -P)
mkdir "$scratch/INTAKE"
cp tests/fixtures/running-balance-workload/source/* "$scratch/INTAKE/"
evidence="/tmp/sas-re-int1-${scratch##*/}"
python3.12 -IB scripts/review_intake.py --p2a --modernization-drafts --intake "$scratch/INTAKE" --destination "$evidence"
evidence=$(cd "$evidence" && pwd -P)
python3.12 -IB scripts/run_running_balance.py --package "$evidence" --intake "$scratch/INTAKE" > "$scratch/candidate.json"
PYTHONPATH=tests python3.12 -B -m unittest discover -s tests/workflow -p test_running_balance.py
~~~

The evidence directory contains the separate generated
[migration profile](../tests/fixtures/running-balance-workload/evidence/migration-profile.yaml)
and [tie-out draft](../tests/fixtures/running-balance-workload/evidence/tie-out.yaml)
with their source and evidence bindings. Read the design examples above to
understand the workload. Use the generated files to trace the review back
to the exact inputs.

[Next: apply the method to your own INTAKE](07-apply-to-your-intake.md)
