#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': letter})

    try:
        json_dict = r.json()
        if json_dict == {}:
            print("No result")
        else:
            print(f"[{json_dict['id']}] {json_dict['name']}")
    except ValueError:
        print("Not a valid JSON")
