#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """write_file.

    :param filename:
    :param text:
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
