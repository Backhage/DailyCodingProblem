import unittest

from Algorithms.Recursive.TowerOfHanoi import tower_of_hanoi


class TestTowerOfHanoi(unittest.TestCase):
    def test_towerOfHanoi(self):
        expected = [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)]
        self.assertListEqual(expected, tower_of_hanoi(3))
