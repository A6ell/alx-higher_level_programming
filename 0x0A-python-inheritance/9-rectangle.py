#!/usr/bin/python3
class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle object with the given width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
