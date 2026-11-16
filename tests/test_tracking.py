
import unittest

from backend.algorithms.tracking_algorithm import TrackingAlgorithm


class TestTracking(unittest.TestCase):

    def setUp(self):
        self.tracker = TrackingAlgorithm()

    def test_panel_aligned(self):
        sensors = {
            "top_left": 500,
            "top_right": 500,
            "bottom_left": 500,
            "bottom_right": 500
        }

        result = self.tracker.calculate_movement(sensors)

        self.assertIn("PANEL ALIGNED", result["movement"])

    def test_tracking_movement(self):
        sensors = {
            "top_left": 900,
            "top_right": 900,
            "bottom_left": 500,
            "bottom_right": 500
        }

        result = self.tracker.calculate_movement(sensors)

        self.assertIn("TILT DOWN", result["movement"])


if __name__ == "__main__":
    unittest.main()
