#!/usr/bin/python3
"""class"""


class MyInt(int):
    """MyInt."""

    def __eq__(self, other):
        """__eq__.

        :param other:
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """__ne__.

        :param other:
        """
        return super().__eq__(other)
