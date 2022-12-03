import unittest

from Tries.FindMaxXor import find_max_xor


class TestFindMaxXor(unittest.TestCase):
    def test_bookTestCase(self):
        input = [4, 6, 7]
        self.assertEqual(find_max_xor(input), 3)
