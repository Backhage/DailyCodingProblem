import unittest

from Graphs.SnakesAndLadders import minimum_turns


class TestBeatSnakesAndLadders(unittest.TestCase):
    def test_bookTestCase(self):
        snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
        ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}

        self.assertEqual(6, minimum_turns(snakes, ladders))
