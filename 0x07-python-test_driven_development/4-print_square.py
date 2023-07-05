#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(size):
    """Print a name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either first_name or last_name are not strings.
        ValueError: If first_name is an empty string.
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
