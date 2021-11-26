#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total = 0
        av = 0
        for tup in my_list:
            total += tup[0] * tup[1]
            av += tup[1]
        return (total / av)
    return 0
