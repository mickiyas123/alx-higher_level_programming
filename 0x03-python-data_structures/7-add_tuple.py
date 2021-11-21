#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        c = tuple(x + y for x, y in zip(tuple_a, tuple_b))
        return (c)
