#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as r:
            response = r.read()
            decoded_response = response.decode('utf-8')
        print(decoded_response)
    except HTTPError as e:
        print('Error code: ', e.code)
