#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new = [replace if num == search else num for num in my_list]
        return (new)
    return (my_list)
