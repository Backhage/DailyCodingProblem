import unittest

from Algorithms.Pathfinding.Dijkstras import dijkstras


class TestDijkstras(unittest.TestCase):
    def test_dijkstras(self):
        edges = [
            (0, 1, 5),
            (0, 2, 3),
            (0, 5, 4),
            (1, 3, 8),
            (2, 3, 1),
            (3, 4, 5),
            (3, 5, 10),
        ]
        self.assertEquals(9, dijkstras(5, edges))
