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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if (list_dictionaries is None) or (list_dictionaries == {}):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representatin of list_objs to a file"""

        class_name = cls.__name__
        file_name = class_name + ".json"
        if list_objs is None:
            list_objs = []
        else:
            with open(file_name, 'w', encoding="utf-8") as f:
                f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

