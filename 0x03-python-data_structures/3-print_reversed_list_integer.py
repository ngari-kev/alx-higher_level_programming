#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    new_list = []
    idx = len(my_list) - 1
    while idx >= 0:
        new_list.append(my_list[idx])
        idx -= 1
    for i in range(len(new_list)):
        print("{}".format(new_list[i]))
