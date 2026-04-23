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

.. req:: Obstacle Detection Sensitivity
   :id: OBS-001
   :status: open
   :safety_level: ASIL-D
   :satisfies: SYS-012

   The obstacle detection module shall identify objects within a minimum range
   of 150 m and classify them within 50 ms of first detection.

.. req:: Emergency Braking Response Time
   :id: BRAKE-001
   :status: accepted
   :efforts: 120
   :safety_level: ASIL-D
   :satisfies: SYS-012

   The braking control module shall engage emergency braking
   within 150 ms of obstacle detection.
