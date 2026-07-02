---
name: ubc-agent-next
description: Report and act on the single next actionable workflow stage.
---

Run `ubc agent next` and act on its result.

- Parse the JSON `{ok, stage}` payload.
- If `stage` is present, read its `id`, `produces` type, `route.path`, and
  `author_skill`, then author the artefact that stage produces at that path.
- If `stage` is null, read `reason` (`empty` / `done` / `blocked`) and respond
  accordingly: author the first artefact, stop, or unblock the dependency.

Always re-run `ubc agent next` after authoring to confirm the stage advanced.
