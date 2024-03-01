#!/usr/bin/python3
""" A Python script that takes in a URL,\
    sends a request to the URL and\
    displays the body of the response (decoded in utf-8).
    To manage urllib.error.HTTPError exceptions.
    using urllib and sys package only.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    try:
        with urllib.request.urlopen(url_arg) as r:
            response = r.read().decode("utf-8")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
