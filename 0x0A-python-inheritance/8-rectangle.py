#!/usr/bin/python3
if __name__ == "__main__":
    from 7-base_geometry import BaseGeometry
"""class Rectangle that inherits BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
