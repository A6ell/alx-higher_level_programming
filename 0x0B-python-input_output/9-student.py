#!/usr/bin/python3
class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance"""
        attributes = self.__dict__  # Get the instance's attributes dictionary
        json_dict = {}

        for attr, value in attributes.items():
            if isinstance(value, (str, int)):
                json_dict[attr] = value

        return json_dict
