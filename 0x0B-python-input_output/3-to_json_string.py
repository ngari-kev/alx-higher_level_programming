#!/usr/bin/python3
"""
this module contains one function:to_json_string
"""
import json


def to_json_string(my_obj):
    """
    converts an object to a JSON string

    Args:
        my_obj - object to be converted to JSON string

    Returns:
        JSON string
    """
    json_string = json.dumps(my_obj)
    return json_string
