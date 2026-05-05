import unittest
from automotive_adas import (
    LaneDetection,
    AdaptiveCruiseControl,
    CollisionAvoidance,
    PedestrianDetection,
   TrafficSignRecognition,
    BlindSpotMonitor,
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


class TestTrafficSignRecognition(unittest.TestCase):
    """
    .. test:: Traffic Sign Recognition Tests
       :id: TEST_014
       :status: passed
       :links: SWREQ_021, SWARCH_007
       :author: THOMAS

       Unit tests for traffic sign recognition functionalities.
    """

    def test_detect_speed_limit(self):
        """
        .. test:: Speed Limit Sign Detection Test
           :id: TEST_015
           :status: passed
           :links: SWREQ_021, SWARCH_007
           :author: THOMAS
        """
        tsr = TrafficSignRecognition()
        self.assertEqual(tsr.detect_speed_limit(camera_feed={"speed_limit": 50}), 50)


class TestBlindSpotMonitor(unittest.TestCase):
    """
    .. test:: Blind Spot Monitor Tests
       :id: TEST_016
       :status: open
       :links: SWREQ_022, SWREQ_023, SWARCH_008
       :author: THOMAS

       Unit tests for blind spot monitor functionalities.
    """

    def test_zone_occupancy_from_radar(self):
        """
        .. test:: Blind Spot Radar Occupancy Test
           :id: TEST_017
           :status: open
           :links: SWREQ_022, SWARCH_008
           :author: THOMAS
        """
        bsm = BlindSpotMonitor()
        zones = bsm.update_zone_occupancy(
            radar_tracks=[{"side": "left"}], camera_detections=[]
        )
        self.assertTrue(zones["left"])
        self.assertFalse(zones["right"])

    def test_lane_change_warning_triggers_only_when_occupied(self):
        """
        .. test:: Blind Spot Lane Change Arbitration Test
           :id: TEST_018
           :status: open
           :links: SWREQ_023, SWARCH_008
           :author: THOMAS
        """
        bsm = BlindSpotMonitor()
        zones = {"left": True, "right": False}
        self.assertTrue(bsm.evaluate_lane_change(zones, turn_signal="left"))
        self.assertFalse(bsm.evaluate_lane_change(zones, turn_signal="right"))
        self.assertFalse(bsm.evaluate_lane_change(zones, turn_signal=None))


if __name__ == "__main__":
    unittest.main()
