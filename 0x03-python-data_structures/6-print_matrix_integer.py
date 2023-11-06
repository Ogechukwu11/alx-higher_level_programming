#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for integers in row:
                print("{:d}".format(integers), end="")
            print()
