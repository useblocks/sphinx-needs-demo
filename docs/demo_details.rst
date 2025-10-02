{% set page="demo_details.rst" %}
{% include "demo_page_header.rst" with context %}

🔍 Demo details
===============
This page gives some details about extensions, configurations and other important files, which were used
to define this documentation project.


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

:`Sphinx-Immaterial <https://jbms.github.io/sphinx-immaterial/>`__:
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
The whole configuration file of this project.

Details are explained as comments in the file itself.

.. literalinclude:: conf.py
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
