#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status using requests"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:i")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
