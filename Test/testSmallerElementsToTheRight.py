import unittest

from Arrays.SmallerElementsToTheRight import smaller_count


class TestSmallerElementsToTheRight(unittest.TestCase):
    def test_bookTestCase(self):
        input = [3, 4, 9, 6, 1]
        expected_result = [1, 1, 2, 1, 0]
        self.assertListEqual(smaller_count(input), expected_result)


if __name__ == "__main__":
    unittest.main()
