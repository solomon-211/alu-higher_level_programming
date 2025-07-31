#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib package
with proper SSL context and displays the formatted response.
"""

from urllib.request import urlopen, Request
import ssl

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # Create unverified SSL context
    context = ssl._create_unverified_context()
    
    try:
        with urlopen(req, context=context) as response:
            body = response.read()
            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
            print("\t- utf8 content:", body.decode('utf-8'))
    except Exception as e:
        print("Error fetching URL:", e)
