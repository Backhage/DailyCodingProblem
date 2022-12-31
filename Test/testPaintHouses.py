import unittest

from Algorithms.DynamicProgramming.PaintingHouses import build_houses


class TestPaintHouses(unittest.TestCase):
    def test_paint_houses(self):
        cost_matrix = [[1, 5, 3], [2, 9, 4]]
        expected_result = 5

        self.assertEqual(build_houses(cost_matrix), expected_result)
