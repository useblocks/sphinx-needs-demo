{% set page="analysis.rst" %}
{% include "demo_page_header.rst" with context %}

📊 Analysis
===========
.. grid:: 1 1 2 3

      .. grid-item::

         **Base Car types**

         .. needpie::
            :labels: req, spec, impl, test, testrun 

            "base_car" in docname and type=="req" 
            "base_car" in docname and type=="spec" 
            "base_car" in docname and type=="impl" 
            "base_car" in docname and type=="test" 
            "base_car" in docname and type=="testrun" 

      .. grid-item::

         **Teen Car types**
         
         .. needpie::
            :labels: req, spec, impl, test, testrun 

            "teen_car" in docname and type=="req" 
            "teen_car" in docname and type=="spec" 
            "teen_car" in docname and type=="impl" 
            "teen_car" in docname and type=="test" 
            "teen_car" in docname and type=="testrun" 

      .. grid-item::

         **Granny Car types**
         
         .. needpie::
            :labels: req, spec, impl, test, testrun 

            "granny_car" in docname and type=="req" 
            "granny_car" in docname and type=="spec" 
            "granny_car" in docname and type=="impl" 
            "granny_car" in docname and type=="test" 
            "granny_car" in docname and type=="testrun" 


      .. grid-item::

         **Base Car Status**

         .. needpie::
            :labels: open, in progress, closed, None

            "base_car" in docname and status=="open"
            "base_car" in docname and status=="in progress"
            "base_car" in docname and status=="closed"
            "base_car" in docname and (status is None or status=="")

      .. grid-item::

         **Teen Car Status**

         .. needpie::
            :labels: open, in progress, closed, None

            "teen_car" in docname and status=="open"
            "teen_car" in docname and status=="in progress"
            "teen_car" in docname and status=="closed"
            "teen_car" in docname and (status is None or status=="")

      .. grid-item::

         **Granny Car Status**

         .. needpie::
            :labels: open, in progress, closed, None

            "granny_car" in docname and status=="open"
            "granny_car" in docname and status=="in progress"
            "granny_car" in docname and status=="closed"
            "granny_car" in docname and (status is None or status=="")
            

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 20 30 30 20
   :align: center

   - * Filter 
     * Base Car
     * Teen Car
     * Granny Car
   - * Reqs
     * :need_count:`"base_car" in docname and type=="req"` 
     * :need_count:`"teen_car" in docname and type=="req"` 
     * :need_count:`"granny_car" in docname and type=="req"` 
   - * Specs
     * :need_count:`"base_car" in docname and type=="spec"` 
     * :need_count:`"teen_car" in docname and type=="spec"` 
     * :need_count:`"granny_car" in docname and type=="spec"`
   - * Test Cases
     * :need_count:`"base_car" in docname and type=="test"` 
     * :need_count:`"teen_car" in docname and type=="test"` 
     * :need_count:`"granny_car" in docname and type=="test"`  
   - * Test Runs
     * :need_count:`"base_car" in docname and type=="testrun"` 
     * :need_count:`"teen_car" in docname and type=="testrun"` 
     * :need_count:`"granny_car" in docname and type=="testrun"` 


Requirement links
-----------------

.. needflow::
   :filter: type in ["req"]