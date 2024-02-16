#!/usr/bin/python3
"""This module defines the base class"""


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        "Initializes the Base class"
        if id is None:
            """ If Id is None, create new id by incrementing __nb_objects"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
