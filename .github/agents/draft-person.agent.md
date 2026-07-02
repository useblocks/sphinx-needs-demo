---
name: draft-person
description: Author a `person` need — reference data for someone working on the feature (role, contact). Referenced by the team's persons link.
---

# Draft a person

A `person` is organisational REFERENCE data: someone who works on the feature. The
feature's `team` references them via its `persons` link, so a `person` carries no
upstream trace link of its own. It is not a requirement.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the resolved route and id prefix. Do
NOT re-discover the project: no `find`, `grep`, `cat`. Author once at the reported
route; do NOT run `ubc build` repeatedly.

## Output shape (one directive per person)

```rst
.. person:: <full name>
   :id: <ID with the reported prefix>
   :role: <role, e.g. Architect / Project manager>
   :contact: <email>
```

## Rules

- **If you lack the context (name, role, contact), do NOT guess or invent people.**
  Write `[NEEDS CLARIFICATION: <exactly what you need to know>]` and stop.
- Reference data, not a requirement: no `shall`, no body obligation.
- A `person` is referenced BY the team's `persons` link; do NOT add an upstream
  trace link on the person itself.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
