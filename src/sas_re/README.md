# How deterministic reconstruction works

The [running-balance source](../../walkthrough/02-sas-to-evidence.md#the-sas-program)
shows what the evidence engine reads. The code here is a reference for
understanding and extending the design.

~~~mermaid
flowchart LR
    A["Declared source files and typed input profile"] --> B["Inventory source bytes and identities"]
    B --> C["Recognize supported SAS statements"]
    C --> D["Record source spans, operations and gaps"]
    D --> E["Assemble dataset and state relationships"]
    E --> F["Evidence for skill-guided design review"]
~~~

| Code | Responsibility |
| --- | --- |
| [evidence.py](evidence.py) | Build an inventory and record source identities and citations. |
| [sas_subset.py](sas_subset.py) | Recognize supported SAS forms and locate the corresponding source spans. |
| [semantic.py](semantic.py) | Combine recognized operations, profile facts, inferred relationships, and unresolved findings. |
| [contracts.py](contracts.py) | Check evidence against its existing structured contracts. |

For example, the SORT declaration reads `WORK.RUNNING` and writes
`WORK.EXPORT_ORDER`. The SQL enrichment also reads `WORK.RUNNING`.
A skill can use these declarations to review a diagram that routes
enrichment through SORT. See the [worked graph](../../walkthrough/03-evidence-to-graphs.md).

When a different project exposes an unsupported SAS construct, identify
the specific source form and the evidence it would need to produce.
A focused extension can preserve original coordinates, record unknowns
explicitly, and add public examples for the newly supported form.
