import unittest

from Algorithms.SortingAndSearching.ShiftedArraySearch import shifted_array_search


class TestShiftedArraySearch(unittest.TestCase):
    def test_shifted_array_search(self):
        arr = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
        self.assertEqual(0, shifted_array_search(arr, 45))
        self.assertEqual(2, shifted_array_search(arr, 71))
        self.assertEqual(9, shifted_array_search(arr, 37))
        self.assertIsNone(shifted_array_search(arr, 100))
