#!/usr/bin/python3
"""inherits_from."""


def inherits_from(obj, a_class):
    """inherits_from.

    :param obj:
    :param a_class:
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
