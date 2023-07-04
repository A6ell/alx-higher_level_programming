#!/usr/bin/python3
"""Module to find the maximum integer in a list"""


def max_integer(lst=[]):
    """Find the maximum integer in a list.

    Args:
        lst (list, optional): A list of integers. Defaults to an empty list.

    Returns:
        int or None: The maximum integer in the list. returns None.
    """
    if len(lst) == 0:
        return None

    result = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > result:
            result = lst[i]

    return result
