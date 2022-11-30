import unittest

from Trees.BST import construct_trees


class TestConstructBsts(unittest.TestCase):
    def test_bookTestCase(self):
        trees = construct_trees(3)
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]]
        actual = [preorder(tree) for tree in trees]

        self.assertListEqual(expected, actual)


def preorder(root):
    result = []

    if root:
        result.append(root.data)
        result += preorder(root.left)
        result += preorder(root.right)

    return result
