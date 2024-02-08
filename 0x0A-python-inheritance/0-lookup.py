#!/usr/bin/python3
'''This module contains a function that looks up the attributes and methods
available to an object'''


def lookup(obj):
    ''' A function that checks the available methods
    and attributes available to an object.
    Args:
        obj - Object
    Returns:
        A list of available attributes and methods
    '''
    return (list(dir(obj)))
