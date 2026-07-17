---
name: draft-arch
description: Draft architecture elements from their parent requirements, each a component that traces up to the requirement it designs for.
---

# Draft an architecture element

The produced need is a component: an architecture element that traces up to the
requirement it designs for via the trace link named in your briefing. Each
element states what something IS and what it owns, in present tense.

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

Author at the route and with the id prefix the engine reports for this stage, and
follow the project authoring directive given in the instruction (it says how many
elements to produce and whether to include a diagram for this project). Whether the
directive asks for a diagram is a separate switch from whether the diagram GATE is
enabled: if the directive asks for one, include it even when the gate is off. Read
each parent requirement (e.g. with `ubc agent audit --id <PARENT_ID> -p <project path>`)
so every obligation is covered.

## Propose before you author

Do NOT write any RST yet. First present a short, scannable outline of what you
plan to author and ask the user to approve or adjust it. The outline lists:

- the id (with the reported prefix) and noun-phrase title of each architecture
  element you will create,
- the trace link named in your briefing that each element draws to its parent
  requirement, and which requirement it points at,
- the key content decisions, above all how you split distinct responsibilities
  into separate elements and whether the project directive asks for a diagram.

Keep it a scannable list, not the full RST. Wait for the user to approve or
adjust, and do not author until they confirm. On approval, author exactly what
you agreed, then leave the independent review to the separate review step.

## Output shape (one directive per element)

```rst
.. <type>:: <noun-phrase title naming the element>
   :id: <ID with the reported prefix>
   :<trace-link>: <PARENT_ID>[, <PARENT_ID>, ...]
   :status: draft

   <1-3 sentence description of what the element IS and what it owns. Present
   tense, descriptive. No ``shall`` — this stage states what something is, not
   what it shall do.>
```

`<type>` is the type named in your briefing for this stage; `<trace-link>` is
the trace link field named in your briefing.

## Rules

- **If you cannot decide or lack the context to author this faithfully, do NOT
  guess or fabricate.** Write `[NEEDS CLARIFICATION: <exactly what you need to
  know>]` in the body and stop. A human resolves it before the gate goes green —
  the gate fails closed on any need whose body still carries the marker.
- One coherent element per directive. Split distinct responsibilities into
  separate elements.
- The `:id:` carries the reported prefix and matches the project's `id_regex`.
- Always set the trace link named in your briefing to the parent requirement so
  the stage's trace gate is satisfied for every element. One element MAY trace
  to several requirements: list them comma-separated (e.g. `<trace-link>:
  PARENT_A, PARENT_B`). Each listed requirement then has its backward trace
  closed by this element.
- No `shall` in the body. Use present tense: "The X component manages Y".
- Do NOT write a verdict here. Drafting authors the NEED; the verdict is authored
  later by the stage's review skill.

## Confirm

After authoring, run `ubc build needs` then
`ubc agent gaps --scope <parent_id> -p <project path>` to confirm every element
traces up to its parent. `--scope` anchors on a need id and scopes to that
stream. Downstream gaps on not-yet-authored stages are expected and clear
later in the loop.
