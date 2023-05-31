#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra M, and Nick A
# Signature=based malware pt 2 of 3

import os
import platform
import hashlib

# Prompt the user for a directory to search in
path = input("Please enter the directory to search in: ")


# Search each file and folder recursively in the directory
def find_all(path):
    result = []
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            result.append(os.path.join(root, directory))
        for file in files:
            result.append(os.path.join(root, file))
    return result

def hash(file):
    # Hash object
    hasher = hashlib.md5()
    try:
        # Open file
        with open(file, 'rb') as file_obj:
            # Loop through the file content
            chunk = file_obj.read(1024)
            while chunk:
                hasher.update(chunk)
                chunk = file_obj.read(1024)
    # If no
    except FileNotFoundError:
        return None
    
    return hasher.hexdigest()

# Call the function to search for the file
search_result = find_all(path)

# Display the search result
if search_result:
    file_hash = hash(search_result[0])
    if file_hash is not None:
        print("This Operating system is: ", platform.system())
        print("Number of files searched:", len(search_result))
        print("Number of hits found:", len(search_result))
        print("File found in the following locations:")
        for file_path in search_result:
            print("Location:", file_path)
            print("Hash: ", file_hash)
    else:
        print("Error in hash for files")
else:
    print("No items found in the specified directory.")
