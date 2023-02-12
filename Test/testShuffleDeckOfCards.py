import unittest

from Algorithms.Randomized.ShuffleDeckOfCards import shuffle


class TestShuffleDeckOfCards(unittest.TestCase):
    def test_shuffleDeck(self):
        card_ids = list(range(1, 53))
        shuffled = shuffle(card_ids)
        self.assertEqual(52, len(shuffled))
        self.assertEqual(52, len(set(shuffled)))
        for card_id in range(1, 53):
            self.assertIn(card_id, shuffled)
