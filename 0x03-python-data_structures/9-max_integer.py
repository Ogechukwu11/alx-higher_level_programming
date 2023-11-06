#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    """A variable to hold the assumed largest integer"""
    largest_int = my_list[0]
    for num in my_list:
        if num > largest_int:
            largest_int = num
    return (largest_int)
