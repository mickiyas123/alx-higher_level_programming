#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(value))
        x = True
    except:
        print("Exception:",sys.exc_info()[1], file=sys.stderr)
        x = False
    return x
