---
name: draft-need
description: Elicit SYS.1 stakeholder needs as sphinx-needs `need` items — the root of the requirement chain, one capability each.
---

# Draft a stakeholder need (SYS.1 elicitation)

A `need` is a SYS.1 elicited stakeholder requirement: ONE capability the system
must provide, stated from the stakeholder's point of view. It is the ROOT of the
requirement chain — it traces up to nothing; everything downstream (`req`, `arch`,
`swreq`, ...) traces back to it.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor and the resolved route. Do
NOT re-discover the project: no `find`, `grep`, `cat`, or reading `.rst` files to
rebuild context. When you genuinely need one specific need's full detail, run `ubc
agent audit <ID>`; for a need's context briefing run `ubc agent context <ID>`.
Author once at the reported route; do NOT run `ubc build` repeatedly to poke at
state — the engine rebuilds and reports after you finish.

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction (it says how many
to produce and what shape they take for this project).

## Output shape (one directive per need)

```rst
.. need:: <short capability title>
   :id: <ID with the reported prefix>
   :status: draft

   The system shall <provide one capability>, stated from the stakeholder's point
   of view as a single obligation, grounded in observable behaviour, with no
   compound "and/or".
```

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- One capability per directive. Split compound needs into separate `need` items.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- A `need` is the ROOT of the chain: do NOT add an upstream trace link — nothing is
  its parent. Downstream `req`s link UP to it (via the `links` field).
- Write `shall` for the normative clause. Keep it solution-free — no design or
  software detail; that is what the downstream `req` / `arch` / `swreq` stages add.
- Do NOT write a verdict here. Drafting authors the NEED; the verdict is authored
  later by `review-feat`.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps --scope <feature>` to
confirm the elicitation is recorded. Downstream gaps on not-yet-authored stages are
expected and clear later in the loop.
