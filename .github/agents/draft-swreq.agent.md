---
name: draft-swreq
description: Draft SWE.1 software requirements (`swreq`) from their parent system requirement / architecture, each a single shall-clause traced up.
---

# Draft a software requirement (SWE.1)

A `swreq` is a single software requirement: ONE obligation stated as a shall-clause,
derived from the system requirement (`req`) and architecture (`arch`) it refines,
and traced up to its parent.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the upstream needs you
must cover, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files. When you need one specific need's full
detail, run `ubc agent audit <ID>`; for its context briefing run `ubc agent context
<ID>`. Author once at the reported route; do NOT run `ubc build` repeatedly.

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction.

## Output shape (one directive per requirement)

```rst
.. swreq:: <one-sentence shall-clause title>
   :id: <ID with the reported prefix>
   :<trace-link>: <PARENT_ID>
   :status: draft

   <Requirement body>. States exactly one software obligation in a single
   shall-clause, grounded in observable behaviour, with no compound "and/or".
```

## Rules

- **If you cannot decide or lack the context, do NOT guess.** Write `[NEEDS
  CLARIFICATION: <exactly what you need to know>]` in the body and stop.
- One obligation per directive. Split compound obligations into separate `swreq`s.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Set the trace link up to the parent using the EXACT field name the engine reports
  as `gate.link` for this stage — copy it verbatim (in this project it is `links`).
  Do not guess a synonym.
- Write `shall`, not `should` or `must`. Keep design detail out — that belongs in
  the `swarch` stage.
- Do NOT write a verdict here; the verdict is authored later by `review-requirement`.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps --scope <feature>` to
confirm every `swreq` traces up to its parent.
