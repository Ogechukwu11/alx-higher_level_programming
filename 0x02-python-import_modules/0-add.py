#!/usr/bin/python3
# To ensure the code is not executed when imported
if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
