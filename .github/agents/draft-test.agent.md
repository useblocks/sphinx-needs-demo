---
name: draft-test
description: Author a test case as a real need via a one-line codelinks marker in the test source, verifying the parent element it covers, so the parent's incoming back-link closes the verification arm.
---

# Draft a test (tests-as-needs)

The verification arm authors a test case as a REAL need, not as a URL field. You
write a ONE-LINE codelinks marker in the test source; `ubc build` materialises it
into a need of the type named in your briefing, carrying an outgoing trace link
up to the parent element it verifies, and the stage's trace edge counts the
parent's incoming back-link for coverage.

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

The briefing in your prompt ALREADY contains the anchor need, the parent elements
you must verify, and the resolved route. Do NOT re-discover the project: no `find`,
`grep`, `cat`, or reading `.rst` files to rebuild context. When you need one
specific need's full detail, run `ubc agent audit --id <PARENT_ID> -p <project path>`;
for its context briefing run `ubc agent context --id <PARENT_ID> -p <project path>`.
Author once at the reported route; do NOT run `ubc build` repeatedly to poke at
state.

## Propose before you author

Do NOT write any test code or marker yet. First present a short, scannable
outline of what you plan to author and ask the user to approve or adjust it. The
outline lists:

- the id (with the reported prefix) and short title of each test marker you
  will write,
- the trace link named in your briefing that each marker carries
  (`[<PARENT_ID>]`) and which parent it covers,
- the test file under the route you will place each marker in, and whether the
  route's trace file already carries the `src-trace` directive or you need to
  author it.

Keep it a scannable list, not the full marker or test code. Wait for the user
to approve or adjust, and do not author until they confirm. On approval, author
exactly what you agreed.

## What you author — TWO things in the route

The stage's route is a directory (e.g. `tests/`). For each parent element to
verify, you author:

1. **The one-line marker in test source.** In a test source file under the
   route (e.g. `tests/test_<feature>.py`), write ONE marker line per test, in a
   comment, in this exact shape:

   ```python
   # @<short title>, <ID>, <type>, [<PARENT_ID>]
   ```

   - `<ID>` carries the reported prefix and matches the project's `id_regex`.
   - `<type>` is the type named in your briefing for this stage.
   - the fourth field is the trace link named in your briefing: a bracketed
     list of the parent ids this test covers (usually one).
   - put real test code beneath the marker if you have it; the marker is what
     materialises the need.

2. **The `src-trace` directive.** A one-line marker materialises a need ONLY
   where a `.. src-trace::` directive naming the src-trace project from your
   briefing appears in a BUILT `.rst` file. Ensure one exists — author
   `code_trace.rst` under the route (or append to it if it already exists)
   with:

   ```rst
   .. src-trace::
      :project: <the src-trace project named in your briefing>
   ```

   Without this directive the markers parse but no need is created and the
   verification gate never closes.

## Rules

- **If you cannot decide which parent a test covers, or lack the context to
  author it faithfully, do NOT guess or fabricate.** A test that covers the
  wrong parent is worse than none. Author only what the briefing grounds.
- Every marker carries `[<PARENT_ID>]` so the trace link is present and the
  trace gate closes for the parent it covers.
- One marker per test case; one trace target per coherent test (split distinct
  responsibilities into separate needs).
- The `<ID>` carries the reported prefix and matches `id_regex`.
- Do NOT reintroduce a per-level URL field — the verification arm is
  needs-in-source, not a URL split.
- Do NOT write a verdict here. Drafting authors the NEED; review is a separate
  stage.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps -p <project path>`
to confirm every parent now carries the incoming back-link the trace gate
checks. A `trace_backward` gap on a parent means it is still unverified.
Add a marker covering it.
