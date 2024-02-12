{% set page="test_runs.rst" %}
{% include "../demo_page_header.rst" with context %}

Test Runs Teen
==============

Overview
--------

.. test-results:: teen_car/test_run_1.xml

Details
-------

.. test-file:: My Test Data
   :file: teen_car/test_run_1.xml
   :id: TESTFILE_1
   :auto_suites:
   :auto_cases:

    Used test xml data: 

   .. literalinclude:: test_run_1.xml
