---
name: review-requirement
description: Review every need this stage produces by scoring it against the criteria in your briefing, and submit one verdict per need.
---

# review-requirement

This is the review stage for **requirements**: judge every need in your
briefing's `review_needs` set and submit one verdict per need to the
substance gate consumed by `ubc agent verdict-check -p <project path>` and
`ubc agent release-check --with-verdicts -p <project path>`.

This skill carries no fixed rubric and no fixed verdict shape. Both are DATA
your briefing resolves fresh every run — a per-type criteria pack for the
rubric, a derived JSON Schema for the verdict — so either can change without
ever editing this file.

Pass `-p <project path>` on every `ubc agent` command. `<project path>` is the
directory that holds the target `ubproject.toml` (the project the need under
review belongs to). A repository can contain several `ubproject.toml` files,
so without `-p` the command runs against the current directory and can target
the wrong project. Resolve `<project path>` once from the briefing you were
handed and reuse it on every call.

When these instructions say `ubc`, run the exact `ubc` binary whose path the
harness gave you in the task (it is version-matched to the editor). Do not
run a bare `ubc` from your PATH, and do not download or install your own
`ubc`. If no explicit path was given, use the `ubc` already on your PATH.

## Execution steps

1. Read your briefing: `review_needs` (the exact set to review this pass —
   already excludes any `failing` need, which is re-authored rather than
   re-reviewed, and anything already freshly reviewed), `criteria` (the axes
   to score, each with a `scoring_guide` and `max_score`, plus the pack's
   overall `guidance`), `verdict_schema` (the exact JSON shape a verdict
   must match), `verdicts_dir`, `submit_command`, and `fingerprints`. If your
   briefing was not already injected, run
   `ubc agent next --id <need_id> -p <project path>` (optionally
   `--stage <STAGE_ID>`) or `ubc agent review-brief <TYPE> -p <project path>`
   (or `--ids <ID,...>`) and read the same fields from the result.
2. For each id in `review_needs`, read `ubc agent audit --id <ID> -p <project path>`
   (the oracle, never grep `.rst` source) plus its linked context via
   `ubc agent context --id <ID> -p <project path>`.
3. Score EVERY axis your briefing's `criteria` lists, from 0 to that axis's
   `max_score`, following its `scoring_guide` and the pack's `guidance`.
   Give a one-line `reason` for every score, and a `suggestion` whenever the
   score is below max.
4. Assemble one verdict object per need matching your briefing's
   `verdict_schema` — an `axes` map keyed by exactly the axis ids `criteria`
   lists, each scored entry carrying at least `score` and `reason`. Also record who
   produced the verdict: set top-level `agent` to your harness (e.g. `copilot`,
   `claude-code`) and `model` to your model id / slug (e.g. `claude-opus-4.8`).
   These are advisory score provenance (#2279) that never gate — include them by
   default, omitting a field only when you genuinely cannot determine it (never
   guess a slug). Submit it
   by PIPING that JSON on stdin to your briefing's `submit_command` (a
   `ubc agent verdict-submit <ID> --fingerprint <FINGERPRINT> --criteria-fingerprint <CRITERIA_FINGERPRINT> --file - -p <project path>`
   call): substitute the need id, its `<FINGERPRINT>` (that need's entry in your
   briefing's `fingerprints` map), and `<CRITERIA_FINGERPRINT>` (your briefing's
   `criteria.fingerprint`), and feed the verdict JSON on stdin; do NOT write a
   draft file. `--fingerprint` pins the exact content you reviewed and
   `--criteria-fingerprint` the exact rubric: if the need changed after you scored
   it the submit is REJECTED (`ContentChanged`), and if the criteria pack changed
   it is REJECTED (`CriteriaChanged`) — re-review against the current
   content/criteria and resubmit rather than recording a stale pass. If your host truly cannot pipe, write the
   draft to a system temp path OUTSIDE the repository (e.g. `mktemp`), pass it to
   `--file`, and delete it after — NEVER write a draft anywhere inside the
   repository (the engine reads every `*.json` under `verdicts_dir` as a verdict,
   and `verdict-submit` REFUSES an in-repo `--file` path). That command stamps
   the schema version, the pack name, the criteria fingerprint, and the
   reviewed-content fingerprint itself, then validates before writing the verdict
   under `verdicts_dir` — do NOT hand-stamp any fingerprint yourself.
5. Report: the needs reviewed, and for each, the scores you gave.

## Operating principles

- Use `ubc agent audit -p <project path>` / `ubc agent context -p <project path>`,
  not file grepping.
- Fail closed: when genuinely uncertain about an axis — including an empty
  or unreadable body — score it 0 and say why in `reason`.
- Exactly one verdict per need. Submitting again for the same id overwrites
  the previous verdict, so re-running this skill is idempotent.
- `ubc agent verdict-check -p <project path>` evaluates the WHOLE graph, so it
  reports `ok: false` and lists OTHER stages' needs as missing while those
  stages are still unreviewed. That is expected and does NOT mean your review
  of this stage failed. Confirm your stage by checking that the needs you
  reviewed appear in NONE of the problem buckets (missing, failing,
  malformed, outdated, unverifiable).
