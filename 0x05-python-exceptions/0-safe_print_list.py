#!/usr/bin/python3
'''
A function that prints a list to a specified index
'''


def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            printed += 1
        print("")
        return x
    except IndexError:
        print("")
        return printed