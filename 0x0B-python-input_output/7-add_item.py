#!/usr/bin/python3

"""This module contains a script for write data from commandline
to a JSON file and also reads back from the file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    try:
        data_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data_list = []
    data = sys.argv[1:]
    data_list += data
    save_to_json_file(data_list, "add_item.json")
