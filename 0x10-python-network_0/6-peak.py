#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """find the peak of a list
    Args:
        list_of_integers: the list
    """
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
