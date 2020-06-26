# BasicPortScanner

### A very basic port scanner

A very basic python port scanner that scans ports in the range of 1-100 of a given IP address. Indicates whether a port is open. 

Usage: python port_scanner.py <ip-address/hostname>

<br>
<br>

I made this port scanner while learning and doing research on penetration testing.

Possible improvements:
1. ~~Use multithreading to speed up the scanning process and maybe scan a larger range of ports.~~  Added multithreading and now scans ports 1-100
1. Return more information if available rather than simply if a port is open or not.
