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

Variant-specific code
---------------------

The turn-signal priority logic exists as one implementation file per
``steering`` variant: ``src/c/variants/turn_signal_left.c`` (traces to
``SWREQ_028``) and ``src/c/variants/turn_signal_right.c`` (traces to
``SWREQ_029``). Only the file matching the selected variant is loaded and
analysed by sphinx-codelinks — the other variant's file is not part of this
build at all, exactly like the software requirement it implements.

.. variant-raw-rst-start

.. if:: var.vehicle.steering_side == "left"

   .. src-trace::
      :project: adas
      :file: variants/turn_signal_left.c

.. if:: var.vehicle.steering_side == "right"

   .. src-trace::
      :project: adas
      :file: variants/turn_signal_right.c

.. variant-raw-rst-end

Automodule example
------------------
Using **Python** language.


.. automodule:: automotive_adas
   :members:
   :undoc-members:
   :show-inheritance:
