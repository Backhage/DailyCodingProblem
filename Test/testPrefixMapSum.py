import unittest

from Tries.PrefixMapSum import PrefixMapSum


class TestPrefixMapSum(unittest.TestCase):
    def test_prefixMapSum(self):
        mapsum = PrefixMapSum()
        mapsum.insert("columnar", 3)

        self.assertEqual(mapsum.sum("col"), 3)

        mapsum.insert("column", 2)
        mapsum.insert("column", 5)
        mapsum.insert("column", 1)

        self.assertEqual(mapsum.sum("col"), 4)
