#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the
GitHub API to display your id. Uses Basic Authentication with a personal
access token as password.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print(None)
