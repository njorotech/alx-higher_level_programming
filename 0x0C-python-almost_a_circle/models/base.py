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
            with open(file_name, 'w', encoding="utf-8") as f:
                f.write("[]")
        else:
            with open(file_name, 'w', encoding="utf-8") as f:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""

        if (json_string is None) or (json_string == ""):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        dummy = Rectangle(2, 3, 0, 0)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
