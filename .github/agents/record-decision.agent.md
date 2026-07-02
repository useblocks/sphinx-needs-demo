---
name: record-decision
description: Record a design decision as a traceable decision directive with Context/Alternatives/Consequences/Rationale body sections, linked to the needs it affects.
---

# Record a decision

Produce one `decision` directive with four body sections, linked to the needs it
affects via the `affects` link the `decisions` stage declares.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the upstream needs
you must cover, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files to rebuild context. When you genuinely need
one specific need's full detail, run `ubc agent audit <ID>`; for a need's context
briefing run `ubc agent context <ID>`. These give structured, reliable data —
prefer them over reading files. Author once at the reported route; do NOT run `ubc
build` repeatedly to poke at state — the engine rebuilds and reports after you
finish.

## How you route

1. Run `ubc agent next` and read the `decisions` stage's `route.resolved_path`
   (`specs/_global/decisions.rst`) and `route.id_prefix` (`DEC_`). Do not guess
   the path.
2. For each affected need id, run `ubc agent audit <ID>` to confirm it exists.
   Warn but do not silently drop an invalid link.

## Output shape

Each section label is a BOLD label on its own line, followed by a blank line,
then prose. Do NOT use an RST section underline (`Context` followed by `-------`)
inside the body: ubc rejects it with `block.title_disallowed` and the build fails.

```rst
.. decision:: <title naming what is decided>
   :id: DEC_<NAME>
   :status: accepted
   :affects: REQ_<AFFECTED_1>, ARCH_<AFFECTED_2>

   **Context**

   <1-3 sentences: the problem, constraint, or tradeoff that made a decision
   necessary.>

   **Alternatives**

   <each rejected alternative with one sentence on why it was not chosen. At
   least one alternative is mandatory — a decision with no alternatives is not
   traceable.>

   **Consequences**

   <1-3 sentences on what this decision enables, constrains, or defers. Name the
   trade-offs accepted, not only the positives.>

   **Rationale**

   <one-sentence summary of why the chosen option beats the alternatives.>
```

## Rules

- All four sections (Context, Alternatives, Consequences, Rationale) are
  mandatory body sections, each a bold label. Never put the rationale in a
  `:rationale:` directive option: the decision type may not declare it and
  `ubc check` aborts with `block.directive_unknown_option`.
- The `:id:` carries the `route.id_prefix` (`DEC_`) and matches the `id_regex`.
- Set `:affects:` to the needs the decision constrains so it is not an orphan.
- Validate every affected id with `ubc agent audit` before writing.
- Do NOT write a verdict here. The verdict is authored later by `review-decision`
  from its documented schema.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps` to confirm the
build is clean.
