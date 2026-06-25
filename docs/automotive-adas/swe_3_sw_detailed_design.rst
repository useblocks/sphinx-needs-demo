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

Customer calibration (variant-specific)
---------------------------------------
The lane-keeping and cruise-control thresholds are customer-specific. Each
customer build traces a *single* calibration source file, so only the
implementation relevant to the active variant (``{{ variant }}``) is shown
below and linked upward to :need:`SWREQ_002` and :need:`SWREQ_005`. Rebuild with
``-t customer_a`` / ``-t customer_b`` (or no tag for the baseline) to swap the
traced file.

.. src-trace::
   :project: adas
   :file: calibration_{{ variant }}.c

Automodule example
------------------
Using **Python** language.


.. automodule:: automotive_adas
   :members:
   :undoc-members:
   :show-inheritance:
