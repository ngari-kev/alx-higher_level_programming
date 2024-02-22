#!/usr/bin/python3

"""This module contains the Square class"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square class. It inherrits from Base"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of a new square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
