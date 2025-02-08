#!/usr/bin/env python

from scapy.all import *
from scapy.layers.inet import IP, TCP
import random
import sys

dest = sys.argv[1]
try:
    if sys.argv[2]:
        getStr = sys.argv[2]
except:
    getStr = 'GET / HTTP/1.1\r\nHost:' + dest + '\r\nAccept-Encoding: gzip, deflate\r\n\r\n'

try:
    if sys.argv[3]:
        max = int(sys.argv[3])
except:
    max = 10

counter = 0
while counter < max:
    # SEND SYN
    syn = IP(dst=dest) / TCP(sport=random.randint(1025, 65500), dport=80, flags='S')
    # GET SYNACK
    syn_ack = sr1(syn)
    # Send ACK
    out_ack = send(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A'))
    # Send the HTTP GET
    sr1(IP(dst=dest) / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='PA') / getStr)
    counter += 1
