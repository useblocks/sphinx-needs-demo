{% set page="test_report_demo.rst" %}
{% include "demo_page_header.rst" with context %}

.. _Test_Report_Demo:

Test-Report Demo
=================

.. test-run:: run test
   :id: TR_TEST_SYS_QUAL_001
   :file: testsuites/junit.xml
   :suite: ExampleTestSuite
   :case: TEST_SYS_QUAL_001
   :status: passed
   :links: [[tr_link('case', 'id')]]

