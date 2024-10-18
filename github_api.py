import requests

def get_user_repos_commits(user_id):
    """
    Given a GitHub user ID, fetch the list of repositories and the number of commits in each repository.
    """
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)
    
    if repos_response.status_code != 200:
        return f"Error: Unable to fetch repositories for user {user_id}"

    repos = repos_response.json()
    result = []

    for repo in repos:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        
        if commits_response.status_code != 200:
            result.append(f"Repo: {repo_name} - Error retrieving commits")
        else:
            commits = commits_response.json()
            commit_count = len(commits)
            result.append(f"Repo: {repo_name} - Number of commits: {commit_count}")
    
    return result

# Example usage
if __name__ == "__main__":
    user = "richkempinski"  # Replace this with any GitHub username.
    print(get_user_repos_commits(user))
# Test trigger for GitHub Actions workflow
