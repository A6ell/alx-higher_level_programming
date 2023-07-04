#!/usr/bin/python3
"""Module containing a dummy adder function for testing"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): The first integer.
        b (int, optional): The second integer. Defaults to 98 if not provided.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If `a` is not an integer.
        TypeError: If `b` is not an integer.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
