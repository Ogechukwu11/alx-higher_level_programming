#!/usr/bin/python3
a = 1
b = 2
# Import the add function from add_0.py
from add_0 import add 
# Calculate the result using the add function
result = add(a, b)
print(f"{a} + {b} = {result}")
#To ensure the code is not executed when imported
if __name__ == "__main__":
    pass
