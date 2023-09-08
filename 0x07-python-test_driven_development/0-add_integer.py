#!/usr/bin/python3
"""This is a simple add 2 integers function documentation"""


def add_integer(a, b=98):
    """ A function that adds 2 integers """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
