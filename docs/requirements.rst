Requirements
============

System Requirement (context only)
---------------------------------

.. sys:: Obstacle Detection and Emergency Braking
   :id: SYS-012
   :status: accepted
   :safety_level: ASIL-D

   The vehicle shall detect obstacles and initiate emergency braking.

Software Requirement
--------------------

.. req:: Emergency Braking Response Time
   :id: BRAKE-001
   :status: accepted
   :safety_level: ASIL-D
   :satisfies: SYS-012
   :verifies: TC-017

   The braking control module shall engage emergency braking
   within 150 ms of obstacle detection.
