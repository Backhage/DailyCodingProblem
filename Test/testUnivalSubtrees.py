import unittest

from Trees.Tree import Node
from Trees.Tree import count_unival_subtrees


class TestUnivalSubtrees(unittest.TestCase):
    def test_bookTestCase(self):
        tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        self.assertEqual(count_unival_subtrees(tree), 5)

    def test_emptyTree(self):
        self.assertEqual(0, count_unival_subtrees(None))

    def test_treeWithOnlyOneNode(self):
        self.assertEqual(1, count_unival_subtrees(Node(1)))

    def test_treeWithAllNodesHavingTheSameValue(self):
        root = Node(1, Node(1), Node(1))
        self.assertEqual(3, count_unival_subtrees(root))

    def test_largerTree(self):
        root = Node(1, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1)))
        self.assertEqual(7, count_unival_subtrees(root))

    def test_nodesWithDifferentValues(self):
        root = Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7)))
        self.assertEqual(4, count_unival_subtrees(root))
