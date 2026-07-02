---
name: draft-impl
description: Author an implementation element as a real `impl` need via a one-line codelinks marker in the production source, implementing the architecture element it realises, so the arch's incoming `implements_back` closes the implementation arm.
---

# Draft an implementation (impl-as-needs)

The implementation arm authors an implementation element as a REAL need, not as a URL
field. You write a ONE-LINE codelinks marker in the production source; `ubc build`
materialises it into an `impl` need carrying an outgoing `implements` link, and the
`code` stage's trace edge counts the arch's incoming `implements_back` for coverage.

## Use the briefing and the tools — do NOT spelunk the filesystem

The briefing in your prompt ALREADY contains the anchor need, the architecture
elements you must implement, and the resolved route. Do NOT re-discover the project: no
`find`, `grep`, `cat`, or reading `.rst` files to rebuild context. When you need one
specific need's full detail, run `ubc agent audit <ARCH_ID>`; for its context
briefing run `ubc agent context <ARCH_ID>`. Author once at the reported route; do
NOT run `ubc build` repeatedly to poke at state.

## What you author — TWO things in the code route

The `code` stage's route is a directory (e.g. `src/`). For each architecture
element to implement, you author:

1. **The one-line marker in production source.** In a source file under the route
   (e.g. `src/<feature>.py`), write ONE marker line per implementation, in a comment,
   in this exact shape:

   ```python
   # @<short impl title>, <IMPL_ID>, impl, [<ARCH_ID>]
   ```

   - `<IMPL_ID>` carries the reported `impl` prefix and matches the project's
     `id_regex` (e.g. `IMPL_LANE`).
   - the fourth field is the `implements` link: a bracketed list of the `arch` IDs
     this implementation realises (usually one, e.g. `[ARCH_LANE]`).
   - put real production code beneath the marker; the marker is what materialises the
     need, the code beneath it is the implementation it stands for. Keep it minimal
     and idiomatic for the target language.

2. **The `src-trace` directive.** A one-line marker materialises a need ONLY where a
   `.. src-trace:: :project: code` directive appears in a BUILT `.rst` file. Ensure
   one exists — author `src/code_trace.rst` (or append to it if it already exists)
   with:

   ```rst
   .. src-trace::
      :project: code
   ```

   Without this directive the markers parse but no `impl` need is created and the
   implementation gate never closes.

## Rules

- **If you cannot decide which arch an implementation realises, or lack the context to
  author it faithfully, do NOT guess or fabricate.** An impl that implements the wrong
  arch is worse than none. Author only what the briefing grounds.
- Every impl marker carries `[<ARCH_ID>]` so the `implements` link is present and the
  trace gate closes for the arch it realises.
- One marker per implementation element; one `implements` target per coherent unit
  (split distinct responsibilities into separate `impl` needs).
- The `<IMPL_ID>` carries the reported `impl` prefix and matches `id_regex`.
- Do NOT reintroduce a `code_url` URL field or a `@need-ids:` back-attach — the
  implementation arm is impl-as-needs, not a ref-URL back-attach onto the arch.
- Do NOT write a verdict here. Drafting authors the NEED; review is a separate stage.

## Confirm

After authoring, run `ubc build needs` then `ubc agent gaps` to confirm every arch
now carries an incoming `implements_back` (the `code` stage's trace gate is closed).
A `trace_backward` gap on an arch means that arch is still unimplemented — add an impl
marker covering it.
