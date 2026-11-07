# SAS reading checklist

Use this reference only when understanding or reviewing source. These are inspection rules, not an executable SAS language implementation.

## Evidence

Source text declares behavior; logs/listings show only their associated run. Matching dataset names alone do not establish physical version continuity. Link includes/logs to entrypoints when supported and keep uncertain associations explicit. A missing include with no visible reads/writes is not effect-free.

## Rows, keys and order

- Record filters, ordered IF/ELSE branches, DELETE/OUTPUT and later transformations; a selected column list does not define row population or types.
- Preserve duplicates and output multiplicity. Check ON versus WHERE placement and missing-key behavior before substituting joins.
- SET concatenation, SAS DATA MERGE and SQL JOIN are different operations. Do not replace a duplicate-key BY merge with Cartesian SQL matching without proving equivalence.
- BY keys and directions, producer order and tie policy matter. BY syntax alone does not prove sorted input. SQL without ORDER BY does not promise order; partial sort keys leave ties unspecified.
- Local partition sorting is not proof of global consumption order. Groups crossing partitions/chunks need explicit continuity obligations.

## State and numeric behavior

- Trace RETAIN initialization, FIRST-key resets, sum statements and statement order. A sum statement's retained/missing-value behavior is not ordinary row-wise addition.
- Composite FIRST./LAST. flags depend on leading-key changes. Temporary group flags are not automatically output columns.
- LAG is a call-site queue. Conditional calls advance only when invoked; BY does not reset it automatically.
- Distinguish value lineage from conservative state annotations: BY flags may be used without every output calculation depending on prior-row values.
- Record SAS missing-value behavior, special missing values, character collation, implicit conversion, overflow, rounding and expression order when relevant. Generic NULL handling is not automatically equivalent.

## Modeling and optimization

Preserve response/event definitions, predictor order, CLASS/reference levels, prepared input, ODS outputs, convergence evidence and exported coefficients/scores. Declared fitting is not proof of a completed fit. Fixed-coefficient row scoring differs from fitting a global model.

Absence of a dependency path is not independence proof. Examine completeness of macro expansion, shared datasets/resources, state, order and side effects. Distinguish independent trials from changes to one optimizer. Shared scans/preparation or parallel branches are candidate transformations with correctness obligations and unmeasured performance hypotheses.

Synthetic examples, hand-authored expectations and repeated document checks do not prove SAS parity. Use the same approved behavior and comparison obligations across runtime candidates; real oracle/tolerance/performance decisions belong downstream.
