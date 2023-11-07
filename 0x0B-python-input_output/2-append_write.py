#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """append_write.

    :param filename:
    :param text:
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
