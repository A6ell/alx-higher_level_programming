#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the Square object with the given size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__width}"
