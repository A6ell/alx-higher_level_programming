#!/usr/bin/python3
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
