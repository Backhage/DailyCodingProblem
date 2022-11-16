import unittest

from Arrays.MaximumSubarraySum import max_subarray_sum


class TestMaximumSubarraySum(unittest.TestCase):
    def test_bookTestCase1(self):
        input = [34, -50, 42, 14, -5, 86]
        expectedResult = 137
        self.assertEqual(max_subarray_sum(input), expectedResult)

    def test_bookTestCase2(self):
        input = [-5, -1, -8, -9]
        expectedResult = 0
        self.assertEqual(max_subarray_sum(input), expectedResult)


if __name__ == "__main__":
    unittest.main()
