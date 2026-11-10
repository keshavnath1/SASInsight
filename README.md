# From SAS code to a modernization design

A presentation for teams evaluating an evidence-first SAS modernization
approach. The public running-balance example follows three SAS files from
business intent through source evidence, architecture choices, and a
proposed tie-out. The comparison with REA explains where an assistant can
investigate and where deterministic evidence makes its conclusions checkable.

| Chapter | Topic |
| --- | --- |
| 1 | [Business problem and REA comparison](walkthrough/01-start-here.md) |
| 2 | [Complete SAS program and Python evidence](walkthrough/02-sas-to-evidence.md) |
| 3 | [As-is dependencies and proposed optimization](walkthrough/03-evidence-to-graphs.md) |
| 4 | [How your team can write its own skills](walkthrough/04-how-to-write-the-skills.md) |
| 5 | [PRD, HLD, LLD and three draft ADRs](walkthrough/05-prd-and-architecture-decisions.md) |
| 6 | [Worked migration profile and tie-out](walkthrough/06-profile-and-tie-out.md) |
| 7 | [Apply the approach to a different INTAKE](walkthrough/07-apply-to-your-intake.md) |

This standalone branch is for design discussion. The [public example](example/)
contains the SAS source and a [plain-language evidence guide](example/evidence/README.md). The [Python reference](src/sas_re/README.md)
shows what deterministic reconstruction does today and where the team could
extend it for a different workload.
