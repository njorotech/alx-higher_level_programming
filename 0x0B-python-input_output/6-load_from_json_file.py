#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a json file"""

    with open(filename, mode='r', encoding='utf-8') as myfile:
        return json.load(myfile)
