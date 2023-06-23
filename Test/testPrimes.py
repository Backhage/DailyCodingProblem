import unittest

from Applications import Primes


class TestPrimes(unittest.TestCase):
    def test_primes_less_than_10(self):
        primes = Primes.primes_less_than(10)
        self.assertListEqual([2, 3, 5, 7], list(primes))

    def test_primes_less_than_100(self):
        primes = Primes.primes_less_than(100)
        self.assertListEqual(
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
            list(primes),
        )

    def test_primes_stream(self):
        all_primes = Primes.primes()
        first_ten_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for i in range(len(first_ten_primes)):
            self.assertEqual(first_ten_primes[i], next(all_primes))
