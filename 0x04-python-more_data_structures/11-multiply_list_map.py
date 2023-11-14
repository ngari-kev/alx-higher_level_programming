#!/usr/bin/python3
'''
A function that multiplies elements of a list by a number
'''


def multiply_list_map(my_list=[], number=0):
    result = list(map(lambda x: x * number, my_list))
