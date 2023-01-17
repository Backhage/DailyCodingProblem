import unittest

from Algorithms.SortingAndSearching.PancakeSort import pancake_sort


class TestPancakeSort(unittest.TestCase):
    def test_pancake_sort(self):
        arr = [20, 40, 10, 50, 30]
        pancake_sort(arr)
        self.assertListEqual([10, 20, 30, 40, 50], arr)
