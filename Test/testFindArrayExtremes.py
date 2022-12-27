import unittest

from Algorithms.Recursive.FindArrayExtremes import min_and_max


class TestFindArrayExtremes(unittest.TestCase):
    def test_findArrayExtremes(self):
        array = [4, 2, 7, 5, -1, 3, 6]
        min_max = (-1, 7)

        self.assertTupleEqual(min_max, min_and_max(array))
