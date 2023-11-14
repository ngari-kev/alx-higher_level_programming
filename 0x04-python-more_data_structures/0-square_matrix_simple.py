#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = matrix
    new = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return new
