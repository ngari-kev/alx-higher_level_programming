#!/usr/bin/python3
'''
This module defines a square class
'''


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        '''new Square.
        Args:
            size (must be an int): The size of the new square.
        '''
        self.size = size

    @property
    def size(self):
        '''access current size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Sets the actual size of the square'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ''' This method calculates the area of a square'''
        return (self.__size ** 2)
