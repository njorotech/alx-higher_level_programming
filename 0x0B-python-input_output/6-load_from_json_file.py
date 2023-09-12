#!/usr/bin/python3
"""Create object from a JSON file module"""

import json


def load_from_json_file(filename):
    """Creates an Object from a Json file"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
