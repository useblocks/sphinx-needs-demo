{% set page="sys_2_req_analysis.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SYS2_Requirement_Analysis:


SYS.2 Requirement Analysis
==========================

.. req:: Lane Detection Algorithm
   :id: REQ_001
   :status: open
   :links: NEED_001
   :release: REL_ADAS_2025_6
   :author: PETER
   :jira: 3
   :post_template: all_post

   Develop a lane detection algorithm to process camera input and accurately identify lane markings under various lighting conditions.

.. req:: Steering Control Logic
   :id: REQ_002
   :status: open
   :links: NEED_001
   :release: REL_ADAS_2025_6
   :author: PETER
   :jira: 4
   :post_template: all_post

   Implement a control logic module to provide smooth and precise steering corrections based on detected lane positions.

.. req:: Distance Measurement System
   :id: REQ_003
   :status: open
   :links: NEED_002
   :release: REL_ADAS_2025_12
   :author: PETER
   :post_template: all_post

   Design a system to measure the distance to the vehicle ahead using radar or LiDAR sensors for adaptive cruise control.

.. req:: Speed Adjustment Algorithm
   :id: REQ_004
   :status: open
   :links: NEED_002
   :release: REL_ADAS_2025_12
   :author: ROBERT
   :post_template: all_post

   Create an algorithm to adjust vehicle speed dynamically while maintaining a safe following distance.

.. req:: Collision Detection Module
   :id: REQ_005
   :status: open
   :links: NEED_003
   :author: ROBERT
   :post_template: all_post

   Develop a module to identify potential collisions using sensor data and predict the time-to-impact.

.. req:: Autonomous Braking Logic
   :id: REQ_006
   :status: open
   :links: NEED_003
   :author: ROBERT
   :post_template: all_post

   Implement logic to autonomously apply brakes when a collision is imminent based on predictions from the collision detection module.

.. req:: Pedestrian Recognition System
   :id: REQ_007
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2025_12
   :author: ROBERT
   :post_template: all_post

   Create a system to detect pedestrians in the vehicle's path using machine learning and sensor fusion.

.. req:: Warning and Alert Mechanism
   :id: REQ_008
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2025_6
   :author: ROBERT
   :post_template: all_post

   Design a mechanism to issue audio or visual alerts when pedestrians are detected near the vehicle.

.. req:: Emergency Braking for Pedestrians
   :id: REQ_009
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2026_6
   :author: ROBERT
   :post_template: all_post

   Develop functionality to initiate emergency braking when a pedestrian is in the collision path.
