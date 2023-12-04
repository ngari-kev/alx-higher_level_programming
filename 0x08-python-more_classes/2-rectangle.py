#!/usr/bin/python3
'''This is a rectangle class'''


class Rectangle:
    '''The rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initializing a new rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Access the width parameter'''
        return (self.__width)

    @property
    def height(self):
        '''Access the height parameter'''
        return (self.__height)

    @width.setter
    def width(self, value):
        '''Mutate or set the width parameter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''Mutate or set the height parameter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Function that calculates the area of a rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Method to calculate the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
