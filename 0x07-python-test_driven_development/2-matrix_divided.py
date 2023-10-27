#!/usr/bin/python3
"""matrix_divided."""


def matrix_divided(matrix, div):
    """matrix_divided.

    Args:
        param matrix: the matrix to e divided.
        param div: the divisor.
    Returns:
        return a new matrix.
    """
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(type_msg)

    if not all(isinstance(item, list) and item for item in matrix):
        raise TypeError(type_msg)

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(type_msg)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = round(num / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
