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
