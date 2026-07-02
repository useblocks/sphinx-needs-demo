---
name: draft-test
description: Author a test case as a real `test` need via a one-line codelinks marker in the test source, verifying the architecture element it covers, so the arch's incoming `verifies_back` closes the verification arm.
---

# Draft a test (tests-as-needs)

The verification arm authors a test case as a REAL need, not as a URL field. You
write a ONE-LINE codelinks marker in the test source; `ubc build` materialises it
into a `test` need carrying an outgoing `verifies` link, and the `tests` stage's
trace edge counts the arch's incoming `verifies_back` for coverage.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the architecture
elements you must verify, and the resolved route. Do NOT re-discover the project: no
`find`, `grep`, `cat`, or reading `.rst` files to rebuild context. When you need one
specific need's full detail, run `ubc agent audit <ARCH_ID>`; for its context
briefing run `ubc agent context <ARCH_ID>`. Author once at the reported route; do
NOT run `ubc build` repeatedly to poke at state.

## What you author — TWO things in the test route

The `tests` stage's route is a directory (e.g. `tests/`). For each architecture
element to verify, you author:

1. **The one-line marker in test source.** In a test source file under the route
   (e.g. `tests/test_<feature>.py`), write ONE marker line per test, in a comment,
   in this exact shape:

   ```python
   # @<short test title>, <TEST_ID>, test, [<ARCH_ID>]
   ```

   - `<TEST_ID>` carries the reported `test` prefix and matches the project's
     `id_regex` (e.g. `TEST_LANE`).
   - the fourth field is the `verifies` link: a bracketed list of the `arch` IDs
     this test covers (usually one, e.g. `[ARCH_LANE]`).
   - put real test code beneath the marker if you have it; the marker is what
     materialises the need.

2. **The `src-trace` directive.** A one-line marker materialises a need ONLY where a
   `.. src-trace:: :project: tests` directive appears in a BUILT `.rst` file. Ensure
   one exists — author `tests/code_trace.rst` (or append to it if it already exists)
   with:

   ```rst
   .. src-trace::
      :project: tests
   ```

   Without this directive the markers parse but no `test` need is created and the
   verification gate never closes.

## Rules

- **If you cannot decide which arch a test covers, or lack the context to author it
  faithfully, do NOT guess or fabricate.** A test that verifies the wrong arch is
  worse than none. Author only what the briefing grounds.
- Every test marker carries `[<ARCH_ID>]` so the `verifies` link is present and the
  trace gate closes for the arch it covers.
- One marker per test case; one `verifies` target per coherent test (split distinct
  responsibilities into separate `test` needs).
- The `<TEST_ID>` carries the reported `test` prefix and matches `id_regex`.
- Do NOT reintroduce a `*_test_url` URL field — the verification arm is tests-as-needs,
  not a per-level URL split.
- Do NOT write a verdict here. Drafting authors the NEED; review is a separate stage.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps` to confirm every arch
now carries an incoming `verifies_back` (the `tests` stage's trace gate is closed).
A `trace_backward` gap on an arch means that arch is still unverified — add a test
marker covering it.
