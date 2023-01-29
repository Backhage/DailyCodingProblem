import unittest

from Algorithms.BitManipulation.FindUnique import find_unique


class TestFindUnique(unittest.TestCase):
    def test_bookTestCase(self):
        self.assertEqual(1, find_unique([6, 1, 3, 3, 3, 6, 6]))
        self.assertEqual(19, find_unique([13, 19, 13, 13]))

    def test_NegativeNumbers(self):
        self.assertEqual(-3, find_unique([-3, -2, 1, 1, -2, 1, -2]))
