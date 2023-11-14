#!/usr/bin/python3
'''
A function that returns the best score
'''


def best_score(my_dict):
    if my_dict is None:
        return None
    return max(my_dict, key=my_dict.get) if my_dict else None
