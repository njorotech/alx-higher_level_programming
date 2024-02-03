#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status using requests"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response")
    print(f"\t- type: {r.__class__}")
    print(f"\t- content: {r.content}")
