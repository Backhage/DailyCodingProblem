import unittest
from Algorithms.AdvancedAlgorithms import QuickSelect


class TestQuickSelect(unittest.TestCase):
    def test_Boundaries(self):
        input = [1, 2, 3, 4, 5]
        # Find the largest
        self.assertEqual(5, QuickSelect.find_kth_largest(input, 1))

        # Find the smallest
        self.assertEqual(1, QuickSelect.find_kth_largest(input, 5))

    def test_randomOrder(self):
        input = [4, 7, 1, 2, 6, 5, 3]

        # Find the largest
        self.assertEqual(7, QuickSelect.find_kth_largest(input, 1))

        # Find the smallest
        self.assertEqual(1, QuickSelect.find_kth_largest(input, 7))

        # Find the middle
        self.assertEqual(4, QuickSelect.find_kth_largest(input, 4))
