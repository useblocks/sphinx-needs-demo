{% set page="swe_6_sw_quali_tests.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE6_Qualification_Tests:

SWE.6 Qualification Test Cases
==============================

This document provides qualification test cases to validate the fulfillment of software requirements from SWE.1.

.. test:: Lane Detection Qualification
   :id: TEST_QUAL_001
   :links: SWREQ_001, SWREQ_002, SWREQ_003

   Qualify the lane detection functionality by verifying its accuracy in identifying lane markings and providing corrective steering under specified conditions.

.. test:: Adaptive Cruise Control Qualification
   :id: TEST_QUAL_002
   :links: SWREQ_004, SWREQ_005, SWREQ_013

   Qualify the adaptive cruise control by testing its ability to measure distances and adjust speed dynamically in accordance with defined safety parameters.

.. test:: Collision Avoidance Qualification
   :id: TEST_QUAL_003
   :links: SWREQ_006, SWREQ_007, SWREQ_015

   Qualify the collision avoidance system by ensuring it can detect potential collisions and execute emergency braking effectively.

.. test:: Pedestrian Safety Qualification
   :id: TEST_QUAL_004
   :links: SWREQ_008, SWREQ_009, SWREQ_010

   Qualify the pedestrian safety system by testing its detection, alerting, and emergency braking functionalities in predefined scenarios.

.. test:: Integrated Qualification Test
   :id: TEST_QUAL_005
   :links: SWREQ_001, SWREQ_004, SWREQ_006, SWREQ_008

   Qualify the integration of lane detection, adaptive cruise control, collision avoidance, and pedestrian detection for seamless functionality and safety compliance.

.. test:: Traffic Sign Recognition Qualification
   :id: TEST_QUAL_006
   :status: passed
   :links: SWREQ_021

   Qualify the speed limit sign detection software by verifying correct recognition of posted limits in representative traffic scenes.

.. test:: Blind Spot Monitoring Qualification
   :id: TEST_QUAL_007
   :status: open
   :links: SWREQ_022, SWREQ_023

   Qualify the blind spot monitoring software by verifying zone occupancy detection and
   lane change warning behavior across mixed traffic, weather, and lighting scenarios.
