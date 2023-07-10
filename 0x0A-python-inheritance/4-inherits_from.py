#!/usr/bin/python3

"""Only subclass of """


def inherits_from(obj, a_class):
    """check if the object is an instance
    of a class that inherited from the specified class
    """

    if issubclass(type(obj), a_class):
        return True
    else:
        return False
