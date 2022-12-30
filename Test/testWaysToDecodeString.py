import unittest

from Algorithms.DynamicProgramming.WaysToDecodeString import num_encodings


class TestWaysToDecodeString(unittest.TestCase):
    def test_waysToDecodeString(self):
        self.assertEqual(num_encodings("0"), 0)
        self.assertEqual(num_encodings("06"), 0)
        self.assertEqual(num_encodings(""), 1)
        self.assertEqual(num_encodings("1"), 1)
        self.assertEqual(num_encodings("11"), 2)
        self.assertEqual(num_encodings("26"), 2)
        self.assertEqual(num_encodings("27"), 1)
        self.assertEqual(num_encodings("111"), 3)
