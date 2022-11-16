import unittest

from Strings.SmallestRotatedString import get_best_word


class TestSmallestRotatedString(unittest.TestCase):
    def test_bookTestCase(self):
        inputString = "daily"
        k = 1
        self.assertEqual(get_best_word(inputString, k), "ailyd")

    def test_ownTestCase(self):
        inputString = "daily"
        k = 2
        self.assertEqual(get_best_word(inputString, k), "adily")
