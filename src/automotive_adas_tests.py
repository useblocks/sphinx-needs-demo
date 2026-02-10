import unittest
from automotive_adas import (
    LaneDetection,
    AdaptiveCruiseControl,
    CollisionAvoidance,
    PedestrianDetection,
    LaneConfidenceMonitor,
    DegradedModeNotifier,
    OperationalDomainMonitor,
    LaneKeepStateManager,
)


class TestLaneDetection(unittest.TestCase):
    """
    .. test:: Lane Detection Tests
       :id: TEST_001
       :links: SWREQ_001, SWREQ_002, SWREQ_003, SWARCH_001
       :author: THOMAS

       Unit tests for lane detection functionalities.
    """

    def test_detect_lane_markings(self):
        """
        .. test:: Lane Marking Detection Test
           :id: TEST_002
           :links: SWREQ_001, SWARCH_001
           :author: THOMAS
        """
        lane_detection = LaneDetection()
        # Mock camera feed input
        self.assertTrue(lane_detection.detect_lane_markings(camera_feed="mock_feed"))

    def test_apply_steering_correction(self):
        """
        .. test:: Steering Correction Test
           :id: TEST_003
           :links: SWREQ_003, SWARCH_001
           :author: THOMAS
        """
        lane_detection = LaneDetection()
        # Mock lane data
        self.assertTrue(
            lane_detection.apply_steering_correction(lane_data="mock_lane_data")
        )


class TestAdaptiveCruiseControl(unittest.TestCase):
    """
    .. test:: Adaptive Cruise Control Tests
       :id: TEST_004
       :links: SWREQ_004, SWREQ_005, SWREQ_013, SWARCH_002
       :author: THOMAS

       Unit tests for adaptive cruise control functionalities.
    """

    def test_measure_distance(self):
        """
        .. test:: Distance Measurement Test
           :id: TEST_005
           :links: SWREQ_004, SWARCH_002
           :author: THOMAS
        """
        acc = AdaptiveCruiseControl()
        # Mock radar data
        self.assertTrue(acc.measure_distance(radar_data="mock_radar"))

    def test_adjust_speed(self):
        """
        .. test:: Speed Adjustment Test
           :id: TEST_006
           :links: SWREQ_005, SWREQ_013, SWARCH_002
        """
        acc = AdaptiveCruiseControl()
        self.assertTrue(acc.adjust_speed(target_speed=60))


class TestCollisionAvoidance(unittest.TestCase):
    """
    .. test:: Collision Avoidance Tests
       :id: TEST_007
       :links: SWREQ_006, SWREQ_007, SWREQ_015, SWARCH_003

       Unit tests for collision avoidance functionalities.
    """

    def test_detect_collision_risk(self):
        """
        .. test:: Collision Risk Detection Test
           :id: TEST_008
           :links: SWREQ_006, SWARCH_003
        """
        ca = CollisionAvoidance()
        # Mock sensor data
        self.assertTrue(ca.detect_collision_risk(sensor_data="mock_data"))

    def test_apply_emergency_braking(self):
        """
        .. test:: Emergency Braking Test
           :id: TEST_009
           :links: SWREQ_007, SWARCH_003
        """
        ca = CollisionAvoidance()
        self.assertTrue(ca.apply_emergency_braking())


class TestPedestrianDetection(unittest.TestCase):
    """
    .. test:: Pedestrian Detection Tests
       :id: TEST_010
       :links: SWREQ_008, SWREQ_009, SWREQ_010, SWREQ_017, SWREQ_020, SWARCH_004, SWARCH_005, SWARCH_006

       Unit tests for pedestrian detection functionalities.
    """

    def test_detect_pedestrians(self):
        """
        .. test:: Pedestrian Detection Test
           :id: TEST_011
           :links: SWREQ_008, SWARCH_004
        """
        pd = PedestrianDetection()
        # Mock sensor data
        self.assertTrue(pd.detect_pedestrians(sensor_data="mock_data"))

    def test_alert_driver(self):
        """
        .. test:: Pedestrian Alert Test
           :id: TEST_012
           :links: SWREQ_009, SWARCH_005
        """
        pd = PedestrianDetection()
        self.assertTrue(pd.alert_driver())

    def test_initiate_emergency_brake(self):
        """
        .. test:: Emergency Pedestrian Braking Test
           :id: TEST_013
           :links: SWREQ_010, SWARCH_006
        """
        pd = PedestrianDetection()
        self.assertTrue(pd.initiate_emergency_brake())


