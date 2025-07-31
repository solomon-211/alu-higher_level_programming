#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status using urllib package
and displays the formatted response body.
"""

from urllib.request import urlopen

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
