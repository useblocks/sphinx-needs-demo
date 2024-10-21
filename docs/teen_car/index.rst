{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}

.. _teen_car:

🚗 Teen Car
===========

.. team:: Teen Car
   :id: TEEN
   :persons: PETER, ALFRED, ROBERT, STEVEN, THOMAS
   :image: _images/teen_car.jpg
   :layout: clean_l

   Presenting the "TeenTrek," an autonomous driving car tailored for teenagers without a driving license. 
   Equipped with advanced AI navigation and safety protocols, it ensures effortless and secure 
   transportation. The interior boasts entertainment systems, study areas, and social hubs, catering to 
   teen preferences. The TeenTrek fosters independence while prioritizing safety and convenience 
   for young passengers.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   requirements
   architecture
   specifications
   test_cases
   test_runs
   releases
   api
   analysis

Traceability objects
--------------------


.. needtable::
   :filter: id.startswith("TEEN")
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
   :filter: "TEEN" in persons_back
   :layout: complete