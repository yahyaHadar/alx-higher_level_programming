#!/usr/bin/python3
"""file"""


class Student:
    """Student."""

    def __init__(self, first_name, last_name, age):
        """__init__.

        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to_json."""
        return self.__dict__.copy()
