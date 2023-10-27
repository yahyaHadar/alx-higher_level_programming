#!/usr/bin/python3
"""say_my_name."""


def say_my_name(first_name, last_name=""):
    """say_my_name.

    Args:
        param first_name: first name.
        param last_name: last_name.
    """
    a = not first_name
    b = not isinstance(first_name, str)
    c = not first_name.strip()
    if a or b or c:
        raise TypeError("first_name must be a string")
    if last_name is None or not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
