{% set page="sys_5_sys_quali_test_results.rst" %}
{% include "demo_page_header.rst" with context %}

.. _sys_5_sys_quali_test_results:

SYS.5 Qualification Test Results
================================

.. test-file:: test file summary
   :id: TF_TEST_SYS_QUAL_TEST_SUMMARY
   :file: testsuites/junit.xml

.. test-run:: run test for Lane Detection Verification
   :id: TR_TEST_SYS_QUAL_001
   :file: testsuites/junit.xml
   :suite: ExampleTestSuite
   :case: TEST_SYS_QUAL_001
   :links: [[tr_link('case', 'id')]]

.. test-run:: run test for Adaptive Cruise Control Verification
   :id: TR_TEST_SYS_QUAL_002
   :file: testsuites/junit.xml
   :suite: ExampleTestSuite
   :case: TEST_SYS_QUAL_002
   :links: [[tr_link('case', 'id')]]

.. test-run:: run test for Collision Avoidance Verification
   :id: TR_TEST_SYS_QUAL_003
   :file: testsuites/junit.xml
   :suite: ExampleTestSuite
   :case: TEST_SYS_QUAL_003
   :links: [[tr_link('case', 'id')]]
