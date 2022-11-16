import unittest

from LinkedLists.LinkedList import Node
from LinkedLists.LinkedList import alternate


class TestAlternateHighLow(unittest.TestCase):
    def test_bookTestCase(self):
        l = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        result = alternate(l)
        expected = [1, 3, 2, 5, 4]

        for num in expected:
            self.assertIsNotNone(result)
            if result:
                self.assertEqual(num, result.data)
                result = result.next
