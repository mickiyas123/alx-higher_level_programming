#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum0 = 0
    sum1 = 1
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        sum0 = tuple_a[0] + tuple_b[0]
        sum1 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) == 0:
        new_list = list(tuple_b)
        new_list += [0, 0]
        tuple_b = tuple(new_list)
        sum0 = tuple_a[0] + tuple_b[0]
        sum1 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) == 1:
        new_list = list(tuple_b)
        new_list += [0]
        tuple_b = tuple(new_list)
        sum0 = tuple_a[0] + tuple_b[0]
        sum1 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 0 and len(tuple_b) >= 2:
        new_list = list(tuple_a)
        new_list += [0, 0]
        tuple_a = tuple(new_list)
        sum0 = tuple_a[0] + tuple_b[0]
        sum1 = tuple_a[1] + tuple_b[1]
    elif len(tuple_a) == 1 and len(tuple_b) >= 2:
        new_list = list(tuple_a)
        new_list += [0]
        tuple_a = tuple(new_list)
        sum0 = tuple_a[0] + tuple_b[0]
        sum1 = tuple_a[1] + tuple_b[1]
    return (sum0, sum1)
