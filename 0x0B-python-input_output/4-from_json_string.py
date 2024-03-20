#!/usr/bin/python3
"""
This module contains one function:from_json_string
"""

import json


def from_json_string(my_str):
    """
    Converts form json string to python object.

    Args:
        my_str - json string.
    Returns:
        Python object.
    """
    obj = json.loads(my_string)
    return obj
