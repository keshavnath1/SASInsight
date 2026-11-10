# Apply the method to your own INTAKE

Start with one authorized SAS program and one business output. Write down
the question you want answered, such as “Does the summary depend on the
stateful preparation?” The same evidence-first approach applies even when
your project uses different SAS constructs.

1. **Scope the source.** Identify the entry point, allowed includes, expected
   source identities, and available input descriptors. Keep private material
   in the authorized inspection environment.
2. **Generate supported evidence.** Choose the appropriate existing review
   route. The public multi-file route requires a declared synthetic scope and
   profile. [Bounded source review](../scripts/review_source.py) is separate.
   Record unsupported or uninspected behavior and unresolved dependencies.
3. **Write the skills for the question.** Use the [skill format](04-how-to-write-the-skills.md).
   Give the LLM an evidence record to cite and a precise deliverable.
4. **Review the proposal.** Require one traceable requirement, one as-is
   dependency view, one justified design change, and one validation case.
   Record the business and runtime decisions that still need a person.

## Replay the teaching example

Start with the public [INTAKE files](../tests/fixtures/running-balance-workload/source/).
Python reconstructs the source, then the candidate uses that evidence and
the same inputs to produce `candidate.json`. In the review, open the
[example tie-out](06-profile-and-tie-out.md#tie-out-draft) and check that the
enrichment result contains both copies of `[1, 2, 3]`.

<details>
<summary>Engineering replay commands</summary>

Use Python 3.12 on macOS or Linux. Run these commands from the walkthrough
folder. Each run creates a fresh INTAKE copy and output directory.

~~~sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install .

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

</details>

The candidate accepts the exact public workload. For a different INTAKE,
start with scope and coverage review. The
[engine guide](../src/sas_re/README.md) shows how the Python pieces fit together.

**Final team exercise:** Like an REA investigation, start from a concrete
question and ask what evidence would answer it. In this SAS workflow,
generate that evidence first, then give your skills clear questions and
checks. End with a modernization proposal the team can review and a list
of claims that still need proof.

[Back to the opening example](01-start-here.md)
