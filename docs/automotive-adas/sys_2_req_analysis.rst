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

   Develop a lane detection algorithm to process camera input and accurately identify lane markings under various lighting conditions.

.. req:: Steering Control Logic
   :id: REQ_002
   :status: in progress
   :links: NEED_001, REQ_001
   :release: REL_ADAS_2025_6
   :author: PETER
   :jira: 4
   :effort: 2
   :approved: True

   Implement a control logic module to provide smooth and precise steering corrections based on detected lane positions.

.. req:: Distance Measurement System
   :id: REQ_003
   :status: open
   :links: NEED_002
   :release: REL_ADAS_2025_12
   :author: PETER

   Design a system to measure the distance to the vehicle ahead using radar or LiDAR sensors for adaptive cruise control.

.. req:: Speed Adjustment Algorithm
   :id: REQ_004
   :status: open
   :links: NEED_002
   :release: REL_ADAS_2025_12
   :author: ROBERT

   Create an algorithm to adjust vehicle speed dynamically while maintaining a safe following distance.

.. req:: Collision Detection Module
   :id: REQ_005
   :status: open
   :links: NEED_003
   :release: REL_ADAS_2025_12
   :author: ROBERT

   Develop a module to identify potential collisions using sensor data and predict the time-to-impact.

.. req:: Autonomous Braking Logic
   :id: REQ_006
   :status: open
   :links: NEED_003
   :release: REL_ADAS_2025_12
   :author: ROBERT

   Implement logic to autonomously apply brakes when a collision is imminent based on predictions from the collision detection module.

.. req:: Pedestrian Recognition System
   :id: REQ_007
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2025_12
   :author: ROBERT

   Create a system to detect pedestrians in the vehicle's path using machine learning and sensor fusion.

.. req:: Warning and Alert Mechanism
   :id: REQ_008
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2025_6
   :author: ROBERT

   Design a mechanism to issue audio or visual alerts when pedestrians are detected near the vehicle.

.. req:: Emergency Braking for Pedestrians
   :id: REQ_009
   :status: open
   :links: NEED_004
   :release: REL_ADAS_2026_6
   :author: ROBERT

   Develop functionality to initiate emergency braking when a pedestrian is in the collision path.

.. req:: Lane Detection Error Handling
   :id: REQ_010
   :status: closed
   :links: NEED_001, REQ_001
   :release: REL_ADAS_2025_6
   :author: PETER

   **Description:**
   The lane keeping system SHALL handle situations where lane markings cannot be reliably detected.

   **Acceptance Criteria:**

   * AC-1: When lane confidence drops below threshold for >2 seconds, issue visual warning to driver
   * AC-2: When lane confidence drops below threshold for >5 seconds, issue audible alert
   * AC-3: System SHALL NOT provide steering corrections when lane confidence is below threshold
   * AC-4: System SHALL log all degraded mode events with timestamp and duration
   * AC-5: System SHALL automatically re-engage when lane confidence exceeds threshold for >1 second

   **Error Conditions:**

   - Faded or missing lane markings
   - Construction zones with temporary markings
   - Heavy rain/snow obscuring camera view
   - Strong shadows or glare
   - Dirt/debris on camera lens

.. req:: Lane Keeping Operational Limits
   :id: REQ_011
   :status: closed
   :links: NEED_001, REQ_001, REQ_002
   :release: REL_ADAS_2025_6
   :author: PETER

   **Description:**
   The lane keeping system SHALL operate only within defined operational constraints.

   **Acceptance Criteria:**

   * AC-1: System SHALL activate only when vehicle speed is between 60 km/h and 180 km/h
   * AC-2: System SHALL disengage when road curvature radius is less than 250 meters
   * AC-3: System SHALL require lane marking width between 10cm and 30cm
   * AC-4: System SHALL disengage if steering angle exceeds ±15 degrees
   * AC-5: System SHALL notify driver 3 seconds before automatic disengagement
   * AC-6: System SHALL remain disengaged until driver explicitly re-enables (no automatic re-engagement after limit violation)

   **Rationale:**

   Operating outside these limits may result in unsafe steering corrections or unreliable lane detection.
