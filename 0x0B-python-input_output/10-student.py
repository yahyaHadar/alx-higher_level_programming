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

    def to_json(self, attrs=None):
        """to_json."""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
