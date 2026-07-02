---
name: review-decision
description: Review every decision need against the V-model decision rubric (context_present, alternatives_listed, consequences_present, traces_to_affected, rationale_quality) and write one verdict file per need.
---

# review-decision

Judge every `decision` need (the type the `decisions` stage produces) on the
V-model decision-quality rubric and write one machine-readable verdict file per
need to `.ubc/verdicts/<need>.json`. The verdicts are the substance gate consumed
by `ubc agent verdict-check` and `ubc agent release-check --with-verdicts`.

## Verdict schema (write this exactly)

Write one file per reviewed need at `.ubc/verdicts/<need>.json`:

```json
{
  "need": "DEC_EXAMPLE",
  "pass": true,
  "axes": {
    "context_present": true,
    "alternatives_listed": true,
    "consequences_present": true,
    "traces_to_affected": true,
    "rationale_quality": true
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
   every need whose `type` is `decision` (confirm via `ubc agent status`).
2. For each id, read the briefing with `ubc agent audit <ID>` and the linked
   context with `ubc agent context <ID>`. `ubc agent audit` is the oracle — do
   not grep `.rst` source.
3. Judge each need on all five axes (below). Fail closed.
4. Write `.ubc/verdicts/<ID>.json` per the schema, copying the `fingerprint`
   from that need's `ubc agent audit <ID>` output into `reviewed_fingerprint` so
   the verdict records the content you validated against. Overwrite any existing
   file.
5. Report: needs reviewed, passed, failed (list ids).

## Axes

- **context_present** — a Context section explains the problem and the constraints
  that drove the decision. FAIL if absent or a mere restatement of the title.
- **alternatives_listed** — at least two alternatives (including the chosen one)
  are enumerated. FAIL if only one option, or alternatives are vague.
- **consequences_present** — describes what changes, the trade-offs accepted, and
  follow-on work. FAIL if positives-only or no consequence language.
- **traces_to_affected** — links outward to at least one affected need (`affects`
  a req / arch / risk). FAIL if `trace.outgoing` shows no outgoing links; an
  unlinked decision is an orphan and fails unconditionally.
- **rationale_quality** — the rationale for the chosen option over the
  alternatives is explicit and coherent. FAIL on circular ("X because X is
  better") or ungrounded subjective rationale.

## Operating principles

- Use `ubc agent audit` / `ubc agent context`, not file grepping.
- Fail closed; ambiguous is FAIL.
- One file per need, no bundling. Idempotent across runs.
- If `audit` returns an empty body, fail all axes and note "body empty".
