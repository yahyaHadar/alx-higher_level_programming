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
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """equality comparison =="""
        if isinstance(other, Square):
            return self.__size == other.__size
        return False

    def __ne__(self, other):
        """not equal comparison !="""
        return not self.__eq__(other)

    def __lt__(self, other):
        """less than comparison <"""
        if isinstance(other, Square):
            return self.__size < other.__size
        return NotImplemented

    def __le__(self, other):
        """less equal comparison <="""
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        """greater than comparison >"""
        if isinstance(other, Square):
            return self.__size > other.__size
        return NotImplemented

    def __ge__(self, other):
        """greater equal comparison >="""
        return self.__gt__(other) or self.__eq__(other)
