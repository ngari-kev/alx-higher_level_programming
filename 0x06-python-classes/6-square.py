#!/usr/bin/python3
'''
This module defines a square class
'''


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        '''new Square.
        Args:
            size (must be an int): The size of the new square.
            position (must be a tuple): The position of the square when printed
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''access current size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Sets the actual size of the square'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        '''sets the position of the square'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' This method calculates the area of a square'''
        return (self.__size ** 2)

    def my_print(self):
        '''This method prints the square using the #'''
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
            
        for col in range(self.__size):
            for pos in range(self.__position[0]):
                print(" ")
                for row in range(self.__size):
                    print("#", end="")
            print("")
