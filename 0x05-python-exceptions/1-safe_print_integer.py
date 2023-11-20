#!/usr/bin/python3
def safe_print_integer(value):
    try:
        result = int(value)
        print("{:d}".format(result))
        return True
    except (ValueError, TypeError):
        return False
