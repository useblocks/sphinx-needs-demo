{% set page="sys_3_sys_arch.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SYS3_Architecture_Design:

===========================
SYS.3 Architecture Design
===========================

.. arch:: Lane Detection Module
   :id: ARCH_001
   :status: in progress
   :links: REQ_001, REQ_002, REQ_010, REQ_011
   :author: ALFRED

   Architectural framework for lane keeping functionality including lane detection, steering control, error handling, and operational limit monitoring.

   .. uml::

      @startuml
      node "Vehicle" {
          component LaneDetection  {
              agent detectLaneMarkings
              agent applySteeringCorrection
          }
          component CameraInput {
              agent captureData
          }
          component SteeringControl {
              agent correctSteering
          }
      }
      CameraInput --> LaneDetection
      LaneDetection --> SteeringControl
      @enduml

.. arch:: Adaptive Cruise Control System
   :id: ARCH_002
   :status: open
   :links: REQ_003, REQ_004
   :author: ALFRED

   Define the architecture for the Adaptive Cruise Control System, with subsystems for distance measurement, speed adjustment, and communication with the vehicle's control systems.

   .. uml::

      @startuml
      node "Vehicle" {
          component AdaptiveCruiseControl {
              agent measureDistance
              agent adjustSpeed
          }
          component RadarSensor {
              agent measureDistance
          }
          component SpeedController {
              agent adjustSpeed
          }
          component CommunicationModule {
              agent sendReceiveData
          }
      }
      RadarSensor --> AdaptiveCruiseControl
      AdaptiveCruiseControl --> SpeedController
      SpeedController --> CommunicationModule
      @enduml

.. arch:: Collision Avoidance System
   :id: ARCH_003
   :status: open
   :links: REQ_005, REQ_006
   :author: ALFRED

   Develop the architecture for the Collision Avoidance System, focusing on modules for collision detection, predictive analytics, and autonomous braking.

   .. uml::

      @startuml
      node "Vehicle" {
          component CollisionAvoidance {
              agent detectCollisionRisk
              agent applyEmergencyBraking
          }
          component CollisionDetector {
              agent detectCollision
          }
          component RiskAnalyzer {
              agent analyzeRisk
          }
          component BrakeController {
              agent applyBrakes
          }
      }
      CollisionDetector --> RiskAnalyzer
      RiskAnalyzer --> BrakeController
      BrakeController --> CollisionAvoidance
      @enduml

.. arch:: Pedestrian Safety Framework
   :id: ARCH_004
   :status: open
   :links: REQ_007, REQ_008, REQ_009
   :author: ALFRED

   Create the architecture for the Pedestrian Safety Framework, integrating pedestrian detection, alert mechanisms, and emergency braking functionalities.

   .. uml::

      @startuml
      node "Vehicle" {
          component PedestrianSafety {
              agent detectPedestrians
              agent alertDriver
              agent applyEmergencyBrakes
          }
          component PedestrianDetector {
              agent detectPedestrians
          }
          component AlertSystem {
              agent triggerAlert
          }
          component EmergencyBrakeController {
              agent applyEmergencyBrakes
          }
      }
      PedestrianDetector --> AlertSystem
      AlertSystem --> EmergencyBrakeController
      EmergencyBrakeController --> PedestrianSafety
      @enduml

.. arch:: Alert System Framework
   :id: ARCH_005
   :status: open
   :links: REQ_008
   :author: ALFRED

   Design the system-level architecture for the Alert System Framework, integrating multiple types of driver alerts including audio, visual, and haptic feedback mechanisms.

   .. uml::

      @startuml
      node "Vehicle" {
          component AlertSystem {
              agent manageAlerts
              agent prioritizeAlerts
          }
          component AudioAlerts {
              agent generateAudioAlert
          }
          component VisualAlerts {
              agent displayVisualAlert
          }
          component HapticAlerts {
              agent provideHapticFeedback
          }
          component SensorInputs {
              agent receiveAlertTriggers
          }
      }
      SensorInputs --> AlertSystem
      AlertSystem --> AudioAlerts
      AlertSystem --> VisualAlerts
      AlertSystem --> HapticAlerts
      @enduml

.. arch:: Emergency Braking System
   :id: ARCH_006
   :status: open
   :links: REQ_009
   :author: ALFRED

   Create the system architecture for the Emergency Braking System, focusing on rapid response, optimal braking force calculation, and integration with pedestrian detection systems.

   .. uml::

      @startuml
      node "Vehicle" {
          component EmergencyBrakingSystem {
              agent calculateBrakingForce
              agent initiateEmergencyBraking
          }
          component BrakeActuator {
              agent applyBrakes
          }
          component ForceCalculator {
              agent optimizeBrakingForce
          }
          component ResponseTimer {
              agent measureResponseTime
          }
          component PedestrianDetection {
              agent detectPedestrianThreat
          }
      }
      PedestrianDetection --> EmergencyBrakingSystem
      EmergencyBrakingSystem --> ForceCalculator
      ForceCalculator --> BrakeActuator
      EmergencyBrakingSystem --> ResponseTimer
      @enduml
