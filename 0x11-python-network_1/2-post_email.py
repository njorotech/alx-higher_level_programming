#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = 'njorogemuchoki15@gmail.com'
    values = {'email': email}
    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as r:
        response = r.read()
    print(response.decode('utf-8'))
