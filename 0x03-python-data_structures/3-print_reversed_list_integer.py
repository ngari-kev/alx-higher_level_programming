#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    for _ in my_list:
	    new_list.append(_)
    for i in range(len(new_list)):
        print("{}".format(new_list[i]))
