#!/usr/bin/python3

"""
This is the print_square module.
This module takes in 1 argument, size, and
prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != size:
            print()
