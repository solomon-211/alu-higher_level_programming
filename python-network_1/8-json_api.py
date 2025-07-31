#!/usr/bin/python3
"""
Sends POST request with letter parameter.
Processes JSON response from server.
"""

import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(
                json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
