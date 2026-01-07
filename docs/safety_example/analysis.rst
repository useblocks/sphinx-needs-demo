{% set page="analysis.rst" %}
{% include "demo_page_header.rst" with context %}

📊 Safety Traceability Analysis
================================

This page provides comprehensive visualization and analysis of the complete safety
artifact traceability chain from hazards through safety goals and functional safety
requirements to system requirements.

Complete Safety Traceability
-----------------------------

This diagram shows the complete traceability from the top-level hazard through all
20 safety goals, 30+ functional safety requirements, to 18 system requirements.

.. needflow::
   :tags: safety_example
   :types: hazard,safety_goal,fsr,sysreq
   :show_link_names:
   :link_types: mitigates,derives_from,implements
   :scale: 80

Safety Artifacts Overview
--------------------------

Complete list of all safety artifacts with key metadata.

.. needtable::
   :filter: docname is not None and "safety_example" in docname
   :columns: id, type_name, title, asil, status
   :style: table
   :sort: type

ASIL Distribution Analysis
---------------------------

Distribution of Safety Artifacts by Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: Safety Artifacts by Type
   :labels: Hazards, Safety Goals, FSRs, SYSREQs

   type == "hazard" and docname is not None and "safety_example" in docname
   type == "safety_goal" and docname is not None and "safety_example" in docname
   type == "fsr" and docname is not None and "safety_example" in docname
   type == "sysreq" and docname is not None and "safety_example" in docname

Safety Goals by Subsystem
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. needpie:: Safety Goals by Subsystem
   :labels: VDC, WRDC, Drive, Brake, Steering

   type == "safety_goal" and docname is not None and "safety_example" in docname and (id == "SG_01" or id == "SG_02" or id == "SG_03" or id == "SG_04")
   type == "safety_goal" and docname is not None and "safety_example" in docname and (id == "SG_05" or id == "SG_06" or id == "SG_07" or id == "SG_08" or id == "SG_09" or id == "SG_10" or id == "SG_11" or id == "SG_12")
   type == "safety_goal" and docname is not None and "safety_example" in docname and (id == "SG_13" or id == "SG_14")
   type == "safety_goal" and docname is not None and "safety_example" in docname and (id == "SG_15" or id == "SG_16")
   type == "safety_goal" and docname is not None and "safety_example" in docname and (id == "SG_17" or id == "SG_18" or id == "SG_19" or id == "SG_20")

FSRs by Subsystem
~~~~~~~~~~~~~~~~~

.. needpie:: FSRs by Subsystem
   :labels: Steering, Brake, Drive, WRDC, VDC, Sensors, Power, Process

   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_STEER")
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_BRAKE")
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_DRIVE")
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_WRDC")
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_VDC")
   type == "fsr" and docname is not None and "safety_example" in docname and (id.startswith("FSR_VEHICLE_SENS") or id.startswith("FSR_WHEEL_SENS"))
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_POWER")
   type == "fsr" and docname is not None and "safety_example" in docname and id.startswith("FSR_PROC")

Critical Path Analysis
-----------------------

Vehicle Dynamics Controller Critical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from hazard through VDC safety goals to VDC FSRs.

.. needflow::
   :filter: (id == "HAZ_TRAJ_DEV") or (type == "safety_goal" and (id == "SG_01" or id == "SG_02" or id == "SG_03" or id == "SG_04")) or (type == "fsr" and id.startswith("FSR_VDC"))
   :show_link_names:
   :link_types: mitigates,derives_from
   :scale: 90

Wheel Rotational Dynamics Controller Critical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from hazard through WRDC safety goals to WRDC FSRs.

.. needflow::
   :filter: (id == "HAZ_TRAJ_DEV") or (type == "safety_goal" and (id == "SG_05" or id == "SG_06" or id == "SG_07" or id == "SG_08" or id == "SG_09" or id == "SG_10" or id == "SG_11" or id == "SG_12")) or (type == "fsr" and id.startswith("FSR_WRDC"))
   :show_link_names:
   :link_types: mitigates,derives_from
   :scale: 90

Steering System Critical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from hazard through steering safety goals to steering FSRs.

.. needflow::
   :filter: (id == "HAZ_TRAJ_DEV") or (type == "safety_goal" and (id == "SG_17" or id == "SG_18" or id == "SG_19" or id == "SG_20")) or (type == "fsr" and id.startswith("FSR_STEER"))
   :show_link_names:
   :link_types: mitigates,derives_from
   :scale: 90

Brake System Critical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from hazard through brake safety goals to brake FSRs.

.. needflow::
   :filter: (id == "HAZ_TRAJ_DEV") or (type == "safety_goal" and (id == "SG_15" or id == "SG_16")) or (type == "fsr" and id.startswith("FSR_BRAKE"))
   :show_link_names:
   :link_types: mitigates,derives_from
   :scale: 90

Drive System Critical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Traceability from hazard through drive safety goals to drive FSRs.

