import unittest

from Algorithms.Backtracking.ComputeFlightItinerary import get_itinerary


class TestComputeItinerary(unittest.TestCase):
    def test_bookTestCases(self):
        self.assertListEqual(
            get_itinerary(
                [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")],
                ["YUL"],
            ),
            ["YUL", "YYZ", "SFO", "HKO", "ORD"],
        )

        self.assertIsNone(get_itinerary([("SFO", "COM"), ("COM", "YYZ")], ["COM"]))
