#!/usr/bin/python3
"""dds a new attribute"""


def add_attribute(obj, attribute, value):
    """add_attribute.

    :param obj:
    :param attribute:
    :param value:
    """
    if '__dict__' not in dir(obj) or '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
