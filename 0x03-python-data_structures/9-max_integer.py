#!/usr/bin/python3
def max_integer(my_list=[]):
    maxx = 0
    for item in my_list:
        if item > maxx:
            maxx = item
    return maxx
