#!/usr/bin/python3
'''
   A function that searches for an element in a list and
   replaces it with another.
   my_list - is the initial list.
   search  - is the element to replace in the list.
   replace - is the new element.
'''


def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    new_list = my_list.copy()
    idx = 0
    for idx in range(len(new_list)):
        if new_list[idx] == search:
            new_list[idx] = replace
    return new_list
