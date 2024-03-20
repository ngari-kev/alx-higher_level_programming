#!/usr/bin/python3
"""
This is a module containg one function: read_file
"""


def read_file(filename=""):
    """
    This is a function that reads from a UTF-8
    encoded file and prints to stdout.

    Args:
        filename - name of file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
