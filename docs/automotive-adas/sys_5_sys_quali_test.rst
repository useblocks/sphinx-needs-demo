{% set page="sys_5_sys_quali_test.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SYS5_Verification_Tests:

SYS.5 Qualification Test Cases
==============================

This document provides verification test cases to ensure the requirements defined in SYS.2 are correctly implemented.

.. test:: Lane Detection Verification
   :id: TEST_SYS_QUAL_001
   :links: REQ_001, REQ_002

   Verify the lane detection system meets requirements for detecting lane markings and providing corrective steering actions.

.. test:: Adaptive Cruise Control Verification
   :id: TEST_SYS_QUAL_002
   :links: REQ_003, REQ_004

   Verify the adaptive cruise control system satisfies requirements for distance measurement and dynamic speed control.

.. test:: Collision Avoidance Verification
   :id: TEST_SYS_QUAL_003
   :links: REQ_005, REQ_006

   Verify the collision avoidance system adheres to requirements for collision detection and emergency braking activation.

.. test:: Pedestrian Detection Verification
   :id: TEST_SYS_QUAL_004
   :links: REQ_007, REQ_008, REQ_009

   Verify the pedestrian detection system fulfills requirements for detection, alerting, and emergency braking in pedestrian scenarios.

.. test:: Multi-Subsystem Verification
   :id: TEST_SYS_QUAL_005
   :links: REQ_001, REQ_003, REQ_005

   Verify the integration and functionality of lane detection, adaptive cruise control, and collision avoidance subsystems.


SYS.5 Qualification Test Results
--------------------------------

Summary of the test Results

- :need:`TF_TEST_SYS_QUAL_TEST_SUMMARY`
