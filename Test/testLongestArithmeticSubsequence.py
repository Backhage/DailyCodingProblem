import unittest

from Algorithms.DynamicProgramming import LongestArithmeticSubsequence


class TestLongestArithmeticSubsequence(unittest.TestCase):
    def test_leetcode_1(self):
        input = [3, 6, 9, 12]
        expected_result = 4
        self.assertEqual(
            expected_result,
            LongestArithmeticSubsequence.longest_arithmetic_subsequence(input),
        )

    def test_leetcode_2(self):
        input = [9, 4, 7, 2, 10]
        expected_result = 3
        self.assertEqual(
            expected_result,
            LongestArithmeticSubsequence.longest_arithmetic_subsequence(input),
        )

    def test_leetcode_3(self):
        input = [20, 1, 15, 3, 10, 5, 8]
        expected_result = 4
        self.assertEqual(
            expected_result,
            LongestArithmeticSubsequence.longest_arithmetic_subsequence(input),
        )

    def test_leetcode_4(self):
        input = [83, 20, 17, 43, 52, 78, 68, 45]
        expected_result = 2
        self.assertEqual(
            expected_result,
            LongestArithmeticSubsequence.longest_arithmetic_subsequence(input),
        )
