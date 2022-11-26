import unittest

from Trees.Tree import Node
from Trees.Tree import evaluate


class TestEvaluateArithmeticTree(unittest.TestCase):
    def test_bookTestCase(self):
        tree = Node("*", Node("+", Node(3), Node(2)), Node("+", Node(4), Node(5)))
        self.assertEqual(evaluate(tree), 45)
