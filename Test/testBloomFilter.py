import unittest

from AdvancedDataStructures.BloomFilter import BloomFilter


class TestBloomFilter(unittest.TestCase):
    def test_BloomFilter(self):
        bf = BloomFilter(10000)

        # When no elements have been added, all checks must return false.
        for i in range(1000):
            self.assertFalse(bf.check(i))

        # False negatives are not allowed.
        for i in range(1000):
            bf.add(i)

        for i in range(1000):
            self.assertTrue(bf.check(i))

        # Some false positives are allowed, and expected.
        true_count = 0
        for i in range(2000):
            if bf.check(i):
                true_count += 1

        self.assertEqual(true_count, 1016)
