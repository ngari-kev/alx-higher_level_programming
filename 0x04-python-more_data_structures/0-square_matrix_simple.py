#!/usr/bin/python3
def squared(value):
    return value ** 2
def square_matrix_simple(matrix=[]):
    if matrix == None:
        return None
    result = list(map(lambda row: list(map(square)), matrix))
    return result
