#!/usr/bin/python3
"""class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle."""

    def __init__(self, width, height):
        """__init__.

        :param width:
        :param height:
        """
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width

    def area(self):
        """area."""
        return self.__width * self.__height

    def __str__(self):
        """__str__."""
        return f"[Rectangle] {self.__width}/{self.__height}"
