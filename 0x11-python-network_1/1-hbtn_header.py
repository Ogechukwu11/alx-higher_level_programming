#!/usr/bin/python3
""" A python script that takes in a URL, \
    sends a request to the URL and displays the value of\
    the X-Request-Id variable found in the header of the response.
    Using urllib and sys packages.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    with urllib.request.urlopen(url_arg) as r:
        x_request_id = r.headers.get("X-Request-Id")
        print(x_request_id)
