#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal_triangle.

    :param n:
    """
    pascal = []
    if n <= 0:
        return pascal
    pascal.append([1])
    for i in range(1, n):
        previous_row = pascal[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_element = previous_row[j - 1] + previous_row[j]
            new_row.append(new_element)

        new_row.append(1)
        pascal.append(new_row)

    return pascal
