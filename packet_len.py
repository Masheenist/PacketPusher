from scapy.all import *

destination_ip = "10.1.10.207"
destination_port = "80"

payload = "J" * 8000

packet = IP(dst=destination_ip)/TCP(dport=int(destination_port))/Raw(load=payload)

send(packet)
