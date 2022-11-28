import unittest

from Trees.BST import BST, get_bounds


class TestBSTFindFloorAndCeiling(unittest.TestCase):
    def test_get_bounds(self):
        bst = BST()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(4)

        self.assertTupleEqual((5, 7), get_bounds(bst.root, 6))
