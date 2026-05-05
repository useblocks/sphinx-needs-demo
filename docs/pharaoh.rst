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
* the Pharaoh plugin installed in your AI assistant of choice
  (see below).

Optional but recommended:

* the ``ubc`` CLI on ``PATH`` (faster, deterministic data access).
* the ubCode VS Code extension (live indexing and MCP integration).

Installing the Pharaoh plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Claude Code.** Add the marketplace, install the plugin, and reload
plugins:

.. code-block:: text

   /plugin marketplace add useblocks/pharaoh
   /plugin install pharaoh@pharaoh-dev
   /reload-plugins

To pin a specific Pharaoh release instead of tracking ``pharaoh-dev``,
add the marketplace at a tag:

.. code-block:: text

   /plugin marketplace add useblocks/pharaoh#v1.0.0

**GitHub Copilot CLI.** Same flow with the ``copilot`` command:

.. code-block:: bash

   copilot plugin marketplace add useblocks/pharaoh
   copilot plugin install pharaoh@pharaoh-dev

Once the plugin is installed, the agents and skills described below
become available in the assistant.

Running the setup
^^^^^^^^^^^^^^^^^

After the plugin is installed and the agents in this PR are committed,
GitHub Copilot Chat exposes ``@pharaoh.setup`` as the entry point:

.. code-block:: text

   @pharaoh.setup

In Claude Code, invoke the same skill via its plugin slash form:

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

🛠️ Walkthrough: AI-assisted V-model authoring
---------------------------------------------

Once setup is complete, the typical Pharaoh workflow on this demo
takes four prompts. Each prompt is self-contained, so they can be run
top-to-bottom or in isolation. The example below uses the GitHub
Copilot Chat syntax (``@pharaoh.<name>``); in Claude Code the
equivalent slash form is ``/pharaoh:pharaoh-<name>``.

The shared scenario across the four prompts is the existing
``REQ_001 — Lane Detection Algorithm`` and the ``LaneDetection`` class
in ``src/automotive_adas.py``. The walkthrough fills a focused
API-encapsulation requirement, writes the test that verifies it, and
then asks what changes if ``REQ_001`` itself is revised.

Step 1: gap analysis
^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   @pharaoh.mece

   Analyse this sphinx-needs project for traceability gaps and
   consistency issues. Use the corpus at docs/_build/html/needs.json.
   Report required-link-chain violations, orphans, status mismatches,
   ID-pattern violations against the project's id_regex, and any need
   type observed in the corpus that is not declared in
   [[needs.types]]. Quote concrete need IDs in every finding.

Expected: the four declared traceability chains hit 100 percent
coverage, but the report surfaces parent-closed/child-open status
mismatches (for example ``EX_SPEC_001 (closed) -> EX_REQ_001 (open)``),
a handful of needs of types injected by ``sphinx-test-reports`` that
are not declared in ``[[needs.types]]``, and a number of existing
need IDs that fail the project's own ``id_regex``.

Step 2: reverse-engineer a focused requirement from code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   @pharaoh.req-from-code

   Read src/automotive_adas.py. The LaneDetection class is already
   linked to SWREQ_001/002/003 and REQ_001 via three IMPL directives
   in its docstrings, so the broad behaviour is captured. What is
   not captured is a focused requirement for the API encapsulation
   contract of the class — what the caller can rely on without
   inspecting raw image data. Emit a single sphinx-needs `req`
   directive that captures that contract as a child of REQ_001.

   Constraints: ID prefix at most 10 chars (e.g. REQ_LANE_01);
   :status: open; :links: REQ_001; only use fields and link options
   declared in docs/ubproject.toml.

Expected: a ``.. req:: REQ_LANE_01`` block (or similar short ID),
``:links: REQ_001``, and a single shall-clause grounded in the
``LaneDetection`` class's public methods, ready to paste under
``docs/automotive-adas/``.

Step 3: write the missing test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   @pharaoh.vplan-draft

   Pick requirement REQ_001 (Lane Detection Algorithm) from the
   corpus and generate a single test case that verifies its
   observable behaviour.

   Constraints: directive name `test` (NOT `tc`); ID prefix at most
   10 chars (e.g. T_LANE_DET_001); :status: open; link to the parent
   via the project's generic option (`:links: REQ_001`), not
   `:verifies:`; body must contain explicit Inputs, Steps, and
   Expected sections with at least one measurable threshold.

Expected: a ``.. test:: T_LANE_DET_001`` block with three RST
paragraphs (Inputs / Steps / Expected) and a measurable acceptance
criterion (for example a lateral-deviation threshold across lighting
scenarios).

Step 4: change-impact analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   @pharaoh.change

   The existing requirement REQ_001 (Lane Detection Algorithm) is
   being revised: tighten the lateral-deviation tolerance and require
   the algorithm to run on a constrained embedded ECU instead of the
   development host.

   Walk the traceability graph in docs/_build/html/needs.json
   starting from REQ_001, following outgoing and incoming :links:
   edges only. Skip person, team, and release nodes. Report:

   * every architecture element linked to REQ_001 (must update)
   * every software requirement linked to REQ_001 (must update)
   * every test case that exercises REQ_001 or the affected swreqs
     (must re-run)
   * the release REQ_001 is scheduled into; flag whether the change
     fits the release window
   * any newly authored child needs from Steps 2 and 3 of this
     walkthrough that depend on REQ_001

   End with a one-paragraph summary suitable for a change-board
   ticket.

Expected: a tight blast radius of 6 to 8 needs in the lane-detection
domain — one architecture element, three software requirements, two
system tests, the release window, and the two new needs authored in
Steps 2 and 3.

Sanity-check the artefacts
^^^^^^^^^^^^^^^^^^^^^^^^^^

The two RST blocks emitted by Steps 2 and 3 paste directly under
``docs/automotive-adas/``. Re-run the build and the ubc check to
confirm both still pass:

.. code-block:: bash

   uv run sphinx-build -W -b html docs docs/_build/html
   ubc check docs

Both commands should report success with the new needs included.

Tailoring layer
---------------

The files under ``.pharaoh/project/`` are intentionally human-readable
so that they can be hand-tuned. Key entry points:

* ``workflows.yaml``: change the allowed lifecycle states or add a
  ``deprecated`` terminal state.
* ``artefact-catalog.yaml``: promote a field from optional to
  required, or add a project-specific link option (for example
  ``mitigates`` for safety goals) to a type's ``required_fields``.
* ``checklists/<type>.md``: edit the review questions consumed by
  the per-type review skills.
* ``id-conventions.yaml``: tighten or relax the ID regex once the
  ID-policy collisions in the project's own ``[[needs.types]]`` are
  resolved.

Re-run ``@pharaoh.tailor-detect`` once the catalogue grows past a
few dozen new needs to refresh the inferred conventions.
