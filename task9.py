from scapy.all import *
from scapy.layers.http import HTTPRequest 

def http_filter(packet):
    if HTTPRequest in packet:
        http_layer = packet[HTTPRequest]
        print(f'{http_layer.Method.decode()} {http_layer.Path.decode()}')

sniff(filter="port 80", prn=http_filter, store=0)
