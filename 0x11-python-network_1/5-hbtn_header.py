#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    headers = r.headers
    if 'X-Request-Id' in headers:
        print(headers['X-Request-Id'])
