#!/usr/bin/python3
"""Write to file function module"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters
    written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
