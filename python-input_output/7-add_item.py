#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a JSON file.
"""
import sys
import os


# Importing functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Load existing data if the file exists, otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Add command line arguments (skipping the script name at index 0)
# sys.argv[1:] captures everything after the filename
items.extend(sys.argv[1:])

# 3. Save the updated list back to the file
save_to_json_file(items, filename)
