#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    args:
        matrix:  a list of lists to print
    Returns: None
    """
    if isinstance(matrix, list):
        if matrix:
            for y in range(len(matrix)):
                for x in range(len(matrix[y])):
                    print("{:d}".format(matrix[y][x]), end="")
                    if matrix[y][x] != matrix[y][-1]:
                        print(" ", end="")
                print()
