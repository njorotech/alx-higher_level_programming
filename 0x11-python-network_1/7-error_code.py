#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
response. If the HTTP status code is greater than or equal to 400, print:
Error code: followed by the value of the HTTP status code
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    code = r.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(r.text)
