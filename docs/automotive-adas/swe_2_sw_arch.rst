{% set page="swe_2_sw_arch.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SWE2_Software_Architecture:

SWE.2 Software Architecture
===========================

.. swarch:: Lane Detection Subsystem
   :id: SWARCH_001
   :status: open
   :links: SWREQ_001, SWREQ_002, SWREQ_003
   :author: ALFRED

   Design the software architecture for the Lane Detection Subsystem, including data acquisition, processing, and corrective action modules.

   .. uml::

      @startuml
      class LaneDetection {
          + detectLaneMarkings()
          + applySteeringCorrection()
      }
      class CameraInput {
          + provideData()
      }
      class SteeringControl {
          + correctSteering()
      }
      LaneDetection --> CameraInput
      LaneDetection --> SteeringControl
      @enduml

.. swarch:: Adaptive Cruise Control Subsystem
   :id: SWARCH_002
   :status: open
   :links: SWREQ_004, SWREQ_005, SWREQ_013
   :author: ALFRED

   Define the architecture for the Adaptive Cruise Control Subsystem, integrating distance measurement, speed adjustment, and driver override mechanisms.

   .. uml::

      @startuml
      class AdaptiveCruiseControl {
          + measureDistance()
          + adjustSpeed()
      }
      class RadarSensor {
          + detectObjects()
      }
      class SpeedController {
          + setSpeed()
      }
      AdaptiveCruiseControl --> RadarSensor
      AdaptiveCruiseControl --> SpeedController
      @enduml

.. swarch:: Collision Avoidance Subsystem
   :id: SWARCH_003
   :status: open
   :links: SWREQ_006, SWREQ_007, SWREQ_016
   :author: ALFRED

   Develop the architecture for the Collision Avoidance Subsystem, focusing on predictive analytics, braking control, and vehicle stabilization.

   .. uml::

      @startuml
      class CollisionAvoidance {
          + detectCollisionRisk()
          + applyEmergencyBraking()
      }
      class SensorArray {
          + collectData()
      }
      class BrakingSystem {
          + applyBrakes()
      }
      CollisionAvoidance --> SensorArray
      CollisionAvoidance --> BrakingSystem
      @enduml

.. swarch:: Pedestrian Detection Subsystem
   :id: SWARCH_004
   :status: open
   :links: SWREQ_008, SWREQ_017, SWREQ_020
   :author: SARAH

   Create the architecture for the Pedestrian Detection Subsystem, including detection algorithms, path prediction, and safety prioritization modules.

   .. uml::

      @startuml
      class PedestrianDetection {
          + detectPedestrians()
          + predictPath()
      }
      class SensorFusion {
          + combineData()
      }
      class AlertSystem {
          + triggerAlert()
      }
      PedestrianDetection --> SensorFusion
      PedestrianDetection --> AlertSystem
      @enduml


.. swarch:: Alert Mechanism Framework
   :id: SWARCH_005
   :status: closed
   :links: SWREQ_009, SWREQ_018, SWREQ_014
   :author: SARAH

   Design the software framework for managing driver alerts, integrating audio, visual, and haptic feedback systems.

   .. uml::

      @startuml
      class AlertFramework {
          + sendAudioAlert()
          + sendVisualAlert()
          + sendHapticAlert()
      }
      class AudioSystem {
          + playSound()
      }
      class VisualSystem {
          + displayAlert()
      }
      class HapticSystem {
          + provideFeedback()
      }
      AlertFramework --> AudioSystem
      AlertFramework --> VisualSystem
      AlertFramework --> HapticSystem
      @enduml

.. swarch:: Emergency Braking Subsystem
   :id: SWARCH_006
   :status: closed
   :links: SWREQ_010, SWREQ_019, SWREQ_015
   :author: SARAH

   Define the architecture for the Emergency Braking Subsystem, focusing on pedestrian safety, predictive emergency stops, and optimization of braking efficiency.

   .. uml::

      @startuml
      class EmergencyBraking {
          + evaluateRisk()
          + applyBraking()
      }
      class RiskAnalyzer {
          + calculateRisk()
      }
      class BrakeController {
          + controlBrakes()
      }
      EmergencyBraking --> RiskAnalyzer
      EmergencyBraking --> BrakeController
      @enduml
