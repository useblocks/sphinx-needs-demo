{% set page="system_requirements.rst" %}
{% include "demo_page_header.rst" with context %}

🏗️ System Requirements (SYSREQ)
=================================

System Requirements specify concrete system capabilities, performance metrics,
and architectural characteristics that implement Functional Safety Requirements.
SYSREQs are technology-aware and define measurable system properties.

**Traceability Chain:** HAZ → SG → FSR → **SYSREQ** → (SWREQ/HWREQ)

System requirements:

- Define specific performance metrics and bounds
- Specify architectural approaches (redundancy, algorithms)
- Remain implementation-independent but technology-aware
- Inherit ASIL from parent FSRs
- Form the basis for software and hardware requirements

SYSREQ Overview
---------------

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname
   :columns: id, title, asil, implements
   :style: table

Vehicle Dynamics Controller System Requirements
------------------------------------------------

.. sysreq:: VDC Trajectory Tracking Accuracy
   :id: SYSREQ_VDC_01
   :asil: D
   :implements: FSR_VDC_CTRL_01
   :status: open

   The VDC shall track the commanded trajectory with maximum lateral error ≤0.5m
   and longitudinal error ≤0.3m at speeds up to 130 km/h under nominal conditions.
   Performance degradation allowed under adverse conditions (reduced visibility,
   low friction surfaces) with notification to supervision layer.

.. sysreq:: VDC Dual-Redundant Processing Architecture
   :id: SYSREQ_VDC_02
   :asil: D
   :implements: FSR_VDC_CTRL_03
   :status: open

   The VDC shall implement dual-redundant processing with two independent processors
   executing diverse control algorithms. Cross-checking shall occur every control
   cycle (10ms) with automatic switchover to healthy processor within 20ms upon
   detection of discrepancy >10%.

.. sysreq:: VDC Multi-Sensor Fusion System
   :id: SYSREQ_VDC_03
   :asil: D
   :implements: FSR_VEHICLE_SENS_01, FSR_VEHICLE_SENS_02
   :status: open

   The VDC shall implement sensor fusion combining IMU (6-axis accelerometer/gyro),
   individual wheel speed sensors, and GNSS/INS using Extended Kalman Filter.
   System shall detect sensor failures within 100ms and maintain state estimation
   with degraded accuracy using remaining sensors.

.. sysreq:: VDC Graceful Degradation Controller
   :id: SYSREQ_VDC_04
   :asil: D
   :implements: FSR_VDC_CTRL_04
   :status: open

   The VDC shall maintain trajectory control capability with single actuator or
   sensor failure. Degraded modes: (1) Single wheel actuator failure: redistribute
   torque to remaining wheels; (2) Steering actuator failure: trajectory control
   via differential braking; (3) Single sensor failure: continue with reduced accuracy.

Wheel Rotational Dynamics Controller System Requirements
---------------------------------------------------------

.. sysreq:: WRDC Single Wheel Fault Tolerance
   :id: SYSREQ_WRDC_01
   :asil: D
   :implements: FSR_WRDC_CTRL_01
   :status: open

   The WRDC shall compensate for failed wheel actuator through coordinated control
   of remaining three wheels. System shall detect actuator failure within 50ms
   (via feedback comparison) and redistribute target torques to maintain yaw
   stability within ±2° and lateral acceleration within ±0.5 m/s² of commanded values.

.. sysreq:: WRDC Tire Friction Estimation System
   :id: SYSREQ_WRDC_02
   :asil: D
   :implements: FSR_WRDC_CTRL_03
   :status: open

   The WRDC shall implement real-time tire-road friction coefficient (µ) estimation
   with ±10% accuracy across all surface conditions (dry asphalt µ=1.0 to ice µ=0.2).
   Estimation algorithm shall use wheel slip ratio, longitudinal/lateral forces,
   and vehicle dynamics model. Update rate: 100Hz.

