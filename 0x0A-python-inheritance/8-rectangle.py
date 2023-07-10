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
