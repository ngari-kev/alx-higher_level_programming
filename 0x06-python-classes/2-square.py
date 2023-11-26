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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        