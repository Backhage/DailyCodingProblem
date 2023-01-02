import unittest

from Algorithms.Backtracking.NQueensPuzzle import n_queens


class TestNQueensPuzzle(unittest.TestCase):
    def test_n_queens(self):
        self.assertEqual(1, n_queens(1))
        self.assertEqual(0, n_queens(2))
        self.assertEqual(0, n_queens(3))
        self.assertEqual(2, n_queens(4))
        self.assertEqual(10, n_queens(5))
        self.assertEqual(724, n_queens(10))
