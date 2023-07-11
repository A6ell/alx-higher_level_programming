#!/usr/bin/python3
"""
Module that adds all arguments to a Python list and saves it to a file
"""

import json


def load_from_json_file(filename):
    '''
    this is the function
    '''
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
