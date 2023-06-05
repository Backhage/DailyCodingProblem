import unittest

from Applications import Ghost


class TestGhost(unittest.TestCase):
    def test_single_winning(self):
        words = ["bear", "coat", "cat", "dog"]
        winnings_letters = ["b"]

        self.assertListEqual(winnings_letters, Ghost.optimal_starting_letters(words))

    def test_dual_winning(self):
        words = ["bear", "calf", "cat", "dog"]
        winning_letters = ["b", "c"]

        self.assertListEqual(winning_letters, Ghost.optimal_starting_letters(words))

    def test_no_winning(self):
        words = ["bear", "bea", "cat", "dog"]
        self.assertListEqual([], Ghost.optimal_starting_letters(words))
