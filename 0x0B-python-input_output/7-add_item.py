#!/usr/bin/python3

""" Module 7-add_item Load, add, save to json file """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

import sys

new_list = []

for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])

json_object = save_to_json_file(new_list, "add_item.json")
