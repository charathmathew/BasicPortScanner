#!/bin/python
"""
A very basic port scanner
@author: Mathew Charath
"""
import sys
import socket
import threading
from datetime import datetime
from queue import Queue


print_lock = threading.Lock()

print("-" * 50)

# define the target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4

else:
    print("Invalid or missing arguments")
    print("Usage: python port-scanner <ip/hostname>")
    print("-" * 50)
    sys.exit()


# print banner
print("scanning target " + target)
print("time started: " + str(datetime.now()))
print("-" * 50)

# attempts to establish a connection to the given port number
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # returns an error indicator
        if result == 0:
            with print_lock:
                print("Port {} is open".format(port))
        s.close()

    except KeyboardInterrupt:
        print("\nExiting program")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

    except socket.error:
        print("Could not connect to server")
        sys.exit()

# dispatches a worker thread to to scan an available portNumber for the ports queue
def dispatch_thread():
    while True:
        portNumber = ports.get()
        scan_port(portNumber)
        ports.task_done()


ports = Queue()

# create a pool of 30 worker threads
for i in range(0, 30):
    t = threading.Thread(target=dispatch_thread)
    t.daemon = True
    t.start()



# add ports to be scanned (1-100) to the ports queue
for portNumber in range(1, 101):
    ports.put(portNumber)

ports.join()
