import unittest

from LinkedLists.LinkedList import Node
from LinkedLists.LinkedList import intersection


class TestFindFirstCommonNode(unittest.TestCase):
    def test_bookTestCase(self):
        intersect = Node(8, Node(10))
        l1 = Node(3, Node(7, intersect))
        l2 = Node(99, Node(1, intersect))

        result = intersection(l1, l2)
        self.assertIsNotNone(result)
        if result:
            self.assertEqual(result.data, 8)
