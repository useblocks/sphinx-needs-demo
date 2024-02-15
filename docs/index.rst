.. Sphinx-Needs Demo documentation master file, created by
   sphinx-quickstart on Mon Feb 12 16:32:39 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sphinx-Needs Demo
=================

This is a demo documentation for showing the features of `Sphinx-Needs <https://sphinx-needs.readthedocs.io/en/latest/>`__. 

.. image:: /_images/sphinx-needs-logo-bg.png
   :align: center
   :width: 75%


A simple Automotive SW project is used as playground, with elements for:

* Requirements
* Specifications
* Implementations
* Test Cases
* and Test Results

Architecture diagrams get described by PlantUML.

There are also Dashboard pages to show specific information for different process roles.

The complete source code can be found here: https://github.com/useblocks/sphinx-needs-demo

Features and technical details are described inside dropdowns like this one:

.. tip:: 
   :title: Demo feature hint: Just an example
   :collapsible:

   Really, this is just an example. Nothing more.


Demo Content
------------
Most of the need content was created using AI. Also most of the images were generated this way.

However, all the meta-data, configuration, and analysis were set by hand, so that the setup shows 
examples of a real-world use cases and solutions.

Demo Status
-----------
This demo page is an early alpha version.
The chapter of :ref:`teen_car` is mostly complete in terms of configuration and show cases, even if the amount
of requirements and co. is quite small.

Demo Object and Meta Model
--------------------------


.. uml::

   @startuml
   
   class "Team" as team #b7ff43 {
      id
      title
      + persons
   }
   class "Person" as person #508002 {
      id
      title
      role
      contact
      title
   }
   
   class "Requirement" as req #10b8c4 {
      id
      title
      status
      tags
      +links
      +author
      +release
      +based_on
   }
   
   
   class "Specification" as spec #5555cc {
      id
      title
      status
      tags
      +links
      +author
      +reqs

   }

   class "Test Case" as test #790691 {
      id
      title
      status
      tags
      +links
      +author
      +spec
      +runs
   }

   class "Test Run" as run #b38405 {
      id
      title
      status
      tags
      +author
      +release
      +based_on
   }

   class "Implementation" as impl #b11616  {
      id
      title
      status
      tags
      +author
      +implements
   }

   class "Release" as release #0d7e6b {
      id
      title
      status
      tags
      +author
   }



   team -> person: persons

   req --> req: based_on
   req <-- spec : reqs
   req -left-> release: release
   spec <-- test: spec
   spec <- impl: implements
   test -> run : runs: automatically\nlinked

   req -[#999]-> person:  <color:#999>author 
   spec -[#999]-> person: <color:#999>author 
   test -[#999]-> person: <color:#999>author 
   release -[#999]-> person: <color:#999>author 


   
   @enduml

ToDo
----

* ☑ Dashboard and Analysis page (tables, flowcharts, pies)
* ☑ Template for need objects, showing connected objects (for reqs and specs)
* ☑ Code API example and linking
* ☑ Sphinx-Preview or alternative
* ☐ Much more content
* ☐ SW Architecture example
* ☐ Sphinx-Build documentation
* ☑ ``needs_constraints`` example
* ☑ ``conf.py`` integration and details
* ☐ CI integration (☑ Read the docs, checks and GitHub action missing)
* ☐ PDF build (postponed, as a build with Sphinx-SimpledPDF needs special handling because of images and used Sphinx-Design grids)
* ☐ Add a drawio example
* ☑ Example for variant handling
* ☐ List of single features, plus explanation and link to doc, where it is used.
* ☐ Nested Needs Example
* ☐ Better Example data. We need to kind of examples. One for all skill-levels, one for Automotive managers

  * All-Skill-Level: Feature-based development of a Rocket (Req,Specs, Tests all on one feature-page)
  * Automotive: ECU-dev by V-model. Per type one file/folder


Page Content
------------

.. toctree::
   :maxdepth: 2

   base_car/index
   teen_car/index
   granny_car/index
   persons
   analysis


.. toctree::
   :maxdepth: 2

   demo_details
