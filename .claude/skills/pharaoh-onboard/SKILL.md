---
name: pharaoh-onboard
description: Onboard an existing project into a workflow graph: derive it, resolve the ambiguous edges with judgment, and write it back.
---

# Onboard a project into a workflow graph

A project already has needs authored, but no `[workflow]` wired up, or an
existing one you must re-derive. Your job: run the detector, use judgment to
resolve what it could not decide on its own, and write the result back. Never
guess the graph from a filesystem skim. The detector already read every need
and every declared type/link, so trust its output and reason from it.

## Step 1: Derive the plan, don't guess the graph

Run `ubc agent install --detect --plan` (add `-p <dir>` when the project's
config lives under a subdirectory, e.g. `docs/`). This writes nothing. It
emits one JSON object:

```json
{
  "mode": "...",
  "proposed_toml": "...",
  "open_questions": [
    { "id": "...", "kind": "...", "subject": "...", "options": ["..."], "recommended": "...", "evidence": "..." }
  ],
  "dropped_types": ["..."]
}
```

- `proposed_toml` is the derived graph as it stands right now. Read it, it
  is the thing you are about to commit to.
- `open_questions` is exactly what needs YOUR judgment. Each has a stable
  `id` you answer by.
- `dropped_types` were observed but did not make it into a stage: sanity
  check that the drop is intentional (e.g. a pure metadata dimension), not a
  real process artefact the detector under-supported.

## Step 1.5: Spot-check a suspiciously empty plan

An empty plan (`proposed_toml` with no stages and no `open_questions` at
all) is NOT by itself proof there is nothing to onboard. A project can
have plenty of needs authored while its config declares no types of its
own (they can live in a separate runtime extension the config never
spells out), and against a real project an empty plan is far more likely
a sign the detector had nothing to index than that there's truly no
process to derive. Never report success on an empty plan without ruling
this out first.

Confirm there really is nothing here before you report anything: run
`ubc build needs` and see whether it turns up any needs at all, or note
whether the existing config already declares types even without an
index. If either shows the project has real content, re-run Step 1 with
`--from-needs-json <path>`, pointing it at the project's already-built
`needs.json` (commonly somewhere under a `_build/` directory). This
grounds the plan directly on that prebuilt index instead of depending on
the detector's own (bounded) discovery. Only when no needs.json exists
and none can be built should you conclude the plan is genuinely empty,
and report back that the project's config needs its types/links declared
before onboarding can proceed.

## Step 2: Resolve each open question, communicate and propose, never guess silently

For every entry in `open_questions`, read its `evidence` first. Only when
the evidence itself is ambiguous, go read the handful of needs it names.
Judge from the link/type NAMES the evidence gives you and from what those
needs actually contain, never from a hardcoded assumption about what a
project's types are called, since that varies project to project.

- **`label-vs-stage:<type>`**: decide whether the subject type is a real
  step of the process (a **stage**, something that gets produced and
  traced) or a metadata dimension hung off other needs (a **label**, dropped
  from the graph along with every edge where it appears). This fires for
  two shapes of metadata candidate (a type that is only ever a link's
  target, or a peripheral type that is never a target itself but whose
  every outgoing link points at such a target-only type). Read the
  `evidence` to see which shape it is and which incoming or outgoing links
  it names. A link that expresses authorship, ownership, assignment, or a
  roster (or a release/version/tag dimension) is metadata: answer
  `"label"`. A link that expresses one step deriving, decomposing,
  realising, verifying, or mitigating another (the real spine of the
  process) is a stage: answer `"stage"`. Read the named links and the
  handful of needs behind them, not the type's bare name, to make the
  call.
- **`fan-in-parents:<child>:<link>`**: the child links to more than one
  parent type through the same link name, and the detector cannot tell
  which is the child's true upstream(s). Read the evidence's per-parent
  support counts. When they are close, open a couple of the child's needs
  and see which parent(s) they actually trace to in practice. Answer with
  the parent type(s) you conclude are the real upstream: a single name, or
  several from `options` joined with commas when the child legitimately
  traces to more than one of them (never invent a name not already among
  `options`). When NONE of the listed parents is a genuine upstream (an
  unconstrained cross-cutting link that fans out to many unrelated types
  with no real parent among them, e.g. a generic "relates to" association,
  not a hierarchy), answer `"drop"` (or `"none"`) instead of forcing a
  parent.
- **`direction-review:<child>:<link>:<parent>`**: this edge already
  defaults to a bidirectional, gate-enforcing link, but its `evidence`
  reports the child-to-parent link's downstream coverage (the percentage
  of the parent's needs the link actually reaches), and that coverage is
  low. Answer `"keep"` (the `recommended` default) when the parent
  genuinely should be fully covered downstream, so the low coverage is a
  real gap worth surfacing and continuing to gate on. Answer `"detach"`
  when the bidirectional relationship isn't real for this pair: the
  parent was never meant to be fully covered by this link, so gating on
  the backward direction would just be noise. This keeps the edge as a
  documented, non-gating, one-directional link instead of dropping it
  outright. Read the handful of needs behind the low-coverage side before
  concluding the gap is spurious rather than real.
- If a question is genuinely undecidable from what you can see (the
  evidence is thin and the needs themselves don't settle it), keep the
  `recommended` answer and additionally surface
  `[NEEDS CLARIFICATION: <question, in your own words>]` to the human instead
  of guessing. Do not fabricate a confident answer you do not have grounds
  for.

Communicate what you conclude and why before you apply it: a short,
scannable line per question (subject → chosen option → the one-sentence
reason) is enough for the human to sanity-check your judgment.

## Step 3: Apply

Write your answers to a JSON file mapping each question's `id` to your
chosen option (for `fan-in-parents`, a single option, several comma-joined,
or `"drop"`/`"none"`):

```json
{ "<question id>": "<chosen option>", "...": "..." }
```

Run `ubc agent install --detect --answers <file>` (same `-p` you used for
the plan). This writes ONLY the derived process-graph block. Whatever you
already had declared for the needs themselves is left untouched.

## Step 4: Verify + iterate

Confirm the written graph actually behaves:

- `ubc agent doctor`: the config comes back `ok`, with no
  `workflow_disconnected` warning.
- `ubc agent trace`: the edges present match the real graph you read the
  needs for. Nothing dangling, nothing missing.
- `ubc agent next`: returns an actionable next step, proving the graph is
  drivable end to end, not just internally consistent.

If any of these come back wrong (junk edges, a disconnected graph, `next`
with nothing sensible to recommend), your answers need another pass. Go back
to Step 2, reconsider the questions that would produce the edges you are
seeing, and re-run Step 3. Do not hand-edit the written block to patch
around a wrong answer. Fix the answer and regenerate.

## Rules

- Never edit the needs' own declared configuration: only the derived
  process-graph block is yours to write, and only through `--answers`.
- Never invent a type, link, or parent that is not already present in the
  plan's `proposed_toml` or a question's `options`. You are resolving
  ambiguity in what was observed, not adding new ontology.
- Only ever choose among a question's own `options`. If none fits, that is a
  sign the question is undecidable, not license to substitute your own
  value. A `label-vs-stage` answer is always a single `"stage"`/`"label"`,
  and a `direction-review` answer is always a single `"keep"`/`"detach"`.
  The one structural exception is `fan-in-parents`, whose answer may
  instead be a comma-joined subset of its `options`, or `"drop"`/`"none"`
  (write no edge), as that bullet describes.
- A derived graph that is not drivable (`next` returns nothing sensible, or
  `doctor` still complains) is not done: resolve more of your answers and
  re-run before you consider the project onboarded.
