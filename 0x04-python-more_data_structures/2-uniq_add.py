#!usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    add = 0
    for num in unique:
        add += num
    return (add)
