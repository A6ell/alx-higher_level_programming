#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.
    Raises a TypeError exception if the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        obj.__setattr__(attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
