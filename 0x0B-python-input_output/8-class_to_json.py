#!/usr/bin/python3
"""Class to JSON"""


def class_to_json(obj):
    """returns the dictionary for JSON serialization"""

    return dir(obj)
