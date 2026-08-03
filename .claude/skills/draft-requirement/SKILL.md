---
name: draft-requirement
description: Draft requirements from a parent, each a single shall-clause traced to its parent.
---

# Draft a requirement

The produced need is a single requirement: ONE obligation stated as a single
shall-clause, grounded in observable behaviour, traced up to the parent it
decomposes.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml` (the project the need you are
authoring belongs to). A repository can contain several `ubproject.toml`
files, so without `-p` the command runs against the current directory and can
target the wrong project. Resolve `<project path>` once from the briefing you
were handed and reuse it on every call.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the upstream needs
you must cover, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files to rebuild context. When you genuinely need
one specific need's full detail, run `ubc agent audit --id <ID> -p <project path>`;
for a need's context briefing run `ubc agent context --id <ID> -p <project path>`.
These give structured, reliable data:
prefer them over reading files. Author once at the reported route; do NOT run `ubc
build` repeatedly to poke at state — the engine rebuilds and reports after you
finish.

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction (it says how many
to produce and what shape they take for this project).

## Propose before you author

Do NOT write any RST yet. First present a short, scannable outline of what you
plan to author and ask the user to approve or adjust it. The outline lists:

- the id (with the reported prefix) and one-line shall-clause title of each
  requirement you will create,
- the trace link named in your briefing that each requirement draws up to its
  parent, and which parent it points at,
- the key content decisions, above all how you split any compound obligation
  into separate requirements and what you deliberately leave to a later stage.

Keep it a scannable list, not the full RST. Wait for the user to approve or
adjust, and do not author until they confirm. On approval, author exactly what
you agreed, then leave the independent review to the separate review step.

## Output shape (one directive per requirement)

```rst
.. <type>:: <one-sentence shall-clause title>
   :id: <ID with the reported prefix>
   :status: draft
   :<trace-link>: <PARENT_ID>

   <Requirement body>. The body states exactly one obligation in a single
   shall-clause, grounded in observable behaviour, with no compound "and/or".
```

`<type>` is the type named in your briefing for this stage; `<trace-link>` is
the trace link field named in your briefing.

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- One obligation per directive. Split compound obligations into separate
  requirements.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Always set the trace link named in your briefing up to the parent so the
  stage's trace gate is satisfied for every requirement.
- Write `shall`, not `should` or `must`, for the normative clause.
- Keep the body free of design detail; that belongs in a later stage.
