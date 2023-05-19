import unittest

from Algorithms.AdvancedAlgorithms.RabinKarp import find_matches


class TestRabinKarp(unittest.TestCase):
    def test_abracadabra(self):
        string = "abracadabra"
        pattern = "abr"

        self.assertListEqual(find_matches(pattern, string), [0, 7])

    def test_nomatch(self):
        string = "aeiou"
        pattern = "bc"

        self.assertListEqual(find_matches(pattern, string), [])


if __name__ == "__main__":
    unittest.main()
