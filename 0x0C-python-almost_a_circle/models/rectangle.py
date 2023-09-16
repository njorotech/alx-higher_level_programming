#!/usr/bin/python3
"""First Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle class objects"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the value of y"""

        return self.__x

    @y.setter
    def y(self, value):
        """Sets the value of x"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints Rectangle to stdout with character #"""

        for item in range(self.__y):
            print()

        for i in range(self.__height):
            for item in range(self.__x):
                print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        """String representation of the Rectangle class"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args):
        """Assigns argument to each attribute"""

        ac = len(args)
        if ac >= 1:
            self.id = args[0]
        if ac >= 2:
            self.__width = args[1]
        if ac >= 3:
            self.__height = args[2]
        if ac >= 4:
            self.__x = args[3]
        if ac >= 5:
            self.__y = args[4]
