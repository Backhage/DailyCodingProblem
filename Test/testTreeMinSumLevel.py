import unittest

from Trees.Tree import Node, smallest_level


class TestTreeMinSumLevel(unittest.TestCase):
    def test_bookTestCase(self):
        tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
        self.assertEqual(smallest_level(tree), 0)
