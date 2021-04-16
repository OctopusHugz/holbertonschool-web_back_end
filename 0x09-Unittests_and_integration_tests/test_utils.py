#!/usr/bin/env python3
""" This module tests the utils.py file """
from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test function for access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ Test function for throwing an exception in access_nested_map """
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)
            self.assertEqual(ke, expected_msg)


if __name__ == '__main__':
    unittest.main()
