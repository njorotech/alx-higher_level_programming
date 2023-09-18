#!/usr/bin/python3
"""Base class model"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances of the Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if (list_dictionaries is None) or (list_dictionaries == {}):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
