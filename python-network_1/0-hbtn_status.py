#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status using urllib package
and displays the response body with specific formatting.
"""

from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
