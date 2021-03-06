#!/usr/bin/python3
# Written By: Douglas Cruz
# Date: 19/11/2021

#import sys
import socket
from colorama import init, Fore
#from termcolor import colored

# initialize colorama
init()

GREEN = Fore.GREEN

ipAddress = input("[*] Please Specify a Host to Scan: ")

for ports in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)

    if s.connect_ex((ipAddress, ports)) == 0:
        print(f"{GREEN}[+] Port {ports} is Open!")
        s.close()