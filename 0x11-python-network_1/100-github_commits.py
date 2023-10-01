#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the repository

Usage: ./100-github_commits.py <repository name> <owner name>
"""
if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    url = url + "/commits?sort=committer-date&order=asc&per_page=10"

    response = requests.get(url)

    for item in response.json():
        print("{}: {}".format(item.get('sha'),
                              item.get('commit').get('author').get('name')))
