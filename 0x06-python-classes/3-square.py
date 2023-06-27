#!/usr/bin/python3

"""Area of a square class"""


class Square:
    """Defines a square by size"""

    def __init__(self, size=0):
        """Initialize a square object with size

        Args:
            size(int): square size with default of 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """return the area of a square"""

        return self.__size * self.__size
