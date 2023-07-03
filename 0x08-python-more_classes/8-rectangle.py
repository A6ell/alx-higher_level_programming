#!/usr/bin/python3
class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Class Attributes:
        number_of_instances (int): instances of the Rectangle class.
        print_symbol: The symbol used for string representation.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns the printable representation of the rectangle.
        __repr__(): Returns a string.
        __del__(): Prints a message when an instance of Rectangle is deleted.
        bigger_or_equal(rect_1, rect_2): Returns the rectangle.

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle.

        Represents the rectangle with the print_symbol character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect)

    def __repr__(self):
        """Return a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the bigger area.

        Arguments:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area.

        Raises:
            TypeError: If rect_1 is not an instance of Rectangle.
            TypeError: If rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
