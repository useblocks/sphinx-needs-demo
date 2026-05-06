{% set page="sys_3_sys_arch.rst" %}
{% include "demo_page_header.rst" with context %}

.. _SYS3_Architecture_Design:

===========================
SYS.3 Architecture Design
===========================

.. arch:: Lane Detection Module
   :id: ARCH_001
   :status: in progress
   :links: REQ_001, REQ_002
   :author: ALFRED

   Design the architecture for the Lane Detection Module, including components for camera input processing, lane identification, and integration with steering control.

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
   :status: closed
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

.. arch:: Traffic Sign Recognition System
   :id: ARCH_007
   :status: closed
   :links: REQ_010
   :author: ALFRED

   Design the system architecture for traffic sign recognition, including camera
   capture, sign classification, and distribution of detected speed limits to vehicle control functions.

   .. uml::

      @startuml
      node "Vehicle" {
          component TrafficSignRecognition {
              agent captureRoadScene
              agent classifySpeedLimitSign
          }
          component FrontCamera {
              agent streamFrames
          }
          component SignInterpreter {
              agent extractSpeedLimit
          }
          component VehicleControl {
              agent consumeSpeedLimit
          }
      }
      FrontCamera --> TrafficSignRecognition
      TrafficSignRecognition --> SignInterpreter
      SignInterpreter --> VehicleControl
      @enduml

.. arch:: Blind Spot Monitoring System
   :id: ARCH_008
   :status: open
   :links: REQ_011, REQ_012
   :author: ALFRED

   Define the system architecture for blind spot monitoring, combining rear-corner
   radar coverage with side-view camera input, and routing occupancy state to the
   driver alert system whenever the turn signal indicates an imminent lane change.

   .. uml::

      @startuml
      node "Vehicle" {
          component BlindSpotMonitor {
              agent fuseSensorInputs
              agent classifyZoneOccupancy
          }
          component RearCornerRadar {
              agent detectApproachingObjects
          }
          component SideCamera {
              agent captureBlindSpotImage
          }
          component TurnSignalSensor {
              agent reportIntent
          }
          component DriverAlertSystem {
              agent issueLaneChangeWarning
          }
      }
      RearCornerRadar --> BlindSpotMonitor
      SideCamera --> BlindSpotMonitor
      TurnSignalSensor --> BlindSpotMonitor
      BlindSpotMonitor --> DriverAlertSystem
      @enduml

.. arch:: Driver Drowsiness Detection System
   :id: ARCH_009
   :status: open
   :links: REQ_013, REQ_014
   :author: ALFRED

   Define the system architecture for driver drowsiness detection, combining cabin
   camera capture with an eye-state estimator and a drowsiness scorer that emits
   progressive alerts via the existing driver alert system.

   .. uml::

      @startuml
      node "Vehicle" {
          component DrowsinessMonitor {
              agent estimateEyeState
              agent scoreDrowsiness
          }
          component CabinCamera {
              agent captureDriverFace
          }
          component DrowsinessScorer {
              agent updateScore
          }
          component DriverAlertSystem {
              agent issueDrowsinessAlert
              agent suggestBreak
          }
      }
      CabinCamera --> DrowsinessMonitor
      DrowsinessMonitor --> DrowsinessScorer
      DrowsinessScorer --> DriverAlertSystem
      @enduml

.. arch:: Automated Parking System
   :id: ARCH_010
   :status: open
   :links: REQ_015, REQ_016
   :author: ALFRED

   Define the system architecture for automated parking, combining ultrasonic ranging
   and surround-view camera input for slot detection, a trajectory planner, and the
   actuator interface that commands steering, throttle, and brake during the park maneuver.

   .. uml::

      @startuml
      node "Vehicle" {
          component ParkingAssist {
              agent detectParkingSlot
              agent planParkTrajectory
              agent executeParkManeuver
          }
          component UltrasonicArray {
              agent measureClearances
          }
          component SurroundCamera {
              agent captureSlotImagery
          }
          component TrajectoryPlanner {
              agent computeWaypoints
          }
          component VehicleActuators {
              agent applySteeringThrottleBrake
          }
      }
      UltrasonicArray --> ParkingAssist
      SurroundCamera --> ParkingAssist
      ParkingAssist --> TrajectoryPlanner
      TrajectoryPlanner --> VehicleActuators
      @enduml
