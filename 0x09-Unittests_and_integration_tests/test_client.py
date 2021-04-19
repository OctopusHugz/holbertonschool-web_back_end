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
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as mock_org:
            mock_org.return_value = {"repos_url": True}
            client = GithubOrgClient("new_org")
            self.assertEqual(client._public_repos_url, True)
