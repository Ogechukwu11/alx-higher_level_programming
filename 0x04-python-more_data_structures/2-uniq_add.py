#!usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    add = 0
    for num in my_list:
        add += num
    return (add)
