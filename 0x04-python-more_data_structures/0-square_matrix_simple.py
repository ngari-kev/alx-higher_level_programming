#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    new = matrix
    for lst in new:
        for i in lst:
            i = i ** 2
    return new
