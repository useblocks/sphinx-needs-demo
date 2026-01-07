{% set page="safety_goals.rst" %}
{% include "demo_page_header.rst" with context %}

🎯 Safety Goals
===============

Safety goals are top-level safety requirements derived from the HARA to reduce
risks to tolerable levels. Each safety goal:

- Mitigates the identified hazard (HAZ_TRAJ_DEV)
- Inherits ASIL D from the mitigated hazard
- Defines required system behavior in technology-agnostic terms
- Forms the basis for functional safety requirement derivation

These 20 safety goals were systematically derived using STPA analysis of unsafe
control actions for vehicle actuation systems.

Safety Goals Overview
---------------------

.. needtable::
   :filter: type == "safety_goal" and docname is not None and "safety_example" in docname
   :columns: id, title, asil
   :style: table

Vehicle Dynamics Controller Safety Goals
-----------------------------------------

.. safety_goal:: VDC Must Set Target Wheel Torque When Required
   :id: SG_01
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain current vehicle state with controlled deceleration

   The Vehicle Dynamics Controller must set a new target wheel torque when
   required for safe trajectory following. Failure to provide necessary torque
   commands can result in trajectory deviation.

.. safety_goal:: VDC Must Set Target Wheel Torque Only When Required
   :id: SG_02
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Reject unintended torque commands

   The Vehicle Dynamics Controller must set a new target wheel torque only when
   required. Unintended torque changes can cause unexpected vehicle behavior.

.. safety_goal:: VDC Must Set Target Steering Angle When Required
   :id: SG_03
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain current steering angle with gradual return to center

   The Vehicle Dynamics Controller must set a new target steering angle when
   required for trajectory execution. Missing steering commands prevent proper
   path following.

.. safety_goal:: VDC Must Set Target Steering Angle Only When Required
   :id: SG_04
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain intended steering angle, reject spurious commands

   The Vehicle Dynamics Controller must set a new target steering angle only when
   required. Unintended steering changes are hazardous to vehicle control.

Wheel Rotational Dynamics Controller Safety Goals
--------------------------------------------------

.. safety_goal:: WRDC Must Change Target Brake Torque When Required
   :id: SG_05
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain safe deceleration capability

   The Wheel Rotational Dynamics Controller must change target brake torque when
   required for proper vehicle speed control along the trajectory.

.. safety_goal:: WRDC Must Change Target Brake Torque Only When Required
   :id: SG_06
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Prevent unintended braking events

   The Wheel Rotational Dynamics Controller must change target brake torque only
   when required. Unintended braking can cause trajectory deviation or collision.

.. safety_goal:: WRDC Must Change Target Drive Torque When Required
   :id: SG_07
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain current speed with controlled adjustment

   The Wheel Rotational Dynamics Controller must change target drive torque when
   required for maintaining the planned velocity profile.

.. safety_goal:: WRDC Must Change Target Drive Torque Only When Required
   :id: SG_08
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Prevent unintended acceleration

   The Wheel Rotational Dynamics Controller must change target drive torque only
   when required to prevent unintended acceleration or deceleration.

Anti-lock and Anti-spin Control Safety Goals
---------------------------------------------

.. safety_goal:: Anti-lock Control Must Be Performed Only When Required
   :id: SG_09
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Normal braking without ABS intervention

   Anti-lock control must be performed only when wheel lock is imminent. Unnecessary
   ABS activation can reduce braking efficiency and affect trajectory control.

.. safety_goal:: Anti-lock Control Must Be Performed When Required
   :id: SG_10
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Activate ABS to prevent wheel lock and maintain steerability

   Anti-lock control must be performed when required to prevent wheel lock during
   braking, maintaining vehicle controllability.

.. safety_goal:: Anti-spin Control Must Be Performed Only When Required
   :id: SG_11
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Normal traction without ASR intervention

   Anti-spin control must be performed only when wheel spin is detected. Unnecessary
   intervention can affect acceleration performance and trajectory execution.

.. safety_goal:: Anti-spin Control Must Be Performed When Required
   :id: SG_12
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Activate ASR to prevent wheel spin and maintain traction

   Anti-spin control must be performed when required to prevent excessive wheel spin
   during acceleration, ensuring stable trajectory following.

Drive Controller Safety Goals
------------------------------

.. safety_goal:: Drive Controller Must Apply Drive Torque When Required
   :id: SG_13
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain minimum safe speed or controlled stop

   The Drive Controller must apply drive torque when required to execute the
   commanded velocity profile along the trajectory.

.. safety_goal:: Drive Controller Must Apply Drive Torque Only When Required
   :id: SG_14
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Zero torque or engine braking only

   The Drive Controller must apply drive torque only when required. Unintended
   drive torque can cause dangerous acceleration.

Brake Controller Safety Goals
------------------------------

.. safety_goal:: Brake Controller Must Engage Brake When Required
   :id: SG_15
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Emergency braking capability available

   The Brake Controller must engage brake when required for deceleration or
   emergency stopping to prevent collision.

.. safety_goal:: Brake Controller Must Engage Brake Only When Required
   :id: SG_16
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Brake released when not commanded

   The Brake Controller must engage brake only when required. Unintended braking
   can cause loss of vehicle control or rear-end collisions.

Steering Controller Safety Goals
---------------------------------

.. safety_goal:: SC Must Change Steering Angle When Required
   :id: SG_17
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Gradual return to neutral steering position

   The Steering Controller must change steering angle when required to follow
   the commanded path. Failure prevents proper trajectory execution.

.. safety_goal:: SC Must Change Steering Angle Only When Required
   :id: SG_18
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain current safe steering angle

   The Steering Controller must change steering angle only when required.
   Unintended steering changes are extremely hazardous.

.. safety_goal:: SC Must Hold Steering Angle When Required
   :id: SG_19
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Maintain stable steering position

   The Steering Controller must hold steering angle when required to maintain
   straight-line travel or constant-radius turns.

.. safety_goal:: SC Must Hold Steering Angle Only When Required
   :id: SG_20
   :asil: D
   :mitigates: HAZ_TRAJ_DEV
   :status: open
   :safe_state: Allow necessary steering adjustments

   The Steering Controller must hold steering angle only when required. Locked
   steering prevents necessary corrections and causes trajectory deviation.

Next Steps
----------

Each of these 20 safety goals is decomposed into Functional Safety Requirements
(FSRs) that specify concrete system behaviors. See :doc:`fsr` for the detailed
requirements.
