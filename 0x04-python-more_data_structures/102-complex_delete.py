#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = [key for key, val in a_dictionary.items() if val == value]
    for key in key_list:
        if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary
