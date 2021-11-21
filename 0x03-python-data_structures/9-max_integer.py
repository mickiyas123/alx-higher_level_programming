#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = ""
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if largest == "":
            largest = my_list[i]
        elif my_list[i] > largest:
            largest = my_list[i]
    return largest
