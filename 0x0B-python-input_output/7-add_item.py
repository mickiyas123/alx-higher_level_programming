#!/usr/bin/python3

import sys

""" Module 7-add_item Load, add, save to json file """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file(sys.argv[1:], 'add_item.json')
load_from_json_file('add_item.json')
