#!/usr/bin/python3

"""
This module contains the Rectangle class
"""


class Rectangle(Base):
    """
    This defines a new Rectangle class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        super().__init__.(id)


    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """WIdth setter"""
        self.__width = value


    @property
    def height(self):
        """Height setter"""
        return self.__height


    @height.setter
    """Height setter"""
    def height(self, value):
        self.__height = value

    
    @proprty
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
        self.__x = x


    @y.setter
    def y(self):
        """y setter"""
        self.__y = y
