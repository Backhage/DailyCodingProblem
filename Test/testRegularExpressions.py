import unittest

from Algorithms.Recursive.RegularExpressions import matches


class TestRegularExpressions(unittest.TestCase):
    def test_bookTestCases(self):
        self.assertTrue(matches("ray", "ra."))
        self.assertFalse(matches("raymond", "ra."))
        self.assertTrue(matches("chat", ".*at"))
        self.assertFalse(matches("chats", ".*at"))
