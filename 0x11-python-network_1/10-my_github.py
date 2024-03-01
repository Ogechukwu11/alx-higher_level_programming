#!/usr/bin/python3
""" A Python script that takes your GitHub \
    credentials (username and password) \
    and uses the GitHub API to display your id.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url_arg = "https://api.github.com/user"

    authen = HTTPBasicAuth(username, password)
    result = requests.get(url_arg, auth=authen)
    print(result.json().get("id"))
