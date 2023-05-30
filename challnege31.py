#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra, and Nick A
# Signature=based malware pt 1 of 3
# https://stackoverflow.com/questions/1724693/find-a-file-in-python - Helped with fuction for search function
import os

# Prompt the user to type in a file name to search for
file = input("Please enter the file name to search for: ")

# Prompt the user for a directory to search in
path = input("Please enter the directory to search in: ")

# Search each file in the directory by name
def find_all(file, path):
    result = []
    for root, dirs, files in os.walk(path):
        if file in files:
            result.append(os.path.join(root, file))
    return result

# Call the function to search for the file
search_result = find_all(file, path)

# Display the search result
if search_result:
    print("Number of files searched:", len(search_result))
    print("Number of hits found:", len(search_result))
    print("File found in the following locations:")
    for file_path in search_result:
        print("Name:", file)
        print("Location:", file_path)
        print("------------------------")
else:
    print("Number of files searched: 0")
    print("Number of hits found: 0")
    print("File not found.")
