#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:    
        return None
    maxx = my_list[0]
    for item in my_list:
        if item > maxx:
            maxx = item
    return maxx
