#!/usr/bin/python3
class Square:
    """
    Square class represents a square shape.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size: The size of the square (default is 0).
            position: The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value: The size value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value: The position value to set.

        Raises:
            TypeError: If the value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints a representation of the square using the '#' character.

        If the size is 0, prints an empty line. Otherwise, prints the square
        with the specified position and size.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            A string representation of the square.
        """
        square_str = []
        if self.__size == 0:
            return ""
        for _ in range(self.__position[1]):
            square_str.append("")
        for _ in range(self.__size):
            square_str.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(square_str)
