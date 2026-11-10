# Evidence from the running-balance example

Start with the [SAS program](../../walkthrough/02-sas-to-evidence.md#the-sas-program).
The table shows how three SAS operations appear in the generated evidence.

| Source | What Python records | Where to find it |
| --- | --- | --- |
| `main.sas.txt`, lines 2–11 | The DATA step reads the declared input and writes `WORK.RUNNING`. | `/operations/2` |
| `main.sas.txt`, lines 12–14 | SORT reads `WORK.RUNNING` and writes `WORK.EXPORT_ORDER`, ordered by `group, subkey`. | `/operations/3` |
| `enrich.sas.txt`, lines 1–6 | SQL reads `WORK.RUNNING` and `WORK.LOOKUP`, joins on `group`, filters by weight, and writes `WORK.ENRICHED`. | `/operations/5` |

The reads and writes are source declarations. Python infers the two
producer-to-consumer links from those declarations in `/edges/2` and
`/edges/3`. Those links describe data dependencies. Actual scheduling
and dataset versions remain unverified.

See how these records support the [dependency diagram and proposed design](../../walkthrough/03-evidence-to-graphs.md).
For the audience-facing YAML examples, see the [migration profile and tie-out](../../walkthrough/06-profile-and-tie-out.md).

The [generated files](generated/) are the original reference artifacts.
Start with [EVIDENCE.json](generated/EVIDENCE.json) to inspect the pointers
above. The inventory and manifest hold file identities, while the generated
review and YAML capture the tool's draft handoff.
