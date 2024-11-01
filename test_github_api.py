import unittest
from unittest.mock import patch
from github_api import get_user_repos_commits  # Import the function to test

class TestGitHubAPI(unittest.TestCase):

    @patch('github_api.requests.get')  # Mock requests.get in the github_api module
    def test_get_user_repos_commits(self, mock_get):
        # Mock response for the list of repositories
        mock_get.side_effect = [
            # First call to requests.get (for repos list)
            unittest.mock.Mock(status_code=200, json=lambda: [
                {"name": "repo1"},
                {"name": "repo2"}
            ]),
            # Second call to requests.get (for commits in repo1)
            unittest.mock.Mock(status_code=200, json=lambda: [{}] * 5),  # 5 commits in repo1
            # Third call to requests.get (for commits in repo2)
            unittest.mock.Mock(status_code=200, json=lambda: [{}] * 10)  # 10 commits in repo2
        ]

        # Call the function and get the result
        result = get_user_repos_commits('dummy_user')

        # Define the expected output based on mocked responses
        expected_output = [
            'Repo: repo1 - Number of commits: 5',
            'Repo: repo2 - Number of commits: 10'
        ]

        # Check if the actual result matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
