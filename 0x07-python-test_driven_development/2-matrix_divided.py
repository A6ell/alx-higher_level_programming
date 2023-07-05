#!/usr/bin/python3

"""
This is the matrix divided module.
This module takes in two arguments, matrix and dic, and
returns a new matrix with each element divided by div
"""


def matrix_divided(matrix, div):
    """
    returns new matrix with each element divided by div
    """

    if (not isinstance(matrix,
        list)) or (not
                   all(isinstance(row, list) for
                       row in matrix)):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return[[round(elem / div, 2) for elem in row] for row in matrix]
