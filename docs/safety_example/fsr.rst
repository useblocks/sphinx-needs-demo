{% set page="fsr.rst" %}
{% include "demo_page_header.rst" with context %}

📋 Functional Safety Requirements (FSR)
========================================

Functional Safety Requirements are specific, verifiable requirements decomposed
from safety goals. FSRs:

- Detail what the system must functionally do
- Are more specific than safety goals
- Remain technology-agnostic (not implementation-specific)
- Inherit ASIL from parent safety goals
- Form the basis for technical safety requirements and implementation

These FSRs are derived from the TU Braunschweig research using STPA causal factor
analysis of the control loop components: sensors, processes, controllers, and actuators.

FSR Overview
------------

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname
   :columns: id, title, asil, derives_from
   :style: table

Traceability by ASIL
--------------------

.. needpie:: FSRs by ASIL Level
   :labels: ASIL D

   type == "fsr" and docname is not None and "safety_example" in docname and asil == "D"

Steering System FSRs
--------------------

Steering Controller FSRs
~~~~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Steering Controller Robust Control Algorithm
   :id: FSR_STEER_CTRL_01
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Control algorithm must be robust against uncertainties of the steering
   dynamics model and disturbances. Algorithm shall maintain stability and
   performance under model parameter variations of ±20%.

.. fsr:: Steering Controller Validated Dynamics Model
   :id: FSR_STEER_CTRL_02
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Sufficiently precise and validated steering dynamics model. Model accuracy
   shall be verified through physical testing with maximum error <5% across
   the operational envelope.

.. fsr:: Steering Controller Fail-Operational Design
   :id: FSR_STEER_CTRL_03
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Fail-operational design of steering controller. Single-point failures shall
   not cause loss of steering control. Redundant execution paths required.

.. fsr:: Steering Controller Timing Requirements
   :id: FSR_STEER_CTRL_04
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Operation must be provided in required cycle time and jitter. Control loop
   execution time: 10ms ± 1ms. Maximum jitter: 500µs.

Steering Sensors FSRs
~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Steering Sensor Feedback Compensation
   :id: FSR_STEER_SENS_01
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Inadequate or missing feedback must be recognized and compensated for.
   Sensor plausibility checks with redundant measurements. Timeout detection: 50ms.

.. fsr:: Steering Sensor Power Supply
   :id: FSR_STEER_SENS_02
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Continuous and sufficient power supply for steering-internal sensors.
   Redundant power supply with automatic switchover <10ms.

.. fsr:: Steering Sensor Measurement Accuracy
   :id: FSR_STEER_SENS_03
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Sufficient measurement accuracy for steering operation. Position accuracy:
   ±0.5°, velocity accuracy: ±1°/s.

Steering Process FSRs
~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Steering Mechanical Design
   :id: FSR_STEER_PROC_01
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Electrical and mechanical design according to state of the art. Components
   shall meet automotive standards (ISO 26262, ISO 16750).

.. fsr:: Steering Component Monitoring
   :id: FSR_STEER_PROC_02
   :asil: D
   :derives_from: SG_17, SG_18, SG_19, SG_20
   :status: open

   Monitoring of electrical and mechanical components and report to superordinate
   controller. Motor current, temperature, position sensor health monitored at 100Hz.

Brake System FSRs
-----------------

Brake Controller FSRs
~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Brake Controller Robust Algorithm
   :id: FSR_BRAKE_CTRL_01
   :asil: D
   :derives_from: SG_15, SG_16
   :status: open

   Control algorithm robust against uncertainties of the brake dynamics model
   and disturbances. Performance maintained under friction coefficient variations
   (µ=0.2 to µ=1.0).

.. fsr:: Brake Controller Fail-Operational Design
   :id: FSR_BRAKE_CTRL_02
   :asil: D
   :derives_from: SG_15, SG_16
   :status: open

   Fail-operational design of brake controller. Independent brake circuits with
   separate power supplies. Each circuit capable of achieving minimum 0.3g deceleration.

.. fsr:: Brake Controller Operational Monitoring
   :id: FSR_BRAKE_CTRL_03
   :asil: D
   :derives_from: SG_15, SG_16
   :status: open

   Monitoring of operational state of brake controller and process and report
   to superordinate controller. Status reported every 10ms with fault detection <100ms.

Brake Process FSRs
~~~~~~~~~~~~~~~~~~

