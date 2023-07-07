#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("The text must be a string")

    cursor = 0

    while cursor < len(text) and text[cursor] == " ":
        cursor += 1

    while cursor < len(text):
        print(text[cursor], end="")

        if text[cursor] == "\n" or text[cursor] in ".?:":
            if text[cursor] in ".?:":
                print("\n\n")
            cursor += 1

            while cursor < len(text) and text[cursor] == " ":
                cursor += 1
            continue

        cursor += 1
