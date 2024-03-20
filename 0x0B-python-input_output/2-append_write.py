#!/usr/bin/python3

"""
This module contains one function: append_write.
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename - name of file.
        text - text to be appended.

    Returns:
        characters number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_appended = file.write(text)
        return characters_appended
