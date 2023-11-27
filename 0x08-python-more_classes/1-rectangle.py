#!/usr/bin/python3
'''This is a rectangle class'''


class rectangle:
    '''The rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initializing a new rectangle'''
        self.__width = width
        self.__height = height

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
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''Mutate or set the height parameter'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
