import unittest

from LinkedLists.LinkedList import Node
from LinkedLists.LinkedList import add


class TestAddLinkedLists(unittest.TestCase):
    def test_bookTestCase(self):
        l1 = Node(9, Node(9))
        l2 = Node(5, Node(2))

        result = add(l1, l2)
        self.assertIsNotNone(result)

        i = 0
        expected = [4, 2, 1]
        while result is not None:
            self.assertEqual(result.data, expected[i])
            result = result.next
            i += 1

    def test_different_len(self):
        # First value = 28
        l1 = Node(8, Node(2))

        # Second value = 397
        l2 = Node(7, Node(9, Node(3)))

        # Expected result: 397 + 28 = 425
        result = add(l1, l2)
        expected = [5, 2, 4]
        i = 0
        while result is not None:
            self.assertEqual(result.data, expected[i])
            result = result.next
            i += 1
