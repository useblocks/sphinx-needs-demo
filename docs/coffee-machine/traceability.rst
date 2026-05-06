Traceability Reports
====================

Complete traceability is a cornerstone of the BrewMaster Pro 3000
development process. Every line of code can be traced back through
architectural designs and requirements to the original customer need
or safety regulation. Conversely, every requirement can be traced
forward to its detailed design and verification test cases. This
bidirectional traceability ensures nothing is missed and enables rapid
impact analysis when requirements change.

Full Traceability Diagram
-------------------------

The following diagram shows all needs and their connections in this
coffee machine example:

.. needflow::
   :types: req, swreq, component, interface, impl, test
   :filter: docname is not None and "coffee-machine" in docname
   :show_link_names:
   :config: toptobottom

Requirements Coverage
---------------------

This table shows all system requirements and which software
requirements specify them, providing a forward-traceability view from
customer needs to software specifications.

.. needtable:: Requirements → SW Requirements
   :filter: type == "req" and docname is not None and "coffee-machine" in docname
   :columns: id, title, status, reqs_back as "Specified by"
   :style: table
   :sort: id

SW Requirements to Architecture
-------------------------------

This table traces software requirements to the architectural
components that implement them.

.. needtable:: SW Requirements → Components
   :filter: type == "swreq" and docname is not None and "coffee-machine" in docname
   :columns: id, title, status, reqs as "Specifies", implements_back as "Implemented by"
   :style: table
   :sort: id

Architecture to Test Coverage
-----------------------------

This table shows which software requirements are covered by test
cases, highlighting any gaps in verification.

.. needtable:: SW Requirements → Tests
   :filter: type == "swreq" and docname is not None and "coffee-machine" in docname
   :columns: id, title, specs_back as "Tested by"
   :style: table
   :sort: id

Test Case Overview
------------------

A summary of all test cases with their current status and the
requirements they verify.

.. needtable:: Test Case Summary
   :filter: type == "test" and docname is not None and "coffee-machine" in docname
   :columns: id, title, status, tags, specs as "Verifies"
   :style: table
   :sort: id

Test Status Metrics
-------------------

.. needpie:: Test Status Distribution
   :labels: Open, In Progress, Closed
   :legend:

   type == "test" and docname is not None and "coffee-machine" in docname and status == "open"
   type == "test" and docname is not None and "coffee-machine" in docname and status == "in progress"
   type == "test" and docname is not None and "coffee-machine" in docname and status == "closed"

Requirements Status Metrics
---------------------------

.. needpie:: Requirements Status Distribution
   :labels: Open, In Progress, Closed
   :legend:

   type in ["req", "swreq"] and docname is not None and "coffee-machine" in docname and status == "open"
   type in ["req", "swreq"] and docname is not None and "coffee-machine" in docname and status == "in progress"
   type in ["req", "swreq"] and docname is not None and "coffee-machine" in docname and status == "closed"

Unlinked Needs
--------------

The following list shows any needs that have no outgoing or incoming
links, which may indicate missing traceability:

.. needlist::
   :filter: docname is not None and "coffee-machine" in docname and type in ["req", "swreq", "component", "test"] and len(links) == 0 and len(links_back) == 0
   :show_status:

Complete Needs Index
--------------------

A comprehensive table of all needs in the coffee machine project:

.. needtable:: All Coffee Machine Needs
   :filter: docname is not None and "coffee-machine" in docname and type in ["req", "swreq", "component", "interface", "impl", "test"]
   :columns: id, type, title, status, tags
   :sort: type
   :style: datatables
