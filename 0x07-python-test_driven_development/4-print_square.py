#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either first_name or last_name are not strings.
        ValueError: If first_name is an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("The first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("The last name must be a string")
    if not first_name:
        raise ValueError("The first name must not be empty")
    if not last_name:
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
