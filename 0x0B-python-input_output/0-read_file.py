#!/usr/bin/python3
'''
function read_file that reads a file
and prints it out
'''


def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to read (default: '').

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.

    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')
