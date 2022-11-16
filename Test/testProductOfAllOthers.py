import unittest

from Arrays.ProductOfAllOthers import products


class TestProductOfAllOthers(unittest.TestCase):
    def test_bookTestCase1(self):
        input = [1, 2, 3, 4, 5]
        expectedResult = [120, 60, 40, 30, 24]
        self.assertListEqual(products(input), expectedResult)

    def test_bookTestCase2(self):
        input = [3, 2, 1]
        expectedResult = [2, 3, 6]
        self.assertListEqual(products(input), expectedResult)


if __name__ == "__main__":
    unittest.main()
