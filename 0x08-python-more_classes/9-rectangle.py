#!/usr/bin/python3
'''This is a rectangle class'''


class Rectangle:
    '''The rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            rect = rect + self.print_symbol * self.width + "\n"
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the bigger rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the larger area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Returns a Rectangle instance with width == height == size.

        Args:
            size: length

        Returns:
            Square with sides == size.
        '''
        return (cls(size, size))