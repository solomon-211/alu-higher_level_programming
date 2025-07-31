#!/usr/bin/python3
"""
Sends a request to URL and displays response body or error code.
Uses only requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
