{% set page="variants.rst" %}
{% include "demo_page_header.rst" with context %}

🔀 Variant Management
=====================

This page is a small, self-contained example of **variant management** with
Sphinx-Needs. The ADAS platform ships against **two orthogonal dimensions** and
keeps **one** set of requirements that resolves per build — the classic "150%
model" from which each build selects its "100%":

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Dimension
     - Values
     - Meaning
   * - ``location``
     - ``eu`` · ``uk`` · ``asia``
     - Target market. ``eu`` is the reference (the untagged default).
   * - ``type``
     - ``combi`` · ``cabrio`` · ``motorcycle``
     - Vehicle body type. ``combi`` is the default.

The benefit: a single requirement is the source of truth. There is no duplicated
per-market or per-body copy that can drift apart. Which ``location`` **and**
which vehicle ``type`` a build targets is chosen **at build time** with Sphinx
*build tags*, not stored on the need.

How it works
------------

The variants are configured in ``ubproject.toml`` against ``build_tags`` — the
set of tags passed to ``sphinx-build`` via ``-t``. Each dimension is just a set
of tag tests, and combinations are expressed as boolean tests over the same tags:

.. code-block:: toml

   [needs.fields.status]
   parse_variants = true

   [needs.variants]
   # location dimension
   eu   = "'eu' in build_tags"
   uk   = "'uk' in build_tags"
   asia = "'asia' in build_tags"
   # vehicle type dimension
   combi      = "'combi' in build_tags"
   cabrio     = "'cabrio' in build_tags"
   motorcycle = "'motorcycle' in build_tags"
   # collapsed calibration profiles (location x type)
   uk_car        = "'uk' in build_tags and 'motorcycle' not in build_tags"
   asia_cabrio   = "'asia' in build_tags and 'cabrio' in build_tags"
   # ... (see ubproject.toml for the full set)

Because ``status`` has ``parse_variants = true``, its value may contain a
``<<...>>`` variant expression. Each entry is ``<key or filter>: <value>``; the
first match wins, and the final comma-separated entry is the fallback when no
variant matches.

A build combines one tag from each dimension, producing that build's document:

.. code-block:: bash

   # Reference document: EU / combi (an untagged build resolves here too)
   uv run sphinx-build -b html -t eu -t combi . _build/html-eu-combi

   # UK / cabrio — identical source, different resolved values
   uv run sphinx-build -b html -t uk -t cabrio . _build/html-uk-cabrio

   # ASIA / motorcycle
   uv run sphinx-build -b html -t asia -t motorcycle . _build/html-asia-motorcycle

A plain build with no ``-t`` flag resolves to the reference point
(``location = eu``, ``type = combi``).

One requirement, one dimension
------------------------------

The simplest case keys a field on a **single** dimension. This requirement's
``status`` resolves from the active ``location`` only:

.. req:: Lane Keeping calibration
   :id: REQ_VAR_001
   :status: <<uk: in progress, asia: closed, open>>
   :links: NEED_001
   :release: REL_ADAS_2025_6
   :author: PETER

   Lane keeping assistance calibration. Type approval is further along in the
   ASIA market (``closed``) than in the UK (``in progress``); the EU reference
   market — and any untagged build — shows ``open``. Only ``location`` matters
   here; the vehicle ``type`` does not change this field.

Likewise, a field can key on the **other** dimension alone. This requirement's
``status`` depends only on the vehicle ``type``:

.. req:: Rider Assist calibration
   :id: REQ_VAR_002
   :status: <<motorcycle: in progress, cabrio: closed, open>>
   :links: NEED_003
   :release: REL_ADAS_2025_12
   :author: ROBERT

   For a ``motorcycle`` build the rider-assist calibration is still
   ``in progress``; a ``cabrio`` build is already ``closed``; every other body
   type (``combi``, the default) falls back to ``open``. Here only ``type``
   matters, independent of the market.

Requirements defined by a combination
--------------------------------------

The interesting case is when a value depends on **both** dimensions at once. The
two dimensions give 3 × 3 = 9 combinations, but we do **not** need 9 distinct
outcomes. They collapse to **7 calibration profiles**:

