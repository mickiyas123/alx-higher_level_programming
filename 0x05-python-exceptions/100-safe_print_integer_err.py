#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        int(value)
        print("{:d}".format(value))
        x = True
    except ValueError:
        sys.stderr.write("Exception: Unknown format\
code 'd' for object of type 'str'\n")
        x = False
    return x
