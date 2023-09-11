#!/usr/bin/python3

"""Only subclass of"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited
    from the specified class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
