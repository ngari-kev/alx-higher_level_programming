#!/usr/bin/python3
'''
A function that checks and returns commomn elements in 2 sets
'''


def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    common = set_1.intersection(set_2)
    return common
