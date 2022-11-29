import unittest

from Trees.BST import make_bst


class TestConvertSortedArrayToBST(unittest.TestCase):
    def test_convertSortedArrayToBST(self):
        input = [5, 8, 13, 31, 127, 432, 440]
        root = make_bst(input)

        def recreate_input(node, res=[]):
            if not node:
                return res

            if node.left:
                recreate_input(node.left, res)

            res.append(node.data)

            if node.right:
                recreate_input(node.right, res)

            return res

        recreated_input = recreate_input(root)

        self.assertListEqual(input, recreated_input)
