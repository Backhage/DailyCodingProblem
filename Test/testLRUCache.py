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
