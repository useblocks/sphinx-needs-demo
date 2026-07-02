---
name: draft-team
description: Author the `team` need — the organisational container for a feature that lists the people working on it. Reference data, not a requirement.
---

# Draft a team

A `team` is organisational REFERENCE data: the project / team container for a
feature. It is a root (it traces up to nothing) and lists the people who work on it
via the `persons` link. It is not a requirement — it carries no shall-clause.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the resolved route and id prefix. Do
NOT re-discover the project: no `find`, `grep`, `cat`. Author once at the reported
route; do NOT run `ubc build` repeatedly.

## Output shape (usually one per feature)

```rst
.. team:: <project / team name>
   :id: <ID with the reported prefix>
   :persons: <PERSON_ID>, <PERSON_ID>

   <1-2 sentence description of the team / project scope.>
```

## Rules

- **If you lack the context (team name, members), do NOT guess or invent an org.**
  Write `[NEEDS CLARIFICATION: <exactly what you need to know>]` and stop.
- Reference data, not a requirement: no `shall`.
- `:persons:` lists the ids of the `person` needs on this team (author those with
  `draft-person`). Omit it if no persons exist yet — the `person` stage fills them.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
