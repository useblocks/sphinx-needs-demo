{% set page="swe_4_unit_tests.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE4_Test_Case_Documentation:


SWE.4 Unit Tests
================

This document provides the test case documentation for the software functionalities as
per SWE.1 and SWE.2 requirements.

.. test:: Speed Limit Validation Test
   :id: TEST_VARIANT_001
   :status: open
   :links: REQ_017, SWREQ_005
   :author: THOMAS
   :test_type: unit

   Verify that the speed controller correctly enforces the regional speed limit
   of :variant:`region.speed_limit_highway` :variant:`region.speed_unit`.

   **Expected behavior varies by region:**

   .. if:: var.region.area == "eu"

      - Maximum speed: 130 km/h (EU regulation)
      - Speed tolerance: ±5 km/h
      - Test procedure: Accelerate to 135 km/h and verify speed limiter activates

   .. if:: var.region.area == "america"

      - Maximum speed: 75 mph (US regulation)
      - Speed tolerance: ±3 mph
      - Test procedure: Accelerate to 78 mph and verify speed limiter activates

.. automodule:: automotive_adas_tests
   :members:
   :undoc-members:
   :show-inheritance:
