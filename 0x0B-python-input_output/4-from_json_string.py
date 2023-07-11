#!/usr/bin/python3
'''
function from_json_string that returns an object
from a json representation
'''


import json


def from_json_string(my_str):
    """
    Converts a JSON string to its corresponding Python object.

    Args:
        my_str: The JSON string to be deserialized.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
