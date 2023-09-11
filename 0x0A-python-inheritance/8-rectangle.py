#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Rectangle module"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiates Rectangle objects"""

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
