#!/usr/bin/python3

"""A class that prints a square"""


class Square:
    """Defines a square with size"""

    def __init__(self, size=0):
        """Initialize square object with given size

        Args:
            size(int): Size of the square
        """

        self.__size = size

    @property
    def size(self):
        """retrieve the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square to value

        Args:
            size(int): size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """compute the area of a square"""

        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        else:
            i = 0
            while i < self.__size:
                j = 0
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1