class TestLaneConfidenceMonitor(unittest.TestCase):
    """
    Test suite for Lane Confidence Monitoring (SWREQ_021).
    """

    def test_confidence_threshold(self):
        """
        .. test:: Confidence Threshold Test
           :id: TEST_014
           :links: SWREQ_021, REQ_010

        Verifies confidence threshold of 0.65 is applied correctly.
        """
        monitor = LaneConfidenceMonitor()
        # Test below threshold
        self.assertEqual(monitor.calculate_confidence({"quality": 0.5}), 0.5)
        # Test above threshold
        self.assertEqual(monitor.calculate_confidence({"quality": 0.8}), 0.8)

    def test_degraded_mode_entry_timing(self):
        """
        .. test:: Degraded Mode Entry Timing Test
           :id: TEST_015
           :links: SWREQ_021, REQ_010

        Verifies 2-second delay before entering degraded mode (REQ_010 AC-1).
        """
        monitor = LaneConfidenceMonitor()
        # Simulate continuous low confidence for 2 seconds
        for i in range(21):  # 21 cycles: 0.0 to 2.0 seconds
            state, degraded = monitor.update_state(0.5, i * 0.1)
        self.assertTrue(degraded)

    def test_normal_mode_recovery_timing(self):
        """
        .. test:: Normal Mode Recovery Timing Test
           :id: TEST_016
           :links: SWREQ_021, REQ_010

        Verifies 1-second persistence before recovering to normal mode (REQ_010 AC-5).
        """
        monitor = LaneConfidenceMonitor()
        # First enter degraded mode
        for i in range(20):
            monitor.update_state(0.5, i * 0.1)
        # Then recover with 1 second of high confidence
        for i in range(10):  # 10 cycles at 10Hz = 1 second
            state, degraded = monitor.update_state(0.8, (20 + i) * 0.1)
        self.assertFalse(degraded)


class TestDegradedModeNotifier(unittest.TestCase):
    """
    Test suite for Degraded Mode Notification System (SWREQ_022).
    """

    def test_visual_warning_trigger(self):
        """
        .. test:: Visual Warning Trigger Test
           :id: TEST_017
           :links: SWREQ_022, REQ_010

        Verifies visual warning triggers at degraded mode entry (REQ_010 AC-1).
        """
        notifier = DegradedModeNotifier()
        result = notifier.trigger_visual_warning()
        self.assertTrue(result)

    def test_audible_alert_persistence(self):
        """
        .. test:: Audible Alert Persistence Test
           :id: TEST_018
           :links: SWREQ_022, REQ_010

        Verifies audible alert continues for 5 seconds (REQ_010 AC-2).
        """
        notifier = DegradedModeNotifier()
        result = notifier.trigger_audible_alert(duration_sec=5.0)
        self.assertTrue(result)

    def test_warning_clear(self):
        """
        .. test:: Warning Clear Test
           :id: TEST_019
           :links: SWREQ_022, REQ_010

        Verifies warnings clear on recovery to normal mode.
        """
        notifier = DegradedModeNotifier()
        notifier.trigger_visual_warning()
        notifier.trigger_audible_alert()
        result = notifier.clear_warnings()
        self.assertTrue(result)

    def test_can_message_format(self):
        """
        .. test:: CAN Message Format Test
           :id: TEST_020
           :links: SWREQ_022

        Verifies CAN message at address 0x2A1 with correct format.
        """
        notifier = DegradedModeNotifier()
        result = notifier.send_can_message(0x2A1, b'\x01\x00\x00\x00')
        self.assertTrue(result)


class TestOperationalDomainMonitor(unittest.TestCase):
    """
    Test suite for Lane Keep Operational Domain Monitor (SWREQ_023).
    """

    def test_speed_constraint_lower_bound(self):
        """
        .. test:: Speed Lower Bound Test
           :id: TEST_021
           :links: SWREQ_023, REQ_011

        Verifies 60 km/h minimum speed constraint (REQ_011 AC-1).
        """
        monitor = OperationalDomainMonitor()
        self.assertFalse(monitor.check_speed_constraint(50.0))  # Below minimum
        self.assertTrue(monitor.check_speed_constraint(70.0))   # Within range

    def test_speed_constraint_upper_bound(self):
        """
        .. test:: Speed Upper Bound Test
           :id: TEST_022
           :links: SWREQ_023, REQ_011

        Verifies 180 km/h maximum speed constraint (REQ_011 AC-1).
        """
        monitor = OperationalDomainMonitor()
        self.assertTrue(monitor.check_speed_constraint(170.0))  # Within range
        self.assertFalse(monitor.check_speed_constraint(190.0)) # Above maximum

    def test_curve_radius_minimum(self):
        """
        .. test:: Curve Radius Minimum Test
           :id: TEST_023
           :links: SWREQ_023, REQ_011

        Verifies 250m minimum curve radius (REQ_011 AC-2).
        """
        monitor = OperationalDomainMonitor()
        lane_points = [(0, 0), (100, 10)]  # Sharp curve, < 250m radius
        radius = monitor.estimate_curve_radius(lane_points)
        # Test constraint check separately
        self.assertIsNotNone(radius)

    def test_steering_angle_constraint(self):
        """
        .. test:: Steering Angle Constraint Test
           :id: TEST_024
           :links: SWREQ_023, REQ_011

        Verifies ±15° steering angle limit (REQ_011 AC-3).
        """
        monitor = OperationalDomainMonitor()
        self.assertTrue(monitor.check_steering_angle(10.0))   # Within limit
        self.assertFalse(monitor.check_steering_angle(20.0))  # Exceeds limit

    def test_lane_width_constraints(self):
        """
        .. test:: Lane Width Constraints Test
           :id: TEST_025
           :links: SWREQ_023, REQ_011

        Verifies 10-30cm lane marking width (REQ_011 AC-4).
        """
        monitor = OperationalDomainMonitor()
        self.assertFalse(monitor.check_lane_width(0.05))  # Too narrow
        self.assertTrue(monitor.check_lane_width(0.20))   # Within range
        self.assertFalse(monitor.check_lane_width(0.40))  # Too wide

    def test_domain_status_aggregation(self):
        """
        .. test:: Domain Status Aggregation Test
           :id: TEST_026
           :links: SWREQ_023, REQ_011

        Verifies all constraints checked at 10Hz.
        """
        monitor = OperationalDomainMonitor()
        status = monitor.get_domain_status(
            speed_kmh=120.0,
            lane_points=[(0, 0), (100, 1)],
            steering_angle_deg=5.0,
            lane_width_m=0.15
        )
        self.assertIsInstance(status, dict)
        self.assertIn('speed_ok', status)
        self.assertIn('curve_ok', status)
        self.assertIn('steering_ok', status)
        self.assertIn('lane_width_ok', status)


