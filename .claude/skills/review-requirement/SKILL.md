---
name: review-requirement
description: Review every requirement need against the V-model rubric (atomicity, verifiability, unambiguity, traceability, comprehensibility, feasibility) and write one verdict file per need.
---

# review-requirement

Judge every `req` need (the type the `reqs` stage produces) on the V-model
quality rubric and write one machine-readable verdict file per need to
`.ubc/verdicts/<need>.json`. The verdicts are the substance gate consumed by
`ubc agent verdict-check` and `ubc agent release-check --with-verdicts`.

## Verdict schema (write this exactly)

Write one file per reviewed need at `.ubc/verdicts/<need>.json`:

```json
{
  "need": "REQ_EXAMPLE",
  "pass": true,
  "axes": {
    "atomicity": true,
    "verifiability": true,
    "unambiguity": true,
    "traceability": true,
    "comprehensibility": true,
    "feasibility": true
  },
  "findings": [],
  "reviewed_fingerprint": "<copy the `fingerprint` field from `ubc agent audit <ID>`>"
}
```

Schema rules (enforced by the engine — a non-conformant file is counted
**malformed** and does NOT clear the need from the `missing` set):

- `need` — string, the reviewed need id.
- `pass` — boolean.
- `axes` — a non-empty object; every value must be `true` or `false`. A bare
  `{"need": "X", "pass": true}` with no `axes` is malformed.
- `pass: true` is allowed ONLY when every axis is `true`. `pass: true` with any
  `false` axis is malformed.
- `findings` — a list of strings; it MUST be non-empty when `pass` is `false` OR
  any axis is `false`. A fail with empty `findings` is malformed.
- Extra keys are tolerated; unknown keys never reject a verdict.
- `reviewed_fingerprint` — OPTIONAL string: the `fingerprint` field from
  `ubc agent audit <ID>` (or `ubc agent context <ID>`), copied verbatim. It
  records the exact content you validated against — the need's own body plus its
  up-link parents' bodies, folded into one hash. Do NOT compute it by hand; copy
  the value the briefing already gives you. When you record it, the substance
  gate later flags this verdict `outdated` (a BLOCKING category, like `failing`)
  the moment the reviewed content changes, forcing a fresh review instead of
  trusting a stale green. Omitting it is allowed and backward-compatible — a
  verdict with no `reviewed_fingerprint` is freshness-unknown and never flagged —
  but then a later content edit goes undetected, so always record it.

Fail closed: when uncertain about an axis, set it `false` and record the reason in
`findings`. Conflicting duplicates fail closed too — if ANY verdict file for a
need records a failing judgment, the need is `failing` regardless of how many
passing verdicts exist for it, so a later passing verdict can never bury a real
failure. Write exactly one verdict per need at the `<need>.json` path.

## Execution steps

1. Build the graph: `ubc build needs`. Read the resulting `needs.json` and select
   every need whose `type` is `req` (confirm via `ubc agent status`).
2. For each id, read the briefing with `ubc agent audit <ID>` and the linked
   context with `ubc agent context <ID>`. `ubc agent audit` is the oracle — do
   not grep `.rst` source.
3. Judge each need on all six axes (below). Fail closed.
4. Write `.ubc/verdicts/<ID>.json` per the schema, copying the `fingerprint`
   from that need's `ubc agent audit <ID>` output into `reviewed_fingerprint` so
   the verdict records the content you validated against. Overwrite any existing
   file.
5. Report: needs reviewed, passed, failed (list ids).

## Axes

- **atomicity** — exactly one obligation. FAIL if "and" conjoins two independent
  obligations, or removing a clause leaves a still-complete separate requirement.
- **verifiability** — a concrete test could confirm it without subjective reading.
  FAIL on unmeasured vague adjectives (fast, scalable, robust, intuitive,
  efficient, appropriate ...) or an undefined success condition.
- **unambiguity** — exactly one valid reading. FAIL if a competent reader could
  read it two ways, or conditional logic is vague ("where appropriate").
- **traceability** — links upward to a parent (`traces_to` a `user_story`). FAIL
  if `trace.outgoing` shows no upstream parent. A test linking in is downstream.
- **comprehensibility** — self-contained and intelligible without adjacent
  requirements. FAIL on undefined abbreviations or forward references.
- **feasibility** — implementable with known technology. FAIL on physically
  impossible properties or contradictions with other stated requirements.

## Operating principles

- Use `ubc agent audit` / `ubc agent context`, not file grepping.
- Fail closed; ambiguous is FAIL.
- One file per need, no bundling. Idempotent across runs.
- If `audit` returns an empty body, fail all axes and note "body empty".
