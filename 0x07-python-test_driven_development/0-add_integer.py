#!/usr/bin/python3

"""
This is the add_integer module.
This module takes in two int arguments and
returns the sum of the arguments
"""


def add_integer(a, b=98):
    """
    returns the sum of two int arguments
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
