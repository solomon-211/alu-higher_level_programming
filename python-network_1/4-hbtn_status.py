#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status using requests package
and displays the formatted response body.
"""

import requests

if __name__ == "__main__":
    response = requests.get('http://0.0.0.0:5050/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
