#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    args:
        matrix: a 2d list of integers.
    Returns: a new list with square values of all integers of a matrix.
    """
    new_matrix = []
    for y in range(len(matrix)):
        row = []
        for x in range(len(matrix[y])):
            row.append(matrix[y][x] ** 2)
        new_matrix.append(row)
    return new_matrix
