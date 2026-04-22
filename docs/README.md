# Episode 1 — Demo: Emergency Braking System

> Companion to `Episode-1-X-as-Code-Foundations.marp.md`
> Demo slot: Part 4 · ~17:00–24:00 · target 6–7 minutes

---

## Project Structure

```
demo/
  conf.py               ← Sphinx configuration, activates sphinx_needs + loads ubproject.toml
  ubproject.toml        ← metamodel: types, fields, valid links, schema pointer
  schemas.json          ← schema validation: allowed link types per need type, field enum
  index.rst             ← root document, includes all pages
  requirements.rst      ← SYS-012 (context) + BRAKE-001 (created live)
  specifications.rst    ← SPEC-042 (pre-existing)
  tests.rst             ← TC-017 (pre-existing)
  _build/               ← Sphinx output (not committed)
```

---

## Sphinx Configuration Files

### `conf.py`

```python
# conf.py — Sphinx configuration for the Emergency Braking demo project

project = "Emergency Braking Demo"
author = "useblocks"
release = "1.0"

extensions = [
    "sphinx_needs",
]

# Load all needs configuration from ubproject.toml
needs_from_toml = "ubproject.toml"

# HTML output settings
html_theme = "alabaster"
exclude_patterns = ["_build"]
```

---

### `ubproject.toml`

```toml
"$schema" = "https://ubcode.useblocks.com/ubproject.schema.json"

[project]
name = "Emergency Braking Demo"
version = "1.0.0"
description = "Episode 1 demo — X-as-Code Foundations"

[needs]
id_required = true
id_regex = "^[A-Z][A-Z0-9_-]{3,}$"

# Point to the schema validation rules
schema_definitions_from_json = "schemas.json"

# Need types
[[needs.types]]
directive = "req"
title = "Requirement"
prefix = "R_"
color = "#5599dd"
style = "node"

[[needs.types]]
directive = "spec"
title = "Specification"
prefix = "S_"
color = "#E4FF3D"
style = "node"

[[needs.types]]
directive = "test"
title = "Test Case"
prefix = "T_"
color = "#4caf50"
style = "node"

# Custom field: safety integrity level (enum-validated)
[needs.fields.safety_level]
description = "ASIL safety integrity level (ISO 26262)"

[needs.fields.safety_level.schema]
type = "string"
enum = ["QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"]

# Custom link types
[[needs.extra_links]]
option = "satisfies"
incoming = "is satisfied by"
outgoing = "satisfies"
copy = false

[[needs.extra_links]]
option = "implements"
incoming = "is implemented by"
outgoing = "implements"
copy = false

[[needs.extra_links]]
option = "verifies"
incoming = "verifies"
outgoing = "verified by"
copy = false

[[needs.extra_links]]
option = "tests"
incoming = "is tested by"
outgoing = "tests"
copy = false

[[needs.extra_links]]
option = "covers"
incoming = "is covered by"
outgoing = "covers"
copy = false
```

> **Key rules enforced by `schemas.json`:**
> - `req` may only use `satisfies` and `verifies` as outgoing links
> - `spec` may only use `implements` and `tests` as outgoing links
> - `test` may only use `covers` as outgoing link
> - `safety_level` is validated as an enum — only `QM`, `ASIL-A` … `ASIL-D` are accepted
>
> ubCode surfaces violations as inline diagnostics; Sphinx fails the build on schema violations.

---

### `schemas.json`

```json
{
  "$defs": {
    "type-req":  { "properties": { "type": { "const": "req"  } } },
    "type-spec": { "properties": { "type": { "const": "spec" } } },
    "type-test": { "properties": { "type": { "const": "test" } } }
  },
  "schemas": [
    {
      "id": "req-allowed-links",
      "severity": "violation",
      "message": "A requirement may only link via 'satisfies' and 'verifies'.",
      "select": { "$ref": "#/$defs/type-req" },
      "validate": {
        "local": {
          "unevaluatedProperties": false,
          "properties": {
            "satisfies":   {},
            "verifies": {}
          }
        }
      }
    },
    {
      "id": "spec-allowed-links",
      "severity": "violation",
      "message": "A specification may only link via 'implements' and 'tests'.",
      "select": { "$ref": "#/$defs/type-spec" },
      "validate": {
        "local": {
          "unevaluatedProperties": false,
          "properties": {
            "implements": {},
            "tests":      {}
          }
        }
      }
    },
    {
      "id": "test-allowed-links",
      "severity": "violation",
      "message": "A test case may only link via 'covers'.",
      "select": { "$ref": "#/$defs/type-test" },
      "validate": {
        "local": {
          "unevaluatedProperties": false,
          "properties": {
            "covers": {}
          }
        }
      }
    },
    {
      "id": "safety-level-enum",
      "severity": "violation",
      "message": "safety_level must be one of: QM, ASIL-A, ASIL-B, ASIL-C, ASIL-D.",
      "validate": {
        "local": {
          "properties": {
            "safety_level": {
              "type": "string",
              "enum": ["QM", "ASIL-A", "ASIL-B", "ASIL-C", "ASIL-D"]
            }
          }
        }
      }
    }
  ]
}
```

> **Note on `unevaluatedProperties`:** the schema lists every *link* field that is permitted for
> that need type. Core fields (`id`, `title`, `status`, `tags`, `safety_level`, `links`, …) are
> always evaluated by Sphinx-Needs before the schema runs and are therefore not flagged.
> Only *custom link fields* not listed in `properties` will trigger the violation.

---

### `index.rst`

