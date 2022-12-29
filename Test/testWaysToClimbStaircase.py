import unittest

from Algorithms.DynamicProgramming.WaysToClimbStaircase import staircase


class TestWaysToClimbStaircase(unittest.TestCase):
    def test_waysToClimbStaircase(self):
        self.assertEqual(1, staircase(1, [1, 2]))
        self.assertEqual(2, staircase(2, [1, 2]))
        self.assertEqual(3, staircase(3, [1, 2]))
        self.assertEqual(5, staircase(4, [1, 2]))
        self.assertEqual(8, staircase(5, [1, 2]))
