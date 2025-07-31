#!/usr/bin/python3
"""
Fetches status URL using requests package.
Displays formatted response body.
"""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    try:
        response = requests.get(url)
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.RequestException:
        print("Error fetching URL")
