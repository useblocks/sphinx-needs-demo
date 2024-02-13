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


As playground a simple Automotive SW project gets documented, using elements for:

* Requirements
* Specifications
* Implementations
* Test Cases
* and Test Results

Architecture diagrams get described by PlantUML.

There are also Dashboard pages to show specific information for different process roles.


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
      +specs
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
   }


   team -> person

   req <- spec
   spec <-- test
   spec <- impl
   test -> run : Automatically\nlinked

   req --> person
   spec --> person
   test --> person
   
   @enduml

ToDo
----

* ☑ Dashboard and Analysis page (tables, flowcharts, pies)
* ☑ Template for need objects, showing connected objects (for reqs and specs)
* ☑ Code API example and linking
* ☐ Sphinx-Preview or alternative
* ☐ Much more content
* ☐ Sphinx-Build documentation
* ☐ ``needs_constraints`` example
* ☐ ``conf.py`` integration and details
* ☐ CI integration (☑ Read the docs, checks GitHub action missing)
* ☐ PDF build (postponed, as a build with Sphinx-SimpledPDF needs special handling because of images and used Sphinx-Design grids)

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