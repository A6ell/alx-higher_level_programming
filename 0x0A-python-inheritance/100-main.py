#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    Class representing a rebel integer.
    Inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to be inverted.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to be inverted.
        """
        return super().__eq__(other)
