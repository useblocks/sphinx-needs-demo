---
name: record-decision
description: Record a design decision as a traceable directive with Context/Alternatives/Consequences/Rationale body sections, linked to the needs it constrains.
---

# Record a decision

Produce one directive of the type named in your briefing, with four body
sections, linked to the needs it constrains via the trace link named in your
briefing.

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

## How you route

1. Run `ubc agent next -p <project path>` and read this stage's
   `route.resolved_path` and `route.id_prefix` reported for it. Do not guess
   the path.
2. For each constrained need id, run `ubc agent audit --id <ID> -p <project path>`
   to confirm it exists. Warn but do not silently drop an invalid link.

## Propose before you author

Do NOT write any RST yet. First present a short, scannable outline of what you
plan to author and ask the user to approve or adjust it. The outline lists:

- the decision id (with the reported prefix) and the title naming what is
  decided,
- the trace links named in your briefing and which validated needs the
  decision constrains,
- the key content decisions: the alternatives you will record and the option
  you chose over them.

Keep it a scannable list, not the full RST. Wait for the user to approve or
adjust, and do not author until they confirm. On approval, author exactly what
you agreed, then leave the independent review to the separate review step.

## Output shape

Each section label is a BOLD label on its own line, followed by a blank line,
then prose. Do NOT use an RST section underline (`Context` followed by
`-------`) inside the body: ubc rejects it with `block.title_disallowed` and the
build fails.

```rst
.. <type>:: <title naming what is decided>
   :id: <ID with the reported prefix>
   :status: accepted
   :<trace-link>: <AFFECTED_ID_1>, <AFFECTED_ID_2>

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

`<type>` is the type named in your briefing for this stage; `<trace-link>` is
the trace link field named in your briefing.

## Rules

- All four sections (Context, Alternatives, Consequences, Rationale) are
  mandatory body sections, each a bold label. Never put the rationale in a
  directive option instead: this need type may not declare one and `ubc check`
  aborts with `block.directive_unknown_option`.
- The `:id:` carries the reported prefix and matches the `id_regex`.
- Set the trace link named in your briefing to the needs the decision
  constrains so it is not an orphan.
- Validate every constrained id with `ubc agent audit -p <project path>`
  before writing.
- Do NOT write a verdict here. The verdict is authored later by the stage's
  review skill, from its documented schema.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps -p <project path>`
to confirm the build is clean.
