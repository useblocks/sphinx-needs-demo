---
name: draft-arch
description: Draft architecture elements from their parent requirements, each a component that covers a requirement, traced up via the stage's link.
---

# Draft an architecture element

An `arch` is a component: an architecture element that covers a requirement. Each
element states what something IS and what it owns, in present tense, and traces up
to the requirement it designs for via the link the engine reports for the stage
(its `gate.link` — in this project, `links`).

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
elements to produce and whether to include a diagram for this project). Read each
parent requirement (e.g. with `ubc agent audit <REQ_ID>`) so every obligation is
covered.

## Output shape (one directive per element)

```rst
.. arch:: <noun-phrase title naming the element>
   :id: <ID with the reported prefix>
   :<trace-link>: <PARENT_REQ_ID>
   :status: draft

   <1-3 sentence description of what the element IS and what it owns. Present
   tense, descriptive. No ``shall`` — architecture states what something is, not
   what it shall do.>
```

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- One coherent element per directive. Split distinct responsibilities into
  separate `arch` needs.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Set the trace link up to the parent requirement using the EXACT field name the
  engine reports as `gate.link` for this stage — copy it verbatim (in this project
  it is `links`). Do not guess a synonym. This satisfies the stage's trace gate for
  every element.
- No `shall` in the body. Use present tense: "The X component manages Y".
- Do NOT write a verdict here. Drafting authors the NEED; the verdict is authored
  later by `review-arch`.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps --scope <feature>` to
confirm every element traces up to its parent. Downstream gaps on not-yet-authored
stages are expected and clear later in the loop.
