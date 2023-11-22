#!/usr/bin/pyhton3
''''
    A function that returns the result of the division of a by b
'''


def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