.. sysreq:: WRDC ABS/ASR Coordination Logic
   :id: SYSREQ_WRDC_03
   :asil: D
   :implements: FSR_WRDC_CTRL_01
   :status: open

   The WRDC shall implement integrated anti-lock braking (ABS) and anti-slip
   regulation (ASR) with coordinated control logic. Wheel lock detection threshold:
   slip ratio >0.15. Wheel spin detection threshold: slip ratio >0.10. Control
   response time from detection to pressure modulation: <20ms.

.. sysreq:: WRDC High-Frequency Control Loop
   :id: SYSREQ_WRDC_04
   :asil: D
   :implements: FSR_WRDC_CTRL_04
   :status: open

   The WRDC control loop shall execute with 5ms cycle time and maximum jitter
   ±0.5ms. Sensor data age shall not exceed 10ms. Anti-lock and anti-spin response
   time from wheel slip detection to first pressure modulation: <20ms.

Steering Controller System Requirements
----------------------------------------

.. sysreq:: Steering Robust Control Algorithm
   :id: SYSREQ_STEER_01
   :asil: D
   :implements: FSR_STEER_CTRL_01
   :status: open

   The steering controller shall implement H-infinity robust control algorithm
   with guaranteed stability and performance under parameter variations of ±20%
   from nominal values. Parameters include: steering inertia, friction, assist
   motor torque constant, and rack geometry. Control bandwidth: 10Hz minimum.

.. sysreq:: Steering Validated Dynamics Model
   :id: SYSREQ_STEER_02
   :asil: D
   :implements: FSR_STEER_CTRL_02
   :status: open

   The steering system shall use physics-based dynamics model validated through
   physical testing with maximum modeling error <5% across operational envelope:
   steering angle ±540°, steering rate ±200°/s, vehicle speed 0-130 km/h,
   lateral acceleration ±8 m/s².

.. sysreq:: Steering Redundant Execution Architecture
   :id: SYSREQ_STEER_03
   :asil: D
   :implements: FSR_STEER_CTRL_03
   :status: open

   The steering controller shall implement dual-channel architecture with
   independent power supplies, processors, and motor windings. Each channel
   capable of providing minimum 50% of maximum steering torque. Channels operate
   in active-active mode with continuous cross-monitoring. Switchover time <10ms.

.. sysreq:: Steering High-Resolution Feedback System
   :id: SYSREQ_STEER_04
   :asil: D
   :implements: FSR_STEER_SENS_03
   :status: open

   The steering system shall provide redundant position and velocity feedback
   with specifications: position accuracy ±0.5° (absolute), velocity accuracy
   ±1°/s, update rate 1kHz, latency <1ms. Dual absolute encoders with diverse
   sensing principles (magnetic + optical).

Brake Controller System Requirements
-------------------------------------

.. sysreq:: Brake Dual-Circuit Hydraulic Architecture
   :id: SYSREQ_BRAKE_01
   :asil: D
   :implements: FSR_BRAKE_CTRL_02
   :status: open

   The brake system shall implement X-split dual hydraulic circuits (FL-RR,
   FR-RL) with independent pressure generation and control. Each circuit shall
   be capable of achieving minimum 0.3g deceleration independently. Electronic
   control units are dual-redundant with independent power supplies.

.. sysreq:: Brake Surface Friction Adaptation
   :id: SYSREQ_BRAKE_02
   :asil: D
   :implements: FSR_BRAKE_CTRL_01
   :status: open

   The brake controller shall adapt pressure modulation strategy based on
   estimated surface friction coefficient across full range µ=0.2 (ice) to
   µ=1.0 (dry asphalt). Adaptation includes: brake force distribution, pressure
   ramp rates, and ABS threshold tuning. Transition time between friction
   regimes: <100ms.

.. sysreq:: Brake Component Monitoring System
   :id: SYSREQ_BRAKE_03
   :asil: D
   :implements: FSR_BRAKE_PROC_02
   :status: open

   The brake system shall continuously monitor: brake pad wear (thickness sensors),
   hydraulic fluid level and pressure, brake disc temperature (IR sensors),
   actuator health (current, position feedback, response time). Monitoring cycle:
   100ms. Fault detection and reporting to VDC within 200ms.

