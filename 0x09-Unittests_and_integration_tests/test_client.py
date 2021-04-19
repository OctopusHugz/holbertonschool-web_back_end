#!/usr/bin/env python3
""" This module tests the clients.py file """
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing access_nested_map function """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    def test_org(self, org_name):
        """ Test function for client.GithubOrgClient.org """
        with patch('client.GithubOrgClient.org') as mock_org:
            client = GithubOrgClient(org_name=org_name)
            self.assertEqual(client.org.return_value, mock_org.return_value)

    def test_public_repos_url(self):
        """ Test function for client.GithubOrgClient._public_repos_url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://fake_url.com"}
            test_obj = GithubOrgClient('foo')
            self.assertEqual(test_obj._public_repos_url,
                             "https://fake_url.com")

    # def test_public_repos(self):
    #     """ Test function for client.GithubOrgClient.public_repos """
        # Use @patch as a decorator to mock get_json
        # and make it return a payload of your choice

        # Use patch as a context manager to mock
        # GitHubOrgClient._public_repos_url and return a value of your choice

        # Test that the list of repos is what you expect from chosen payload
        # Test that the mocked property and the mocked get_json was called once
