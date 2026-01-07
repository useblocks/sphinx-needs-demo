{% set page="hara.rst" %}
{% include "demo_page_header.rst" with context %}

🔍 HARA - Hazard Analysis & Risk Assessment
============================================

This page documents the Hazard Analysis and Risk Assessment for vehicle
actuation systems of automated vehicles, identifying potential hazardous events
and their associated ASIL ratings.

Methodology
-----------

The hazard analysis follows ISO 26262-3 and uses the following assessment criteria:

**Severity (S)** - Potential harm to persons:
  - S0: No injuries
  - S1: Light and moderate injuries
  - S2: Severe and life-threatening injuries (survival probable)
  - S3: Life-threatening injuries (survival uncertain), fatal injuries

**Exposure (E)** - Probability of operational scenario:
  - E0: Incredible
  - E1: Very low probability
  - E2: Low probability
  - E3: Medium probability
  - E4: High probability

**Controllability (C)** - Ability to avoid harm through driver intervention:
  - C0: Controllable in general
  - C1: Simply controllable
  - C2: Normally controllable
  - C3: Difficult to control or uncontrollable

These ratings determine the ASIL assignment per ISO 26262-3:2018 Table 4.

Top-Level Hazard
----------------

.. hazard:: Vehicle Not Following Intended Trajectory
   :id: HAZ_TRAJ_DEV
   :asil: D
   :status: open
   :scenario: Automated driving on public roads (all operational scenarios)

   The vehicle deviates from its intended trajectory, potentially resulting in
   collision with other traffic participants or stationary objects.

   This is the fundamental hazard for vehicle actuation systems in automated
   driving. When the actuation system fails to execute the trajectory commands
   correctly, the vehicle may:

   - Depart from the intended lane
   - Collide with obstacles or other vehicles
   - Fail to maintain safe following distance
   - Execute unintended maneuvers

   **ASIL Rationale:** This hazard is assigned **ASIL D** as the highest safety
   integrity level because trajectory deviation during automated driving can lead
   to severe accidents with life-threatening consequences. The assessment considers:

   - **Severity (S3):** Life-threatening injuries or fatalities are likely outcomes
     of trajectory deviation, especially at highway speeds
   - **Exposure (E4):** Trajectory control is continuously active during all automated
     driving operations
   - **Controllability (C2-C3):** Limited ability for intervention in SAE Level 4/5
     automation where no human driver is monitoring or ready to take over

   According to ISO 26262-3 Table 4, the combination of S3 + E4 + C2/C3 results
   in ASIL D classification.

.. note::

   While specific operational scenarios may have different S/E/C ratings and lower
   ASIL levels, this example uses ASIL D to demonstrate the most safety-critical case
   for actuation systems in fully automated vehicles.

Hazard Context
--------------

The hazard analysis is performed in the context of the **STPA (System-Theoretic Process
Analysis)** methodology, which models the vehicle actuation system as a hierarchical
control structure:

1. **Trajectory Input**: Commanded trajectory from vehicle automation controller
2. **Vehicle Dynamics Controller (VDC)**: Translates trajectory to wheel torques and steering angles
3. **Wheel Rotational Dynamics Controller (WRDC)**: Controls individual wheel dynamics
4. **Low-level Controllers**: Steering, brake, and drive controllers
5. **Physical Processes**: Actual vehicle dynamics

The hazard ``HAZ_TRAJ_DEV`` occurs when any component in this control chain fails,
resulting in the vehicle not following its intended trajectory.

Safety Analysis Scope
---------------------

**In Scope:**
  - Failures of actuation system components (controllers, actuators, sensors)
  - Control algorithm malfunctions
  - Communication failures within the actuation system
  - Mechanical/electrical component failures

**Out of Scope:**
  - Trajectory planning errors (assumed correct in this analysis per ISO 26262-3:7.4.2.2.2)
  - Environment perception failures
  - Vehicle-to-vehicle communication failures
  - Cybersecurity attacks (covered by ISO/SAE 21434)

Next Steps
----------

From this top-level hazard, **20 safety goals** are systematically derived using
STPA analysis of unsafe control actions. See :doc:`safety_goals` for the complete
set of safety goals that mitigate this hazard.

.. seealso::

   **ISO 26262-3:2018** - Road vehicles — Functional safety — Part 3: Concept phase

   **STPA Handbook** - N.G. Leveson and J.P. Thomas, "STPA Handbook," 2018