Drive Controller System Requirements
-------------------------------------

.. sysreq:: Drive Torque Control System
   :id: SYSREQ_DRIVE_01
   :asil: D
   :implements: FSR_DRIVE_CTRL_01
   :status: open

   The drive controller shall maintain torque control accuracy ±5% of commanded
   value across full speed-torque envelope: 0-200 km/h, -100% to +100% torque
   (regen to full power). Control bandwidth: 20Hz. Response time from command
   to 90% torque achievement: <150ms.

.. sysreq:: Drive Limp-Home Mode Architecture
   :id: SYSREQ_DRIVE_02
   :asil: D
   :implements: FSR_DRIVE_CTRL_03
   :status: open

   The drive system shall implement fail-operational architecture with graceful
   degradation to limp-home mode upon component failure. Limp-home mode capabilities:
   minimum 20% of maximum torque, maximum speed 30 km/h, sufficient power to
   reach safe stopping location. Mode transition time: <500ms.

.. sysreq:: Drive Electrical and Thermal Protection
   :id: SYSREQ_DRIVE_03
   :asil: D
   :implements: FSR_DRIVE_PROC_02
   :status: open

   The drive controller shall implement protection systems: (1) Overspeed: limit
   at 210 km/h with soft cutoff; (2) Overcurrent: inverter current limit with
   10µs response time; (3) Overtemperature: motor 180°C, inverter 125°C with
   thermal derating starting at 80% limits. All limits shall trigger safe state
   transition and fault reporting.

Implementation Notes
--------------------

These 18 system requirements bridge the gap between functional safety requirements
(FSRs) and implementation-level requirements. They will be further decomposed into:

**Software Requirements (SWREQ)**
   - Control algorithms and signal processing
   - Diagnostic and monitoring software
   - Safety mechanisms (checksums, watchdogs, voting)
   - State machines and fault management

**Hardware Requirements (HWREQ)**
   - ECU specifications (processing power, memory, I/O)
   - Sensor and actuator specifications
   - Power supply architecture
   - Physical interfaces and connectors

**Interface Requirements (IFREQ)**
   - Communication protocols (CAN, FlexRay, Ethernet)
   - Message formats and timing
   - Diagnostic protocols (UDS, XCP)

.. note::

   **Example of Further Decomposition**

   For a detailed example of how system requirements are further decomposed into
   architectural and software requirements following the V-Model development process,
   see the :doc:`/automotive-adas/index` example. That example demonstrates:

   - System architecture design and component decomposition
   - Software requirement analysis and detailed design
   - Software unit implementation and testing
   - Integration testing at both software and system levels
   - Qualification testing and traceability

   The automotive-adas example shows the complete V-Model workflow from system
   requirements through implementation and back up through verification and validation.

Verification and Validation
----------------------------

Each system requirement shall be verified through appropriate methods per ASIL D:

**Analysis and Simulation**
   - Model-in-the-Loop (MIL) testing of control algorithms
   - Fault injection simulation for redundancy verification
   - Timing analysis for real-time constraints

**Hardware-in-the-Loop Testing**
   - Controller validation with real actuators and sensors
   - Fault tolerance testing with component failures
   - Environmental stress testing (temperature, vibration, EMI)

**Vehicle Integration Testing**
   - Closed test track validation
   - Edge case scenarios (low friction, emergency maneuvers)
   - Long-duration reliability testing

**ISO 26262 Compliance**
   - Requirements traceability to FSRs
   - Architectural safety analysis (FMEA, FTA)
   - Verification coverage per ASIL D targets
   - Independent safety assessment

.. seealso::

   **ISO 26262-4:2018** - Product development at the system level

   **ISO 26262-5:2018** - Product development at the hardware level

   **ISO 26262-6:2018** - Product development at the software level

   Research paper: Stolte, Bagschik, Maurer, "Safety Goals and Functional Safety
   Requirements for Actuation Systems of Automated Vehicles," IEEE ITSC 2016
