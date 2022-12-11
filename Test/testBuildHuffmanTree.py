import unittest

from Heaps.BuildHuffmanTree import build_tree, encode


class TestBuildHuffmanTree(unittest.TestCase):
    def test_buildHuffmanTree(self):
        input = {"a": 3, "c": 6, "e": 8, "f": 2}
        expected = {"a": "101", "c": "11", "e": "0", "f": "100"}

        tree = build_tree(input)
        encoded = encode(tree)

        self.assertDictEqual(encoded, expected)
