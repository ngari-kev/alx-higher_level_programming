#!/usr/bin/python3
'''
   A function that adds all unique integers and returns result
'''


def uniq_add(my_list=[]):
    if my_list is None:
        return None
    new = set(my_list)
    summ = 0
    for uniq in new:
        summ += uniq
    return summ
