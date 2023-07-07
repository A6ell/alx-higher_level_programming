#!/usr/bin/python3
"""
This is the text_indentation module.
This module takes in 1 argument, text, and
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):

    """
    prints a text with 2 lines after each of
    characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    lines = [line.strip() for line in text.split("\n")]
    print("\n".join(lines))
