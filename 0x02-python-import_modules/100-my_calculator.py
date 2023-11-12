#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Check if the operator is valid
    if operator not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = None

    # Perform the operation based on the operator provided
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)

    print("{} {} {} = {:d}".format(a, operator, b, result))
