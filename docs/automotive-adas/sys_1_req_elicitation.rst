{% set page="sys_1_req_elicitation.rst" %}
{% include "demo_page_header.rst" with context %}

SYS.1 Requirement Elicitation
=============================

.. need:: Lane Keeping Assistance
   :id: NEED_001
   :status: in progress
   :author: ROBERT
   :jira: 1

   The system shall detect lane markings and provide corrective steering input to keep the
   vehicle within the lane.

.. need:: Adaptive Cruise Control
   :id: NEED_002
   :status: closed
   :author: ROBERT
   :jira: 2

   The system shall automatically adjust the vehicle's speed to maintain a safe distance
   from the vehicle ahead.

.. need:: Emergency Braking System
   :id: NEED_003
   :status: in progress
   :author: ROBERT

   The system shall detect potential collisions and apply the brakes autonomously to
   avoid or mitigate the impact.

.. need:: Pedestrian Detection
   :id: NEED_004
   :status: in progress
   :author: ROBERT

   The system shall identify pedestrians in the vehicle's path and issue warnings or
   initiate braking to prevent collisions.

.. need:: Traffic Sign Recognition
   :id: NEED_005
   :status: closed
   :author: ROBERT

   The system shall recognize traffic signs, with a focus on posted speed limits,
   so that downstream driving assistance functions can react appropriately.

.. need:: Blind Spot Monitoring
   :id: NEED_006
   :status: open
   :author: ROBERT

   The system shall monitor zones to the rear and sides of the vehicle that are not
   directly visible to the driver, and warn the driver when another road user enters
   those zones while a lane change is intended.

.. need:: Driver Drowsiness Detection
   :id: NEED_007
   :status: open
   :author: ROBERT

   The system shall observe driver state via the cabin camera and warn the driver,
   and optionally suggest a break, when sustained signs of drowsiness or inattention
   are detected.

.. need:: Automated Parking Assist
   :id: NEED_008
   :status: open
   :author: ROBERT

   The system shall identify suitable parallel and perpendicular parking slots and
   semi-autonomously steer, accelerate, and brake the vehicle into the selected slot
   under driver supervision.
