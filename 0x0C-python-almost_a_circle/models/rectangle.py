#!/usr/bin/python3
"""
This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    This defines a new Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @x.setter
    def x(self, value):
        """ Setter for x"""
        if value < 0:
            raise TypeError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints the rectangle to stdout"""
        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """String representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
            )
