#!/usr/bin/python3
"""
Module that adds all arguments to a Python list and saves it to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # Load existing list from file
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    # Create a new list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to file
save_to_json_file(my_list, "add_item.json")
