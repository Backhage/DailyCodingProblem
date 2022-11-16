import unittest

from LinkedLists.LinkedList import Node
from LinkedLists.LinkedList import intersection


class TestIntersectingLinkedLists(unittest.TestCase):
    def test_intersectingLinkedLists(self):
        common_part = Node(8, Node(10))
        l1 = Node(3, Node(7, common_part))
        l2 = Node(99, Node(1, common_part))

        intersecting_node = intersection(l1, l2)

        self.assertEqual(intersecting_node, common_part)
