#!/usr/bin/python3
def no_c(my_string):
    """This variable will be used to accumulate the characters
    from my_string that are not 'c' or 'C."""
    store = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            store += my_string[i]
    return (store)
