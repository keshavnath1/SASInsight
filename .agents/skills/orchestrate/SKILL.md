---
name: orchestrate
description: Drive SASInsight from authorized intake to a readable draft package. Use for new or resumed end-to-end SAS understanding and architecture requests, not migration or deployment.
---

# Orchestrate

Read root AGENTS.md and README.md. Use `intake/` by default or the explicit authorized root in the user request. Write only to a fresh `output/<run-id>/`; maintain a short PROGRESS.md there.

## Execute

1. Inspect repository state without changing history. If intake is empty, explain what to add and stop. Do not analyze bundled examples unless requested, execute source or stage private input in Git.
2. Choose a readable unique run ID and nonexisting output folder. Record the request, input root, stage, existing constraints and DRAFT authority in PROGRESS.md. No separate scope/config form is required.
3. Load and invoke `understand`; it owns the source snapshot, factual record and unknowns. Other skills cite that record, not a second factual graph.
4. Load and invoke `specify`, then `design`. Continue ordinary draft work automatically. Keep affected conclusions conditional/blocked when evidence is missing; never infer business approval.
5. Load and invoke `review` in a fresh subagent/chat where supported. Supply original input and actual draft paths, not only the author's summary. Record actual reviewer context. If fresh review is unavailable, record NOT_AVAILABLE and package PARTIAL findings, not independent approval.
6. For requirement/design errors, allow one author revision and fresh re-review. Factual errors or changed source require a new linked run, not an edit to sealed facts. After one retry, package open findings PARTIAL or stop BLOCKED; never loop indefinitely.
7. Invoke `package`. End with output paths, readiness, open decisions, what was not executed and a copy-ready continuation request. Stop for final human review; do not authorize downstream implementation.

Append a short progress entry after each skill: skill, artifact, COMPLETE/PARTIAL/BLOCKED draft-stage status, limitation and next action. Runtime parity/performance and human approval remain separate NOT_RUN/NOT_APPROVED fields.

## Resume

Use only the exact previous run named by the user; do not guess the latest approved run. Read progress/artifacts. Check the source manifest before trusting facts. Changed input starts a new run. Resume the next unfinished skill without overwriting/replaying completed outputs. If no checkable snapshot exists, retain NOT_CHECKED integrity and partial readiness.

Use agent reading/writing tools. Do not generate analysis scripts, install a parser/runtime or add a CLI/state engine. This skill coordinates the specialist skills; it does not replace them. Respect host permission prompts even during automatic drafting.
