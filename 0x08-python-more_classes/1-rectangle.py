#!/usr/bin/python3
class Rectangle:
    """
    Represents a Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialization of a new rectangle
        Args:
            width (optional, default = 0, must be an int): The width of the rectangle.
            height (optional, default = 0, must be an int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
