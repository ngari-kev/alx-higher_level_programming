#!/usr/bin/python3
'''This is a rectangle class'''


class Rectangle:
    '''The rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
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

    def __str__(self):
        '''Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        '''
        if self.__height == 0 or self.__width == 0:
            return ("")
        rect = ""
        for _ in range(self.__height):
            rect = rect + "#" * self.width + "\n"
        return rect.rstrip()
    
    def __repr__(self):
        '''Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        '''
        if self.__height == 0 or self.__width == 0:
            return ("")
        s = f"Rectangle(width={self.__width}, height={self.__height})"
        return s

    def __del__(self):
        '''Deletes an instance'''
        print("Bye rectangle ...")