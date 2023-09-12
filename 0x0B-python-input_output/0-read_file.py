#!/usr/bin/python3

"""Read file module"""


def read_file(filename=""):
    """A function that reads a text file and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
