import unittest

from Arrays.SmallestWindowToBeSorted import window


class TestSmallestWindowToBeSorted(unittest.TestCase):
    def test_bookTestCase(self):
        input = [3, 7, 5, 6, 9]
        expectedResult = (1, 3)
        self.assertTupleEqual(window(input), expectedResult)


if __name__ == "__main__":
    unittest.main()
