#!/usr/bin/python3
"""
Sends a POST request with email parameter and displays response body.
Uses only requests and sys packages.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
