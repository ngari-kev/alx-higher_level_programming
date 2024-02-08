#!/usr/bin/python3
'''
A module that has a new class called MyList
that inherits from List. It also has a function
that prints a sorted list.
'''


class MyList(list):
    '''
    A class that inherits from the class list
    '''

    def print_sorted(self):
        ''' A function that prints a list sorted in ascending order'''
        return (self.sort())
