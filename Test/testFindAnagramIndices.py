import unittest

from Strings.FindAnagramIndices import anagram_indices


class TestFindAnagramIndices(unittest.TestCase):
    def test_bookTestCase(self):
        input_word = "ab"
        input_string = "abxaba"
        expected_result = [0, 3, 4]
        self.assertListEqual(anagram_indices(input_word, input_string), expected_result)

    def test_ownTestCase(self):
        input_word = "abcd"
        input_string = "xyzqabcdxydcbaoo"
        expected_result = [4, 10]
        self.assertListEqual(anagram_indices(input_word, input_string), expected_result)
