# Read the actual migration profile and tie-out drafts

Open [migration-profile.yaml](../tests/fixtures/running-balance-workload/evidence/migration-profile.yaml)
and [tie-out.yaml](../tests/fixtures/running-balance-workload/evidence/tie-out.yaml).
Python generates these drafts when the operator requests modernization
drafts. Both bind the exact source identities and evidence manifest. The
typed [input profile](../tests/fixtures/running-balance-workload/source/profile.json)
is a different file. It supplies synthetic assumptions for reconstruction.

The excerpts below show the actual generated fields in YAML block style.
The linked files contain the full `binding` block with the source and
evidence hashes.

## Migration profile draft

The profile records the decisions the team needs to make about how the
candidate should run. For this example, the review should address equal-key
SORT ties and whether repeated enrichment rows must be preserved.

~~~yaml
status: DRAFT
target:
  runtime: PENDING
  distributed: PENDING
execution:
  ordering_policy: PENDING
  multiplicity_policy: PENDING
  category_policy: PENDING
approval:
  architecture: REQUIRED
  business_intent: REQUIRED
~~~

## Tie-out draft

The tie-out records what the team needs to verify. For this example,
review SORT order separately from enrichment multiplicity. The reference
section records the status of independent SAS verification.

~~~yaml
status: DRAFT
checks:
  source_coverage: REVIEW_REQUIRED
  ordering_and_output: PENDING
  population_and_multiplicity: PENDING
  numeric_tolerance: PENDING
reference:
  sas_execution: NOT_RUN
  semantic_verification: UNVERIFIABLE
  semantic_acceptance: BLOCKED
~~~

## One concrete engineering check

The [public Python candidate](../scripts/run_running_balance.py) produces
three enrichment rows with columns `group, balance, weight`:

~~~text
[1, 2, 3]
[1, 2, 3]
[2, 4, 5]
~~~

The [engineering expectations](../tests/workflow/test_running_balance.py)
check those values. Compare enrichment as a multiset, so both copies of
the first row count. Check SORT separately for ascending keys and preserved
rows. A stable tie order is an engineering choice for the candidate.

In the REA analogy, follow-up checks test the claim a tool finding motivates.
Here the tie-out draft records the proposed checks and what evidence they
need. The Python comparison covers the public fixture. A SAS comparison
would need attributable typed inputs, execution and outputs, and a
performance claim would need a separate representative benchmark.

**Try it:** Would a set comparison catch a missing duplicate?
**Output:** One multiset check and one separate ordering check.

[Next: apply the method to your own INTAKE](07-apply-to-your-intake.md)
