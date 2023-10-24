#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init Square
        Args:
            size (int): square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
