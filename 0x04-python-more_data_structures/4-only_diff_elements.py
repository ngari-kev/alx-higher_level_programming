#!/usr/bin/python3
'''
A function that returns the difference between two sets
'''


def only_diff_elements(set_1, set_2):
    new = set_1.symmetric_difference(set_2)
    return new
