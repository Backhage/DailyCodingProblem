import unittest

from Algorithms.SortingAndSearching.DutchFlagProblem import partition


class TestDutchFlagProblem(unittest.TestCase):
    def test_bookTestCase(self):
        arr = ["G", "B", "R", "R", "B", "R", "G"]
        partition(arr)
        self.assertListEqual(["R", "R", "R", "G", "G", "B", "B"], arr)
