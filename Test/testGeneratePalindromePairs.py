import unittest

from Strings.GeneratePalindromePairs import palindrome_pairs


class TestGeneratePalindromePairs(unittest.TestCase):
    def test_bookTestCase(self):
        input = ["code", "edoc", "da", "d"]
        expected_result = [(1, 0), (0, 1), (2, 3)]

        self.assertListEqual(palindrome_pairs(input), expected_result)
