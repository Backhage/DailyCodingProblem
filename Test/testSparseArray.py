import unittest

from HashTables.SparseArray import SparseArray


class TestSparseArray(unittest.TestCase):
    def test_sparseArray(self):
        capacity = 100000
        large_array = [0 for _ in range(capacity)]
        large_array[1] = 1
        large_array[10] = 10
        large_array[100] = 100
        large_array[1000] = 1000
        large_array[10000] = 10000

        sparse_array = SparseArray(large_array, capacity)

        self.assertEqual(sparse_array.get(0), 0)
        self.assertEqual(sparse_array.get(1), 1)
        self.assertEqual(sparse_array.get(10), 10)
        self.assertEqual(sparse_array.get(100), 100)
        self.assertEqual(sparse_array.get(1000), 1000)
        self.assertEqual(sparse_array.get(10000), 10000)
        self.assertEqual(sparse_array.get(99999), 0)

        with self.assertRaises(IndexError):
            sparse_array.get(-1)

        with self.assertRaises(IndexError):
            sparse_array.get(capacity)

        sparse_array.set(1, 9)
        self.assertEqual(sparse_array.get(1), 9)

        with self.assertRaises(IndexError):
            sparse_array.set(-1, 1)

        with self.assertRaises(IndexError):
            sparse_array.set(capacity, 1)
