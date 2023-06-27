#!/usr/bin/python3
import math


class MagicClass:
    """
    MagicClass represents a class with magic properties and methods.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius: The radius of the magic object (default is 0).
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """
        Getter method for the radius attribute.

        Returns:
            The radius of the magic object.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Setter method for the radius attribute.

        Args:
            value: The radius value to set.

        Raises:
            TypeError: If the value is not a number (integer or float).
        """
        if type(value) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """
        Calculates the area of the magic object.

        Returns:
            The area of the magic object.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic object.

        Returns:
            The circumference of the magic object.
        """
        return 2 * math.pi * self.__radius
