import unittest

from Algorithms.SortingAndSearching.RadixSort import radix_sort


class TestRadixSort(unittest.TestCase):
    def test_radix_sort(self):
        arr = [4, 100, 54, 537, 2, 89]
        self.assertListEqual(sorted(arr), radix_sort(arr))
