#!/usr/bin/python3
"""class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square."""

    def __init__(self, size):
        """__init__.

        :param size:
        """
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size
