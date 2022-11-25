import unittest

from Trees.Tree import Node
from Trees.Tree import reconstruct


def create_preorder(root):
    result = []

    def helper(node):
        if node is None:
            return
        result.append(node)
        helper(node.left)
        helper(node.right)

    helper(root)
    return result


def create_inorder(root):
    result = []

    def helper(node):
        if node is None:
            return
        helper(node.left)
        result.append(node)
        helper(node.right)

    helper(root)
    return result


class TestReconstructTree(unittest.TestCase):
    def test_bookTestCase(self):
        tree = Node(
            "a", Node("b", Node("d"), Node("e")), Node("c", Node("f"), Node("g"))
        )
        pre_order = create_preorder(tree)
        in_order = create_inorder(tree)

        reconstructed_tree = reconstruct(pre_order, in_order)

        self.assertListEqual(pre_order, create_preorder(reconstructed_tree))
        self.assertListEqual(in_order, create_inorder(reconstructed_tree))
