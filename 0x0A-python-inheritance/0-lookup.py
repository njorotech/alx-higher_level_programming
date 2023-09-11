#!/usr/bin/python3

""" Module for a function that shows the list of available attributes and methods"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object"""

    return dir(obj)
