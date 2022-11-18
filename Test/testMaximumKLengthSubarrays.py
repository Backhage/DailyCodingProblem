import unittest

from Queues.MaxKLenSubarrays import max_of_subarrays


class TestMaxKLenSubarrays(unittest.TestCase):
    def test_bookTestCase(self):
        input = [10, 5, 2, 7, 8, 7]
        expected_result = [10, 7, 8, 8]

        self.assertListEqual(max_of_subarrays(input, 3), expected_result)
