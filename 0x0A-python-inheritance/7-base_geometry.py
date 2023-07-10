#!/usr/bin/python3

"""Base Geometry class"""


class BaseGeometry:
    """class for base geometry"""

    def area(self):
        """raises  exceptin"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f'{self.name} must be an integer')
        if value <= 0:
            raise ValueError(f'{self.name} must be greater than 0')
