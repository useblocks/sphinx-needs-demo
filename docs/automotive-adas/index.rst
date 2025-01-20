{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}


🚗 Automotive ADAS
==================

.. team:: Software Development Project for ADAS Components
   :id: ADAS
   :persons: PETER, ALFRED, ROBERT, STEVEN, THOMAS
   :image: docs/_images/adas.png
   :layout: clean_l

   This project focuses on developing a modular software platform for 
   Advanced Driver Assistance Systems (ADAS), aimed at enhancing vehicle safety 
   and automation. The primary objective is to create a robust system that 
   integrates multiple functionalities such as lane-keeping assistance, adaptive 
   cruise control, emergency braking, and pedestrian detection.

.. toctree::
   :maxdepth: 1

   releases
   persons
   analysis
   external_data
   sys_1_req_elicitation
   sys_2_req_analysis
   sys_3_sys_arch
   swe_1_sw_req_analysis
   swe_2_sw_arch
   swe_3_sw_detailed_design
   swe_4_unit_tests
   swe_5_sw_integration_tests
   swe_6_sw_quali_tests
   sys_4_sys_integation_tests
   sys_5_sys_quali_test


V-model and service connectors
------------------------------

.. image:: /_images/useblocks_v_model.png
   :width: 50%

Commercial connectors for the following services are available by `useblocks <https://useblocks.com/>`__:
Codebeamer, Jira, Azure DevOps, Github, Excel.


Demo Object and Meta Model
--------------------------

.. uml::

   @startuml
   
   class "Team" as team #CEA262 {
      id
      title
      + persons
   }
   class "Person" as person #C10020 {
      id
      title
      role
      contact
      title
   }
   
   
   class "Need" as need #F6768E {
      id
      title
      status
      tags
      +links
      +author
      +release
   }
   
   class "Requirement" as req #FFB300 {
      id
      title
      status
      tags
      +links
      +author
      +release
      +based_on
   }
   
   
   class "Architecture" as arch #4aac73 {
      id
      title
      status
      tags
      +links
      +author
      +reqs

   }
   
   class "SW Requirement" as swreq #FF7A5C {
      id
      title
      status
      +links
      +author
   }
   
   class "SW Architecture" as swarch #2d86c1 {
      id
      title
      status
      +links
      +author
   }

   class "Test Case" as test #A6BDD7 {
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

   class "Implementation" as impl #FF6800  {
      id
      title
      status
      tags
      +author
      +implements
   }

   class "Release" as release #817066 {
      id
      title
      status
      tags
      +author
   }

   team -> person: persons

   need <-- req: links
   
   req <- arch : links
   req <-- swreq : links
   req <-- test : links
   req -left-> release: release
   
   arch <-- test: links
   arch <-- swreq: links
      
   swarch <-- test : links
   swarch <- impl: links
   
   swreq <-- test : links
   swreq  <- impl: links
   swreq <-- swarch: links
   
   test -> run : runs: automatically\nlinked

   req -[#999]-> person:  <color:#999>author 
   arch -[#999]-> person: <color:#999>author 
   swreq -[#999]-> person:  <color:#999>author 
   swarch -[#999]-> person: <color:#999>author 
   test -[#999]-> person: <color:#999>author 
   release -[#999]-> person: <color:#999>author 
   
   @enduml