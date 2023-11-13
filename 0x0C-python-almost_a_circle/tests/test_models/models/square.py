#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__.

        :param size:
        :param x:
        :param y:
        :param id:
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        """size.

        :param value:
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update.

        :param args:
        :param kwargs:
        """
        attributes = ['id', 'size', 'x', 'y']

        for i, arg in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary."""
        attr_dic = {}
        attribute_names = ['id', 'size', 'x', 'y']
        for attr in attribute_names:
            attr_value = getattr(self, attr, None)
            attr_dic[attr] = attr_value
        return attr_dic

    def __str__(self):
        """__str__."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
