{% set page="swe_1_sw_req_analysis.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE1_Software_Requirements:

SWE.1 Software Requirements
===========================

.. swreq:: Lane Marking Detection Algorithm
   :id: SWREQ_001
   :status: open
   :links: ARCH_001, REQ_001
   :author: PETER

   Develop software to process camera inputs and accurately identify lane markings under various environmental conditions.

.. swreq:: Lane Deviation Warning
   :id: SWREQ_002
   :status: open
   :links: ARCH_001, REQ_002
   :author: ROBERT

   Implement a feature to trigger warnings if the vehicle deviates from its lane without proper signaling.

.. swreq:: Steering Correction Algorithm
   :id: SWREQ_003
   :status: open
   :links: ARCH_001, REQ_002
   :author: ROBERT

   Create an algorithm to calculate and apply corrective steering actions to maintain the vehicle within the detected lane boundaries.

.. swreq:: Radar-Based Distance Measurement
   :id: SWREQ_004
   :status: open
   :links: ARCH_002, REQ_003
   :author: ROBERT

   Design software to process radar inputs and measure the distance to objects ahead with high precision.

.. swreq:: Speed Control Integration
   :id: SWREQ_005
   :status: open
   :links: ARCH_002, REQ_004
   :author: PETER

   Implement a module to dynamically adjust the vehicle's speed based on distance measurements and desired following distance.

.. swreq:: Collision Risk Estimation
   :id: SWREQ_006
   :status: open
   :links: ARCH_003, REQ_005
   :author: SARAH

   Develop a feature to estimate collision risk using real-time sensor data and predictive analytics.

.. swreq:: Emergency Brake Activation
   :id: SWREQ_007
   :status: open
   :links: ARCH_003, REQ_006
   :author: SARAH

   Implement a software module to autonomously apply brakes when a collision is imminent.

.. swreq:: Pedestrian Detection Algorithm
   :id: SWREQ_008
   :status: open
   :links: ARCH_004, REQ_007
   :author: SARAH

   Develop an algorithm to detect pedestrians using sensor fusion techniques, combining camera, LiDAR, and radar data.

.. swreq:: Pedestrian Alert System
   :id: SWREQ_009
   :status: open
   :links: ARCH_004, REQ_008
   :author: SARAH

   Create a system to issue audio and visual alerts when pedestrians are detected near the vehicle's path.

.. swreq:: Emergency Braking for Pedestrians
   :id: SWREQ_010
   :status: open
   :links: ARCH_004, REQ_009
   :author: SARAH

   Implement functionality to apply emergency braking when a pedestrian is detected in the collision path.

.. swreq:: Lane Marking Data Visualization
   :id: SWREQ_011
   :status: open
   :links: ARCH_001, REQ_001
   :author: STEVEN

   Provide a visual representation of detected lane markings on the vehicle's dashboard for driver awareness.

.. swreq:: Environmental Adaptation
   :id: SWREQ_012
   :status: open
   :links: ARCH_001, REQ_001
   :author: STEVEN

   Develop software to adapt lane marking detection under challenging conditions, such as rain or fog.

.. swreq:: Adaptive Speed Limits
   :id: SWREQ_013
   :status: open
   :links: ARCH_002, REQ_004
   :author: STEVEN

   Implement a feature to adjust vehicle speed based on detected speed limits and road conditions.

.. swreq:: Proximity Alert
   :id: SWREQ_014
   :status: open
   :links: ARCH_002, REQ_003
   :author: STEVEN

   Create alerts for the driver when objects come within a critical distance.

.. swreq:: Multi-Object Tracking
   :id: SWREQ_015
   :status: closed
   :links: ARCH_003, REQ_005
   :author: STEVEN

   Implement tracking software to monitor multiple objects simultaneously and evaluate their threat level.

.. swreq:: Braking Efficiency Optimization
   :id: SWREQ_016
   :status: open
   :links: ARCH_003, REQ_006
   :author: STEVEN

   Develop algorithms to optimize braking force during emergency stops to minimize impact risks.

.. swreq:: Pedestrian Path Prediction
   :id: SWREQ_017
   :status: closed
   :links: ARCH_004, REQ_007
   :author: STEVEN

   Implement machine learning models to predict pedestrian movements and improve detection accuracy.

.. swreq:: Integrated Alert System
   :id: SWREQ_018
   :status: open
   :links: ARCH_004, REQ_008
   :author: STEVEN

   Combine audio, visual, and haptic alerts into a unified system for enhanced driver awareness.

.. swreq:: Predictive Emergency Braking
   :id: SWREQ_019
   :status: closed
   :links: ARCH_004, REQ_009
   :author: SARAH

   Develop software to anticipate emergencies and initiate braking earlier to prevent accidents.

.. swreq:: Crosswalk Detection
   :id: SWREQ_020
   :status: closed
   :links: ARCH_004, REQ_007
   :author: SARAH

   Create functionality to identify crosswalks and prioritize pedestrian safety in such zones.
