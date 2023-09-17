#!/usr/bin/python3
"""The square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes objects of the square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square class"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.height))

    @property
    def size(self):
        """Retrieves the size value"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
