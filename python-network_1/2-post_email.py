#!/usr/bin/python3
"""
Sends a POST request to URL with email parameter and displays response.
Uses only urllib and sys packages.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
