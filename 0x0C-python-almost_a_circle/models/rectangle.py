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

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Retrieves the rectangle's height"""

        return self.__height

    @height.setter
    def height(self, height):
        """set the rectangle's height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Retrieves the value of x"""

        return self.__x

    @x.setter
    def x(self, x):
        """setting the value of x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x

    @property
    def y(self):
        """retriving the value of y"""

        return self.__y

    @y.setter
    def y(self, y):
        """setting the value of y"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

    def area(self):
        """returns the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """String representation"""

        re = "[Rectangle] ({}) {}/{} - {}/{}"
        return re.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        args_no = len(args)
        if args and args_no > 0:
            if args_no > 0:
                self.id = args[0]
            if args_no > 1:
                self.__width = args[1]
            if args_no > 2:
                self.__height = args[2]
            if args_no > 3:
                self.__x = args[3]
            if args_no > 4:
                self.__y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
