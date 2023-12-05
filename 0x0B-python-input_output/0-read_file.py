#!/usr/bin/python3

"""Defines a text file-reading function."""

def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout.
    Args:
        filename (str): The name of the file
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
