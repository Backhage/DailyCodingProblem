import unittest

from Stacks.BalancedBrackets import is_balanced


class TestBalancedBrackets(unittest.TestCase):
    def test_bookTestCase1(self):
        input = "([])[]({})"
        self.assertTrue(is_balanced(input))

    def test_bookTestCase2(self):
        input = "([)]"
        self.assertFalse(is_balanced(input))

    def test_bookTestCase3(self):
        input = "((()"
        self.assertFalse(is_balanced(input))
