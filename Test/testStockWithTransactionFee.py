import unittest

from Algorithms.DynamicProgramming import StockWithTransactionFee


class TestStockWithTransactionFee(unittest.TestCase):
    def test_leetcode_1(self):
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        expected_result = 8

        self.assertEqual(
            expected_result, StockWithTransactionFee.max_profit(prices, fee)
        )

    def test_leetcode_2(self):
        prices = [1, 3, 7, 5, 10, 3]
        fee = 3
        expected_result = 6

        self.assertEqual(
            expected_result, StockWithTransactionFee.max_profit(prices, fee)
        )
