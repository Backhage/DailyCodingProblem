import unittest

from Heaps.GenerateRegularNumbers import regular_numbers


class TestGenerateRegularNumbers(unittest.TestCase):
    def test_generateRegularNumbers(self):
        expected = [
            1,
            2,
            3,
            4,
            5,
            6,
            8,
            9,
            10,
            12,
            15,
            16,
            18,
            20,
            24,
            25,
            27,
            30,
            32,
            36,
            40,
            45,
            48,
            50,
            54,
            60,
        ]
        for i, num in enumerate(regular_numbers(len(expected))):
            self.assertEqual(expected[i], num)
