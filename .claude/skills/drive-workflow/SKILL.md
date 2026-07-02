---
name: drive-workflow
description: Author the NEXT workflow stage (one step) with the ubc agent heartbeat verbs, then report what is next. Does NOT run the whole workflow.
---

# Drive the next workflow stage

Use this skill to advance the workflow by exactly ONE stage, then stop and hand
control back to the user. Do NOT loop through the whole V: author the single next
stage, confirm it, report what comes next, and stop. The user decides when to
drive the next stage.

This single-stage boundary is a hard safety rule. If the wording is ambiguous
(for example, "follow the loop"), interpret it as: complete one full stage cycle
(`next`, `context`, `author`, `gaps`, `report`) and then stop.

## Steps (one stage, then stop)

1. Run `ubc agent next --id <need_id>` to get the next actionable stage (0 or 1,
   never a list). `<need_id>` is a need id, not a stage name. If `next` exits
   non-zero the id was wrong: fix it, do not infer the stage is resolved.
2. If `stage` is null, read `reason`:
   - `empty`: nothing authored yet. Author the first artefact for this workflow.
   - `done`: the active stream is complete. Stop.
   - `blocked`: a dependency is unmet. Resolve it first.
3. Read the `author_skill` field from the `next` output. Run
   `ubc agent context <need_id> --no-code` to get the full briefing for the
   anchor need. Use the `<author_skill>` skill named by `ubc agent next` to
   draft the artefact IN CHAT (do not use `ubc agent run`): in Claude Code it
   is loaded from `.claude/skills/<author_skill>/SKILL.md`, in Copilot invoke
   `@<author_skill>`. When writing the trace link, copy the exact field name
   from the `gate.link` value in `next`'s output. Do not guess a synonym or
   substitute a related link name.
4. Run `ubc agent gaps --scope <feature>` to confirm the stage closed its trace
   obligations.
5. **STOP. Do not start the next stage.** Report to the user: what you authored,
   whether its gate is green, and what `ubc agent next` now names as the next
   stage. The user re-runs the drive when they want that next stage authored.

Before ending, run this hard-stop check:

- Did I author exactly one stage? If no, stop and correct course.
- Did I run `gaps` for confirmation? If no, do it now.
- Did I avoid starting the next stage? If no, stop immediately.
- Did I report the next stage name and return control to the user? If no, do it now.

## Notes

- `ubc agent status` shows every stage's state at once (the heartbeat).
- `ubc agent gaps` is the whole-graph gate. It exits non-zero while gaps remain.
- `ubc agent next --id` and `ubc agent run --id` take a need id, never a stage
  or feature name. A non-zero `next` means the id was wrong.
- `ubc agent gaps` takes NO `--id`: it gates the whole graph (narrow it with
  `--scope <feature>`). Only `next`, `run`, `context`, `impact`, and `audit`
  accept `--id`. Never append `--id` to `gaps`, `status`, or `release-check`.
- Never skip a stage: the trace edges in `[workflow]` are what the gates enforce.
- Always use the `author_skill` named by `next` for the current stage. Do not
  substitute a different skill or infer the skill from the stage name.
- To drive a SPECIFIC stage (e.g. one the cockpit Flow strip offered that is not
  the recommended next — a global `risks`/`decisions` stage, or a parallel arm
  stage), pass `--stage <STAGE_ID>` to `ubc agent next --id <need_id>`. It briefs
  that stage instead of the recommendation; read its `author_skill` exactly as
  usual. The need id still anchors the briefing (need-seeded). An unknown stage
  exits non-zero. Everything else is unchanged: one stage, then stop.
