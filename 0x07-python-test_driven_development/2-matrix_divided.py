#!/usr/bin/python3

"""This module contains one function matrix_divided(matrix, div)

matrix_divided(matrix, div) function takes a 2D list of integers
and divides all the integer in the matrix with the div value.
It return a new matrix containing division results without affecting
The original matrix.
For example:
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix
[[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    args:
       matrix: a list of list of integers or floats all of the
            same length otherwise an exception is raised.
       div: an int or a float number and must not be zero otherwise
            an exception is raised.
    Returns: a new matrix of all elements divided by div.
    """
    if isinstance(matrix, list):
        size = len(matrix[0])
        int_err = "matrix must be a matrix (list of lists) of integers/floats"
        len_err = "Each row of the matrix must have the same size"
        if isinstance(div, int) or isinstance(div, float):
            if div == 0:
                raise ZeroDivisionError("division by zero")
            for x in matrix:
                if size != len(x):
                    raise TypeError(len_err)
                for y in x:
                    if isinstance(y, int) or isinstance(y, float):
                        if y == 0:
                            raise ZeroDivisionError("division by zero")
                    else:
                        raise TypeError(int_err)
        else:
            raise TypeError("div must be a number")
        return (list(map(lambda y: list(map(lambda x:
                                            round(x / div, 2), y)), matrix)))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt", verbose=True)
