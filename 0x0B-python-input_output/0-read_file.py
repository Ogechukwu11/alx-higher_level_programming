#!/usr/bin/python3

def read_file(filename=""):
    """ A function that opens and read a file
    Args:
        filename (str): The name of the file
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read())
