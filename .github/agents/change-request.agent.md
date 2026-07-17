---
name: change-request
description: Reconcile ONE downstream stage's artefacts with a changed upstream — the engine cascades a human's edit down the full V and invokes this skill once per downstream stage; show the blast radius, then modify only the artefacts the change made inconsistent, as uncommitted changes for human approval.
---

# Change request

A human has EDITED one need (the anchor) and the engine is propagating that edit
DOWN the V. The engine drives the cascade: it derives the downstream stages of the
anchor's stage and runs ONE reconcile pass per stage, rebuilding between passes so
each pass sees the upstream already reconciled. THIS pass reconciles ONE stage.

Your prompt's CHANGED-UPSTREAM section carries the new, authoritative content this
stage must become consistent with. Your job for THIS stage: MODIFY its existing
artefacts so they match the changed upstream. Change ONLY what the edit actually
invalidated — do not rewrite anything that still matches, and do not re-author
artefacts wholesale. Author a brand-new artefact ONLY when a genuinely new upstream
item now requires one. Never commit.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml` (the project the anchor need
belongs to). A repository can contain several `ubproject.toml` files, so
without `-p` the command runs against the current directory and can reconcile
the wrong project. Resolve `<project path>` once from the anchor need or file
you were handed and reuse it on every call in this pass.

Do NOT re-discover the project with `find`, `grep`, or `cat`. Use
`ubc agent impact --id <anchor_id> -p <project path>` for the blast radius and
`ubc agent audit --id <id> -p <project path>` for an artefact's body and its
source path + line range. For ad-hoc need queries use `ubc query filter
<query>`. Prefer the `ubc` CLI over the ubCode MCP query tools
— the CLI is more capable. These give structured, reliable data. The only files
you read or edit are this stage's own artefacts, at the exact paths `audit`
reports.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

## Step 1 — Blast radius

Run `ubc agent impact --id <anchor_id> -p <project path>` for the originally-edited
anchor named in the prompt and read its JSON. Note what the change reaches
DOWN (children, code, impl and test needs) so the impact on THIS stage is
named, not guessed. Call out any `stale_gaps` already attributed to the anchor
or anything it reaches — they are debt the change either fixes or inherits.

## Step 2 — Reconcile this stage's artefacts

The prompt tells you which stage you are reconciling and gives you, for a NEED
stage, the EXISTING artefacts of this stage and the CHANGED UPSTREAM they trace up
to; for a CODE stage, the CHANGED CONTRACT and the source target directory.

For each existing artefact of this stage:

- compare it against the changed upstream. Decide whether the edit made it
  inconsistent;
- if it is STILL consistent, leave it alone — do not touch it;
- if the edit made it INCONSISTENT, MODIFY it in place so it matches the new
  upstream. For a NEED stage, get the artefact's `.rst` path and line range from
  `ubc agent audit --id <id> -p <project path>` (its `source` field) and edit only
  that need's body. For a MARKER-AUTHORED stage (an implementation or
  verification arm), the artefact
  is a one-line codelinks marker in the production or test source, in the exact
  shape your prompt's CHANGED CONTRACT section shows: edit the marker (its title,
  its outgoing link target) and the code beneath it so it still realises the
  changed upstream, KEEPING the marker so the need it materialises stays linked.

Leave every edit as an UNCOMMITTED working-tree change — do not `git add`, do not
commit. The diff on each artefact IS the proposal; the human reviews and approves.

If you cannot tell HOW an artefact should change to stay consistent with the new
upstream, do NOT guess. Write `[NEEDS CLARIFICATION: <what you need to know>]` into
its body and stop — the clarification gate flags it for the human, who answers it.

## The engine handles the cascade

You reconcile ONE stage. The engine runs the next downstream stage as a SEPARATE
pass (a separate agent), after rebuilding so it sees your reconciled output. You do
not need to recurse or drive the next stage yourself — reconcile your stage well
and stop.

## After approval

Once the human accepts the downstream edits, the normal loop closes them out:
because each edit staled that need's and its children's verdicts,
`ubc agent release-check --with-verdicts -p <project path>` reddens on the
`outdated` downstream. Re-running `ubc agent run -p <project path>` (which
re-reviews and records fresh verdicts carrying the new fingerprints) returns
the gate to green. The change is not "done" until that re-review lands.
The gate enforces it.
