#!/usr/bin/python3
""" A Python script that lists 10 commits (from the most recent to oldest)\
    of a given repository by the specified owner using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url_arg = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    result = requests.get(url_arg)
    commits = result.json()
    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
