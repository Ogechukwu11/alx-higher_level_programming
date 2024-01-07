#!/usr/bin/python3
def add_integer(a, b=98):
    """function that add 2 numbers"""

    if not a or (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
