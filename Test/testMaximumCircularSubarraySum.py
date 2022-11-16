import unittest

from Arrays.MaximumCircularSubarraySum import maximum_circular_subarray


class TestMaximumCircularSubarray(unittest.TestCase):
    def test_bookTestCase(self):
        input = [8, -1, 3, 4]
        expected_result = 15
        self.assertEqual(maximum_circular_subarray(input), expected_result)


if __name__ == "__main__":
    unittest.main()
