import unittest
from unittest.mock import patch
from github_api import get_user_repos_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_repos_commits(self, mock_get):
        # Mock response for the list of repositories
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: [
                {"name": "repo1"},
                {"name": "repo2"}
            ]),
            # Mock response for commits in repo1
            unittest.mock.Mock(status_code=200, json=lambda: [{}] * 5),
            # Mock response for commits in repo2
            unittest.mock.Mock(status_code=200, json=lambda: [{}] * 10)
        ]

        result = get_user_repos_commits('dummy_user')
        expected_output = [
            'Repo: repo1 - Number of commits: 5',
            'Repo: repo2 - Number of commits: 10'
        ]
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
