{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}

🗃 Base Car
===========

.. team:: Base Car
   :id: BASE
   :persons: PETER, ROBERT, SARAH, THOMAS
   :image: docs/_images/base_car.jpg
   :layout: clean_l


   A "Base Car" serves as the foundation for other vehicles, providing essential structural support and 
   components. It lacks external features like body panels and interior fittings but is crucial for 
   prototyping and testing new automotive designs.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements
   releases

Traceability objects
--------------------


.. needtable::
   :filter: id.startswith("BASE")
   :columns: id, title, type, release, author


Involved persons
----------------
.. tip::
   :title: Demo feature hint
   :collapsible:

   The below list is auto-generated based on the links in the ``persons`` option of the above ``team`` object.

   Code for this::

      .. needextract::
         :filter: "GRANNY" in persons_back 

.. needextract::
   :filter: "BASE" in persons_back