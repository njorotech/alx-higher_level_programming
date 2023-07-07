#!/usr/bin/python3

""" A rectangle class"""


class Rectangle:
    """ A class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Instantiates an object of the rectangle class"""

        self.width = width
        self.height = height

    def width(self):
        """A method to retrieve the width of the object"""

        return self.__width

    def width(self, value):
        """A method to set the width of the object"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    def height(self):
        """A method to retrieve the height of the object"""

        return self.__height

    def height(self, value):
        """A method to set the height of the object"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be an integer')
        else:
            self.__height = value
