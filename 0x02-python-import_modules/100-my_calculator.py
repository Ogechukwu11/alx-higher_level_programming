#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    av = len(argv)
    if av != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    signs = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] in signs:
        i = int(argv[1])
        j = int(argv[3])
        sign = signs[argv[2]]
        reult = sign(i, j)
        print("{:d} {:s} {:d} = {:d}".foramat(i, argv[2], j, result))
    else:
        print{"Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
