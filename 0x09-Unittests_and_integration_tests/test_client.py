#!/usr/bin/env python3
""" This module tests the clients.py file """
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
from unittest.mock import PropertyMock, patch
from utils import get_json
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test function for client.GithubOrgClient.public_repos """
        mock_get_json.return_value = [
            {"name": "public_repo_0"}, {"name": "public_repo_1"}]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = "https://api.github.com/users/google/repos"
            new_client = GithubOrgClient("google")
            self.assertEqual(new_client.public_repos(), [repo.get(
                "name") for repo in mock_get_json.return_value])
            mock_get_json.assert_called_once()
            mock_pru.assert_called_once()
