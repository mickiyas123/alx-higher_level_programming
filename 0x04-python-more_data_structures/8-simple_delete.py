#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary.keys())
    if key not in key_list:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
