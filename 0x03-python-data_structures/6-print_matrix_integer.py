#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        idx = 0
        for i in row:
            print("{:d}{}".format(i, '' if idx == (len(row) - 1) else ' '), end='')
            idx += 1
        print()
