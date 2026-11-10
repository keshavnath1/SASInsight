# From SAS code to an execution plan

This public walkthrough follows a running-balance and enrichment example from
three SAS files to draft requirements, design decisions and a bounded Python
candidate. [Start with the business question](walkthrough/01-start-here.md)
or [read the full SAS program](walkthrough/02-sas-to-evidence.md#the-sas-program).

| Step | Read |
| --- | --- |
| 1 | [Business problem and REA comparison](walkthrough/01-start-here.md) |
| 2 | [SAS source and what Python recovers](walkthrough/02-sas-to-evidence.md) |
| 3 | [As-is graph and proposed optimization](walkthrough/03-evidence-to-graphs.md) |
| 4 | [How to write the five skills](walkthrough/04-how-to-write-the-skills.md) |
| 5 | [PRD, HLD, LLD and three ADRs](walkthrough/05-prd-and-architecture-decisions.md) |
| 6 | [Actual migration profile and tie-out drafts](walkthrough/06-profile-and-tie-out.md) |
| 7 | [Replay and apply the method to another INTAKE](walkthrough/07-apply-to-your-intake.md) |

The [Python engine guide](src/sas_re/README.md) shows the call flow in Mermaid.
The example is a separate Python-first teaching path. The
[SASInsight intake workflow](../../README.md) is skills-led and does not
depend on this example. SAS reference execution and benchmarking are
`NOT_RUN`. SAS semantic acceptance is `BLOCKED`.
