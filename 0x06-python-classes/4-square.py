#!/usr/bin/python3

"""class to access and update private attribute"""


class Square:
    """defines a square by size"""
    def __init__(self, size=0):
        """Initializes square object with size

        Args:
            size(int): square size with default 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0.
        """

        self.__size = size

    @property
    def size(self):
        """return size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square

        Args:
            value(int): size of the square

        Raises:
            TypeErrror: If size is not an integer.
            ValueError: if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return area of the square"""

        return self.size ** 2
