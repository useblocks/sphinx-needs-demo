Safety Feature View
===================

This document provides a **vertical, feature-level view** of the
safety functionality in the BrewMaster Pro 3000. While the
architecture document presents a horizontal, layer-by-layer
decomposition, this view cuts through all layers to show how the
safety feature is realised end-to-end — from the system-level safety
requirement down to architectural components, interfaces, and
verification tests.

This perspective is particularly relevant for functional safety
engineers performing impact analysis: any change to a safety-related
element can be traced upward to the customer need it protects, and
downward to every component and test that must be reviewed.

Full Safety Chain
-----------------

The following diagram shows the complete vertical traceability of the
safety feature — from the system requirement through software
requirements, architectural components, interfaces, and test cases.

.. needflow::
   :filter: docname is not None and "coffee-machine" in docname and ("safety" in tags or "critical" in tags)
   :show_link_names:
   :config: toptobottom

System-Level Safety Requirement
-------------------------------

The safety feature originates from a single system-level requirement
that mandates automatic shutdown under hazardous conditions:

.. needtable:: Safety System Requirements
   :filter: type == "req" and "coffee-machine" in docname and "safety" in tags
   :columns: id, title, status, tags
   :style: table

Software Safety Requirements
----------------------------

The system-level safety requirement is decomposed into two independent
software requirements — one addressing thermal hazards and one
addressing dry-run prevention:

.. needtable:: Safety SW Requirements
   :filter: type == "swreq" and "coffee-machine" in docname and "safety" in tags
   :columns: id, title, status, reqs as "Traces to System Req"
   :style: table

The following diagram shows how these software requirements refine the
system requirement:

.. needflow::
   :filter: docname is not None and ("coffee-machine" in docname) and ((type == "req" and "safety" in tags) or (type == "swreq" and "safety" in tags))
   :show_link_names:
   :config: toptobottom

Safety Architecture
-------------------

The software requirements are implemented by the Safety Monitor
Module, which resides in its own dedicated Safety Layer — isolated
from application and control logic. The Safety Monitor observes all
other subsystems through status interfaces and can override them via
the Safety Command Interface.

.. needflow::
   :filter: docname is not None and ("coffee-machine" in docname) and ((type == "swreq" and "safety" in tags) or id in ["COMP_SAFETY_MON", "LAYER_SAFETY", "INTF_SAFETY_CMD", "INTF_TEMP_CTRL_STATUS", "INTF_BREW_CTRL_STATUS", "INTF_SENSOR_DATA"])
   :show_link_names:
   :config: toptobottom

The table below summarises the safety-relevant architectural elements
and their roles:

.. needtable:: Safety Architecture Elements
   :filter: "coffee-machine" in docname and type in ["component", "interface"] and "safety" in tags
   :columns: id, title, type_name as "Type", status
   :style: table

Safety Verification
-------------------

The following test cases verify the safety requirements. Each test is
linked back to the software requirements it covers:

.. needtable:: Safety Test Cases
   :filter: type == "test" and "coffee-machine" in docname and "safety" in tags
   :columns: id, title, status, specs as "Verifies"
   :style: table

Safety Shutdown Sequence
^^^^^^^^^^^^^^^^^^^^^^^^

The following sequence diagram shows the runtime behaviour when the
Safety Monitor detects an over-temperature condition. It issues an ``EMERGENCY_STOP``
command on ``INTF_SAFETY_CMD`` to all controlled subsystems. All
modules must respond within 100 ms.

.. needsequence:: Safety Shutdown Sequence
   :start: COMP_ADC_DRV
   :link_types: shutdown_calls

Complete Safety Traceability
----------------------------

The diagram below shows the full vertical chain from system
requirement through to test verification, demonstrating complete
bidirectional traceability of the safety feature:

.. needflow::
   :filter: docname is not None and ("coffee-machine" in docname) and ((type == "req" and "safety" in tags) or (type == "swreq" and "safety" in tags) or id in ["COMP_SAFETY_MON", "INTF_SAFETY_CMD"] or (type == "test" and "safety" in tags))
   :show_link_names:
   :config: toptobottom

Coverage Summary
----------------

.. needpie:: Safety Needs by Type
   :labels: System Reqs, SW Reqs, Components, Interfaces, Tests
   :legend:

   type == "req" and "coffee-machine" in docname and "safety" in tags
   type == "swreq" and "coffee-machine" in docname and "safety" in tags
   type == "component" and "coffee-machine" in docname and "safety" in tags
   type == "interface" and "coffee-machine" in docname and "safety" in tags
   type == "test" and "coffee-machine" in docname and "safety" in tags
