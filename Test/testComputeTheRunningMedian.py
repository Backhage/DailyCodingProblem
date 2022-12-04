import unittest

from Heaps.ComputeTheRunningMedian import running_median


class TestComputeTheRunningMedian(unittest.TestCase):
    def test_bookTestCase(self):
        input = [2, 1, 5, 7, 2, 0, 5]
        expected = [2, 1.5, 2, 3.5, 2, 2, 2]

        self.assertListEqual(expected, running_median(input))
