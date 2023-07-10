#!/usr/bin/python3
"""
Holds the MyList class
"""


class MyList(list):
    """
    Custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
