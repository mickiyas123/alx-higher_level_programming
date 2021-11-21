#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        for i in range(2):
            c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        new_list = list(tuple_b)
        for i in range(len(new_list)):
            new_list.append(0)
        tuple_b = tuple(new_list)
        c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        new_list = list(tuple_b)
        for i in range(2):
            new_list.append(0)
        tuple_b = tuple(new_list)
        c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        new_list = list(tuple_a)
        for i in range(2):
            new_list.append(0)
        tuple_a = tuple(new_list)
        c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        new_list = list(tuple_a)
        for i in range(1):
            new_list.append(0)
        tuple_a = tuple(new_list)
        c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
    return c    
