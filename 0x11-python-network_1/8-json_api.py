#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request to\
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url_arg = "http://0.0.0.0:5000/search_user"
    info = {"q": q}
    result = requests.post(url_arg, data=info)
    json_info = result.json()

    try:
        if json_info:
            print("[{}] {}".format(json_info.get('id'), json_info.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
