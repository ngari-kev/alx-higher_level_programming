#!/usr/bin/python3
def max_integer(my_list=[]):
    maxx = my_list[0]
    for item in range(1, len(my_list)):
        if item > maxx:
            maxx = item
    return maxx
