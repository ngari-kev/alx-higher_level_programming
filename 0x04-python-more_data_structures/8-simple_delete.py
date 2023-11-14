#!/usr/bin/python3
'''
A function that deletes a dictionary entry using the key
'''


def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
