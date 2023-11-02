#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_argv = len(sys.argv) - 1
    if num_argv > 1:
        print("{} arguments:".format(num_argv))
        for i in range(1, num_argv + 1):
            print("{}: {}".format(i, sys.argv[i]))
    elif num_argv == 0:
        print("{} arguments.".format(num_argv))
    else:
        print("{} arguments:".format(num_argv))
        print("{}: {}".format(num_argv, sys.argv[1]))
