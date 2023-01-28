import unittest

from Algorithms.Pathfinding.BellmanFord import find_cheapest_price


class TestBellmanFord(unittest.TestCase):
    def test_leetcode_tc1(self):
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1

        self.assertEqual(700, find_cheapest_price(n, flights, src, dst, k))

    def test_leetcode_tc2(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1

        self.assertEqual(200, find_cheapest_price(n, flights, src, dst, k))

    def test_leetcode_tc3(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0

        self.assertEqual(500, find_cheapest_price(n, flights, src, dst, k))

    def test_leetcode_tc4(self):
        n = 5
        flights = [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]]
        src = 2
        dst = 1
        k = 1

        self.assertIsNone(find_cheapest_price(n, flights, src, dst, k))
