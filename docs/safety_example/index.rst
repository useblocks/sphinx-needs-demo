{% set page="index.rst" %}
{% include "demo_page_header.rst" with context %}

🛡️ ISO 26262 Functional Safety Example
========================================

This example demonstrates the ISO 26262 functional safety development process
for vehicle actuation systems of automated vehicles, following the safety lifecycle
from Hazard Analysis and Risk Assessment (HARA) through Functional Safety
Requirement (FSR) derivation.

.. note::

   This example is based on real research from **TU Braunschweig** (Stolte, Bagschik, Maurer, 2016):
   *"Safety Goals and Functional Safety Requirements for Actuation Systems of Automated Vehicles"*
   presented at IEEE 19th International Conference on Intelligent Transportation Systems (ITSC).

System Scope
------------

**Vehicle Actuation Systems for Automated Vehicles**

The example focuses on safety requirements for vehicle actuation systems that perform
**trajectory follow control** for automated vehicles. The system includes:

- Vehicle Dynamics Controller (VDC)
- Wheel Rotational Dynamics Controller (WRDC)
- Steering Controller (SC)
- Brake Controller
- Drive Controller

These systems operate without human supervision (SAE Level 4/5 automation) and must
ensure functional safety through systematic hazard analysis and requirement derivation.

ISO 26262 Safety Process
-------------------------

This example demonstrates the following safety lifecycle phases:

**1. HARA (Hazard Analysis & Risk Assessment)**
   Identify hazardous events, assess severity (S), exposure (E), and controllability (C),
   and assign Automotive Safety Integrity Level (ASIL).

**2. Safety Goals**
   Define top-level safety requirements to mitigate identified hazards. Safety goals
   are technology-agnostic and assigned ASIL ratings from HARA.

**3. FSRs (Functional Safety Requirements)**
   Decompose safety goals into specific, verifiable functional requirements that
   describe what the system must do to achieve the safety goals.

**4. SYSREQs (System Requirements)**
   Define concrete system capabilities, performance metrics, and architectural
   characteristics that implement the FSRs in a technology-aware manner.

ASIL Levels
-----------

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - ASIL
     - Description
   * - QM
     - Quality Management (no safety requirements)
   * - A
     - Lowest safety integrity level
   * - B
     - Medium-low safety integrity level
   * - C
     - Medium-high safety integrity level
   * - D
     - Highest safety integrity level (most stringent)

STPA Methodology
----------------

The safety goals and functional safety requirements in this example were derived
using **STPA (System-Theoretic Process Analysis)**, a hazard analysis technique
based on systems theory. STPA systematically identifies:

- Unsafe control actions
- Causal factors for unsafe behavior
- Safety requirements at multiple levels of abstraction

Documentation Structure
-----------------------

.. toctree::
   :maxdepth: 1

   hara
   safety_goals
   fsr
   system_requirements
   analysis

Key Statistics
--------------

.. needpie:: Safety Artifacts by Type
   :labels: Hazards, Safety Goals, FSRs, SYSREQs

   type == "hazard" and "safety_example" in docname
   type == "safety_goal" and "safety_example" in docname
   type == "fsr" and "safety_example" in docname
   type == "sysreq" and "safety_example" in docname

.. warning::

   **Demonstration Purpose Only**

   This safety example is provided for demonstration and educational purposes to illustrate
   the capabilities of Sphinx-Needs for ISO 26262 safety documentation. The content is based
   on academic research and simplified for clarity.

   **This example should NOT be used as-is for real-world safety-critical systems without:**

   - Comprehensive hazard analysis specific to your system and operational design domain
   - Detailed engineering analysis and validation by qualified safety engineers
   - Full ISO 26262 compliance activities including independent safety assessment
   - Adaptation to your specific vehicle architecture, sensors, and actuators
   - Verification and validation per ASIL D requirements
   - Proper review and approval by your organization's safety management

   Real safety-critical automotive systems require rigorous engineering processes, independent
   audits, and certification activities that go far beyond this documentation example.
