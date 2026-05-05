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

.. test:: Traffic Sign Recognition and Speed Control Integration
   :id: TEST_INT_007
   :status: failed
   :links: SWARCH_007, SWARCH_002
   :author: THOMAS

   Validate that recognized speed limits are propagated correctly from traffic sign processing to the adaptive cruise control subsystem.

.. test:: Blind Spot Sensor Fusion Integration
   :id: TEST_INT_008
   :status: open
   :links: SWARCH_008
   :author: THOMAS

   Exercise the blind spot monitoring subsystem end to end: feed synthesized radar and
   side-camera streams plus turn-signal events, and verify the warning emitter fires
   only when an occupied zone aligns with the indicated lane change.

.. test:: Drowsiness Detection Pipeline Integration
   :id: TEST_INT_009
   :status: open
   :links: SWARCH_009
   :author: THOMAS

   Exercise the drowsiness detection subsystem end to end: feed cabin frame sequences
   spanning alert, fatigued, and severely drowsy driver states, and verify progressive
   alerts are raised once the smoothed drowsiness score exceeds the calibrated dwell time.
