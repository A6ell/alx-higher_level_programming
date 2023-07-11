#!/usr/bin/python3
'''
function append_write that appends onto a file
and returns the number of characters added
'''


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number.

    Args:
        filename (str): The name of the text file to append (default: '').
        text (str): The string to append to the file (default: '').

    Returns:
        int: The number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        characters_added = file.write(text)

    return characters_added
