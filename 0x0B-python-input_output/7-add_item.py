#!/usr/bin/python3
"""Load, add, save module"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        arguments_list = load_from_json_file('add_item.json')
    except Exception:
        arguments_list = []

    for arg in sys.argv[1:]:
        arguments_list.append(arg)

    save_to_json_file(arguments_list, 'add_item.json')
    load_from_json_file('add_item.json')
