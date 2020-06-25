#!/bin/python
"""
A very basic port scanner
@author: Mathew Charath
"""
import sys
import socket
from datetime import datetime

# define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4

else:
    print("Invalid or missing arguments")
    print("Syntax: python3 port-scanner <ip/hostname>")
    sys.exit()


# print banner
print("-" * 50)
print("scanning target " + target)
print("time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connet to server")
    sys.exit()
