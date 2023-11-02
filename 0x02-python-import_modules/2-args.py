#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_argv = len(sys.argv) - 1
    if num_argv == 0:
        print("0 arguments.")
    elif num_argv == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(num_argv))
    for i in range(num_argv):
        print("{} {}".format(i + 1, sys.argv[i + 1]))
