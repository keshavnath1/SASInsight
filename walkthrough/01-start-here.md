# From SAS code to a modernization design

We want to modernize a job that calculates running balances and enriches
those balances with lookup weights. The team needs to preserve the
calculations and required ordering while choosing a maintainable design.
The [public SAS example](02-sas-to-evidence.md#the-sas-program) uses small
synthetic transaction groups to explain that business problem.

## Start with the business question

**Does enrichment need to wait for SORT?**

The job prepares running balances. SORT produces an ordered copy for one
consumer. SQL joins the prepared balances to a lookup table for another.
The source tells us which dataset each operation reads.

~~~mermaid
flowchart LR
    A["Prepared running balances"] --> B["SORT by group and subkey"]
    B --> C["Ordered output"]
    A --> D["Join lookup and filter weights"]
    D --> E["Enriched output"]
~~~

SORT appears before SQL in the program. However, SQL reads `WORK.RUNNING`
directly and never reads SORT's output, `WORK.EXPORT_ORDER`. This supports
keeping enrichment off the sorted-output path in the proposed design.
Actual scheduling and safe parallel execution still need separate evidence.

## Explain the approach in everyday terms

Python reads supported SAS statements and records what each step consumes
and produces. Copilot uses those findings to explain the workflow and
propose a design. People can check the proposal against the original code.

**We make the evidence repeatable so the team can check Copilot's explanation
and design decisions against the SAS source.**

An LLM already understands SAS syntax. Supplying evidence gives the team
specific findings to review when an explanation or diagram is disputed.
Here, the input and output declarations let a reviewer check whether a
proposed `SORT → enrichment` dependency belongs in the design.

## Show engineers how the finding is established

The parser recognizes statements and records source locations. The graph
builder uses those facts and the supplied input profile to describe
relationships and constraints.

| SAS declaration | What Python records | Design implication |
| --- | --- | --- |
| `data work.running;` | The DATA step writes `WORK.RUNNING`. | This prepared dataset supplies both consumers. |
| `proc sort data=work.running out=work.export_order;` | SORT reads the prepared dataset and writes an ordered copy. | Preserve the separate ordered output. |
| `by group subkey;` in SORT | Ascending sort keys are `group, subkey`. | Review ties and preserve row multiplicity. |
| `from work.running as a left join work.lookup as b` | Enrichment reads the prepared dataset and lookup table. | Feed enrichment from the prepared population. |

The two producer-to-consumer links are inferred from declared reads and
writes. The [evidence guide](../example/evidence/README.md) points to the
actual records. Unsupported syntax and unresolved prerequisites remain
visible as gaps.

## Explain the technical guarantees

For supported syntax, the same source bytes, scope, input profile, and
engine version produce repeatable evidence. Original byte spans and hashes
let a reviewer locate a finding and detect a changed input. Input types and
sample ordering supplied by the profile remain explicit assumptions.

The parser records `RETAIN` initialization, group resets, and the guarded
`LAG` call separately. These details constrain the design because state and
call order affect the calculation. Recognizing them does not establish the
contents of an actual SAS runtime dataset. See [how Python turns SAS into
evidence](02-sas-to-evidence.md) for the implementation path.

## Compare the approach with REA

REA also uses analysis code behind its tools. An assistant can call those
tools through MCP, receive structured findings and limitations, and choose
what to inspect next. Our demonstrated SAS workflow generates a scoped
Python evidence package before the skill-guided review.

| Question | REA | This SAS example |
| --- | --- | --- |
| How is analysis requested? | The assistant calls inspection tools through MCP. | The operator selects the declared source scope and profile. |
| What produces findings? | Parsers, analyzers, and runtime providers behind the tools. | Python parsing and graph construction for supported SAS forms. |
| What does the assistant do? | Chooses further inspection and interprets findings. | Interprets the package and drafts requirements and design options. |
| How can the team assess an answer? | Examine the returned evidence, scope, and limitations. | Follow the source spans, facts, inferred edges, and gaps. |

For this example, both approaches would need evidence of the datasets read
by SORT and enrichment to justify the dependency diagram. The interface
used to request analysis does not itself establish the dependency.

## Follow the example through the design

1. [Read the full SAS program and trace it through Python](02-sas-to-evidence.md).
2. [Compare the as-is graph with the proposed design](03-evidence-to-graphs.md).
3. [Write skills with clear inputs, outputs, and checks](04-how-to-write-the-skills.md).
4. [Review the PRD, module design, and three ADRs](05-prd-and-architecture-decisions.md).
5. [Inspect the worked migration profile and tie-out](06-profile-and-tie-out.md).
6. [Apply the approach to a different INTAKE](07-apply-to-your-intake.md).
