#!/usr.bin/python3
''''
    This function print integers and returns True or False if value is not int
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
