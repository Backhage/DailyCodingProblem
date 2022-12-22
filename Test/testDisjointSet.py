import unittest

from AdvancedDataStructures.DisjointSet import friend_groups


class TestDisjointSet(unittest.TestCase):
    def test_bookTestCase(self):
        friendship_list = {0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}
        self.assertEqual(friend_groups(friendship_list), 3)