.. fsr:: Brake System Design Limits
   :id: FSR_BRAKE_PROC_01
   :asil: D
   :derives_from: SG_05, SG_06, SG_15, SG_16
   :status: open

   Brake controller must recognize brakes operating beyond design limits and
   react appropriately. Maximum pressure, temperature, duty cycle monitoring
   with protective actions.

.. fsr:: Brake Component Health Monitoring
   :id: FSR_BRAKE_PROC_02
   :asil: D
   :derives_from: SG_15, SG_16
   :status: open

   Monitoring of electrical and mechanical brake components with reporting to
   VDC. Pad wear, fluid level, actuator health, sensor status monitored continuously.

Drive System FSRs
-----------------

Drive Controller FSRs
~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Drive Controller Robust Algorithm
   :id: FSR_DRIVE_CTRL_01
   :asil: D
   :derives_from: SG_13, SG_14
   :status: open

   Control algorithm robust against uncertainties of the drive dynamics model
   and disturbances. Torque control accuracy ±5% under all conditions.

.. fsr:: Drive Controller Validated Model
   :id: FSR_DRIVE_CTRL_02
   :asil: D
   :derives_from: SG_13, SG_14
   :status: open

   Sufficiently precise and validated drive dynamics model. Process variables
   must comply with the physical process state. Model verified across full
   speed and torque range.

.. fsr:: Drive Controller Fail-Operational Design
   :id: FSR_DRIVE_CTRL_03
   :asil: D
   :derives_from: SG_13, SG_14
   :status: open

   Fail-operational design of drive controller. Graceful degradation to limp-home
   mode with minimum 20% torque capability maintained.

Drive Process FSRs
~~~~~~~~~~~~~~~~~~

.. fsr:: Drive Component Monitoring
   :id: FSR_DRIVE_PROC_01
   :asil: D
   :derives_from: SG_07, SG_08, SG_13, SG_14
   :status: open

   Monitoring of electrical/mechanical drive components and report to WRDC.
   Motor temperature, inverter status, gear health monitored at 50Hz.

.. fsr:: Drive System Design Limits
   :id: FSR_DRIVE_PROC_02
   :asil: D
   :derives_from: SG_13, SG_14
   :status: open

   Drive controller must recognize drive operating beyond design limits and
   react appropriately. Overspeed, overcurrent, overtemperature protection active.

Wheel Rotational Dynamics Controller FSRs
------------------------------------------

.. fsr:: WRDC Fault-Tolerant Algorithm
   :id: FSR_WRDC_CTRL_01
   :asil: D
   :derives_from: SG_05, SG_06, SG_07, SG_08, SG_09, SG_10, SG_11, SG_12
   :status: open

   Fault-tolerant wheel rotational dynamics control algorithm. Algorithm shall
   detect and compensate for single wheel actuator failures while maintaining
   vehicle stability.

.. fsr:: WRDC Fail-Operational Design
   :id: FSR_WRDC_CTRL_02
   :asil: D
   :derives_from: SG_05, SG_06, SG_07, SG_08, SG_09, SG_10, SG_11, SG_12
   :status: open

   Fail-operational design of wheel rotational dynamics controller. Redundant
   processing elements with cross-monitoring. Switchover time <20ms.

.. fsr:: WRDC Precise Dynamics Model
   :id: FSR_WRDC_CTRL_03
   :asil: D
   :derives_from: SG_05, SG_06, SG_07, SG_08, SG_09, SG_10, SG_11, SG_12
   :status: open

   Sufficiently precise and validated wheel rotational dynamics model. Tire
   friction estimation accuracy ±10% across all surface conditions.

.. fsr:: WRDC Timing Requirements
   :id: FSR_WRDC_CTRL_04
   :asil: D
   :derives_from: SG_05, SG_06, SG_07, SG_08, SG_09, SG_10, SG_11, SG_12
   :status: open

   Operation must be provided in required cycle time and jitter. Control loop:
   5ms ± 0.5ms. Anti-lock/anti-spin response time <20ms.

Vehicle Dynamics Controller FSRs
---------------------------------

.. fsr:: VDC Robust Control Algorithm
   :id: FSR_VDC_CTRL_01
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Control algorithm robust against uncertainties of the vehicle dynamics model
   and disturbances. Trajectory tracking error <0.5m at speeds up to 130 km/h.

.. fsr:: VDC Validated Dynamics Model
   :id: FSR_VDC_CTRL_02
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Sufficiently precise and validated vehicle dynamics model. Process variables
   must comply with the physical process state. Model validated through
   hardware-in-the-loop testing.

