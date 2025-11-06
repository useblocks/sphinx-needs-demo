{% set page="analysis.rst" %}
{% include "demo_page_header.rst" with context %}

📊 Analysis
===========

Overview
--------

.. needtable::
   :filter: c.this_doc()
   :columns: id, title, type, status, author

.. tip::
   :title: Big picture
   :collapsible:

   .. needflow::
      :filter: c.this_doc()

ADAS Objects
------------

.. grid:: 2

   .. grid-item::

      .. needpie:: Object Types of ADAS project
         :labels: need, req, arch, swreq, swarch, test, impl

         docname is not None and "automotive-adas" in docname and type=="need"
         docname is not None and "automotive-adas" in docname and type=="req"
         docname is not None and "automotive-adas" in docname and type=="arch"
         docname is not None and "automotive-adas" in docname and type=="swreq"
         docname is not None and "automotive-adas" in docname and type=="swarch"
         docname is not None and "automotive-adas" in docname and type=="test"
         docname is not None and "automotive-adas" in docname and type=="impl"

   .. grid-item::

      .. needpie:: Object status of ADAS project
         :labels: open, closed

         docname is not None and "automotive-adas" in docname and status=="open"
         docname is not None and "automotive-adas" in docname and status=="closed"

.. needbar:: Object authors
   :legend:
   :xlabels: FROM_DATA
   :ylabels: FROM_DATA
   :show_sum:
   :show_top_sum:
   :stacked:

   , Peter, Steven, Sarah, Thomas
   SW Reqs, docname is not None and "automotive-adas" in docname and "PETER" in author and type=="swreq", docname is not None and "automotive-adas" in docname and "STEVEN" in author and type=="swreq", docname is not None and "automotive-adas" in docname and "SARAH" in author  and type=="swreq", docname is not None and "automotive-adas" in docname and "THOMAS" in author and type=="swreq"
   SW Arch, docname is not None and "automotive-adas" in docname and "PETER" in author and type=="swarch", docname is not None and "automotive-adas" in docname and "STEVEN" in author and type=="swarch", docname is not None and "automotive-adas" in docname and "SARAH" in author  and type=="swarch", docname is not None and "automotive-adas" in docname and "THOMAS" in author and type=="swarch"
   Tests, docname is not None and "automotive-adas" in docname and "PETER" in author and type=="test", docname is not None and "automotive-adas" in docname and "STEVEN" in author and type=="test", docname is not None and "automotive-adas" in docname and "SARAH" in author  and type=="test", docname is not None and "automotive-adas" in docname and "THOMAS" in author and type=="test"

SWE Implementation
------------------

.. needflow::
   :filter: c.this_doc() and type in ["swreq", "swarch", "impl"]
