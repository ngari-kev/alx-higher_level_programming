#!/usr/bin/python3
'''
A function that returns a dictionary sorted in ascending order
'''


def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    sortd = dict(sorted(a_dictionary.items()))
    for key, value in a_dictionary.items():
        print("{}: {}".format(key, value))
