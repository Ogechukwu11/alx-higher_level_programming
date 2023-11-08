#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return
    for key in sorted(a_dictionary):
        value = a_dictionary[key]
        print(f"{key}: {value}")
