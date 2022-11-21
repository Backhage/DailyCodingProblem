import unittest

from HashTables.FewestCuts import fewest_cuts


class TestFewestCuts(unittest.TestCase):
    def test_bookTestCase(self):
        input = [
            [3, 5, 1, 1],
            [2, 3, 3, 2],
            [5, 5],
            [4, 4, 2],
            [1, 3, 3, 3],
            [1, 1, 6, 1, 1],
        ]
        self.assertEqual(fewest_cuts(input), 2)
