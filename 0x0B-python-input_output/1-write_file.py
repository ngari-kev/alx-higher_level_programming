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
    """
    with open(filename, 'w') as file:
        file.write(text)
