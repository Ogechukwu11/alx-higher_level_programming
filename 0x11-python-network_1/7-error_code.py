#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to the URL,\
    and displays the body of the response. If the HTTP status\
    code is greater than or equal to 400,\
    it prints: Error code: followed by the value of\
    the HTTP status code. Uses only requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    result = requests.get(url_arg)
    if result.status_code >= 400:
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)
