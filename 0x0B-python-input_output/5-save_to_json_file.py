#!/usr/bin/python3
"""Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes aan Object to a text file"""

    with open('filename', mode='w', encoding='utf-8') as myfile:
        myfile.write(json.dumps(my_obj))
