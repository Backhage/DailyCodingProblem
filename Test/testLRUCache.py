import unittest

from HashTables.LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_LRUCache(self):
        cache = LRUCache(3)
        cache.set("a", 1)
        cache.set("b", 2)
        cache.set("c", 3)

        self.assertIsNone(cache.get("d"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), 3)

        cache.set("d", 4)
        cache.set("b", 5)

        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get("d"), 4)

    def test_LeetCodeExample(self):
        cache = LRUCache(2)

        cache.set(2, 1)
        cache.set(1, 1)
        cache.set(2, 3)
        cache.set(4, 1)

        self.assertIsNone(cache.get(1))
        self.assertEqual(cache.get(2), 3)
