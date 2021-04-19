#!/usr/bin/env python3
""" This module tests the utils.py file """
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
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
    """ Class for testing get_json function """

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
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class for testing memoize function """

    def test_memoize(self):
        """ Test function for memoize """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_obj:
            mock_tc = TestClass()
            first_call = mock_tc.a_property
            second_call = mock_tc.a_property
            self.assertEqual(first_call, mock_obj.return_value)
            self.assertEqual(second_call, mock_obj.return_value)
            mock_obj.assert_called_once()


if __name__ == '__main__':
    unittest.main()
