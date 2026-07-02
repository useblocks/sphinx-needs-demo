---
name: draft-requirement
description: Draft sphinx-needs requirements from a parent, each a single shall-clause traced to its parent.
---

# Draft a requirement

A `req` is a single requirement: ONE obligation stated as a single shall-clause,
grounded in observable behaviour, traced up to the parent it decomposes.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the upstream needs
you must cover, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files to rebuild context. When you genuinely need
one specific need's full detail, run `ubc agent audit <ID>`; for a need's context
briefing run `ubc agent context <ID>`. These give structured, reliable data —
prefer them over reading files. Author once at the reported route; do NOT run `ubc
build` repeatedly to poke at state — the engine rebuilds and reports after you
finish.

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction (it says how many
to produce and what shape they take for this project).

## Output shape (one directive per requirement)

```rst
.. req:: <one-sentence shall-clause title>
   :id: <ID with the reported prefix>
   :status: draft
   :<trace-link>: <PARENT_ID>

   <Requirement body>. The body states exactly one obligation in a single
   shall-clause, grounded in observable behaviour, with no compound "and/or".
```

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- One obligation per directive. Split compound obligations into separate reqs.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Always set the trace link up to the parent so the stage's trace gate is
  satisfied for every requirement.
- Write `shall`, not `should` or `must`, for the normative clause.
- Keep the body free of design detail; that belongs in the architecture stage.
