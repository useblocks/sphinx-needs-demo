{% set page="demo_details.rst" %}
{% include "demo_page_header.rst" with context %}

🔍 Demo details
===============
This page gives some details about extensions, configurations and other important files, which are used
across the demo projects of this repository.

This landing project (the one rendering this very page) is intentionally minimal — it has no
Sphinx-Needs objects of its own. Each of the four demonstration projects
(:doc:`basic_example <basic_example:index>`, :doc:`coffee-machine <coffee-machine:index>`,
:doc:`automotive-adas <automotive-adas:index>` and :doc:`safety_example <safety_example:index>`)
is a fully independent Sphinx project with its own ``conf.py``/``ubproject.toml`` and only turns on
the extensions it actually needs. The ``automotive-adas`` project uses the widest set, so it is used
as the example below.

Extensions
----------

:`Sphinx-Needs <https://sphinx-needs.readthedocs.io>`__:
    Used to create and link objects in the documentation, mainly requirements, specifications and tests.
    Provides also features to filter and represent the objects in tables and flow charts.

:`Sphinx-Test-Reports <https://sphinx-test-reports.readthedocs.io>`__:
    Loads test-results/runs into a Sphinx project, by reading a junit-based result file.
    Is based on top of Sphinx-Needs.

:`Sphinx-Design <https://sphinx-design.readthedocs.io>`__:
    Provides features to layout the content or to use dropdown, buttons or tabs.

:`Furo <https://pradyunsg.me/furo/>`__:
    The Sphinx theme for this documentation.

:`Sphinxcontrib-PlantUML <https://github.com/sphinx-contrib/plantuml>`__:
    Allows to use `PlantUML <https://plantuml.com/>`__ inside a Sphinx project. Used to create all kinds of diagrams.
    Also Sphinx-Needs features like ``needflow`` are based on it.

:`Sphinx-SimplePDF <https://sphinx-simplepdf.readthedocs.io/>`__:
    Provides a Sphinx builder to create a beautiful PDF out of the documentation.

:`Sphinx-Preview <https://sphinx-preview.readthedocs.io>`__:
    Allows you to get a quick preview of a link without leaving the page.
    Especially useful for getting a quick impression of linked Sphinx-Needs objects.

Configurations
--------------

pyproject.toml
~~~~~~~~~~~~~~
Used to specify project metadata and install all needed packages for the used Python environment.

The file will be consumed when calling::

    pip install .

or::

    uv sync

conf.py
~~~~~~~
The configuration file of the ``automotive-adas`` project, the demo project using the
widest set of extensions (Sphinx-Needs, sphinx-codelinks, PlantUML, Sphinx-Test-Reports,
Sphinx-SimplePDF, autodoc/viewcode, variant builds and the ubtrace uploader).

This landing project's own ``conf.py`` is much smaller, since it has no Sphinx-Needs
objects to configure.

Details are explained as comments in the file itself.

.. literalinclude:: automotive-adas/conf.py
   :language: python
   :linenos:

Templates
---------

all_post
~~~~~~~~
Adds the "Object traceability details" under each object.

.. literalinclude:: needs_templates/all_post.need
   :language: rst
   :linenos:

Includes
--------

demo_page_header
~~~~~~~~~~~~~~~~

This is used to add the "Demo page details" on top of each page.

.. literalinclude:: demo_page_header.rst
   :language: rst
   :linenos:
