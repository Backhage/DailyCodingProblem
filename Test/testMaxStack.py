import unittest

from Stacks.stack import MaxStack


class TestMaxStack(unittest.TestCase):
    def test_maxstack(self):
        stack = MaxStack()
        stack.push(1)
        stack.push(3)
        stack.push(2)

        self.assertEqual(3, stack.max())
        self.assertEqual(2, stack.pop())
        self.assertEqual(3, stack.max())
        self.assertEqual(3, stack.pop())
        self.assertEqual(1, stack.max())
