#!/usr/bin/python3
"""function"""
import json


def load_from_json_file(filename):
    """load_from_json_file.

    :param filename:
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
