import unittest

from AdvancedDataStructures.FenwickTree import Subscribers


class TestFenwickTree(unittest.TestCase):
    def test_fenwickTree(self):
        subs_array = [4, 8, 1, 9, 3, 5, 5, 3]
        subs = Subscribers(subs_array)

        self.assertEqual(subs.query(0, 6), 35)
