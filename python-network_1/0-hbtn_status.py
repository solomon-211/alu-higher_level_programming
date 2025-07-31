#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib package
with proper error handling and displays the formatted response.
"""

from urllib.request import urlopen
from urllib.error import URLError

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    try:
        with urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))
    except URLError as e:
        print("Error fetching URL:", e)
