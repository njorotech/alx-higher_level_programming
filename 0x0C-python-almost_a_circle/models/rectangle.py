#!/usr/bin/python3
"""First rectangle module"""

from models.base import Base
class Rectangle(Base):
    """Class rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes an object of the rectangle class"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the rectangle's width"""

        return self.__width

    @width.setter
    def width(self, width):
        """Set the rectangle's width"""

        self.__width = width

    @property
    def height(self):
        """Retrieves the rectangle's height"""

        return self.__height

    @height.setter
    def height(self, height):
        """set the rectangle's height"""

        self.__height = height

    @property
    def x(self):
        """Retrieves the value of x"""

        return self.__x

    @x.setter
    def x(self, x):
        """setting the value of x"""

        self.__x = x

    @property
    def y(self):
        """retriving the value of y"""

        return self.__y

    @y.setter
    def y(self, y):
        """setting the value of y"""

        self.__y = y
