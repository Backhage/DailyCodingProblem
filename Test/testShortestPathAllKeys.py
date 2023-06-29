import unittest

from Graphs import ShortestPathAllKeys


class TestShortestPathAllKeys(unittest.TestCase):
    def test_only_keys_are_needed(self):
        input = ["@.a..", "###.#", "b.A.B"]
        expected_result = 8
        self.assertEqual(
            expected_result, ShortestPathAllKeys.shortest_path_all_keys(input)
        )

    def test_dont_walk_back(self):
        input = ["@..aA", "..B#.", "....b"]
        expected_result = 6
        self.assertEqual(
            expected_result, ShortestPathAllKeys.shortest_path_all_keys(input)
        )

    def test_unsolvable(self):
        input = ["@Aa"]
        expected_result = -1
        self.assertEqual(
            expected_result, ShortestPathAllKeys.shortest_path_all_keys(input)
        )
