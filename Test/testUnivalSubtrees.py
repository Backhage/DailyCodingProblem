import unittest

from Trees.Tree import Node
from Trees.Tree import count_unival_subtrees


class TestUnivalSubtrees(unittest.TestCase):
    def test_bookTestCase(self):
        tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        self.assertEqual(count_unival_subtrees(tree), 5)
