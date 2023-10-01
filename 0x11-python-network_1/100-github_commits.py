#!/usr/bin/python3
"""
Lists 10 commits from a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./100-github_commits.py <repository> <owner>")

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        sys.exit(f"Request error: {e}")
    except ValueError as ve:
        sys.exit(f"JSON decoding error: {ve}")
