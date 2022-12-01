import unittest

from Tries.Trie import autocomplete


class TestAutocomplete(unittest.TestCase):
    def test_bookTestCase(self):
        self.assertListEqual(
            autocomplete("de", ["dog", "deer", "deal"]), ["deer", "deal"]
        )
