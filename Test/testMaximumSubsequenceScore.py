import unittest
from Heaps.MaximumSubsequenceScore import max_score


class TestMaximumSubsequenceScore(unittest.TestCase):
    def test_leetcode1(self):
        nums1 = [1, 3, 3, 2]
        nums2 = [2, 1, 3, 4]
        k = 3

        expected_result = 12

        self.assertEqual(expected_result, max_score(nums1, nums2, k))

    def test_leetcode2(self):
        nums1 = [4, 2, 3, 1, 1]
        nums2 = [7, 5, 10, 9, 6]
        k = 1

        expected_result = 30

        self.assertEqual(expected_result, max_score(nums1, nums2, k))
