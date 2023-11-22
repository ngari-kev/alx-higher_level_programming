#!/usr/bin/pyhton3
''''
    A function that returns the result of the division of a by b
'''


def safe_print_division(a, b):
    try:
        div = a / b
    except (ZeroDivisionError, TypeError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