.. fsr:: VDC Fail-Operational Design
   :id: FSR_VDC_CTRL_03
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Fail-operational design of vehicle dynamics controller. Dual-redundant
   processing with diverse algorithms. Cross-checking every cycle.

.. fsr:: VDC Fault-Tolerant Algorithm
   :id: FSR_VDC_CTRL_04
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Fault-tolerant vehicle dynamics control algorithm capable of handling
   degraded actuation (e.g., loss of one steering actuator or brake circuit).

Vehicle Motion Sensor FSRs
---------------------------

.. fsr:: Vehicle Motion Sensor Feedback
   :id: FSR_VEHICLE_SENS_01
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Inadequate or missing feedback must be recognized. Sensor fusion from multiple
   sources (IMU, wheel speeds, GNSS). Fault detection within 100ms.

.. fsr:: Vehicle Motion Sensor Accuracy
   :id: FSR_VEHICLE_SENS_02
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Sufficient measurement accuracy for vehicle dynamics control. Lateral
   acceleration: ±0.1 m/s², yaw rate: ±0.5°/s, velocity: ±0.1 m/s.

.. fsr:: Vehicle Motion Sensor Timing
   :id: FSR_VEHICLE_SENS_03
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Updated feedback available in required cycle time and jitter. Sensor data
   age <10ms, synchronized across all sensors with <1ms skew.

Wheel Motion Sensor FSRs
~~~~~~~~~~~~~~~~~~~~~~~~~

.. fsr:: Wheel Motion Sensor Compensation
   :id: FSR_WHEEL_SENS_01
   :asil: D
   :derives_from: SG_09, SG_10, SG_11, SG_12
   :status: open

   Inadequate or missing wheel speed feedback must be recognized and compensated.
   Redundant sensing per wheel with plausibility checking against vehicle sensors.

.. fsr:: Wheel Motion Sensor Power
   :id: FSR_WHEEL_SENS_02
   :asil: D
   :derives_from: SG_09, SG_10, SG_11, SG_12
   :status: open

   Continuous and sufficient power supply for wheel motion sensors. Battery-backed
   power during transients. Voltage regulation ±5%.

Process Dynamics FSRs
---------------------

.. fsr:: Vehicle Dynamics Control Action Consistency
   :id: FSR_PROC_CONFLICT_01
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04
   :status: open

   Control actions of the vehicle dynamics controller must target the same
   vehicle motion. Coordination logic prevents conflicting brake/drive commands.
   Maximum conflict resolution time: 10ms.

.. fsr:: Wheel Dynamics Brake-Drive Conflict Prevention
   :id: FSR_PROC_CONFLICT_02
   :asil: D
   :derives_from: SG_05, SG_06, SG_07, SG_08
   :status: open

   Exclusion of drive and brake actuation with conflicting targets. Hardware
   interlocks prevent simultaneous brake and drive application >10% torque.

Power Supply FSRs
-----------------

.. fsr:: Actuator Power Supply Continuity
   :id: FSR_POWER_01
   :asil: D
   :derives_from: SG_13, SG_14, SG_15, SG_16, SG_17, SG_18, SG_19, SG_20
   :status: open

   Continuous and sufficient power supply for all safety-critical actuators.
   Redundant power sources with automatic failover. Minimum hold-up time: 500ms.

.. fsr:: Controller Power Supply Continuity
   :id: FSR_POWER_02
   :asil: D
   :derives_from: SG_01, SG_02, SG_03, SG_04, SG_05, SG_06, SG_07, SG_08
   :status: open

   Continuous and sufficient power supply for VDC and WRDC. Independent power
   domains with galvanic isolation. Voltage monitoring and brown-out protection.

Implementation Notes
--------------------

These FSRs form the foundation for Technical Safety Requirements (TSRs) that
specify implementation details including:

- Hardware architecture and redundancy concepts
- Software safety mechanisms (checksums, watchdogs, voting)
- Diagnostic coverage targets per ASIL D requirements
- Safety response times and fail-safe behaviors

.. seealso::

   **ISO 26262-4:2018** - Product development at the system level

   **ISO 26262-6:2018** - Product development at the software level

   Research paper: Stolte et al., "Safety Goals and Functional Safety Requirements
   for Actuation Systems of Automated Vehicles," IEEE ITSC 2016
