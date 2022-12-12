import unittest

from Graphs.Graph import has_cycle


class TestDetermineIfCycleExists(unittest.TestCase):
    def test_cycleExists(self):
        graph = {
            "ORL": ["DFW", "LAX", "JFK"],
            "JFK": ["SFO", "LAX"],
            "SFO": ["ORL"],
            "LAX": ["DFW"],
            "DFW": [],
        }

        self.assertTrue(has_cycle(graph))

    def test_noCycleExists(self):
        graph = {"JFK": ["LAX"], "LAX": []}

        self.assertFalse(has_cycle(graph))
