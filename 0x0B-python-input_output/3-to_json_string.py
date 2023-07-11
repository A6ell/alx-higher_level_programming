#!/usr/bin/python3
'''
function to_json_string that returns a JSON
representation of an object
'''


import json


def to_json_string(my_obj):
    """
    Converts an object to its JSON representation.

    Args:
        my_obj: The object to be serialized.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
