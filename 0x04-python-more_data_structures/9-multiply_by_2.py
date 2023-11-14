#!/usr/bin/python3
'''
A function that returns a dictionary with values * 2
'''


def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    for key in dic:
        dic[key] *= 2
    return dict(sorted(dic.items()))
