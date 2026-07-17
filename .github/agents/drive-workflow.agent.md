---
name: drive-workflow
description: Author the NEXT workflow stage (one step) with the ubc agent heartbeat verbs, then report what is next. Does NOT run the whole workflow.
---

# Drive the next workflow stage

Use this skill to advance the workflow by exactly ONE stage, then stop and hand
control back to the user. Do NOT loop through the whole V: author the single next
stage, run its independent review, confirm it, report what comes next, and stop.
The user decides when to drive the next stage.

This single-stage boundary is a hard safety rule. If the wording is ambiguous
(for example, "follow the loop"), interpret it as: complete one full stage cycle
(`next`, `context`, propose-and-author, review, `gaps`, `report`) and then stop.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml` (the project the need you are
driving belongs to). A repository can contain several `ubproject.toml` files,
so without `-p` the command runs against the current directory and can target
the wrong project. Resolve `<project path>` once from the need or file you
were handed and reuse it on every call in this stage.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

## Steps (one stage, then stop)

1. Run `ubc agent next --id <need_id> -p <project path>` to get the next
   actionable stage (0 or 1, never a list). `<need_id>` is a need id, not a
   stage name. If `next` exits non-zero the id was wrong: fix it, do not infer
   the stage is resolved.
2. If `stage` is null, read `reason`:
   - `empty`: nothing authored yet. Author the first artefact for this workflow.
   - `done`: the active stream is complete. Stop.
   - `blocked`: a dependency is unmet. Resolve it first.
3. Read the `author_skill` field from the `next` output. Run
   `ubc agent context --id <need_id> --no-code -p <project path>` to get the full
   briefing for the anchor need. Use the `<author_skill>` skill named by
   `ubc agent next -p <project path>` to
   work the stage IN CHAT: in Claude Code it is loaded from
   `.claude/skills/<author_skill>/SKILL.md`, in Copilot invoke
   `@<author_skill>`. That skill PROPOSES a short outline first and asks you to
   approve or adjust it. It authors only after you confirm, so get the user's
   approval, THEN let it author. When the trace link is written, copy the exact
   field name from the `gate.link` value in `next`'s output. Do not guess a
   synonym or substitute a related link name.
4. INDEPENDENT review. Run this ONLY when the `next` output carries a `review`
   field. That field names the exact review skill for this stage (for example
   `review-requirement` for `reqs`, `review-feat` for `user_stories`). Use the
   field's value verbatim. Do NOT construct a `review-<type>` name. Dispatch a
   SEPARATE reviewer in a FRESH context (a subagent / Task), NOT the context that
   authored the artefact, so the author never grades its own output. The reviewer
   re-derives its judgment from `ubc agent audit --id <ID> -p <project path>` for
   every need this stage produced, then writes one verdict per need to
   `<verdicts_dir>/<ID>.json`
   (the directory `next`'s output reports in its `verdicts_dir` field), with a
   fresh `reviewed_fingerprint` copied from that same
   `ubc agent audit --id <ID> -p <project path>` output.
   Pass your OWN harness name and model id into the reviewer's dispatch prompt
   so each verdict carries top-level `agent` (e.g. `claude-code` / `copilot`)
   and `model` — advisory score provenance, never gating. The fresh reviewer
   context cannot observe them itself; omit a field only when genuinely
   undeterminable (never guess a slug).
   When the `next` output has no `review` field (the `code`, `tests`, and `risks`
   stages), skip this step.
5. Subagent guidance (best-effort). If your agent supports independent
   subagents, run each need `ubc agent next -p <project path>` names for this stage as its own
   fresh subagent, and when the stage is a review stage, use a DIFFERENT
   subagent for the review than authored the artefact. This keeps each item
   in clean context and stops an author from rubber-stamping its own work.
   If your agent has no subagents, do the items in sequence in this chat.
   This is soft, best-effort guidance conditional on subagent support. It
   reduces bias. It does not guarantee independence.
6. Run `ubc agent gaps --scope <need_id> -p <project path>` (the same anchor
   need id) to confirm the stage closed its trace obligations for that stream,
   then run `ubc agent next --id <need_id> -p <project path>` again. `gaps` is the
   trace gate only and does not read verdicts, so a green `gaps` alone does not
   mean the stage advances. For a review-required stage the engine holds the
   stage until the independent verdict is fresh and passing, so this re-run of
   `next` is what confirms the advance.
7. **STOP. Do not start the next stage.** Report to the user: what you authored,
   whether its trace gate is green, whether an independent reviewer wrote a
   passing verdict, and what `ubc agent next -p <project path>` now names as the next stage. The
   user re-runs the drive when they want that next stage authored.

Before ending, run this hard-stop check:

- Did I author exactly one stage? If no, stop and correct course.
- Whenever `next` named a `review` skill, did an INDEPENDENT reviewer (a fresh
  context, not the author) write a passing verdict for every need this stage
  produced? If no, do it now.
- Did I run `gaps` for confirmation? If no, do it now. A green `gaps` is
  necessary but not sufficient: it is the trace gate and does not read verdicts.
  The authoritative advance condition is a fresh passing verdict plus the final
  `next` read.
- Did I avoid starting the next stage? If no, stop immediately.
- Did I report the next stage name and return control to the user? If no, do it now.

## Notes

- `ubc agent status -p <project path>` shows every stage's state at once (the
  heartbeat).
- `ubc agent next -p <project path>`'s `review` field, when present, names the
  exact review skill for the stage. Use it verbatim, do not build a
  `review-<stage>` name. It is absent on the `code`, `tests`, and `risks`
  stages, which carry no review.
- `ubc agent gaps -p <project path>` is the whole-graph gate. It exits non-zero
  while gaps remain. It is the trace gate and does not read verdicts, so on a
  review-required stage a green `gaps` is necessary but not sufficient. The
  `next` re-run after a fresh passing verdict is the authoritative advance
  signal.
- `ubc agent next --id` takes a need id, never a stage or stream name. A
  non-zero `next` means the id was wrong.
- `ubc agent gaps -p <project path>` takes NO `--id`: it gates the whole graph.
  Narrow it to one stream with `--scope <need_id>`, which anchors on a need and
  scopes to its trace-subtree. Only `next`, `context`, `impact`, and `audit`
  accept `--id`. Never append `--id` to `gaps`, `status`, or `release-check`.
- Never skip a stage: the trace edges in `[workflow]` are what the gates enforce.
- Always use the `author_skill` named by `next` for the current stage. Do not
  substitute a different skill or infer the skill from the stage name.
- To drive a SPECIFIC stage (one that is not the recommended next, such as a
  global `risks`/`decisions` stage or a parallel arm stage), pass
  `--stage <STAGE_ID>` to `ubc agent next --id <need_id> -p <project path>`. It
  briefs that stage instead of the recommendation; read its `author_skill`
  exactly as usual. The need id still anchors the briefing (need-seeded). An
  unknown stage exits non-zero. Everything else is unchanged: one stage, then
  stop.
