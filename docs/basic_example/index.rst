{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}


🧰 Basic Example
================

Sphinx-Needs objects
--------------------

.. req:: Example Requirement
   :id: EX_REQ_001
   :tags: security
   :status: open

   A simple requirement used as example.
   The content supports all kind of Sphinx features, like:

   **Bold** or *italic* text
   
   Web links, like this `google <https://google.com>`__ link.
   
   Or even images: 

   .. image:: /_images/sphinx-needs-logo.png
      :width: 50px

.. spec:: Example Specification
   :id: EX_SPEC_001
   :links: EX_REQ_001
   :tags: security, safety
   :status: closed

   
   But also features from integated Sphinx exentions can be used, like this PlantUML generated image from this code

   .. grid:: 2

      .. grid-item::

         .. code-block:: rst

            .. uml::
            
               node A
               node B
               A --> B
   
      .. grid-item::

         .. uml::
            
               node A
               node B
               A --> B


.. test:: Example Test case
   :id: EX_TEST_001
   :links: EX_SPEC_001
   :status: passed

   And for sure also all features from Sphinx-Needs, like this needflow:

   .. needflow::
      :filter: "basic_example" in docname

Sphinx-Needs filtering
----------------------

.. code-block:: rst

   .. needtable::
      :filter: "basic_example" in docname

.. needtable::
      :filter: "basic_example" in docname


.. code-block:: rst

   .. needflow::
      :filter: "basic_example" in docname

.. needflow::
      :filter: "basic_example" in docname


Sphinx-Needs debuging
---------------------

A Sphinx-Needs object using the ``debug`` layout to show all set and internal values, which can also be used in all filter strings.

Sphinx-Needs collect and assigns a lot of data automatically for the specific needs, like their location or the headlines, under which
it is presented.

.. req:: Example Requirement with debug view
   :id: EX_REQ_002
   :status: open
   :tags: debug
   :layout: debug

   Some content   