.. list-table:: location × type → calibration profile
   :header-rows: 1
   :stub-columns: 1
   :widths: 16 28 28 28

   * -
     - ``combi``
     - ``cabrio``
     - ``motorcycle``
   * - ``eu``
     - ``eu_car``
     - ``eu_car``
     - ``eu_motorcycle``
   * - ``uk``
     - ``uk_car``
     - ``uk_car``
     - ``uk_motorcycle``
   * - ``asia``
     - ``asia_combi``
     - ``asia_cabrio``
     - ``asia_motorcycle``

For **EU** and **UK**, ``combi`` and ``cabrio`` share a single ``*_car`` profile
and only ``motorcycle`` diverges. For **ASIA**, all three body types stay
distinct. Two real requirements in the
:doc:`Software Requirements <swe_1_sw_req_analysis>` chapter,
:need:`SWREQ_002` (*Lane Deviation Warning*) and :need:`SWREQ_005`
(*Speed Control Integration*), keep a single shared requirement text but resolve
a profile-specific calibration through their ``tuning`` field, e.g.

.. code-block:: rst

   :tuning: <<uk_car: 0.3 m, uk_motorcycle: 0.2 m, eu_motorcycle: 0.25 m,
             asia_combi: 0.5 m, asia_cabrio: 0.55 m, asia_motorcycle: 0.35 m, 0.4 m>>

The profile keys are ordinary variant expressions over ``build_tags`` (see
``[needs.variants]`` in ``ubproject.toml``); the trailing ``0.4 m`` is the
``eu_car`` reference fallback, also used by an untagged build.

Visualizing the resolved variants
---------------------------------

The table below lists the variant requirements with their resolved ``status``.
Rebuild with a different ``-t <location> -t <type>`` pair to see the values
change.

.. needtable::
   :filter: id in ['REQ_VAR_001', 'REQ_VAR_002']
   :columns: id, title, status
   :style: table

From shared requirements to per-profile code
--------------------------------------------

Variants are not limited to field values on a single need — the same idea scales
all the way down to the *implementation*. When the difference is only a value,
the ``tuning`` field is enough. When the difference reaches the *code*, each
calibration profile gets its own implementation file that links back to the
shared requirement via sphinx-codelinks. Seven calibration files exist side by
side — one per profile in the table above:

.. code-block:: text

   src/c/calibration_eu_car.c          ->  IMPL_LKA_DEVIATION_CAL_EU_CAR,          IMPL_ACC_SPEED_CAL_EU_CAR
   src/c/calibration_eu_motorcycle.c   ->  IMPL_LKA_DEVIATION_CAL_EU_MOTORCYCLE,   IMPL_ACC_SPEED_CAL_EU_MOTORCYCLE
   src/c/calibration_uk_car.c          ->  IMPL_LKA_DEVIATION_CAL_UK_CAR,          IMPL_ACC_SPEED_CAL_UK_CAR
   src/c/calibration_uk_motorcycle.c   ->  IMPL_LKA_DEVIATION_CAL_UK_MOTORCYCLE,   IMPL_ACC_SPEED_CAL_UK_MOTORCYCLE
   src/c/calibration_asia_combi.c      ->  IMPL_LKA_DEVIATION_CAL_ASIA_COMBI,      IMPL_ACC_SPEED_CAL_ASIA_COMBI
   src/c/calibration_asia_cabrio.c     ->  IMPL_LKA_DEVIATION_CAL_ASIA_CABRIO,     IMPL_ACC_SPEED_CAL_ASIA_CABRIO
   src/c/calibration_asia_motorcycle.c ->  IMPL_LKA_DEVIATION_CAL_ASIA_MOTORCYCLE, IMPL_ACC_SPEED_CAL_ASIA_MOTORCYCLE

Each file declares an ``impl`` need with a one-line codelink comment that points
*upward* to the requirement it realises — the conventional code-to-requirement
direction:

