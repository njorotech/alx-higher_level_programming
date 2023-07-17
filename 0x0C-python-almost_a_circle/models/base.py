#!/usr/bin/python3
"""Base class model"""


class Base:
    """Base class for all the classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an object of the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
