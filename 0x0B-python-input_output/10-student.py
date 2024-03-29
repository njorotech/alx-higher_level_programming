#!/usr/bin/python3
"""Student to JSON with filter module"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an object of the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""

        dictionary = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age}
        return dictionary
