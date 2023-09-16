#!/usr/bin/python3
"""First Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class objects"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Retrieves the value of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""

        self.__width = value

    @property
    def height(self):
        """Retrieves the height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""

        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""

        return self.__x
    
    @x.setter
    def x(self, value):
        """Sets the value of x"""

        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y"""

        return self.__x

    @y.setter
    def y(self, value):
        """Sets the value of x"""

        self.__y = value
