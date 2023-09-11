#!/usr/bin/python3

"""Geometry module"""


class BaseGeometry:
    """An Geometry class"""

    def area(self):
        """A method that implements the area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
