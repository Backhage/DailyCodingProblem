import unittest

from Algorithms.Recursive import ReorderArraySameBst


class TestReorderArraySameBst(unittest.TestCase):
    def test_simple_bst(self):
        self.assertEqual(1, ReorderArraySameBst.number_of_ways([2, 1, 3]))

    def test_three_level_bst(self):
        self.assertEqual(5, ReorderArraySameBst.number_of_ways([3, 4, 5, 1, 2]))

    def test_no_reordering_possible(self):
        self.assertEqual(0, ReorderArraySameBst.number_of_ways([1, 2, 3]))
