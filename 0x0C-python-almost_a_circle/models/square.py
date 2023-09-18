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
                self.y, self.width))

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

    def update(self, *args, **kwargs):
        """Assigns attributes from arguments"""

        if args:
            ac = len(args)
            if ac >= 1:
                self.id = args[0]
            if ac >= 2:
                self.size = args[1]
            if ac >= 3:
                self.x = args[2]
            if ac >= 4:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictinary(self):
        """Dictionary representation of a Square"""

        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
