import unittest

from Algorithms.Backtracking.SolveSudoku import sudoku


class TestSolveSudoku(unittest.TestCase):
    def test_solve_sudoku(self):
        puzzle_one = [
            [0, 0, 9, 7, 4, 8, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 1, 0, 9, 0, 0, 0],
            [0, 0, 7, 0, 0, 0, 2, 4, 0],
            [0, 6, 4, 0, 1, 0, 5, 9, 0],
            [0, 9, 8, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 8, 0, 3, 0, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 2, 7, 5, 9, 0, 0],
        ]

        solution_one = [
            [5, 1, 9, 7, 4, 8, 6, 3, 2],
            [7, 8, 3, 6, 5, 2, 4, 1, 9],
            [4, 2, 6, 1, 3, 9, 8, 7, 5],
            [3, 5, 7, 9, 8, 6, 2, 4, 1],
            [2, 6, 4, 3, 1, 7, 5, 9, 8],
            [1, 9, 8, 5, 2, 4, 3, 6, 7],
            [9, 7, 5, 8, 6, 3, 1, 2, 4],
            [8, 3, 2, 4, 9, 1, 7, 5, 6],
            [6, 4, 1, 2, 7, 5, 9, 8, 3],
        ]

        self.assertListEqual(sudoku(puzzle_one), solution_one)

        puzzle_two = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7],
        ]

        solution_two = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7],
        ]

        self.assertListEqual(sudoku(puzzle_two), solution_two)