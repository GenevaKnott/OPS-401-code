#!/usr/bin/env python3
# Geneva Knott
# Worked with Sierra, and Nick A
# Attack Tools Part 2 of 3
# https://github.com/nmmapper/python3-nmap
import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

# Prompt the user to enter the IP address to scan
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)


# Prompt the user to select a scan option
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Idle Scan             
                4) Exit\n""") 

print("You have selected option: ", resp)

# Prompt the user to enter the port range to scan
port_range = input("Please type in port range to scan: ")
print("The range you put was", range)


if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("No open TCP ports found.")
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    if 'udp' in scanner[ip_addr]:
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    else:
        print("No open UDP ports found.")
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sI zombie_ip')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    else:
        print("No open TCP ports found.")
elif resp >= '4':
    # Exit the program
    exit()
