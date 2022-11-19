import unittest

from Stacks.ReconstructArray import reconstruct


class TestReconstructArray(unittest.TestCase):
    def test_bookTestCase(self):
        input = [None, "+", "+", "-", "+"]
        expected_output = [0, 1, 3, 2, 4]
        self.assertListEqual(reconstruct(input), expected_output)
