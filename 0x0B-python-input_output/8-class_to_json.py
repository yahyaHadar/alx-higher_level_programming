#!/usr/bin/python3
"""file"""


def class_to_json(obj):
    """class_to_json.

    :param obj:
    """
    serial_obj = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serial_obj[key] = value

    return serial_obj