.. code-block:: c

   // @ Lane deviation warning - UK passenger car calibration (0.3 m), IMPL_LKA_DEVIATION_CAL_UK_CAR, impl, [SWREQ_002]

Two settings make this variant-aware:

#. The project-wide scan in ``ubproject.toml`` excludes the calibration files
   (``exclude = ["calibration_*.c"]``), so they never all show up at once.
#. The :doc:`SWE.3 detailed design <swe_3_sw_detailed_design>` page traces only
   the active profile's file. ``conf.py`` collapses the two build tags into the
   ``profile`` value and exposes it to the page templating:

   .. code-block:: rst

      {% raw %}.. src-trace::
         :project: adas
         :file: calibration_{{ profile }}.c{% endraw %}

As a result, a ``-t uk -t combi`` (or ``-t uk -t cabrio``) build shows **only**
``IMPL_LKA_DEVIATION_CAL_UK_CAR`` and ``IMPL_ACC_SPEED_CAL_UK_CAR`` and links
them to :need:`SWREQ_002` / :need:`SWREQ_005`; every other profile's calibration
is neither traced nor linked. Switching either build tag swaps the
implementation that satisfies the shared requirement.

When to use this pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~

This layering suits a product line that wants to **reuse as much as possible**
and only diverge where it must:

- **Shared at the top.** High-level and system requirements stay common to every
  location and vehicle type — a single source of truth, with no copies to keep
  in sync.
- **Fork late, stay mostly shared.** Where a build genuinely differs, fork into
  variant requirements that are *still mostly reused*: the same need, with only
  the variant-specific field (``status``, ``tuning``, …) resolving differently
  per dimension — or per *combination* of dimensions.
- **Collapse combinations that do not really differ.** Nine cells do not mean
  nine outcomes: EU and UK cars behave identically across ``combi`` and
  ``cabrio``, so they share one profile. Only model the distinctions that exist.
- **Escalate to different code only when unavoidable.** When the divergence can
  no longer be expressed as a value and the implementations truly differ, point
  each profile at its own implementation — a separate file as shown here, or,
  taken further, a different branch or even a different repository — while the
  requirement above it stays shared. Traceability still resolves to exactly one
  implementation per build, so every document remains complete and
  self-consistent.

.. note::

   **Showcasing variants in ubTrace.** ubTrace is a Sphinx builder, so the same
   build tags apply. Its structural data model is *organization → project →
   version*, and variants are **not** versions or projects — they are an
   orthogonal classification. ubTrace models exactly this with
   `dimensions <https://ubtrace.useblocks.com/dev/usage/configuration.html#ubtrace-dimensions>`__:
   free-form key/value labels attached to a build. ``conf.py`` publishes **both**
   axes as dimensions from the active build tags, while ``project`` and
   ``version`` stay single (``sphinx-needs-demo`` / ``main``):

   .. code-block:: python

      # location axis
      if tags.has("uk"):
         _location = "uk"
      elif tags.has("asia"):
         _location = "asia"
      else:
         _location = "eu"     # reference market (also the untagged default)

      # vehicle type axis
      if tags.has("cabrio"):
         _type = "cabrio"
      elif tags.has("motorcycle"):
         _type = "motorcycle"
      else:
         _type = "combi"      # default body type

      ubtrace_dimensions = {"location": _location, "type": _type}

   Because ubTrace stores one dataset per *version*, each combination is folded
   into its own version id (``eu``/``combi`` → ``main``, otherwise
   ``main-<location>-<type>``) so they coexist. Build every combination at once:

   .. code-block:: bash

      make ubtrace-all   # -> _build/ubtrace-<location>-<type>  (9 combinations)

   The emitted ``config/ubtrace_project.toml`` records both labels under
   ``[ubtrace.dimensions]``:

   .. code-block:: toml

      [ubtrace.dimensions]
      location = "uk"
      type = "cabrio"

   Because every combination shares the same *organization → project → version*
   root, the **dimensions** — not the directories — are what keep them apart once
   ingested into ubTrace. The version switcher stays clean for real product
   versions, and builds can be filtered and compared independently by their
   ``location`` **or** ``type`` dimension.
