#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file.

    :param my_obj:
    :param filename:
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
