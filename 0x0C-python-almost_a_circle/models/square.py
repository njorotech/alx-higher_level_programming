#!/usr/bin/python3
"""A module for a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    def __str__(self):
        """string representation of square objects"""

        re = "[Square] ({}) {}/{} - {}"
        return re.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """return size value"""

        return size

    @size.setter
    def size(self, size):
        """set the size"""

        super().width(size)
        super().height(size)
