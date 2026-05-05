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

.. swarch:: Traffic Sign Processing Subsystem
   :id: SWARCH_007
   :status: closed
   :links: SWREQ_021
   :author: SARAH

   Define the software architecture for speed limit sign processing, covering frame analysis,
   sign classification, and publishing recognized limits for downstream consumers.

   .. uml::

      @startuml
      class TrafficSignProcessor {
          + detectSpeedLimit()
      }
      class FrameAnalyzer {
          + extractCandidates()
      }
      class SignClassifier {
          + classifyLimit()
      }
      class LimitPublisher {
          + publishLimit()
      }
      TrafficSignProcessor --> FrameAnalyzer
      TrafficSignProcessor --> SignClassifier
      TrafficSignProcessor --> LimitPublisher
      @enduml

.. swarch:: Blind Spot Monitoring Subsystem
   :id: SWARCH_008
   :status: open
   :links: SWREQ_022, SWREQ_023
   :author: ALFRED

   Define the software architecture for the blind spot monitoring subsystem, covering
   radar/camera fusion, zone occupancy tracking, and arbitration with turn signal intent
   before raising a driver alert.

   .. uml::

      @startuml
      class BlindSpotMonitor {
          + updateZoneOccupancy()
          + evaluateLaneChange()
      }
      class RadarTracker {
          + trackApproachingVehicles()
      }
      class SideCameraDetector {
          + detectAdjacentRoadUsers()
      }
      class TurnSignalArbiter {
          + isLaneChangeIntent()
      }
      class WarningEmitter {
          + raiseBlindSpotAlert()
      }
      BlindSpotMonitor --> RadarTracker
      BlindSpotMonitor --> SideCameraDetector
      BlindSpotMonitor --> TurnSignalArbiter
      BlindSpotMonitor --> WarningEmitter
      @enduml

.. swarch:: Driver Drowsiness Subsystem
   :id: SWARCH_009
   :status: open
   :links: SWREQ_024, SWREQ_025
   :author: STEVEN

   Define the software architecture for the driver drowsiness subsystem, covering
   cabin camera capture, per-frame eye-state estimation, drowsiness score aggregation,
   and emission of progressive driver alerts.

   .. uml::

      @startuml
      class DrowsinessMonitor {
          + estimateEyeState()
          + updateDrowsinessScore()
          + emitAlert()
      }
      class CabinFrameSource {
          + readFrame()
      }
      class EyeStateClassifier {
          + classifyEyeAspectRatio()
      }
      class ScoreAggregator {
          + aggregateScore()
      }
      class AlertEmitter {
          + raiseDrowsinessAlert()
      }
      DrowsinessMonitor --> CabinFrameSource
      DrowsinessMonitor --> EyeStateClassifier
      DrowsinessMonitor --> ScoreAggregator
      DrowsinessMonitor --> AlertEmitter
      @enduml
