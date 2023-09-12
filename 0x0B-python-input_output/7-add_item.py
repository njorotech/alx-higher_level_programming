#!/usr/bin/python3
"""Load, add, save module"""

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
save_to_json_file(arguments, 'json_file')
load_from_json_file('json_file')
