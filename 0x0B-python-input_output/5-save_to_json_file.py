#!/usr/bin/python3
'''
function that saves an object
onto a file using json
'''


import json


def save_to_json_file(my_obj, filename):
    """
    Serializes an object to JSON and saves it to a file.

    Args:
        my_obj: The object to be serialized and saved.
        filename: The name of the file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
