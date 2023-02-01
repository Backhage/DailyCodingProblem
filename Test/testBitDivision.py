import unittest

from Algorithms.BitManipulation.DivisionWithoutNormalOperators import divide


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(3, divide(6, 2))
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(1, divide(6, 4))
        self.assertEqual(1, divide(6, 5))
