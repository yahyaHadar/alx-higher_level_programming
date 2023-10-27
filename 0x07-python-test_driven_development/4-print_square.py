#!/usr/bin/python3
"""print_square."""


def print_square(size):
    """print_square.
    Args:
        param size: square size.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    square_pattern = "#" * size + "\n"
    print(square_pattern * size, end="")
