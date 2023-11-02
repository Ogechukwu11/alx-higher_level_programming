#!/usr/bin/python3
# To ensure the code is not executed when imported
if __name__ == "__main__":
    pass
# Import the add function from add_0.py
from add_0 import add

a = 1
b = 2
# Calculate the result using the add function
result = add(a, b)
print("{:d}  + {:d} = {:d}".format(a, b, result))
