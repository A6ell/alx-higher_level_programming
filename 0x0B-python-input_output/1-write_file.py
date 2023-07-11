def write_file(filename="", text=""):
    """
    write to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the text file to write (default: '').
        text (str): The string to write to the file (default: '').

    Returns:
        int: The number of characters written.

    """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)

    return characters_written
