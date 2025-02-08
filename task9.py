#!/usr/bin/env python

"""
Script to open TCP connection and send 1 HTTP GET request containing
a specific string, and header
Usage:
./http.py <IP_of_target>
There is only one mandatory argument, which is the target IP address.
If other arguments are omitted, will send a preconfigured URL string 
10 times
Optional arguments are : 
./http.py <IP_of_target> |HTTP GET STRING| |Max requests|
e.g.
./http.py 10.10.10.10 'GET / HTTP/1.1\r\n' 100
"""
from scapy.all import *
from scapy.layers.inet import TCP

def http_filter(packet):
    return packet.haslayer(TCP) and packet.haslayer(Raw) and (b"HTTP" in packet[Raw].load)

sniff(filter="tcp port 80", prn=lambda x: x.show() if http_filter(x) else None, store=False)
