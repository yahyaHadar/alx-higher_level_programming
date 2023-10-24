#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """init square
        Args:
            size (int): square size.
        """
        self.__size = size

    @property
    def size(self):
        """get value attribute.

        Returns:
            int: the attribute value.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): square size.

        Raises:
            TypeError: if not int.
            ValueError: if not positive.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calc area
        returns:
            return area.
        """
        return self.__size * self.__size
