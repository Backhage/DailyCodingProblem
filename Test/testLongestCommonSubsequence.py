import unittest

from Algorithms.DynamicProgramming.LongestCommonSubsequence import lcs


class TestLcs(unittest.TestCase):
    def test_sample_case_1(self):
        self.assertListEqual(lcs("ZXVVYZW", "XKYKZPW"), ["X", "Y", "Z", "W"])

    def test_empty_strings(self):
        self.assertListEqual(lcs("", ""), [])

    def test_single_empty(self):
        self.assertListEqual(lcs("ABCDEFG", ""), [])

    def test_equal_strings(self):
        self.assertListEqual(lcs("ABCDE", "ABCDE"), ["A", "B", "C", "D", "E"])
