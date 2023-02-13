import unittest

from Algorithms.Randomized.MarkovChain import histogram_counts


class TestMarkovChain(unittest.TestCase):
    def test_markov_chain(self):
        start = "a"
        probs = [
            ("a", "a", 0.9),
            ("a", "b", 0.075),
            ("a", "c", 0.025),
            ("b", "a", 0.15),
            ("b", "b", 0.8),
            ("b", "c", 0.05),
            ("c", "a", 0.25),
            ("c", "b", 0.25),
            ("c", "c", 0.5),
        ]
        steps = 5000

        outcome = histogram_counts(start, probs, steps)
        self.assertGreater(outcome["a"], 2800)
        self.assertLess(outcome["a"], 3400)

        self.assertGreater(outcome["b"], 1300)
        self.assertLess(outcome["b"], 1900)

        self.assertGreater(outcome["c"], 200)
        self.assertLess(outcome["c"], 400)
