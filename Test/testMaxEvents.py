import unittest
from Algorithms.DynamicProgramming import MaxEvents


class TestMaxEvents(unittest.TestCase):
    def test_two_back_to_back(self):
        events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
        k = 2
        self.assertEqual(7, MaxEvents.max_value(events, k))

    def test_one_with_large_value(self):
        events = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
        k = 2
        self.assertEqual(10, MaxEvents.max_value(events, k))

    def test_best_of_several_adjecent(self):
        events = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
        k = 3
        self.assertEqual(9, MaxEvents.max_value(events, k))
