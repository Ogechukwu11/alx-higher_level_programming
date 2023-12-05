#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename (str): The name of the file.
        text: The text to be written to the file.
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='UTF8') as f:
        return (f.write(text))
