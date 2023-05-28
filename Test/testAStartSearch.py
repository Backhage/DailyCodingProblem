from Algorithms.AdvancedAlgorithms import AStarSearch
import unittest


class TestAStarSearch(unittest.TestCase):
    def test_alreadySolved(self):
        board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTupleEqual((0, ""), AStarSearch.solve(board))

    def test_solve(self):
        board = [1, 2, 3, 7, 4, 0, 8, 6, 5]
        self.assertTupleEqual((7, "URRDLLU"), AStarSearch.solve(board))

        board = [2, 3, 6, 5, 7, 4, 0, 1, 8]
        self.assertTupleEqual((14, "LDRULDLDRRULUL"), AStarSearch.solve(board))
