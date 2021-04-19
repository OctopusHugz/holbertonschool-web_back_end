#!/usr/bin/env python3
""" This module tests the utils.py file """
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test function for utils.access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_msg):
        """ Test function for utils.access_nested_map throwing an exception """
        with self.assertRaises(KeyError) as ke:
            access_nested_map(nested_map, path)
            self.assertEqual(ke, expected_msg)


class TestGetJson(unittest.TestCase):
    """ Class for testing get_json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test function for get_json """
        with patch('requests.get') as mock_obj:
            mock_obj.return_value = Mock()
            mock_obj.return_value.json.return_value = test_payload
            response = get_json(test_url)
            # Test that the mocked get method was called exactly once
            # per input with test_url as argument.
            self.assertEqual(response, test_payload)


if __name__ == '__main__':
    unittest.main()
