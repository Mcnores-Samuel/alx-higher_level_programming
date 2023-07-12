#!/usr/bin/python3

"""This module contains a script for write data from commandline
to a JSON file and also reads back from the file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    data_list = load_from_json_file("add_item.json")
    if len(data_list) != 0:
        data = sys.argv
        if len(data) > 1:
            for item in range(1, len(data)):
                try:
                    data_list.append(data[item])
                except IndentationError:
                    break
        save_to_json_file(data_list, "add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")
