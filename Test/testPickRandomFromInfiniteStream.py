import unittest

from Algorithms.Randomized.RandomFromInfiniteStream import pick


class TestPickRandom(unittest.TestCase):
    def test_pickRandomElement(self):
        self.assertIsNone(pick([]))
        self.assertEqual(42, pick([42]))
        self.assertIn(pick([4, 5, 6]), [4, 5, 6])
