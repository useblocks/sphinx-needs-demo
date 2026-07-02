---
name: draft-release
description: Author a `release` need — reference data for a planned release (date, status) that requirements are assigned to.
---

# Draft a release

A `release` is planning REFERENCE data: a planned release the requirements are
assigned to (via their `release` link). It is a root — it traces up to nothing — and
carries no shall-clause.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the resolved route and id prefix. Do
NOT re-discover the project: no `find`, `grep`, `cat`. Author once at the reported
route; do NOT run `ubc build` repeatedly.

## Output shape (one directive per release)

```rst
.. release:: <release name>
   :id: <ID with the reported prefix>
   :date: <DD.MM.YYYY>
   :status: open
```

## Rules

- **If you lack the context (which releases exist, dates), do NOT guess.** Write
  `[NEEDS CLARIFICATION: <exactly what you need to know>]` and stop.
- Reference data, not a requirement: no `shall`.
- A `release` is referenced BY requirements (their `release` link points here); do
  NOT add an upstream trace link on the release itself.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
