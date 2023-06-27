#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""


def __init__(self, size=0):
    """Initialize a new Square object.

    Args:
        size (int): The size of the square's side length.
    """
    if not isinstance(size, int):
        raise TypeError("Size must be an integer.")
    elif size < 0:
        raise ValueError("Size must be greater than or equal to 0.")
    self.__size = size
