#!/usr/bin/python3

"""A rectangle class"""


class Rectangle:
    """class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """instantiates the object"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """a method to retrieve the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """A method to set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """A method to retrieve the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """A method to set the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """A method that the rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """A method that returns the perimeter of the rectangle"""
        if (self.__height == 0) or (self.__width == 0):
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """returns a string representation of an instance"""

        if (self.__height == 0) or (self.__width == 0):
            return ""
        else:
            return "\n".join(["#" * self.__width] * self.height)

    def __repr__(self):
        """returns a string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance"""

        print("Bye rectangle...")
