#!/usr/bin/python3

"""Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiates Rectangle objects"""

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """A method that implements the area"""

        return self.__width * self.__height

    def __str__(self):
        """string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
