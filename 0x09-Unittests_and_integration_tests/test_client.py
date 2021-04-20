#!/usr/bin/env python3
""" This module tests the clients.py file """
from unittest import mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test function for client.GithubOrgClient.has_license """
        new_client = GithubOrgClient("new_org")
        self.assertEqual(new_client.has_license(repo, license_key), expected)


@parameterized_class([{"org_payload": TEST_PAYLOAD[0][0],
                      "repos_payload": TEST_PAYLOAD[0][1],
                       "expected_repos": TEST_PAYLOAD[0][2],
                       "apache2_repos": TEST_PAYLOAD[0][3]}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for integration test of GithubOrgClient """

    @classmethod
    def setUpClass(cls):
        """ setUp function to run before tests """
        cls.get_patcher = patch('requests.get')
        cls.get_patcher.side_effect = cls.side_effect()
        cls.get_patcher.start()

    @classmethod
    def side_effect(cls):
        """ Checks url for validity """
        assert cls.get_patcher.return_value == TEST_PAYLOAD
        # use side_effect to make sure the mock of requests.get(url).json()
        # returns the correct fixtures for the various
        # values of url that you anticipate to receive

    # only mock code that sends external requests
    # def test_public_repos(self):
    #     """ Test function for public_repos """
    #     repos = self.__class__.get_patcher("")

    @classmethod
    def tearDownClass(cls):
        """ tearDown function to run after tests """
        cls.get_patcher.stop()
