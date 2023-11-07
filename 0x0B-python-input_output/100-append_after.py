#!/usr/bin/python3
"""file"""


def append_after(filename="", search_string="", new_string=""):
    """append_after.

    :param filename:
    :param search_string:
    :param new_string:
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
