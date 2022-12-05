import unittest

from Heaps.FindMostSimilarWebsites import top_pairs


class TestFindMostSimilarWebites(unittest.TestCase):
    def test_bookTestCase(self):
        input_log = [
            ("google.com", 1),
            ("google.com", 3),
            ("google.com", 5),
            ("pets.com", 1),
            ("pets.com", 2),
            ("yahoo.com", 6),
            ("yahoo.com", 2),
            ("yahoo.com", 3),
            ("yahoo.com", 4),
            ("yahoo.com", 5),
            ("wikipedia.org", 4),
            ("wikipedia.org", 5),
            ("wikipedia.org", 6),
            ("wikipedia.org", 7),
            ("bing.com", 1),
            ("bing.com", 3),
            ("bing.com", 5),
            ("bing.com", 6),
        ]

        expected = [("google.com", "bing.com")]
        self.assertListEqual(expected, top_pairs(input_log, 1))
