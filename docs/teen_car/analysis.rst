{% set page="analysis.rst" %}
{% include "demo_page_header.rst" with context %}

📊 Analysis Teen
================

Project overview
----------------

.. needtable::
   :filter: "teen_car" in docname
   :columns: id, title, type, status, author 


.. needpie:: Object Types of Teen Car project
   :labels: req, spec, impl, test, testrun 

   "teen_car" in docname and type=="req" 
   "teen_car" in docname and type=="spec" 
   "teen_car" in docname and type=="impl" 
   "teen_car" in docname and type=="test" 
   "teen_car" in docname and type=="testrun" 


.. needbar:: A more real bar chart
   :legend:
   :xlabels: FROM_DATA
   :ylabels: FROM_DATA
   :show_sum:
   :show_top_sum:
   :stacked:

                    , open                                                                  , in progress                                                                   , closed
   Requirements     , "teen_car" in docname and type=="req" and status=="open"              , "teen_car" in docname and type=="req" and status=="in progress"               , "teen_car" in docname and type=="req" and status=="closed" 
   Specifications   , "teen_car" in docname and type=="spec" and status=="open"             , "teen_car" in docname and type=="spec" and status=="in progress"              , "teen_car" in docname and type=="spec" and status=="closed" 
   Test Cases       , "teen_car" in docname and type=="test" and status=="open" and is_need , "teen_car" in docname and type=="test" and status=="in progress" and is_need  , "teen_car" in docname and type=="test" and status=="closed" and is_need

Tests
-----

Failed test runs
~~~~~~~~~~~~~~~~

.. needtable::
   :filter: "teen_car" in docname and type=="testrun"  and result=="failure"
   :columns: id, title, result, runs_back as "Test Cases"



⚠ Data problems
----------------

No status
~~~~~~~~~
Requirements, Specifications, or Test cases without a status.

.. needtable::
   :filter: type in ["req", "spec", "test"] and (status == "" or status is None)
   :style: table
   :columns: id, title, status, author


Tests without specs
~~~~~~~~~~~~~~~~~~~
Test cases without a link to a specification.

.. needtable::
   :filter: type in ["test"] and len(specs)==0
   :style: table
   :columns: id, title, specs, author