---
name: ubc-agent-next
description: Report and act on the single next actionable workflow stage.
---

Run `ubc agent next -p <project path>` and act on its result.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml`. A repository can contain
several `ubproject.toml` files, so without `-p` the command runs against the
current directory and can target the wrong project. Resolve it once from the
need you were handed and reuse it on every call.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

- Parse the JSON `{ok, stage}` payload.
- If `stage` is present, read its `id`, `produces` type, `route.path`, and
  `author_skill`, then author the artefact that stage produces at that path.
- If `stage` is null, read `reason` (`empty` / `done` / `blocked`) and respond
  accordingly: author the first artefact, stop, or unblock the dependency.

Always re-run `ubc agent next -p <project path>` after authoring to confirm
the stage advanced.
