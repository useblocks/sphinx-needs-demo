{% set page="variants.rst" %}
{% include "demo_page_header.rst" with context %}

🔀 Variant Management
=====================

This page is a small, self-contained example of **variant management** with
Sphinx-Needs. The ADAS platform is delivered to two customers that share **one**
set of requirements but need slightly different field values per build — the
classic "150% model" from which each customer build selects its "100%".

The benefit: a single requirement is the source of truth. There is no duplicated
``Customer A`` / ``Customer B`` copy that can drift apart. Which customer a build
targets is chosen **at build time** with a Sphinx *build tag*, not stored on the
need.

How it works
------------

The variants are configured in ``ubproject.toml`` against ``build_tags`` — the
set of tags passed to ``sphinx-build`` via ``-t``:

.. code-block:: toml

   [needs.fields.status]
   parse_variants = true

   [needs.variants]
   customer_a = "'customer_a' in build_tags"
   customer_b = "'customer_b' in build_tags"

Because ``status`` has ``parse_variants = true``, its value may contain a
``<<...>>`` variant expression. Each entry is ``<key or filter>: <value>``; the
first match wins, and the final comma-separated entry is the fallback when no
variant is active.

The same source, built twice, produces two customer documents:

.. code-block:: bash

   # Customer A document
   uv run sphinx-build -b html -t customer_a . _build/html-a

   # Customer B document — identical source, different resolved values
   uv run sphinx-build -b html -t customer_b . _build/html-b

A plain build with no ``-t`` flag resolves every variant to its fallback value.

One requirement, two variants
-----------------------------

This single requirement is shared by both customers. Its ``status`` resolves
from whichever build tag is active — no ``customer`` field is hardcoded on the
need.

.. req:: Lane Keeping calibration
   :id: REQ_VAR_001
   :status: <<customer_a: in progress, customer_b: closed, open>>
   :links: NEED_001
   :release: REL_ADAS_2025_6
   :author: PETER

   Lane keeping assistance calibration. The work is further along for
   Customer B (``closed``) than for Customer A (``in progress``); an untagged
   build shows the ``open`` fallback. The requirement text itself is identical
   for both customers — only the build-tracked ``status`` differs.

Inline filter variants
-----------------------

You do not have to pre-define a variant in ``ubproject.toml`` — an inline filter
expression in square brackets works directly inside the ``<<...>>`` block. This
is handy for a one-off, per-requirement distinction.

.. req:: Emergency Braking calibration
   :id: REQ_VAR_002
   :status: <<['customer_b' in build_tags]: closed, in progress>>
   :links: NEED_003
   :release: REL_ADAS_2025_12
   :author: ROBERT

   For the Customer B build the emergency braking calibration is already
   ``closed``; every other build falls back to ``in progress``.

Visualizing the resolved variants
---------------------------------

The table below lists the variant requirements with their resolved ``status``.
Rebuild with ``-t customer_a`` or ``-t customer_b`` to see the values change.

.. needtable::
   :filter: id in ['REQ_VAR_001', 'REQ_VAR_002']
   :columns: id, title, status
   :style: table

From shared requirements to per-customer code
---------------------------------------------

Variants are not limited to field values on a single need — the same idea scales
all the way down to the *implementation*. Two real requirements in the
:doc:`Software Requirements <swe_1_sw_req_analysis>` chapter,
:need:`SWREQ_002` (*Lane Deviation Warning*) and :need:`SWREQ_005`
(*Speed Control Integration*), keep a single shared requirement text but resolve
a customer-specific calibration through their ``tuning`` field, e.g.
``<<customer_a: 0.3 m, customer_b: 0.5 m, 0.4 m>>``.

When the difference is only a value, that ``tuning`` field is enough. When the
difference reaches the *code*, each customer gets its own implementation file
that links back to the shared requirement via sphinx-codelinks. Three
calibration files exist side by side:

