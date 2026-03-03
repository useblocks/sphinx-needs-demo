{% set page="swe_1_sw_req_analysis.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE1_Software_Requirements:

SWE.1 Software Requirements
===========================

.. swreq:: Lane Marking Detection Algorithm
   :id: SWREQ_001
   :status: in progress
   :links: ARCH_001, REQ_001, REQ_010
   :author: PETER
   :github: 4

   Develop software to process camera inputs and accurately identify lane markings under various environmental conditions. The algorithm SHALL output a confidence metric (0.0-1.0) for each detected lane marking to support error handling and degraded mode operation.

.. swreq:: Lane Deviation Warning
   :id: SWREQ_002
   :status: open
   :links: ARCH_001, REQ_002
   :author: ROBERT
   :github: 5

   Implement a feature to trigger warnings if the vehicle deviates from its lane without proper signaling.

.. swreq:: Steering Correction Algorithm
   :id: SWREQ_003
   :status: in progress
   :links: ARCH_001, REQ_002, REQ_010, REQ_011
   :author: ROBERT

   Create an algorithm to calculate and apply corrective steering actions to maintain the vehicle within the detected lane boundaries. The algorithm SHALL NOT apply corrections when lane confidence is below threshold or when system is outside operational limits.

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

.. swreq:: Lane Confidence Monitoring
   :id: SWREQ_021
   :status: closed
   :links: ARCH_001, REQ_001, REQ_010, SWREQ_001
   :author: PETER

   **Description:**
   Implement software to continuously monitor lane detection confidence and track degraded mode conditions.

   **Functional Requirements:**

   * FR-1: Calculate aggregate confidence score from left and right lane markings
   * FR-2: Use confidence threshold of 0.65 (below = degraded mode)
   * FR-3: Maintain rolling 1-second buffer to prevent oscillation
   * FR-4: Timestamp all confidence state transitions
   * FR-5: Log confidence values at 10 Hz when below threshold
   * FR-6: Trigger degraded mode entry after 2.0 seconds below threshold
   * FR-7: Trigger degraded mode exit after 1.0 seconds above threshold

   **Interface:**

   - Input: Lane confidence from SWREQ_001 (left/right, 0.0-1.0)
   - Output: System state (normal/degraded), state duration

.. swreq:: Degraded Mode Notification System
   :id: SWREQ_022
   :status: closed
   :links: ARCH_001, REQ_010
   :author: PETER

   **Description:**
   Implement driver notification system for lane keeping degraded mode.

   **Functional Requirements:**

   * FR-1: Display visual warning (yellow icon) on HMI after 2 seconds in degraded mode
   * FR-2: Issue audible alert (single beep) after 5 seconds in degraded mode
   * FR-3: Clear visual warning within 0.5 seconds of exiting degraded mode
   * FR-4: Use CAN bus message 0x2A1 for HMI communication
   * FR-5: Log all notification events to system event log

   **Interface:**

   - Input: System state from SWREQ_021
   - Output: HMI notification commands, CAN messages

.. swreq:: Lane Keep Operational Domain Monitor
   :id: SWREQ_023
   :status: closed
   :links: ARCH_001, REQ_011
   :author: PETER

   **Description:**
   Monitor vehicle and road conditions to enforce lane keeping operational constraints.

   **Functional Requirements:**

   * FR-1: Monitor vehicle speed (from CAN 0x100) - enforce 60-180 km/h range
   * FR-2: Estimate road curvature from lane geometry - enforce ≥250m radius
   * FR-3: Monitor steering wheel angle (from CAN 0x120) - enforce ≤±15° range
   * FR-4: Check lane marking width from SWREQ_001 - enforce 10-30cm range
   * FR-5: Generate out-of-domain event when any constraint violated
   * FR-6: Trigger 3-second warning before disengagement
   * FR-7: Update operational domain status at 10 Hz

   **Interface:**

   - Input: Vehicle CAN data, lane geometry from SWREQ_001
   - Output: Operational domain status (in/out/warning), constraint violations

.. swreq:: Lane Keep System State Manager
   :id: SWREQ_024
   :status: closed
   :links: ARCH_001, REQ_010, REQ_011, SWREQ_021, SWREQ_023
   :author: PETER

   **Description:**
   Manage overall lane keeping system state machine and coordinate transitions.

   **State Machine:**

   States:

   - DISABLED: System off (driver hasn't activated)
   - ENABLED_NORMAL: Actively providing steering, normal conditions
   - ENABLED_DEGRADED: No steering, confidence too low (per REQ_010)
   - DISENGAGING: 3-second countdown before disabling (per REQ_011)

   Transitions:

   - DISABLED → ENABLED_NORMAL: Driver activation + all constraints satisfied
   - ENABLED_NORMAL → ENABLED_DEGRADED: Confidence drops per SWREQ_021
   - ENABLED_DEGRADED → ENABLED_NORMAL: Confidence recovers per SWREQ_021
   - ENABLED_NORMAL → DISENGAGING: Operational constraint violated per SWREQ_023
   - ENABLED_DEGRADED → DISENGAGING: Operational constraint violated per SWREQ_023
   - DISENGAGING → DISABLED: 3-second timer expires
   - Any state → DISABLED: Driver manual deactivation

   **Functional Requirements:**

   * FR-1: Process inputs from SWREQ_021 (confidence monitor)
   * FR-2: Process inputs from SWREQ_023 (domain monitor)
   * FR-3: Enable/disable SWREQ_003 steering corrections based on state
   * FR-4: Trigger SWREQ_022 notifications based on state
   * FR-5: Implement 3-second disengagement countdown
   * FR-6: NO automatic re-engagement after DISENGAGING → DISABLED
   * FR-7: Log all state transitions with timestamp

   **Interface:**

   - Input: Confidence state (SWREQ_021), domain status (SWREQ_023), driver commands
   - Output: System state, steering enable/disable, notification triggers

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
