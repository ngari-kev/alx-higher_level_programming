#!/usr/bin/python3
"""
This is a module containing one function: write_file
"""


def write_file(filename="", text=""):
    """
    Writes text to a file.

    Args:
        filename - name of the file.
        text - text to be written to file.

    Returns:
        number of characters written.
    """
    with open(filename, 'w') as file:
        no_of_characters = file.write(text)
        return no_of_characters