```rst
Emergency Braking Demo
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents

   requirements
   specifications
   tests

Traceability Overview
---------------------

.. needflow::
   :filter: id in ["SYS-012", "BRAKE-001", "SPEC-042", "TC-017"]
   :show_link_names:
```

---

## Artifacts

### `requirements.rst`

```rst
Requirements
============

System Requirement (context only)
----------------------------------

.. req:: Obstacle Detection and Emergency Braking
   :id: SYS-012
   :status: accepted
   :safety_level: ASIL-D

   The vehicle shall detect obstacles and initiate emergency braking.

Software Requirement (created live in step 2)
---------------------------------------------

.. req:: Emergency Braking Response Time
   :id: BRAKE-001
   :status: draft
   :safety_level: ASIL-D
   :satisfies: SYS-012
   :verifies: TC-017

   The braking control module shall engage emergency braking
   within 150 ms of obstacle detection.
```

---

### `specifications.rst`

```rst
Specifications
==============

.. spec:: Braking Control Module Behaviour
   :id: SPEC-042
   :implements: BRAKE-001

   The braking control module shall process sensor input,
   trigger actuator engagement, and log the event with a timestamp.
```

---

### `tests.rst`

```rst
Test Cases
==========

.. test:: Emergency Braking Timing and Log Integrity
   :id: TC-017
   :covers: BRAKE-001

   Verify that braking actuation occurs within 150 ms of obstacle
   detection and that the event log contains a valid timestamp.
```

---

## Step-by-Step Narrative

| Step | Action | What the audience sees |
|------|--------|------------------------|
| 1 | Open `ubproject.toml` + `schemas.json` | Types, fields (with enum), valid link types per need type — all committed to the repo |
| 2 | Create `BRAKE-001` live, field by field in `requirements.rst` | A typed artifact taking shape: ID, status, safety level, link to SYS-012 |
| 2b | Type `:safety_level: ASIL-Z` | **Immediate ubCode diagnostic** — not a valid enum value |
| 2c | Correct to `:safety_level: ASIL-D` | Diagnostic disappears |
| 3 | Add `:implements: TC-017` to BRAKE-001 | **Immediate ubCode diagnostic** — `implements` is not an allowed link for `req` |
| 3b | Remove the invalid line | Diagnostic disappears instantly — model is valid again |
| 4 | Add `:verifies: TC-017` — correct link type | Chain completes: BRAKE-001 links correctly to TC-017 |
| 5 | Run `sphinx-build -b html . _build/html` | Sphinx builds; `needflow` renders the full chain: SPEC-042 → BRAKE-001 → SYS-012, TC-017 → BRAKE-001 |
| 6 | Change `:status: draft` → `accepted`, run `git diff` | Two lines changed — author, timestamp, exact diff — auditable record |
| 7 *(optional)* | Trigger CI or run local check | Pipeline: all links valid, required attributes present, coverage complete |

---

## Build Instructions

```bash
# From the demo/ directory:

# Install dependencies (once)
pip install sphinx sphinx-needs

# Build HTML documentation
sphinx-build -b html . _build/html

# Open result
open _build/html/index.html
```

> **Presenter note:** Run the build once before the demo to confirm it works.
> The `needflow` diagram requires either Graphviz (`pip install sphinxcontrib-graphviz`) or PlantUML.
> For a no-dependency fallback, replace `.. needflow::` in `index.rst` with a `.. needtable::`.

---

## What to Cut if Time is Tight

Drop step 7. End on the Git diff — it's visual, concrete, and lands the version-control point cleanly.

**Target:** steps 1–6 in 6 minutes.

---

## Traceability Chain (final state)

```
SPEC-042 (spec)          ──── implements ────→ BRAKE-001 (software req, ASIL-D, accepted)
TC-017   (test case)     ──── covers     ────→ BRAKE-001
TC-017   (test case)     ──── covers     ────→ SPEC-042
BRAKE-001                ──── satisfies  ────→ SYS-012 (system req, ASIL-D, accepted)
```

---

## Key Talking Points Per Step

**Step 1 — Metamodel (`ubproject.toml` + `schemas.json`)**
- the config is a file, committed to the repo — reviewable, versioned, part of the baseline
- `conf.py` activates sphinx_needs and points to `ubproject.toml` — separation of concerns
- need types, custom fields (with enum constraints), and valid link types per need type are declared here
- `schemas.json` is the enforcement layer — declarative, JSON-based, no Python required

**Step 2 — Creating BRAKE-001 + enum validation**
- type the fields live — each one has a purpose
- `:id:` is stable and referenceable from anywhere in the model
- `:safety_level:` is a domain field — defined with an enum in `ubproject.toml`
- type `ASIL-Z` deliberately — ubCode flags it immediately (enum constraint from the field schema)
- correct to `ASIL-D` — diagnostic gone
- `:satisfies: SYS-012` — validated link: SYS-012 must exist

**Step 3 — The invalid link (most important moment)**
- add `:implements: TC-017` — a requirement "implementing" a test case
- ubCode flags it immediately: `implements` is not in the allowed link set for `req` (enforced by `schemas.json`)
- pause — let the error land — this is the proof that the quality gate is real
- then fix it: remove the line, diagnostic is gone

**Step 4 — Correct link**
- `:verifies: TC-017` — requirement pointing to the test case that verifies it
- link type is in the allowed set for `req` — model is valid

**Step 5 — Sphinx build + traceability render**
- run `sphinx-build` in the terminal
- open `_build/html/index.html` — the `needflow` diagram shows the full chain
- not a spreadsheet: a live, rendered model

**Step 6 — Git diff**
- change `:status: draft` to `accepted`
- run `git diff` — show the two lines changed
- author, timestamp, exact change — this is the review record
- same workflow as code — same auditability
