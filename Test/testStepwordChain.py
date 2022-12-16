import unittest

from Graphs.Graph import stepword_chain


class TestStepwordChain(unittest.TestCase):
    def test_successful(self):
        start = "dog"
        end = "cat"
        d = {"dot", "dop", "dat", "cat"}

        self.assertListEqual(
            ["dog", "dot", "dat", "cat"], stepword_chain(start, end, d)
        )

    def test_not_possible(self):
        start = "dog"
        end = "cat"
        d = {"dot", "tod", "dat", "dar"}

        self.assertIsNone(stepword_chain(start, end, d))
