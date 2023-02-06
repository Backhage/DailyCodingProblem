import unittest

from Algorithms.BitManipulation.NthSevenish import nth_sevenish_number


class TestNthSevenish(unittest.TestCase):
    def test_nth_sevenish(self):
        self.assertEqual(1, nth_sevenish_number(1))
        self.assertEqual(7, nth_sevenish_number(2))
        self.assertEqual(8, nth_sevenish_number(3))
        self.assertEqual(49, nth_sevenish_number(4))
        self.assertEqual(50, nth_sevenish_number(5))
