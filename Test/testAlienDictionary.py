import unittest

from Applications import AlienDictionary


class TestAlienDictionary(unittest.TestCase):
    def test_bookTestCase(self):
        input = ["xww", "wxyz", "wxyw", "ywx", "ywz"]
        expected = ["x", "z", "w", "y"]

        self.assertListEqual(expected, AlienDictionary.alien_letter_order(input))
