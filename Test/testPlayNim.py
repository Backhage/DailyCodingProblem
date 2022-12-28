import unittest

from Algorithms.Recursive.PlayNim import nim


class TestPlayNim(unittest.TestCase):
    def test_play_nim(self):
        self.assertFalse(nim([1, 1, 1]))
        self.assertTrue(nim([1, 1, 2]))
        self.assertFalse(nim([1, 2, 3]))
        self.assertTrue(nim([3, 4, 5]))
