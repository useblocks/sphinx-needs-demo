{% set page="pharaoh.rst" %}
{% include "demo_page_header.rst" with context %}

🦅 Pharaoh setup
================

`Pharaoh <https://github.com/useblocks/pharaoh>`__ is an authoring and
review layer that sits on top of Sphinx-Needs. It does not change how
needs are stored or built. Sphinx-Needs remains the source of truth.
Pharaoh adds:

* atomic skills for drafting, reviewing, and auditing requirements,
  architecture elements, FMEA entries, test cases, and decisions.
* a per-project tailoring layer (``.pharaoh/project/``) that captures
  workflow states, artefact catalogs, ID conventions, and review
  checklists in YAML.
* a traceability gate (``pharaoh:mece``) that reports gaps, orphans,
  and link inconsistencies against the project's declared chains.
* GitHub Copilot agents (``@pharaoh.req-draft``, ``@pharaoh.mece``,
  ``@pharaoh.flow``, ...) installed under ``.github/agents``.

This page records how Pharaoh was bootstrapped on the
sphinx-needs-demo repository so the setup can be reproduced.

What Pharaoh adds on top of Sphinx-Needs
----------------------------------------

The demo project already declares its need types and link options in
``docs/ubproject.toml``. Pharaoh re-uses those declarations and adds
the files described below.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - File / directory
     - Purpose
     - Tracked in git?
   * - ``pharaoh.toml``
     - Pharaoh strictness, mode, traceability rules, codelinks toggle.
       Only Pharaoh's own behavior, not Sphinx-Needs configuration.
     - yes
   * - ``.pharaoh/project/workflows.yaml``
     - Lifecycle state machine per need type
       (``draft → reviewed → approved``).
     - yes
   * - ``.pharaoh/project/id-conventions.yaml``
     - Per-type ID prefixes and the project's ``id_regex`` mirror.
     - yes
   * - ``.pharaoh/project/artefact-catalog.yaml``
     - Required and optional fields per type, parent-of relations,
       lifecycle reference.
     - yes
   * - ``.pharaoh/project/checklists/<type>.md``
     - Review checklist consumed by ``pharaoh:<type>-review`` skills.
     - yes
   * - ``.pharaoh/runs/``, ``.pharaoh/plans/``,
       ``.pharaoh/session.json``, ``.pharaoh/cache/``
     - Run-time artefacts emitted by Pharaoh skills.
     - **no** (gitignored)
   * - ``.github/agents/pharaoh.*.agent.md``
     - Custom Copilot Chat agents.
     - yes
   * - ``.github/prompts/pharaoh.*.prompt.md``
     - Reusable prompts (``/pharaoh.author``, ``/pharaoh.mece``, ...).
     - yes
   * - ``.github/copilot-instructions.md``
     - Repository-wide Copilot preamble that loads Pharaoh context.
     - yes

Setup
-----

The setup is performed by the Pharaoh setup agent. It is idempotent:
re-running it on an already-configured project shows a diff and asks
before overwriting any file.

Prerequisites
^^^^^^^^^^^^^

* a Sphinx project with Sphinx-Needs already configured
  (``ubproject.toml`` or ``conf.py`` declaring at least one
  ``[[needs.types]]`` entry).
* the Pharaoh plugin installed in your Claude Code or Copilot CLI
  workspace.

Optional but recommended:

* the ``ubc`` CLI on ``PATH`` (faster, deterministic data access).
* the ubCode VS Code extension (live indexing and MCP integration).

Running the setup
^^^^^^^^^^^^^^^^^

After the agents in this PR are committed, GitHub Copilot Chat
exposes ``@pharaoh.setup`` as the entry point:

.. code-block:: text

   @pharaoh.setup

In Claude Code, invoke the same skill via its plugin name:

.. code-block:: text

   /pharaoh:pharaoh-setup

Either form runs the same five steps:

1. **Detect project structure.** Reads ``ubproject.toml``, lists
   declared types and link options, samples existing IDs, and detects
   whether sphinx-codelinks is configured.
2. **Generate** ``pharaoh.toml``. Asks for a strictness mode and a
   project-lifecycle mode (``reverse-eng``, ``greenfield``, or
   ``steady-state``) and writes the file at the workspace root.
3. **Scaffold Copilot agents** under ``.github/agents/`` and
   ``.github/prompts/``.
4. **Configure** ``.gitignore``. Adds narrow entries for the
   ephemeral ``.pharaoh/`` paths and leaves ``.pharaoh/project/``
   tracked.
5. **Bootstrap tailoring.** Calls ``pharaoh-tailor-bootstrap`` to
   write the YAML tailoring files and the per-type checklists into
   ``.pharaoh/project/``.

This demo's ``pharaoh.toml``
----------------------------

.. literalinclude:: ../pharaoh.toml
   :language: toml
   :caption: pharaoh.toml

A few decisions worth calling out:

* **Mode** is ``reverse-eng``. The catalogue already exists, so the
  ``require_change_analysis`` and ``require_mece_on_release`` gates
  start permissive. They can be tightened with ``pharaoh:gate-advisor``
  once the workflow stabilises.
* **Strictness** is ``advisory``. Pharaoh skills suggest the
  recommended workflow but never block authoring.
* **Required link chains** reflect the 100%-coverage policy that the
  existing 268 needs already satisfy: ``spec → req``, ``arch → req``,
  ``safety_goal → hazard``, ``fsr → safety_goal``. Chains for
  ``impl`` and ``test`` were intentionally left out because the
  corpus shows mixed parent types below 90% coverage.
* **Codelinks** are enabled. Pharaoh's change-impact analysis follows
  the ``[codelinks.projects.coffee_machine]`` configuration declared
  in ``docs/ubproject.toml``.

Verifying the setup
-------------------

Build the documentation and run the MECE check to confirm the
traceability rules match the corpus:

.. code-block:: bash

   uv sync
   uv run sphinx-build -b html docs docs/_build/html -W

After the build emits ``docs/_build/html/needs.json``, invoke MECE
from your agent. In Copilot Chat:

.. code-block:: text

   @pharaoh.mece

The same prompt is available as ``/pharaoh.mece`` and, in Claude
Code, as ``/pharaoh:pharaoh-mece``.

For the demo's current state the report shows zero gaps against the
configured chains. Other findings (status mismatches, ID-regex
violations, undeclared types injected by ``sphinx-test-reports``) are
pre-existing properties of the corpus and are surfaced for review,
not introduced by Pharaoh.

Tailoring layer
---------------

The YAML files under ``.pharaoh/project/`` are intentionally
human-readable so that they can be hand-tuned. Key entry points:

* ``workflows.yaml``: change the allowed states or add a
  ``deprecated`` terminal state.
* ``artefact-catalog.yaml``: promote a field from optional to
  required, or restrict ``child_of`` to a smaller set of parent types.
* ``checklists/<type>.md``: edit the review questions consumed by
  ``pharaoh:<type>-review``.

Re-run ``pharaoh:tailor-detect`` once the catalogue grows past a few
dozen needs to refresh the inferred conventions.
