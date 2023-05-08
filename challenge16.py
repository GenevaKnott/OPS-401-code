#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra, and Nick A


# Import
import time

# Function 1

def mode1():
    # User inpit word list file path
    filepath = input("Enter your dictionary filepath:\n")
    #Open the file 
    file = open(filepath)
    line = file.readline()
    # Iterate through each word in given list
    while line:
        line = line.rstrip()
        word = line
        time.sleep(1)
        print(word)
        line = file.readline()
    file.close()

def mode2():
    filepath = input("Enter your dictionary filepath:\n")
    with open(filepath) as file:
        password_list = [line.strip() for line in file]
        while True:
            password = input("Please type your new password: \n")
            if password in password_list:
                print("Password is weak! Try again")
            else:
                print("Password is strong!")
                break

while True:
    answer = input("Mode 1 or Mode 2: ")
    if answer == "Mode 1":
        mode1()
    if answer == "Mode 2":
        mode2()
    else:
        break
# end
