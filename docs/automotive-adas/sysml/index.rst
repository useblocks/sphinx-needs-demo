{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SysML_Demo:

🧩 SysML diagrams via Gaphor
=============================

This page demonstrates how `Gaphor <https://gaphor.org/>`__ models can be
embedded inside Sphinx-Needs alongside the existing ``.. uml::`` PlantUML
directives. Gaphor implements a large part of the OMG **SysML 1.6**
specification (a minor revision of SysML 1.5 that retains the same core
constructs — Block, Property, Port, Connector, Requirement). For a customer
showcase that says "SysML 1.5", Gaphor is the same modeling family.

How it works
------------

Three pieces are needed:

1. **A** ``.gaphor`` **model file** — an XML document that holds blocks,
   properties, ports, diagrams and their layout. It can be authored in the
   Gaphor desktop GUI or programmatically through the Gaphor Python API
   (see :file:`author_adas_bdd.py` for an example).
2. **The** ``gaphor.extensions.sphinx`` **extension** — registers a
   ``.. diagram::`` directive and renders the chosen diagram to SVG/PDF
   on every Sphinx build.
3. **A** ``gaphor_models`` **mapping in** :file:`conf.py` — maps logical
   model names (``"tsr"``, ``"car"``, ...) to ``.gaphor`` files relative
   to ``docs/``.

Example: under :need:`ARCH_007` the BDD lives next to a PlantUML view of the
same architecture and is rendered from the model file by:

.. code:: rst

   .. diagram:: TSR Block Definition
      :model: tsr
      :align: center

The directive accepts the standard ``image``/``figure`` options
(``:align:``, ``:figwidth:``, ``:alt:``, plus a caption block).

Using a stock Gaphor SysML example
----------------------------------

The ``car`` model below is the un-modified ``sysml-car.gaphor`` example
from the Gaphor distribution, demonstrating that an existing ``.gaphor``
file can be dropped into the docs tree and referenced verbatim.

.. diagram:: main
   :model: car
   :align: center
   :alt: SysML Block Definition Diagram of a Car

   ``Car`` block from Gaphor's ``examples/sysml-car.gaphor``, decomposed
   into ``rear: Wheel[2]``, ``: Engine`` and two ``axle`` proxy ports.

Programmatic authoring
----------------------

For repeatable, code-reviewable models we generate ``adas-tsr-bdd.gaphor``
from a small Python script using Gaphor's API:

.. code:: console

   uv run python docs/automotive-adas/sysml/author_adas_bdd.py

The script creates a ``Package``, four ``Block`` elements, three
composite ``Property`` parts and a ``BlockDefinitionDiagram`` with the
items laid out, then ``storage.save()`` writes the XML. Re-running the
script regenerates the file deterministically.

Converting existing SysML 1.5 XMI
---------------------------------

A common customer ask is *"we already have SysML 1.5 XMI files from
Cameo/Papyrus/MagicDraw — can we just drop them in?"*. Today the
honest answer is **no, not directly**:

- Gaphor's own XMI export was removed in `Gaphor 3.1.0
  <https://github.com/gaphor/gaphor/pull/3444>`__ after the maintainers
  declared it under-tested and unmaintained.
- The ``.gaphor`` format is **not** XMI. It is a Gaphor-native XML schema
  (root ``<gaphor>`` namespaced under
  ``https://gaphor.org/model``) that mixes semantic elements
  (``<UML:Package>``, ``<SysML:Block>``, ``<UML:Property>``, ...) with
  per-diagram presentation items (``<SysML:BlockItem>`` carrying a
  transformation matrix, width and height).
- Conversion therefore requires a custom XMI → ``.gaphor`` translator
  that walks the source tree, generates UUIDs, maps element types and
  rebuilds layout. There is no off-the-shelf tool today.

The pragmatic options for a project that needs SysML 1.5 content in the
docs are:

1. **Re-author** the diagrams in Gaphor (GUI) or via the Python API
   shown above — fastest for a small, curated set of system views that
   matter for the documentation.
2. **Write a converter** — feasible for a constrained SysML 1.5
   subset (Blocks, Properties, BDDs, simple Connectors). The ``.gaphor``
   file format is documented at
   https://docs.gaphor.org/en/latest/storage.html and only ~10 element
   types are needed for a typical BDD.
3. **Keep the original tool** for full-fidelity authoring and only
   import a curated subset into Gaphor for publication.

Limitations to be aware of
--------------------------

- The Gaphor Sphinx extension renders SVG **and** PDF for each diagram.
  Rendering uses Cairo via PyGObject, so the build host needs the GTK
  girepository / Cairo system packages. See ``.readthedocs.yaml`` for
  the apt list.
- With Gaphor installed, matplotlib auto-selects the ``gtk4agg``
  backend, which hangs the build on a headless host. ``conf.py`` pins
  ``matplotlib.use("Agg")`` before any extension imports it.
- ``gaphor`` is a heavy dependency (it pulls in ``pycairo`` and
  ``PyGObject``). If only a few pages need it, consider extracting the
  SysML pages into an opt-in toctree.
