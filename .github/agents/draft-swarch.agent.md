---
name: draft-swarch
description: Draft SWE.2 software architecture elements (`swarch`) from their parent software requirements, each a component traced up.
---

# Draft a software architecture element (SWE.2)

A `swarch` is a software component: an architecture element that realises one or
more software requirements (`swreq`). Each element states what something IS and what
it owns, in present tense, and traces up to the `swreq` it designs for.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the upstream needs you
must cover, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files. When you need one specific need's full
detail, run `ubc agent audit <ID>`; for its context briefing run `ubc agent context
<ID>`. Author once at the reported route; do NOT run `ubc build` repeatedly.

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction (it says how many
elements to produce and whether to include a diagram). Read each parent `swreq`
(e.g. with `ubc agent audit <SWREQ_ID>`) so every obligation is covered.

## Output shape (one directive per element)

```rst
.. swarch:: <noun-phrase title naming the element>
   :id: <ID with the reported prefix>
   :<trace-link>: <PARENT_SWREQ_ID>
   :status: draft

   <1-3 sentence description of what the element IS and what it owns. Present
   tense, descriptive. No ``shall`` — architecture states what something is, not
   what it shall do.>
```

## Rules

- **If you cannot decide or lack the context, do NOT guess.** Write `[NEEDS
  CLARIFICATION: <exactly what you need to know>]` in the body and stop.
- One coherent element per directive. Split distinct responsibilities into separate
  `swarch` needs.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Set the trace link up to the parent using the EXACT field name the engine reports
  as `gate.link` for this stage — copy it verbatim (in this project it is `links`).
  Do not guess a synonym.
- No `shall` in the body. Use present tense: "The X subsystem manages Y".
- Do NOT write a verdict here; the verdict is authored later by `review-arch`.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps --scope <feature>` to
confirm every element traces up to its parent.
