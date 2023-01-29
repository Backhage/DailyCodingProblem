import unittest

from Algorithms.Pathfinding.FloydWarshall import transitive_closure


class TestFloydWarshall(unittest.TestCase):
    def test_bookTestCase(self):
        graph = [[0, 1, 3], [1, 2], [2], [3]]
        expected_output = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

        self.assertListEqual(expected_output, transitive_closure(graph))
