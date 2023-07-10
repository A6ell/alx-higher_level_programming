#!/usr/bin/python3
class BaseGeometry:
    """
    Class representing base geometry.
    """

    def area(self):
        """
        Raises an exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
