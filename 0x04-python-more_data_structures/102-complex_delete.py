#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        value_list = list(a_dictionary.values())
        key_list = list(a_dictionary.keys())
        new_dictionary = {}
        for i in range(len(value_list)):
            if value not in value_list:
                new_dictionary[key_list[i]].append(value_list[i])
        return new_dictionary
    else:
        a_dictionary

