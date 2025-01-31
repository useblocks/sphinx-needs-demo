{% set page="swe_5_sw_integration_tests.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE5_Integration_Tests:

SWE.5 Integration Test Cases
============================

This document provides integration test cases for the software architecture, ensuring the seamless interaction of various subsystems.

.. test:: Lane Detection and Steering Integration
   :id: TEST_INT_001
   :links: SWARCH_001
   :author: THOMAS

   Validate the integration of the lane detection module with the steering correction logic under various road conditions.

.. test:: Adaptive Cruise Control and Distance Measurement
   :id: TEST_INT_002
   :links: SWARCH_002
   :author: THOMAS

   Ensure proper integration between the adaptive cruise control system and the radar-based distance measurement module.

.. test:: Collision Avoidance and Emergency Braking
   :id: TEST_INT_003
   :links: SWARCH_003
   :author: THOMAS

   Test the interaction between the collision avoidance system and the emergency braking subsystem during high-risk scenarios.

.. test:: Pedestrian Detection and Alert Mechanism
   :id: TEST_INT_004
   :links: SWARCH_004, SWARCH_005
   :author: THOMAS

   Validate the integration of the pedestrian detection module with the driver alert system for timely warnings.

.. test:: Pedestrian Detection and Emergency Braking
   :id: TEST_INT_005
   :links: SWARCH_004, SWARCH_006
   :author: THOMAS

   Ensure smooth coordination between pedestrian detection and emergency braking functionalities to avoid collisions.

.. test:: Multi-Subsystem Coordination
   :id: TEST_INT_006
   :links: SWARCH_001, SWARCH_002, SWARCH_003
   :author: THOMAS

   Test the interaction between lane detection, adaptive cruise control, and collision avoidance systems for cohesive behavior.
