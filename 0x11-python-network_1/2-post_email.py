#!/usr/bin/python3
""" A Python script that takes in a URL and an email,\
    sends a POST request to the passed URL with the email as a parameter,\
    and displays the body of the response (decoded in utf-8). \
    Using urllib and sys packages.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url_arg = sys.argv[1]
    email_value = sys.argv[2]

    data = urllib.parse.urlencode({"email": email_value}).encode('utf-8')
    with urllib.request.urlopen(url_arg, data) as r:
        body = r.read().decode('utf-8')
        print(body)
