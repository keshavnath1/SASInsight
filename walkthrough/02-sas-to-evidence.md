# How Python turns SAS into evidence

Open the public [source scope](../example/source/scope.json)
and [typed input profile](../example/source/profile.json).
The scope identifies the entry point, literal include edges, and expected
file hashes. The profile supplies column types, small public input rows,
and an input-order assumption for the DATA step. The profile is a declared
input contract.

## The SAS program

The complete public example is three files. Start with `main.sas.txt`. Its
first include defines the source dataset. Its final include runs enrichment.

### [`main.sas.txt`](../example/source/main.sas.txt)

~~~sas
%include 'settings.sas.txt';
data work.running;
set &source.;
by group subkey;
retain balance 8;
if first.group then balance = 0;
balance + amount;
if amount > 0 then previous = lag(amount);
if last.subkey then marker = 1;
keep group subkey amount balance previous marker;
run;
proc sort data=work.running out=work.export_order;
by group subkey;
run;
%include 'enrich.sas.txt';
~~~

### [`settings.sas.txt`](../example/source/settings.sas.txt)

~~~sas
%let source=work.raw;
~~~

### [`enrich.sas.txt`](../example/source/enrich.sas.txt)

~~~sas
proc sql;
create table work.enriched as
select a.group as group, a.balance as balance, b.weight as weight
from work.running as a left join work.lookup as b on a.group = b.group
where b.weight > 0;
quit;
~~~

On the first row of each group, the explicit reset to zero runs before
accumulation, even though `RETAIN` initializes the balance to 8. The `LAG` call
is guarded by `amount > 0`, so this contract tracks prior calls rather than
blindly shifting every input row. The lookup filter appears after the join.
Those details matter when reviewing the Python candidate.

## What Python reads and records

~~~mermaid
flowchart TD
    A["SAS bytes, declared scope and typed profile"] --> B["Verify declared files and hashes"]
    B --> C["evidence.py: build_inventory"]
    C --> D["semantic.py: reconstruct"]
    D --> E["sas_subset.py: parse_source"]
    E --> F["Supported facts and unresolved findings"]
    F --> G["semantic.py: assemble operations and inferred edges"]
    G --> H["INVENTORY.json, EVIDENCE.json and MANIFEST.json"]
~~~

Follow the [engine code map](../src/sas_re/README.md). The parser uses implemented
grammar rules. For example, it can recognize the input after `DATA=`, the
output after `OUT=`, and the keys in `BY`. The reconstruction combines
those declarations with source citations, input contracts, and related
operations. Unsupported forms or missing preconditions remain visible.

## Follow two statements into the graph

The source contains these excerpts:

~~~sas
proc sort data=work.running out=work.export_order;
by group subkey;
run;
~~~

~~~sas
from work.running as a left join work.lookup as b on a.group = b.group
where b.weight > 0;
~~~

| Original source | What the actual evidence records |
| --- | --- |
| [main.sas.txt](../example/source/main.sas.txt), lines 12–14, bytes [278,350) | Operation 3 reads `WORK.RUNNING`, writes `WORK.EXPORT_ORDER`, and sorts by `group, subkey`. |
| [enrich.sas.txt](../example/source/enrich.sas.txt), lines 1–6, bytes [0,202) | Operation 5 reads `WORK.RUNNING` and `WORK.LOOKUP`, left joins on group, applies the weight filter, and writes `WORK.ENRICHED`. |

Open the [actual graph](../example/evidence/EVIDENCE.json).
Compare `/operations/3` and `/operations/5` with `/edges/2` and `/edges/3`.
The operations carry source declarations. Both edges are `INFERENCE` records
from operation 2, the DATA step. The public package contains six operations
and four inferred edges. See the [bound inventory](../example/evidence/INVENTORY.json)
and [evidence manifest](../example/evidence/MANIFEST.json)
for the identities.

**Deterministic** means the same verified bytes, profile, and engine version
reproduce the evidence. The reconstruction does not execute the SAS program.
As in the REA analogy, ask what the tool actually observed and where the
assistant is interpreting a finding.

**Try it:** Point to the source span that declares each consumer's input.
**Output:** Two cited source facts and two separately labeled inferred edges.

[Next: turn the evidence into graphs](03-evidence-to-graphs.md)
