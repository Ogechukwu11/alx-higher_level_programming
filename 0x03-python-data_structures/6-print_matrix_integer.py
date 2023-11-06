#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for num in row:
                print("{:d}".format(num), end=" " if num != row[-1] else "")
                """end=" " if num != row[-1] else "": checks if 
                the number is not the last one on the paper, we add a space; otherwise
                we don't add anything after it."""
            print()
