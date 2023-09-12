#!/usr/bin/python3
"""Append to file function module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
