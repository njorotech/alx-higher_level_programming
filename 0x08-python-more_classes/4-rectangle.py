#!/usr/bin/python3

"""Eval is magic"""


class Rectangle:
    """A class that defines a rectangle based on width and height"""

    def __init__(self, width=0, height=0):
        """Intializes an instance of the Rectangle class"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """computes the rectangle perimeter"""

        if (self.width == 0) or (self.height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """string representation of the object"""

        if (self.__width == 0) or (self.__height == 0):
            empty_string = ""
            return empty_string
        else:
            string_print = ""
            for i in range(self.__height):
                string_print += "#" * self.__width + "\n"
            return string_print[:-1]

    def __repr__(self):
        """string representation to recreate new instance of rectangle"""

        return ("Rectangle(" + str(self.__width)
                + ", " + str(self.__height) + ")")