.. needflow::
   :filter: (id == "HAZ_TRAJ_DEV") or (type == "safety_goal" and (id == "SG_13" or id == "SG_14")) or (type == "fsr" and id.startswith("FSR_DRIVE"))
   :show_link_names:
   :link_types: mitigates,derives_from
   :scale: 90

Safety Goal Coverage
---------------------

Coverage of Safety Goals by FSRs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This table shows which FSRs derive from each safety goal, providing visibility
into requirement decomposition completeness.

.. needtable::
   :filter: type == "safety_goal" and docname is not None and "safety_example" in docname
   :columns: id, title, derives_from_back
   :style: table
   :colwidths: 15, 45, 40

FSR Completeness Analysis
--------------------------

FSRs by Category
~~~~~~~~~~~~~~~~

Controller FSRs
^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname and "Controller" in title
   :columns: id, title, asil, status
   :style: table

Sensor FSRs
^^^^^^^^^^^

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname and "Sensor" in title
   :columns: id, title, asil, status
   :style: table

Process FSRs
^^^^^^^^^^^^

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname and ("Process" in title or "Component" in title)
   :columns: id, title, asil, status
   :style: table

Power Supply FSRs
^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname and "Power" in title
   :columns: id, title, asil, status
   :style: table

FSR Implementation Coverage
----------------------------

This table shows which System Requirements implement each FSR, providing visibility
into the decomposition from functional safety requirements to concrete system specifications.

.. needtable::
   :filter: type == "fsr" and docname is not None and "safety_example" in docname
   :columns: id, title, implements_back
   :style: table
   :colwidths: 15, 45, 40

System Requirements Analysis
-----------------------------

SYSREQs by Subsystem
~~~~~~~~~~~~~~~~~~~~

.. needpie:: System Requirements by Subsystem
   :labels: VDC, WRDC, Steering, Brake, Drive

   type == "sysreq" and docname is not None and "safety_example" in docname and "VDC" in id
   type == "sysreq" and docname is not None and "safety_example" in docname and "WRDC" in id
   type == "sysreq" and docname is not None and "safety_example" in docname and "STEER" in id
   type == "sysreq" and docname is not None and "safety_example" in docname and "BRAKE" in id
   type == "sysreq" and docname is not None and "safety_example" in docname and "DRIVE" in id

VDC System Requirements
^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname and "VDC" in id
   :columns: id, title, asil, status
   :style: table

WRDC System Requirements
^^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname and "WRDC" in id
   :columns: id, title, asil, status
   :style: table

Steering System Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname and "STEER" in id
   :columns: id, title, asil, status
   :style: table

Brake System Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname and "BRAKE" in id
   :columns: id, title, asil, status
   :style: table

Drive System Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. needtable::
   :filter: type == "sysreq" and docname is not None and "safety_example" in docname and "DRIVE" in id
   :columns: id, title, asil, status
   :style: table

ASIL D Requirements Summary
----------------------------

All safety artifacts in this example are assigned ASIL D, the highest automotive
safety integrity level. This demonstrates the safety-critical nature of vehicle
actuation systems in automated driving.

**Total Safety Artifacts:**

- **1** Hazard (HAZ_TRAJ_DEV)
- **20** Safety Goals (SG_01 to SG_20)
- **30+** Functional Safety Requirements
- **18** System Requirements

**ISO 26262 Compliance:**

- All hazards have ASIL assignment with rationale
- All safety goals mitigate identified hazards
- All FSRs derive from safety goals
- All SYSREQs implement FSRs with concrete specifications
- Complete traceability chain maintained (HAZ → SG → FSR → SYSREQ)
- Schema validation ensures compliance

**STPA-Based Derivation:**

This example demonstrates the STPA (System-Theoretic Process Analysis) methodology
applied to vehicle actuation systems:

1. **Control Structure Analysis**: Hierarchical control from trajectory input through
   VDC/WRDC to individual actuators
2. **Unsafe Control Actions**: Systematic identification of "when required" and
   "only when required" conditions
3. **Causal Factor Analysis**: Control loop components (sensors, processes, controllers,
   actuators) analyzed for failure modes
4. **Requirement Derivation**: Safety goals and FSRs derived from causal factors

Verification and Validation
----------------------------

The safety artifacts in this example would typically be verified through:

- **Requirements Review**: Completeness, consistency, correctness
- **Design Review**: Architectural safety mechanisms, fault tolerance
- **FMEA/FTA**: Failure modes and fault trees analysis
- **Hardware-in-the-Loop Testing**: Controller validation with real actuators
- **Vehicle Testing**: Full system validation on test track
- **ISO 26262 Audit**: Independent safety assessment

.. seealso::

   **ISO 26262-3:2018** - Concept phase (HARA, safety goals)

   **ISO 26262-4:2018** - Product development at system level (FSRs, system architecture)

   **ISO 26262-6:2018** - Product development at software level

   Research paper: Stolte, Bagschik, Maurer, "Safety Goals and Functional Safety
   Requirements for Actuation Systems of Automated Vehicles," IEEE ITSC 2016
