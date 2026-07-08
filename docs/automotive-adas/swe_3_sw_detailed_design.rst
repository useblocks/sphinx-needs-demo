{% set page="swe_3_sw_detailed_design.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE3_Code_Documentation:

SWE.3 Detailed Design
=====================

This document provides the software implementation documentation as per SWE.1 and SWE.2 requirements.

Codelinks example
------------------
Using **C** language.

.. src-trace::
   :project: adas

Calibration profile (variant-specific)
--------------------------------------
The lane-keeping and cruise-control thresholds depend on the **combination** of
both variant dimensions — the ``location`` (``{{ location }}``) and the vehicle
``type`` (``{{ type }}``). That combination collapses to a single calibration
profile (``{{ profile }}``), and each build traces exactly *one* calibration
source file, so only the implementation relevant to the active profile is shown
below and linked upward to :need:`SWREQ_002` and :need:`SWREQ_005`. Rebuild with
a different ``-t <location> -t <type>`` pair (or no tag for the EU / combi
reference) to swap the traced file.

.. src-trace::
   :project: adas
   :file: calibration_{{ profile }}.c

Automodule example
------------------
Using **Python** language.


.. automodule:: automotive_adas
   :members:
   :undoc-members:
   :show-inheritance:
