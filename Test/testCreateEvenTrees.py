import unittest

from Graphs.Graph import max_edges


class TestCreateEvenTrees(unittest.TestCase):
    def test_bookTestCase(self):
        input_graph = {
            1: [2, 3],
            2: [],
            3: [4, 5],
            4: [6, 7, 8],
            5: [],
            6: [],
            7: [],
            8: [],
        }

        self.assertEqual(max_edges(input_graph), 2)
