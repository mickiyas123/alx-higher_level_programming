#!/usr/bin/python3
def safe_print_integer(value):
    x = ""
    try:
        print("{:d}".format(value))
        x = True
    except ValueError:
        x = False
    return (x)
