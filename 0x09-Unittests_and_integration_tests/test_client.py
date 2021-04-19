#!/usr/bin/env python3
""" This module tests the clients.py file """
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing access_nested_map function """

    # @patch('client.org')
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org_name):
        """ Test function for client.org """
        with patch('client.GithubOrgClient.org') as mock_org:
            # Should test that GitHubOrgClient.org returns the correct value
            new_client = GithubOrgClient(org_name=org_name)
            # Use @patch as a decorator to make sure get_json is called once
            # with the expected argument but make sure it is not executed
            self.assertEqual(new_client.org.return_value,
                             mock_org.return_value)
