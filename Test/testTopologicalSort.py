import unittest

from Graphs.TopologicalSort import find_order


class TestTopologicalSort(unittest.TestCase):
    def test_bookTestCase(self):
        course_to_prereqs = {
            "CSC300": ["CSC100", "CSC200"],
            "CSC200": ["CSC100"],
            "CSC100": [],
        }
        expected_result = ["CSC100", "CSC200", "CSC300"]

        self.assertListEqual(find_order(course_to_prereqs), expected_result)
