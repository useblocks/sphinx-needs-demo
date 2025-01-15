{% set page="analysis.rst" %}
{% include "demo_page_header.rst" with context %}

📊 Analysis
===========

Overview
--------

.. needtable::
   :filter: "automotive-adas" in docname
   :columns: id, title, type, status, author

.. tip:: 
   :title: Big picture
   :collapsible:

   .. needflow::
      :filter: "automotive-adas" in docname

ADAS Objects
------------

.. grid:: 2

   .. grid-item::

      .. needpie:: Object Types of ADAS project
         :labels: need, req, arch, swreq, swarch, test, impl

         "automotive-adas" in docname and type=="need"
         "automotive-adas" in docname and type=="req"
         "automotive-adas" in docname and type=="arch"
         "automotive-adas" in docname and type=="swreq"
         "automotive-adas" in docname and type=="swarch"
         "automotive-adas" in docname and type=="test"
         "automotive-adas" in docname and type=="impl"

   .. grid-item::

      .. needpie:: Object status of ADAS project
         :labels: open, closed

         "automotive-adas" in docname and status=="open"
         "automotive-adas" in docname and status=="closed"

.. needbar:: Object authors
   :legend:
   :xlabels: FROM_DATA
   :ylabels: FROM_DATA
   :show_sum:
   :show_top_sum:
   :stacked:

   , Peter, Steven, Sarah, Thomas
   SW Reqs, "automotive-adas" in docname and "PETER" in author and type=="swreq", "automotive-adas" in docname and "STEVEN" in author and type=="swreq", "automotive-adas" in docname and "SARAH" in author  and type=="swreq", "automotive-adas" in docname and "THOMAS" in author and type=="swreq"
   SW Arch, "automotive-adas" in docname and "PETER" in author and type=="swarch", "automotive-adas" in docname and "STEVEN" in author and type=="swarch", "automotive-adas" in docname and "SARAH" in author  and type=="swarch", "automotive-adas" in docname and "THOMAS" in author and type=="swarch"
   Tests, "automotive-adas" in docname and "PETER" in author and type=="test", "automotive-adas" in docname and "STEVEN" in author and type=="test", "automotive-adas" in docname and "SARAH" in author  and type=="test", "automotive-adas" in docname and "THOMAS" in author and type=="test"

SWE Implementation
------------------

.. needflow::
   :filter: "automotive-adas" in docname and type in ["swreq", "swarch", "impl"]

