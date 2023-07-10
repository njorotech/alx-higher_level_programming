#!/usr/bin/python3
"""check if an instance"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of a specified class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