.. code-block:: text

   src/c/calibration_base.c        ->  IMPL_LKA_DEVIATION_CAL_BASE, IMPL_ACC_SPEED_CAL_BASE
   src/c/calibration_customer_a.c  ->  IMPL_LKA_DEVIATION_CAL_A,    IMPL_ACC_SPEED_CAL_A
   src/c/calibration_customer_b.c  ->  IMPL_LKA_DEVIATION_CAL_B,    IMPL_ACC_SPEED_CAL_B

Each file declares an ``impl`` need with a one-line codelink comment that points
*upward* to the requirement it realises — the conventional code-to-requirement
direction:

.. code-block:: c

   // @ Lane deviation warning - Customer A calibration (0.3 m), IMPL_LKA_DEVIATION_CAL_A, impl, [SWREQ_002]

Two settings make this variant-aware:

#. The project-wide scan in ``ubproject.toml`` excludes the calibration files
   (``exclude = ["calibration_*.c"]``), so they never all show up at once.
#. The :doc:`SWE.3 detailed design <swe_3_sw_detailed_design>` page traces only
   the active variant's file, selected at build time from the ``variant`` value
   exposed to the page templating:

   .. code-block:: rst

      {% raw %}.. src-trace::
         :project: adas
         :file: calibration_{{ variant }}.c{% endraw %}

As a result, a ``customer_a`` build shows **only** ``IMPL_LKA_DEVIATION_CAL_A``
and ``IMPL_ACC_SPEED_CAL_A`` and links them to :need:`SWREQ_002` /
:need:`SWREQ_005`; the base and Customer B calibrations are neither traced nor
linked. Switching the build tag swaps the implementation that satisfies the
shared requirement.

When to use this pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~

This layering suits a product line that wants to **reuse as much as possible**
and only diverge where it must:

- **Shared at the top.** High-level and system requirements stay common to every
  customer — a single source of truth, with no copies to keep in sync.
- **Fork late, stay mostly shared.** Where a customer genuinely differs, fork
  into variant requirements that are *still mostly reused*: the same need, with
  only the variant-specific field (``status``, ``tuning``, …) resolving
  differently per build tag.
- **Escalate to different code only when unavoidable.** When the divergence can
  no longer be expressed as a value and the implementations truly differ, point
  each customer at its own implementation — a separate file as shown here, or,
  taken further, a different branch or even a different repository — while the
  requirement above it stays shared. Traceability still resolves to exactly one
  implementation per build, so every customer document remains complete and
  self-consistent.

.. note::

   **Showcasing variants in ubTrace.** ubTrace is a Sphinx builder, so the same
   build tags apply. Its structural data model is *organization → project →
   version*, and variants are **not** versions or projects — they are an
   orthogonal classification. ubTrace models exactly this with
   `dimensions <https://ubtrace.useblocks.com/dev/usage/configuration.html#ubtrace-dimensions>`__:
   free-form key/value labels attached to a build. ``conf.py`` sets a ``variant``
   dimension from the active build tag, while ``project`` and ``version`` stay
   single (``sphinx-needs-demo`` / ``main``):

   .. code-block:: python

      if tags.has("customer_b"):
         _variant = "customer_b"
      elif tags.has("customer_a"):
         _variant = "customer_a"
      else:
         _variant = "base"

      ubtrace_dimensions = {"variant": _variant}

   Each variant build is produced into its own output directory and carries its
   ``variant`` dimension:

   .. code-block:: bash

      make ubtrace-customer-a   # -> _build/ubtrace-customer_a  (variant = customer_a)
      make ubtrace-customer-b   # -> _build/ubtrace-customer_b  (variant = customer_b)

   The emitted ``config/ubtrace_project.toml`` records the label under
   ``[ubtrace.dimensions]``:

   .. code-block:: toml

      [ubtrace.dimensions]
      variant = "customer_a"

   Because every variant shares the same *organization → project → version*
   path, the dimension — not the directory — is what keeps them apart once
   ingested into ubTrace. The version switcher stays clean for real product
   versions, and builds can be filtered and compared by their ``variant``
   dimension instead.
