#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra M, and Nick A
import subprocess
import socket

def banner_grabbing(target_address, port):
    try:
        # Perform banner grabbing using netcat
        print("Banner Information (Netcat):")
        nc_output = subprocess.check_output(['nc', '-v', target_address, port])
        print(nc_output.decode().strip())
        
        # Perform banner grabbing using telnet
        print("Banner Information (Telnet):")
        telnet_output = subprocess.check_output(['telnet', target_address, port])
        print(telnet_output.decode().strip())
        
        # Perform banner grabbing using Nmap
        print("Banner Information (Nmap):")
        nmap_output = subprocess.check_output(['nmap', '-sV', '-p-', target_address])
        print(nmap_output.decode().strip())
        
    except (subprocess.CalledProcessError, socket.error) as e:
        print("Error: {}".format(e))
        # Handle any error that occurs during the banner grabbing

# Prompt the user to enter the target address and port
target_address = input("Please enter the target address: ")
port = input("Please enter the port: ")

# Call the banner_grabbing function with the provided target address and port
banner_grabbing(target_address, port)