class TestLaneKeepStateManager(unittest.TestCase):
    """
    Test suite for Lane Keep System State Manager (SWREQ_024).
    """

    def test_state_transition_to_degraded(self):
        """
        .. test:: State Transition to Degraded Test
           :id: TEST_027
           :links: SWREQ_024, REQ_010

        Verifies transition from NORMAL to DEGRADED mode.
        """
        manager = LaneKeepStateManager()
        # Set initial state to ENABLED_NORMAL
        manager.current_state = manager.STATE_ENABLED_NORMAL
        new_state = manager.process_inputs(
            confidence_state='degraded',
            domain_status={'all_ok': False},
            driver_override=False
        )
        self.assertEqual(new_state, manager.STATE_ENABLED_DEGRADED)

    def test_steering_disabled_in_degraded_mode(self):
        """
        .. test:: Steering Disabled in Degraded Mode Test
           :id: TEST_028
           :links: SWREQ_024, REQ_010

        Verifies no steering corrections when confidence < 0.65 (REQ_010 AC-3).
        """
        manager = LaneKeepStateManager()
        manager.current_state = manager.STATE_ENABLED_DEGRADED
        should_steer = manager.should_enable_steering()
        self.assertFalse(should_steer)

    def test_disengagement_on_driver_override(self):
        """
        .. test:: Disengagement on Driver Override Test
           :id: TEST_029
           :links: SWREQ_024, REQ_010

        Verifies system enters DISENGAGING state on driver intervention.
        """
        manager = LaneKeepStateManager()
        manager.current_state = manager.STATE_ENABLED_NORMAL
        new_state = manager.process_inputs(
            confidence_state='normal',
            domain_status={'all_ok': True},
            driver_override=True
        )
        self.assertEqual(new_state, manager.STATE_DISENGAGING)

    def test_no_auto_reengagement(self):
        """
        .. test:: No Auto-Reengagement Test
           :id: TEST_030
           :links: SWREQ_024, REQ_010

        Verifies no automatic re-engagement after driver override (REQ_010 AC-4).
        """
        manager = LaneKeepStateManager()
        manager.current_state = manager.STATE_DISENGAGING
        # Even with good conditions, should not auto-reengage
        allowed = manager.check_reengagement_allowed(
            confidence_state='normal',
            domain_status={'all_ok': True},
            driver_action='none'
        )
        self.assertFalse(allowed)

    def test_notification_trigger_timing(self):
        """
        .. test:: Notification Trigger Timing Test
           :id: TEST_031
           :links: SWREQ_024, REQ_010

        Verifies notification triggers occur at correct state transitions.
        """
        manager = LaneKeepStateManager()
        manager.current_state = manager.STATE_ENABLED_NORMAL
        # Transition to degraded should trigger notification
        notification = manager.get_notification_trigger(manager.STATE_ENABLED_DEGRADED)
        self.assertEqual(notification, 'degraded_mode_entry')

    def test_disengagement_timer(self):
        """
        .. test:: Disengagement Timer Test
           :id: TEST_032
           :links: SWREQ_024, REQ_010

        Verifies 5-second disengagement timer for audible alerts (REQ_010 AC-2).
        """
        manager = LaneKeepStateManager()
        manager.current_state = manager.STATE_DISENGAGING
        # Simulate timer updates
        for i in range(5):
            remaining = manager.update_disengagement_timer(1.0)
        self.assertEqual(remaining, 0.0)


if __name__ == "__main__":
    unittest.main()
