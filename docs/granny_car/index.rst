{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}

🚘 Granny Car
=============
.. team:: Granny Car
   :id: GRANNY 
   :persons: PETER, ALFRED, THOMAS
   :image: docs/_images/granny_car.jpg
   :layout: clean_l

   Introducing the "Granny Glide," a specially designed car catering to the needs of elderly drivers. 
   With plush, ergonomic seating, easy-to-reach controls, and assisted steering, it offers comfort and 
   convenience. Safety features include automatic braking and adjustable speed limits. The Granny Glide 
   ensures a smooth and secure ride for seniors, prioritizing their comfort and safety.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements


Traceability objects
--------------------


.. needtable::
   :filter: id.startswith("GRANNY")
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
   :filter: "GRANNY" in persons_back