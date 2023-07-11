#!/usr/bin/python3
'''
function class_to_json that returns a dictionary
of all the object's attributes
'''


def class_to_json(obj):
    """Converts an instance of a class to a JSON-serializable dictionary"""
    attributes = obj.__dict__  # Get the instance's attributes dictionary
    json_dict = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
