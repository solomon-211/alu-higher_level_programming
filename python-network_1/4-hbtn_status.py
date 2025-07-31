#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests package
with proper error handling and displays the formatted response.
"""

import requests

if __name__ == "__main__":
    try:
        response = requests.get('https://intranet.hbtn.io/status', verify=False)
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error fetching URL:", e)
