#!/usr/bin/python3
def multiply_by_2(value):
    return value * 2
def square_matrix_simple(matrix=[]):
    if matrix == None:
        return None
    result = list(map(lambda row: list(map(multiply_by_2, row)), matrix))
    return result
