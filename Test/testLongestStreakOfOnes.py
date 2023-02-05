import unittest

from Algorithms.BitManipulation.LongestStreakOfOnes import find_length


class TestLongesStreakOfOnes(unittest.TestCase):
    def test_bookTestCase(self):
        self.assertEqual(3, find_length(156))
