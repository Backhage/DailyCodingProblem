import unittest

from LinkedLists.LinkedList import Node
from LinkedLists.LinkedList import reverse


class TestReverseSinglyLinkedList(unittest.TestCase):
    def test_reverse(self):
        l = Node(1, Node(2, Node(3)))

        values = [1, 2, 3]
        curr = l
        for val in values:
            self.assertIsNotNone(curr)
            if curr is not None:
                self.assertEqual(val, curr.data)
                curr = curr.next

        l = reverse(l)
        curr = l
        for val in reversed(values):
            self.assertIsNotNone(curr)
            if curr is not None:
                self.assertEqual(val, curr.data)
                curr = curr.next
