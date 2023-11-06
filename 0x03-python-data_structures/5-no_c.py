#!/usr/bin/python3
def no_c(my_string):
    my_list = []
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            my_list.append(ch)
    my_string = ''.join( my_list)
    return str(my_string)
