#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status\
    using request package.
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    result = response.text
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
