import unittest

from Algorithms.Backtracking.AndroidUnlockCombinations import unlock_combinations


class TestAndroidUnlockCombinations(unittest.TestCase):
    def test_androidUnlockCombinations(self):
        self.assertEqual(9, unlock_combinations(1))
        self.assertEqual(56, unlock_combinations(2))
        self.assertEqual(320, unlock_combinations(3))
        self.assertEqual(1624, unlock_combinations(4))
        self.assertEqual(7152, unlock_combinations(5))
        self.assertEqual(26016, unlock_combinations(6))
